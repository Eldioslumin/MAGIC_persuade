import csv
import json
import os
import time
from typing import List, Dict, Any, Optional
from prompts.agents import GREAgentPrompts
from dotenv import load_dotenv
from openai import OpenAI, APIError

# Load environment variables
load_dotenv()

# Configuration
CORPUS_PATH = "corpora/PERSUADE2.0/persuade_corpus_2.0_test.csv"
NUM_EXAMPLES = 5

# Providers Configuration
PROVIDERS = [
    {
        "name": "OpenRouter",
        "api_key": os.getenv("OPENROUTER_API_KEY"),
        "base_url": os.getenv("OPENROUTER_BASE_URL"),
        "model": os.getenv("OPENROUTER_MODEL")
    },
    {
        "name": "Ollama",
        "api_key": os.getenv("OLLAMA_API_KEY", "ollama"),
        "base_url": os.getenv("OLLAMA_BASE_URL"),
        "model": os.getenv("OLLAMA_MODEL")
    }
]

# Provide fallback to legacy env vars if specific ones aren't set, for backward compatibility or single-run
# (Optional logic, but keeping it simple for now as we updated .env)

class LLMClient:
    """
    Wrapper for OpenAI compatible client.
    """
    def __init__(self, api_key: str, base_url: Optional[str], model_name: str):
        if not api_key:
            raise ValueError("API Key is missing.")
        
        self.model_name = model_name
        self.api_key = api_key
        self.base_url = base_url
        
        print(f"Initializing LLM Client with model: {self.model_name} (Base URL: {self.base_url})")
        if self.base_url:
            self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        else:
            self.client = OpenAI(api_key=self.api_key)

    def generate(self, prompt: str) -> str:
        """
        Generates a response from the LLM.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}, # Ensure JSON output if supported by model
                temperature=0.0,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except APIError as e:
            print(f"LLM API Error: {e}")
            return json.dumps({"error": str(e), "score": "0", "examiner_comment": "Error generating feedback."})
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return json.dumps({"error": str(e), "score": "0", "examiner_comment": "Error generating feedback."})

def load_persuade_corpus(filepath: str, limit: int = NUM_EXAMPLES) -> List[Dict[str, str]]:
    """
    Loads essays from the Persuade corpus CSV file.
    """
    essays = []
    if not os.path.exists(filepath):
        print(f"Error: Corpus file not found at {filepath}")
        return []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                if count >= limit:
                    break
                essays.append({
                    "essay_id": row.get("essay_id", "unknown"),
                    "full_text": row.get("full_text", ""),
                    "prompt_name": row.get("prompt_name", "No prompt provided")
                })
                count += 1
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []
    
    return essays

def run_agents(essays: List[Dict[str, str]], llm_client: LLMClient, provider_name: str):
    """
    Runs the agents on the provided essays.
    """
    results = []
    
    for i, essay in enumerate(essays):
        print(f"[{provider_name}] [{i+1}/{len(essays)}] Processing Essay ID: {essay['essay_id']}")
        essay_result = {
            "essay_id": essay['essay_id'],
            "prompt_name": essay['prompt_name'],
            "agent_feedbacks": {}
        }
        
        grading_instruction = {
            "essay_text": essay['full_text'],
            "prompt": essay['prompt_name'],
        }

        # Iterate through all configured aspects in GREAgentPrompts
        for aspect_name, aspect_rubric, aspect_description in GREAgentPrompts.aspect_rubrics:
            # Skip aspects without a rubric if any
            if aspect_name == "additional_features":
                 pass

            try:
                print(f"  [{provider_name}] Processing aspect: {aspect_name}...")
                # Generate the prompt
                prompt_text = GREAgentPrompts.format_prompt_inference(
                    grading_instruction, 
                    agent_rubric_type=aspect_name, 
                    current_aspect_rubric=aspect_rubric if aspect_rubric else "" 
                )
                
                # Call LLM
                llm_response_str = llm_client.generate(prompt_text)
                
                # Sleep to avoid rate limits on free tier or local load
                time.sleep(1) # Reduced sleep for local
                
                # Parse the response
                try:
                    llm_response = json.loads(llm_response_str)
                except json.JSONDecodeError:
                    print(f"  [{provider_name}] Warning: Invalid JSON for {aspect_name}. Raw: {llm_response_str[:100]}...")
                    llm_response = {
                        "error": "Failed to parse JSON", 
                        "raw_output": llm_response_str,
                        "score": "0",
                        "examiner_comment": "Failed to parse JSON response."
                    }

                essay_result["agent_feedbacks"][aspect_name] = llm_response

            except Exception as e:
                print(f"  [{provider_name}] Error processing aspect {aspect_name}: {e}")
                essay_result["agent_feedbacks"][aspect_name] = {"error": str(e)}

        results.append(essay_result)
        
        # Save results incrementally
        output_file = f"agent_feedback_results_{provider_name}.json"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=4)
            print(f"  [{provider_name}] Results saved incrementally to {output_file}")
        except Exception as e:
            print(f"  [{provider_name}] Error saving incremental results: {e}")
    
    return results

def main():
    print("Starting agent testing on Persuade Corpus with Parallel Providers...")
    
    essays = load_persuade_corpus(CORPUS_PATH, limit=NUM_EXAMPLES)
    if not essays:
        print("No essays loaded. Exiting.")
        return

    print(f"Loaded {len(essays)} essays.")
    
    for provider in PROVIDERS:
        p_name = provider["name"]
        print(f"\n--- Running for Provider: {p_name} ---")
        
        if not provider["api_key"] or not provider["model"]:
            print(f"Skipping {p_name}: Missing API Key or Model configuration.")
            continue
            
        try:
            llm = LLMClient(
                api_key=provider["api_key"],
                base_url=provider["base_url"],
                model_name=provider["model"]
            )
            
            results = run_agents(essays, llm, p_name)
            
            # Save results
            output_file = f"agent_feedback_results_{p_name}.json"
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(results, f, indent=4)
                print(f"Results for {p_name} saved to {output_file}")
            except Exception as e:
                print(f"Error saving results for {p_name}: {e}")
                
        except ValueError as e:
            print(f"Initialization Error for {p_name}: {e}")
        except Exception as e:
            print(f"Error running {p_name}: {e}")

if __name__ == "__main__":
    main()
