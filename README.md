# The Typewriter AI - automated article creation.
The Typewriter helps you convert your ideas into a readable article. It uses a pre-trained model to generate responses to your questions. It also helps you automate all phases of article creation - from the brainstorming phase to the final article, including proofreading, source validation, formatting, peer review, and publishing. Using this iteravite approach, your ideas and questions are converted into a coherent article.


# How it works?
This is an app that will generate an article based on the list of topics and questions provided. 
It uses OpenAI GPT-3 to generate responses and assembles the article based on a template.

- prepare a list of topics and questions (e.g. "What is the best way to learn to code?")
- select a template (e.g. "templates/article.md" or "templates/brainshtorming.md") )
- generate an article using the template and the list of questions and topics
- enjoy your article!


# Prerequisites
Required environment variable:
```
export OPENAI_API_KEY=<your_api_key>
```

# Installation
```
python -m venv .venv
source .venv/bin/activate
pip install --editable .
```
# Test installation
```
typewriter --version
```

# Usage
## Prepare list of questions
Save your questions to a file. Each question should be on a separate line.
Here is an example of a list of questions:
```
$ cat data/input.txt

What is the knowledge economy?
How to thrive in the knowledge economy as a business?
```

## Generating a canvas
First you need to create a canvas for an article. Canvas is a blueprint in a json format. It contains title,introduction, summary and list of questions and answers. 

You can create a canvas by running the following command:

```
$ typewriter create-canvas \
--title "How to thrive in the Knowledge Economy?" \
--input_file "data/input.txt" \
--output_file "data/out.json" \
--options 3

Output:
Generating an answer for a question - What is the knowledge economy? . . . Done.
Generating an answer for a question - How to thrive in the knowledge economy as a business? . . . Done.
```

## Review the canvas
Canvas saved in json format can be reviewed by running the following command:

```
$ typewriter show-canvas --canvas_file "data/out.json"

Output (truncated for readability):
{
    "title": "How to thrive in the Knowledge Economy?",
    "introduction": "\n\nIn today's society, the term \"knowledge economy\" is used to describe the production and exchange of knowledge and information. The knowledge economy has transformed the way we live and work, and it is becoming increasingly important in the global marketplace. As the world becomes more interconnected, the demand for knowledge workers is growing. In order to thrive in the knowledge economy, it is essential to ...",
    "questions": {
        "q0": {
            "type": "text",
            "question": "What is the knowledge economy?",
            "answers": [
                "\n\nThe knowledge economy is an economy where knowledge is a key factor of production. This may include knowledge of technology, science, and processes.",
                "\n\nThe knowledge economy is an economy which is primarily based on the production and distribution of knowledge and information. The term was first coined in the late 1960s ..."
            ]
        },
}
```

## Add new answer
Sometimes you want to see more answer options for a particular questions. You can do this by running the following command:

```
typewriter add-new-answer --canvas_file "data/out.json" --question_number "q1"
```

## Generating an article
Once you satisfied with the canvas, you can generate an article by running the following command:

```
typewriter save-article --canvas_file "data/out.json"
```

# An example of generated article
The output article is saved in the artciles folder.

Here is an example of generated article:

[HOW_TO_THRIVE_IN_THE_KNOWLEDGE_ECONOMY.md](articles/HOW_TO_THRIVE_IN_THE_KNOWLEDGE_ECONOMY.md)