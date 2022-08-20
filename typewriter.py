import click
from canvas import Canvas
from helper import MarkdownFile

pass_canvas = click.make_pass_decorator(Canvas)

def get_version():
    with open("setup.py") as f:
        for line in f:
            if "version" in line:
                return line.split("=")[1].strip()[1:-1]

@click.group()
@click.version_option("get_version()")
@click.pass_context
def cli(ctx):
    ctx.obj = Canvas()

@cli.command()
@click.option('--title', required=True, help='The title of the article.')
@click.option('--input_file', required=True, help='Path to a file containing a list of questions')
@click.option('--output_file', required=True, help='Path to a canvas json file.')
@click.option('--options', required=False, default=3, help='Number of answers to generate. Default is 3.')
@pass_canvas
def create_canvas(canvas, title, input_file, output_file, options):
    """ Create a canvas json file from a list of questions. """
    canvas.create_canvas(title, input_file, output_file, options)

@cli.command()
@click.option('--canvas_file', required=True, help='Path to a canvas json file.')
@pass_canvas
def show_canvas(canvas, canvas_file):
    """ Show content of a canvas json file. """
    canvas.show_canvas(canvas_file)

@cli.command()
@click.option('--canvas_file', required=True, help='Path to a canvas json file.')
@click.option('--question_number', required=True, help='A question id to add an answer to.')
@pass_canvas
def add_new_answer(canvas, canvas_file, question_number):
    """ Add a new answer to a question. """
    canvas.add_new_answer(canvas_file, question_number)

@cli.command()
@click.option('--canvas_file', required=True, help='Path to a canvas json file.')
@pass_canvas
def save_article(canvas, canvas_file):
    """ Save an article to a markdown file. """
    canvas = canvas.read_json_file(canvas_file)
    article = MarkdownFile(canvas)
    article.save_file()
    