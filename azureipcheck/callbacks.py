from importlib.metadata import version

import typer

from . import APP_NAME, console


def version_callback(value: bool):
    """Displays the version of azureipcheck."""

    if value:
        console.print(f"[bold green]{APP_NAME}[/bold green]: {version(APP_NAME)}")
        raise typer.Exit()