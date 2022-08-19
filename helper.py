class MarkdownFile:
    def __init__(self, canvas):
        self.canvas = canvas
        self.title = canvas["title"]
        self.introduction = canvas["introduction"]
        self.content = ""
        self.summary = canvas["summary"]
        self.separator = "-" * 100
    
    def save_file(self):
        self.create_markdown_file(self.contstruct_output_file_name())
    
    def create_markdown_file(self, output_file_name):
        
        self.add_content_to_article()

        with open(f"articles/{output_file_name}", 'w') as f:
            f.write(f"# {self.title}")
            f.write(self.introduction + "\n")
            f.write("\n")
            f.write(self.content + "\n")
            f.write("## Summary\n")
            f.write(self.summary + "\n")
            f.close()
    

    def add_content_to_article(self):
        questions = self.canvas["questions"]
        for id in questions:
            self.add_question_to_article(questions[id]["question"])
            self.add_separator_to_article()
            for index, answer in enumerate(questions[id]["answers"]):
                self.add_answer_to_article(f"Option {index + 1} - {answer}\n")


    def add_separator(self, symbol):
        self.separator = symbol
        
    def add_separator_to_article(self):
        self.content += "\n" + self.separator + "\n"
        
    def add_question_to_article(self, question):
        self.content += "## " + question + "\n"
        
    def add_answer_to_article(self, answer):
        self.content += "\n" + answer + "\n"

    def contstruct_output_file_name(self):
        output_file_name = self.remove_non_alphanumeric_characters(self.title)
        return output_file_name.upper() + ".md"


    def remove_non_alphanumeric_characters(self, string):
        """
        a function that remove any not-alphanumeric characters from a string except for spaces.
        if char is a space replace it with an underscore.
        """
        return ''.join(char for char in string if char.isalnum() or char == " ").replace(" ", "_")
    
        
