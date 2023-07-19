import typer

from .co_utils import get_cpu_limit

app = typer.Typer()


@app.command()
def main():
    """This function returns an integer corresponding to the number of cores available"""
    typer.echo(get_cpu_limit())
