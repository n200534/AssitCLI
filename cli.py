import click
from assistant.explain import explain_code

@click.group()
def cli():
    pass

@cli.command()
@click.option('--code', help='Code snippet to explain', required=False)
@click.option('--file', type=click.Path(exists=True), help='Path to code file to explain')
def explain(code, file):
    """Explain code snippet or file."""
    if not code and not file:
        click.echo("Error: Please provide either --code or --file option.")
        return

    if file:
        with open(file, 'r') as f:
            code = f.read()

    click.echo("Sending code to AI for explanation...")
    explanation = explain_code(code)
    click.echo("\nExplanation:\n")
    click.echo(explanation)
