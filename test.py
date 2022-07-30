"""
class that creates a markdown file.
and has the following methods:
    - create_new_article()
    - add_title_to_article()
    - add_introduction_to_article()
    - save_file()
    
"""
class MarkdownFile:
    def __init__(self):
        self.title = ""
        self.introduction = ""
        self.content = ""
        self.summary = ""
        self.separator = "-" * 100
        
    def add_title_to_article(self, title, heading_level=1):
        self.title = f"# {title}"
        
    def add_introduction_to_article(self, introduction):
        self.introduction = introduction
        
    def add_summary_to_article(self, summary):
        self.summary = summary
        
    def save_file(self, output_file_name):
        self.create_markdown_file(output_file_name)
    
    def create_markdown_file(self, output_file_name):
        with open(output_file_name, 'w') as f:
            f.write(self.title + "\n")
            f.write(self.introduction + "\n")
            f.write(self.content + "\n")
            f.write(self.summary + "\n")
            f.close()
    
    """
    build the markdown file structure like this:
    ## question
    ----- Option 1 -----
    answer

    from the data structure:
    content = {
        "question 1": ["answer 1", "answer 2"],
        "question 2": ["answer 1", "answer 2"],
    """
    def add_content_to_article(self, questions):
        for question in questions:
            self.add_question_to_article(question)
            self.add_separator_to_article()
            for index, answer in enumerate(questions[question]):
                self.add_answer_to_article(f"Option {index + 1} - {answer}")
   
        
    def add_separator(self, symbol):
        self.separator = symbol
        
    def add_separator_to_article(self):
        self.content += "\n" + self.separator + "\n"
        
    def add_question_to_article(self, question):
        self.content += "## " + question + "\n"
        
    def add_answer_to_article(self, answer):
        self.content += "\n" + answer + "\n"
    
if __name__ == "__main__":
    
    title = "How to thrive in the Knowledge Economy?"
    introduction = "In a rapidly changing economy, it's more important than ever to have a wealth of knowledge at your fingertips. Whether you're looking to start a new business or just stay ahead of the curve, here are a few ways to make sure you're thriving in the Knowledge Economy."
    content = {
        "What is the knowledge economy?":[
            "The knowledge economy is where the majority of economic activity is based on providing or using knowledge.", 
            "The knowledge economy is an economy that is driven by knowledge and information. It is an economy in which knowledge and information are used to create wealth and generate social and economic benefits.", 
            "The knowledge economy is an economy that is based on the production and exchange of knowledge and information."
            ],
        "What is the purpose of the knowledge economy?":["Answer A", "Answer B", "Answer C"],
    }
    summary = "This is the summary"

    article = MarkdownFile()
    article.add_title_to_article(title)
    article.add_introduction_to_article(introduction)
    article.add_content_to_article(content)
    article.add_summary_to_article(summary)
    article.save_file("test.md")






