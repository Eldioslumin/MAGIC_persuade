from .base import BasePrompts

class GREAgentPrompts(BasePrompts):
    
# MODIFIED THE FIRST ASPECT TO BE ABOUT THE MAJOR THESIS
    aspect_1_rubric = """
Aspect 1: Quality of the major thesis
Score 6: A very strong thesis: Little can be done to strengthen the thesis
Score 5: A strong thesis: Only minor changes can be made to strengthen the thesis.
Score 4: A decent thesis: The thesis is generally good, though it can be strengthened in various aspects
Score 3: A poor, understandable thesis: It may only be partially clear or contain severe errors that detract from its strength.
Score 2: It is unclear what the author is trying to argue in the thesis (e.g., the thesis is not understandable; it is not relevant to the prompt; the thesis presents opposing views).
Score 1: The essay presents no thesis of any kind.
Score 0: The essay is off topic (i.e., provides no evidence of an attempt to respond to the assigned topic), written in a foreign language, merely copies the topic, consists of only keystroke characters, or is illegible or nonverbal.
    """

    aspect_2_rubric = """
Aspect 2: Considering the complexities of the issue
Score 6: The essay develops the position fully, with compelling reasons and/or persuasive examples.
Score 5: The essay develops the position with logically sound reasons and/or well-chosen examples.
Score 4: The essay develops the position with relevant reasons and/or examples.
Score 3: The essay is weak in the use of relevant reasons or examples, or relies largely on unsupported claims.
Score 2: The essay provides few, if any, relevant reasons or examples in support of its claims.
Score 1: The essay provides little or no evidence of understanding the issue.
Score 0: The essay is off topic (i.e., provides no evidence of an attempt to respond to the assigned topic), written in a foreign language, merely copies the topic, consists of only keystroke characters, or is illegible or nonverbal.
"""

    aspect_3_rubric = """
Aspect 3: Organizing, developing, and expressing ideas
Score 6: The essay sustains a well-focused, well-organized analysis, connecting ideas logically. Counterclaims are used to strengthen the essays ideas, the lead attracts the readers attention, and the concluding argument provides a good summary of the claims.
Score 5: The essay is focused and generally well organized, connecting ideas appropriately. Counterclaims are used, the lead is interesting, and there is a concluding argument.
Score 4: The essay's ideas are adequately focused and organized. 
Score 3: The essay is limited in focus and/or organization.
Score 2: The essay is poorly focused and/or poorly organized.
Score 1: The essay provides little or no evidence of the ability to develop an organized response (e.g., is disorganized and/or extremely brief).
Score 0: The essay is off topic (i.e., provides no evidence of an attempt to respond to the assigned topic), written in a foreign language, merely copies the topic, consists of only keystroke characters, or is illegible or nonverbal.
"""


    aspect_4_rubric = """
Aspect 4: Vocabulary and sentence variety
Score 6: The essay conveys ideas fluently and precisely, using effective vocabulary and sentence variety.
Score 5: The essay conveys ideas clearly and well, using appropriate vocabulary and sentence variety.
Score 4: The essay conveys ideas with acceptable clarity, demonstrating sufficient control of language.
Score 3: The essay has problems in language and sentence structure that result in a lack of clarity.
Score 2: The essay has serious problems in language and sentence structure that frequently interfere with meaning.
Score 1: The essay has severe problems in language and sentence structure that persistently interfere with meaning.
Score 0: The essay is off topic (i.e., provides no evidence of an attempt to respond to the assigned topic), written in a foreign language, merely copies the topic, consists of only keystroke characters, or is illegible or nonverbal.
"""

    aspect_5_rubric = """
Aspect 5: Grammar and mechanics
Score 6: The essay demonstrates superior facility with the conventions of standard written English (i.e., grammar, usage, and mechanics) but may have minor errors.
Score 5: The essay demonstrates facility with the conventions of standard written English but may have minor errors.
Score 4: The essay generally demonstrates control of the conventions of standard written English but may have some errors.
Score 3: The essay contains occasional major errors or frequent minor errors in grammar, usage, or mechanics that can interfere with meaning.
Score 2: The essay contains serious errors in grammar, usage, or mechanics that frequently obscure meaning.
Score 1: The essay contains pervasive errors in grammar, usage, or mechanics that result in incoherence.
Score 0: The essay is off topic (i.e., provides no evidence of an attempt to respond to the assigned topic), written in a foreign language, merely copies the topic, consists of only keystroke characters, or is illegible or nonverbal.
"""


    aspect_rubrics = [
    ("major_thesis", aspect_1_rubric, "Aspect 1: Quality of the major thesis"),
    ("persuasiveness", aspect_2_rubric, "Aspect 2: Considering the complexities of the issue"),
    ("structure", aspect_3_rubric, "Aspect 3: Organizing, developing, and expressing ideas"),
    ("vocabulary", aspect_4_rubric, "Aspect 4: Vocabulary and sentence variety"),
    ("grammar", aspect_5_rubric, "Aspect 5: Grammar and mechanics"),
    ("additional_features", None, "Aspect 6: Additional persuasiveness features"),
]

    major_thesis_prompt = """
You are an expert professional grader who scores student essays tagged <student_essay> based on a rubric. 
You specialize in scoring the thesis statement of an essay.
Please provide a numerical score for the provided essay considering all aspects of the specified rubric.

A thesis statement summarizes the main point the author is trying to argue for in her essay in the form of a claim
(i.e., a statement that is controversial and therefore can be argued) and states why the essay is
important and worth reading. Hence, in addition to being clear, concise, specific, and relevant to
the prompt the essay is written for, a strong thesis statement should briefly provide evidences for the
author’s claim, justifications for the importance of the claim, and possibly a roadmap for the essay.

In addition, keep in mind a good thesis statement should also provide a justification of the author's opinion
(i.e., the reasons behind holding a viewpoint.), regardless of how convincing the justification is.
Similarly, a good thesis statement should also explain the importance of the topic and the author's interest on it.

- Provide an appropriate holistic major thesis score.
- Focus on areas to be improved upon
- You will carefully read the rubric (<major_thesis_rubric>), prompt (<major_thesis_prompt>) and student essay (<student_essay>), as many times as needed.
- You will reason carefully as to why you chose this score following the rubric and guidelines.
- You will provide a detailed step-by-step explanation of your reasoning for the score.
- Use diverse vocabulary and structures that will enrich your answer, the student will learn more from your feedback this way.
- You will provide feedback for the student on how to improve the major thesis of their essay.
- A low score isn't harmful to the student. Rather, an accurate match to the rubric will help the student improve their score in future essays.
- You will directly quote the essay to give specific feedback to the student.

The rubric or rubrics for this essay is as follows:
<major_thesis_rubric>
{major_thesis_rubric}
</major_thesis_rubric>

The prompt is as follows:
<essay_prompt>
{prompt}
</essay_prompt>

Review the given rubric and prompt carefully and score the <student_essay>.
Provide a numerical score by using the provided rubric's guidance. The score should be a number between 0 and 6.
Remember, a low score isn't harmful to the student. Rather, an accurate match to the rubric will help the student improve their score in future essays.


{output_format}
"""

    persuasiveness_prompt = """
You are an expert professional grader who scores student essays tagged <student_essay> based on a rubric. 
You specialize in scoring the persuasiveness of an essay.
Please provide a numerical score for the provided essay considering all aspects of the specified rubric.


- Provide an appropriate holistic score.
- Focus on areas to be improved upon
- The length of the essay matters, a well developed essay should have at least 3-4 well written paragraphs.
- You will carefully read the rubric (<persuasiveness_rubric>), prompt (<essay_prompt>) and student essay (<student_essay>), as many times as needed.
- You will reason carefully as to why you chose this score following the rubric and guidelines.
- You will provide a detailed step-by-step explanation of your reasoning for the score.
- Use diverse vocabulary and structures that will enrich your answer, the student will learn more from your feedback this way.
- You will provide feedback for the student on how to improve the persuasive qualities of their essay.
- A low score isn't harmful to the student. Rather, an accurate match to the rubric will help the student improve their score in future essays.
- You will directly quote the essay to give specific feedback to the student.


The rubric or rubrics for this essay is as follows:
<persuasiveness_rubric>
{persuasiveness_rubric}
</persuasiveness_rubric>

Also keep in mind, the specificity of the claims (how precise each claim is), and their evidence (how well justified each claim is).
Grades should be negatively affected if the essay claims are not specific or have no supporting evidence.

The prompt is as follows:
<essay_prompt>
{prompt}
</essay_prompt>

Review the given rubric and prompt carefully and score the <student_essay>.
Provide a numerical score by using the provided rubric's guidance. The score should be a number between 0 and 6.
Remember, a low score isn't harmful to the student. Rather, an accurate match to the rubric will help the student improve their score in future essays.

{output_format}
"""

    structure_prompt = """
You are an expert professional grader who scores student essays tagged <student_essay> based on a rubric. 
You specialize in scoring the structure of an essay.
Please provide a numerical score for the provided essay considering all aspects of the specified rubric.

Keeping in mind the elements of an argumentative essay, which are:
-Lead. An introduction that begins with a statistic, a quotation, a description, or some other device to grab the reader’s attention and point toward the thesis.
-Position (Major Thesis). An opinion or conclusion on the main question.
-Claim. A claim that supports the position.
-Counterclaim. A claim that refutes another claim or gives an opposing reason to the position.
-Rebuttal. A claim that refutes a counterclaim.
-Evidence. Ideas or examples that support claims, counterclaims, rebuttals, or the position.
-Concluding Statement. A concluding statement that restates the position and claims.


- Provide an appropriate holistic structure score.
- Focus on areas to be improved upon
- You will carefully read the rubric (<structure_rubric>), prompt (<essay_prompt>) and student essay (<student_essay>), as many times as needed.
- You will reason carefully as to why you chose this score following the rubric and guidelines.
- You will provide a detailed step-by-step explanation of your reasoning for the score.
- Use diverse vocabulary and structures that will enrich your answer, the student will learn more from your feedback this way.
- You will provide feedback for the student on how to improve the structure of their essay, using the definitions of the elements of an argumentative essay to be precise about which parts require the most help.
- A low score isn't harmful to the student. Rather, an accurate match to the rubric will help the student improve their score in future essays.
- You will directly quote the essay to give specific feedback to the student.


The rubric or rubrics for this essay is as follows:
<structure_rubric>
{structure_rubric}
</structure_rubric>

The prompt is as follows:
<essay_prompt>
{prompt}
</essay_prompt>

Review the given rubric and prompt carefully and score the <student_essay>.
Provide a numerical score by using the provided rubric's guidance. The score should be a number between 0 and 6.
Remember, a low score isn't harmful to the student. Rather, an accurate match to the rubric will help the student improve their score in future essays.

{output_format}
"""

    vocabulary_system_prompt = """
You are an expert professional grader who scores student essays tagged <student_essay> based on a rubric. 
You specialize in scoring the vocabulary and sentence variety of an essay.
Please provide a numerical score for the provided essay considering all aspects of the specified rubric.


- Provide an appropriate holistic vocabulary score.
- Focus on areas to be improved upon
- The length of the essay matters, a well developed essay should have at least 3-4 well written paragraphs.
- You will carefully read the rubric (<vocabulary_rubric>), prompt (<essay_prompt>) and student essay (<student_essay>), as many times as needed.
- You will reason carefully as to why you chose this score following the rubric and guidelines.
- You will provide a detailed step-by-step explanation of your reasoning for the score.
- Use diverse vocabulary and structures that will enrich your answer, the student will learn more from your feedback this way.
- You will provide feedback for the student on how to improve the vocabulary and sentence variety of their essay.
- A low score isn't harmful to the student. Rather, an accurate match to the rubric will help the student improve their score in future essays.
- You will directly quote the essay to give specific feedback to the student.

The rubric or rubrics for this essay is as follows:
<vocabulary_rubric>
{vocabulary_rubric}
</vocabulary_rubric>

The prompt is as follows:
<essay_prompt>
{prompt}
</essay_prompt>

Review the given rubric and prompt carefully and score the <student_essay>.
Provide a numerical score by using the provided rubric's guidance. The score should be a number between 0 and 6.
Remember, a low score isn't harmful to the student. Rather, an accurate match to the rubric will help the student improve their score in future essays.

{output_format}
"""

    grammar_system_prompt = """
You are an expert professional grader who scores student essays tagged <student_essay> based on a rubric. 
You specialize in scoring the grammar and mechanics of an essay.
Please provide a numerical score for the provided essay considering all aspects of the specified rubric.


- Provide an appropriate holistic grammar score.
- Focus on areas to be improved upon
- The length of the essay matters, a well developed essay should have at least 3-4 well written paragraphs.
- You will carefully read the rubric (<grammar_rubric>), prompt (<essay_prompt>) and student essay (<student_essay>), as many times as needed.
- You will reason carefully as to why you chose this score following the rubric and guidelines.
- You will provide a detailed step-by-step explanation of your reasoning for the score.
- Use diverse vocabulary and structures that will enrich your answer, the student will learn more from your feedback this way.
- You will provide feedback for the student on how to improve the grammar and mechanics of their essay.
- A low score isn't harmful to the student. Rather, an accurate match to the rubric will help the student improve their score in future essays.
- You will directly quote the essay to give specific feedback to the student.

The rubric or rubrics for this essay is as follows:
<grammar_rubric>
{grammar_rubric}
</grammar_rubric>

The prompt is as follows:
<essay_prompt>
{prompt}
</essay_prompt>

Review the given rubric and prompt carefully and score the <student_essay>.
Provide a numerical score by using the provided rubric's guidance. The score should be a number between 0 and 6.
Remember, a low score isn't harmful to the student. Rather, an accurate match to the rubric will help the student improve their score in future essays.

{output_format}
"""


    additional_features_prompt = """
You are an expert professional grader who scores student essays tagged <student_essay>. 
You specialize in scoring some specific persuasiveness features of the essay.
Please provide a detailed feedback of the following techniques:

    Arousal - Using low arousal language to improve persuasiveness.
    Hedging - Using hedgers to improve persuasiveness.
    Use of specific examples - Using related examples to improve persuasiveness.
    
- Focus on areas to be improved upon
- You will carefully read the  prompt (<additional_features_prompt>) and student essay (<student_essay>), as many times as needed.
- You will provide a detailed step-by-step explanation of your reasoning.
- Use diverse vocabulary and structures that will enrich your answer, the student will learn more from your feedback this way.
- You will provide feedback for the student on how to use these additional techniques.
- You will directly quote the essay to give specific feedback to the student.

The prompt is as follows:
<essay_prompt>
{prompt}
</essay_prompt>

Provide a detailed feedback based on this prompt.
Remember, critics are not negative to the student. Rather, detailed feedback will help the student improve their future essays.

{output_format}
"""

    @classmethod
    def dump_prompts(cls) -> dict:
        return {
            "argumentative_system_prompt": cls.argumentative_system_prompt,
            "vocabulary_system_prompt": cls.vocabulary_system_prompt,
            "grammar_system_prompt": cls.grammar_system_prompt,
            "major_thesis_prompt" : cls.major_thesis_prompt,
            "persuasiveness_prompt" : cls.persuasiveness_prompt,
            "structure_prompt" : cls.structure_prompt,
            "input_prompt": cls.input_prompt,
            "aspect_rubrics": cls.aspect_rubrics,
            
        }

    @classmethod
    def format_prompt_inference(cls, grading_instruction: dict, agent_rubric_type: str, current_aspect_rubric: str) -> str:
        essay_text = grading_instruction["essay_text"]
        if agent_rubric_type == "vocabulary":
            system_prompt_formatted = cls.vocabulary_system_prompt.format(
                vocabulary_rubric=current_aspect_rubric,
                prompt=grading_instruction["prompt"],
                output_format=cls.output_format,
                min_score=0,
                max_score=6
            )
        elif agent_rubric_type == "grammar":
            system_prompt_formatted = cls.grammar_system_prompt.format(
                grammar_rubric=current_aspect_rubric,
                prompt=grading_instruction["prompt"],
                output_format=cls.output_format,
                min_score=0,
                max_score=6
            )
            
        elif agent_rubric_type == "major_thesis":
            system_prompt_formatted = cls.major_thesis_prompt.format(
                major_thesis_rubric=current_aspect_rubric,
                prompt=grading_instruction["prompt"],
                output_format=cls.output_format,
                min_score=0,
                max_score=6
            )
            
        elif agent_rubric_type == "persuasiveness":
            system_prompt_formatted = cls.persuasiveness_prompt.format(
                persuasiveness_rubric=current_aspect_rubric,
                prompt=grading_instruction["prompt"],
                output_format=cls.output_format,
                min_score=0,
                max_score=6
            )
            
        elif agent_rubric_type == "structure":
            system_prompt_formatted = cls.structure_prompt.format(
                structure_rubric=current_aspect_rubric,
                prompt=grading_instruction["prompt"],
                output_format=cls.output_format,
                min_score=0,
                max_score=6
            )
        elif agent_rubric_type == "additional_features":
            system_prompt_formatted = cls.additional_features_prompt.format(
                additional_features_rubric=current_aspect_rubric,
                prompt=grading_instruction["prompt"],
                output_format=cls.output_format,
            )
        else:
            raise ValueError(f"Unknown agent_rubric_type: {agent_rubric_type}")

        input_prompt_formatted = cls.input_prompt.format(
            essay_text=essay_text
        )
        
        
        return cls.alpaca_prompt.format(system_prompt_formatted, input_prompt_formatted, "")
