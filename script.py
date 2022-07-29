import openai
import os


ARTICLE_NAME="How to thrive in the Knowledge Economy?" 
ARTICLE_NAME_WITH_UNDERSCORE = ARTICLE_NAME.replace(" ", "_").replace("?", "")

QUESTIONS = {
    "What is the knowledge economy?":[],
    "How to thrive in the knowledge economy?":[],
    "How to make money in the knowledge economy?":[],
    "How to stay independent in the knowledge economy?":[],
    "How to make a good life in the knowledge economy?":[],
    "What are the backwards-looking issues in the knowledge economy?":[],
    "Summary: How to be successfull in the knowledge economy?":[],
}

"""
A function to call openai to generate a text response to a question.
"""
def get_answser(question, max_tokens=1000, temperature=0.8):
    # Get the answer from openai
    openai.api_key = os.environ['OPENAI_API_KEY']
    response = openai.Completion.create(engine='text-davinci-002', prompt=question,  max_tokens=max_tokens, temperature=temperature)
    return response.choices[0].text

"""
A function to iterate over a list of questions, get the answers and save answer to them to the output.
"""
def print_answers(questions):
    for question in questions:
        answer = get_answser(question)
        # print(question)
        # print(answer)
        # print()
        questions[question].append(answer)

"""
A function that iterates overa a dictionary of questions and answers and save outout to a *.MD file.
Each questions should be on a new line formatter as the second largest heading.
Each answer should be on a new line formatter as regular text.
"""


"""
A function that creates a markdown file with the questions and answers.
Where each question is on a new line formatter as the second largest heading.
And each answer is on a new line formatter as regular text.
"""
def create_markdown_file(questions, output_file_name):
    with open(output_file_name, "w") as file:
        for question in questions:
            file.write("## " + question + "\n")
            for answer in questions[question]:
                file.write(answer + "\n")
            file.write("\n")


"""
a function that submit the markdown file to grammatly api and get the grammatly analysis.
"""



# print(QUESTIONS[0])
# print(get_answser(QUESTIONS[0]))

print_answers(QUESTIONS)

create_markdown_file(QUESTIONS, f'{ARTICLE_NAME_WITH_UNDERSCORE}.md')




