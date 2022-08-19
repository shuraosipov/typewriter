import click
from canvas import Canvas
from helper import MarkdownFile

pass_canvas = click.make_pass_decorator(Canvas)

@click.group()
@click.version_option("0.1.0")
@click.pass_context
def cli(ctx):
    ctx.obj = Canvas()

@cli.command()
@click.option('--title', required=True, help='Title of the article')
@click.option('--input_file', required=True, help='Path to input_file containing a list of questions')
@click.option('--output_file', required=True, help='Path to output_file')
@click.option('--options', required=False, default=3, help='Number of answers to generate')
@pass_canvas
def create_canvas(canvas, title, input_file, output_file, options):
    canvas.create_canvas(title, input_file, output_file, options)

@cli.command()
@click.option('--canvas_file', required=True, help='Path to a canvas json file.')
@pass_canvas
def show_canvas(canvas, canvas_file):
    canvas.show_canvas(canvas_file)

@cli.command()
@click.option('--canvas_file', required=True, help='Path to a canvas json file.')
@click.option('--question_number', required=True, help='A question number to add a new answer to.')
@pass_canvas
def add_new_answer(canvas, canvas_file, question_number):
    canvas.add_new_answer(canvas_file, question_number)

@cli.command()
@click.option('--canvas_file', required=True, help='Path to a canvas json file.')
@pass_canvas
def save_article(canvas, canvas_file):
    canvas = canvas.read_json_file(canvas_file)
    article = MarkdownFile(canvas)
    article.save_file()
    