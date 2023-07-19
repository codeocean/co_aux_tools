import typer

from .co_utils import is_pipeline

app = typer.Typer()


@app.command()
def main():
    """Returns '1' if the current computation is in a pipeline utilizing AWS Batch.
    Returns '0' otherwise."""
    typer.echo(is_pipeline())
