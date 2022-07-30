import openai
import os
from helper_class import MarkdownFile


"""
A function that calls the openai to get a response for a given prompt.
"""
def get_answser(question, max_tokens=1000, temperature=1):
    openai.api_key = os.environ['OPENAI_API_KEY']
    response = openai.Completion.create(engine='text-davinci-002', prompt=question,  max_tokens=max_tokens, temperature=temperature)
    return response.choices[0].text

"""
A function to iterate over a list of questions, get the answers from openai and save them back to the content dict.
"""

# TODO - rewrite this function to minimize the number of calls to openai

def add_answers(questions):
    for question in questions:
        print("Question: " + question)
        print("Generating an answer...", end =" ")
        
        for _ in range(2):
            answer = get_answser(question)
            print(".", end =" ")
            questions[question].append(answer)

        print("Done.")
        
        print()
        questions[question].append(answer)

def create_markdown_file(title, introduction, content, summary,output_file_name):
    article = MarkdownFile()
    article.add_title_to_article(title)
    article.add_introduction_to_article(introduction)
    article.add_content_to_article(content)
    article.add_summary_to_article(summary)
    article.save_file(output_file_name) 


def main(title, content, output_file_name):
    print(f"Generating an article - {title}")
    print()

    # Generate the introduction
    introduction = get_answser(f"Generate a blog post intro about the following topic {title}")

    # Generate the summary
    summary = get_answser(f"Generate a blog post summary about the following topic {title}")

    # update content with the answers
    add_answers(content)

    # Create the markdown file
    create_markdown_file(title, introduction, content, summary, f'{output_file_name}.md')


if __name__ == "__main__":

    ARTICLE_NAME="How to thrive in the Knowledge Economy?" 
    ARTICLE_NAME_WITH_UNDERSCORE = ARTICLE_NAME.replace(" ", "_").replace("?", "")

    CONTENT = {
        "What is the knowledge economy?":[],
        "How to thrive in the knowledge economy as a business?":[],
        "How to thrive in the knowledge economy as an employee?":[],
        "How to thrive in the knowledge economy as an individual?":[],
        "How the knowledge economy affects my privacy and freedom?":[],
        "How to stay independent in the knowledge economy?":[],
        "How to monetize knowledge in the knowledge economy?":[],
        "How do you transition from being an employee to a successful entrepreneur in the knowledge economy?":[],
        "Can you give me an example of a knowledge-based product?":[],
        "What are the drawbacks of the knowledge economy?":[],
        "What would be the next stage in the economic development after the knowledge economy?":[],
        "What are the stages of the economy, starting from agriculture?":[],
    }

    TEST_CONTENT = {
        "What is the knowledge economy?":[],
        "How to monetize knowledge in the knowledge economy?":[],
    }

    
    main(ARTICLE_NAME, CONTENT, f"{ARTICLE_NAME_WITH_UNDERSCORE}")    





