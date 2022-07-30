# The Typewriter AI - automated article creation.
The Typewriter helps you convert your ideas into a readable article. It uses a pre-trained model to generate responses to your questions. It also helps you automate all phases of article creation - from the brainstorming phase to the final article, including proofreading, source validation, formatting, peer review, and publishing. Using this iteravite approach, your ideas and questions are converted into a coherent article.


# How it works?
This is an app that will generate an article based on the list of topics and questions provided. 
It uses OpenAI GPT-3 to generate responses and assembles the article based on a template.

- prepare a list of topics and questions (e.g. "What is the best way to learn to code?")
- select a template (e.g. "templates/article.md" or "templates/brainshtorming.md") )
- generate an article using the template and the list of questions and topics
- enjoy the article!


# Prerequisites
Required environment variable:
```
export OPENAI_API_KEY=<your_api_key>
```

# Installation
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Run the app
```
python3 typewriter.py
```

# An example of generated article
[How_to_thrive_in_the_Knowledge_Economy.md](How_to_thrive_in_the_Knowledge_Economy.md)