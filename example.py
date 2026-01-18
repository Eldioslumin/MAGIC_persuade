from prompts.baseline import GREGeneralGraderPrompts
from prompts.agents import GREAgentPrompts
from prompts.orchestrator import GREOrchestratorPrompts
from prompts.judge import RubricJudgePrompts

def main():
    grading_instruction = {
        "essay_text": "The essay text is here",
        "prompt": "The essay prompt is here",
    }
    print(GREGeneralGraderPrompts.format_prompt_inference(grading_instruction, current_rubric="Example rubric."))
    print(GREAgentPrompts.format_prompt_inference(grading_instruction, agent_rubric_type="major_thesis", current_aspect_rubric="Example rubric."))
    print(GREOrchestratorPrompts.format_prompt_inference(grading_instruction, domain_scores=[5, 5, 5, 5, 5], domain_feedbacks=["Example feedback 1", "Example feedback 2", "Example feedback 3", "Example feedback 4", "Example feedback 5"]))
    print(RubricJudgePrompts.format_prompt_judge(feedback_1="Example feedback 1", feedback_2="Example feedback 2", student_essay="The essay text is here", prompt="The essay prompt is here"))

if __name__ == "__main__":
    main()