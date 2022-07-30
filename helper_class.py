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
            f.write("## Summary\n")
            f.write(self.summary + "\n")
            f.close()
    
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






