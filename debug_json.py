
import os
import json
from openai import OpenAI
from prompts.agents import GREAgentPrompts

# Mock grading instruction
grading_instruction = {
    "essay_text": "Drivers should not use phones. It is bad. Very bad.",
    "prompt": "Should drivers use phones?"
}

# Setup client
client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

def test_generation(use_json_mode=True):
    print(f"\n--- Testing with JSON Mode: {use_json_mode} ---")
    
    # Vocabulary prompt
    aspect_name = "vocabulary"
    aspect_rubric = GREAgentPrompts.aspect_rubrics[3][1] # Vocabulary rubric
    
    prompt_text = GREAgentPrompts.format_prompt_inference(
        grading_instruction, 
        agent_rubric_type=aspect_name, 
        current_aspect_rubric=aspect_rubric 
    )

    try:
        kwargs = {
            "model": "deepseek-r1:8b",
            "messages": [{"role": "user", "content": prompt_text}],
            "temperature": 0.0,
            "max_tokens": 1000
        }
        if use_json_mode:
            kwargs["response_format"] = {"type": "json_object"}

        response = client.chat.completions.create(**kwargs)
        content = response.choices[0].message.content
        print(f"Content Length: {len(content) if content else 0}")
        print(f"Raw Content Preview: {content[:200] if content else 'EMPTY'}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Test WITH JSON mode (current behavior)
    test_generation(use_json_mode=True)
    
    # Test WITHOUT JSON mode (proposed fix)
    test_generation(use_json_mode=False)
