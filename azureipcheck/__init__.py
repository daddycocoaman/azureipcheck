from pathlib import Path

import typer
from rich import pretty, traceback
from rich.console import Console

APP_NAME = "azureipcheck"

console = Console()
traceback.install(show_locals=True)
pretty.install()

app_dir = typer.get_app_dir(APP_NAME)

if not app_dir.exists():
    Path(app_dir).mkdir(parents=True)


__all__ = ["APP_NAME", "console", "app_dir"]