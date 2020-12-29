import requests
from importlib.metadata import version

import typer

from . import APP_NAME, console, app_dir
from .styles import CustomHelpColorsCommand, CustomHelpColorsGroup

app = typer.Typer(
    name=APP_NAME,
    cls=CustomHelpColorsGroup,
    context_settings={"help_option_names": ["-h", "--help"]},
)


def version_callback(value: bool):
    if value:
        console.print(f"[bold green]{APP_NAME}[/bold green]: {version(APP_NAME)}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        callback=version_callback,
        is_eager=True,
        show_default=False,
        help="Display version information",
    ),
):
    pass

@app.command()
def update(url: typer.Option("")):


if __name__ == "__main__":
    app()
