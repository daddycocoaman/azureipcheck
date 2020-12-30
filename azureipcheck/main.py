import ipaddress
import json
from pathlib import Path

import gazpacho
import typer
from clumper import Clumper
from rich.panel import Panel
from rich.progress import track
from rich.columns import Columns


from . import APP_NAME, app_dir, console
from .callbacks import *
from .constants import DOWNLOAD_URLS
from .styles import CustomHelpColorsCommand, CustomHelpColorsGroup
from .utils import *

app = typer.Typer(
    name=APP_NAME,
    cls=CustomHelpColorsGroup,
    context_settings={"help_option_names": ["-h", "--help"]},
)

state = {"verbose": False}


@app.command(cls=CustomHelpColorsCommand)
def check(ip: str = typer.Argument(..., help="IP Address to check")):
    """Check IP or CIDR against Azure service tags"""

    if not list(Path(app_dir).glob("ServiceTags_*.json")):
        console.print(
            "No service tag JSONs found. Run [bold yellow]azureipcheck update"
        )
        raise typer.Exit(-1)

    try:
        addr = ipaddress.ip_network(ip, strict=False)
    except ValueError:
        raise typer.BadParameter("Must provide a valid IPv4/IPv6 address or network!")

    clumper = Clumper.read_json(str(Path(app_dir) / "ServiceTags_*.json"))
    service_list = (
        clumper.select("cloud", "values")
        .explode("values")
        .keep(lambda d: d["values"]["id"] != "AzureCloud")
        .collect()
    )

    found = []
    for service in service_list:
        addresses = list(
            map(
                ipaddress.ip_network, service["values"]["properties"]["addressPrefixes"]
            )
        )
        for network in addresses:
            if type(addr) == type(network):
                if addr.subnet_of(network):
                    found.append({"service": service, "netmatch": network})

    if state["verbose"]:
        console.print([service["service"] for service in found])
    else:
        render_groups = [
            Panel(
                "\n".join(
                    [
                        f'[bold green]Cloud:[/bold green] {service["service"]["cloud"]}',
                        f'[bold green]Network:[/bold green] {service["netmatch"]}',
                        f'[bold green]Service:[/bold green] {service["service"]["values"]["name"]}',
                        f'[bold green]Features:[/bold green] {str(service["service"]["values"]["properties"]["networkFeatures"])}',
                    ]
                ),
                title=f"[bold cyan]{ip}",
                border_style="green",
            )
            for service in found
        ]
        console.print(Columns(render_groups))


@app.command(cls=CustomHelpColorsCommand)
def update():
    """Update JSON files for service tags"""

    downloaded_files = []
    for url in track(DOWNLOAD_URLS.values(), "Downloading service tag files..."):
        html = gazpacho.Soup(gazpacho.get(url))
        download_url = html.find("td", {"class": "file-link"}).find("a").attrs["href"]
        filename = download_url.split("/")[-1]
        file_json = gazpacho.get(download_url)
        with open(Path(app_dir) / filename, "wb") as output:
            output.write(file_json.encode())
        downloaded_files.append(str(Path(app_dir) / filename))
    console.print(Panel.fit("Service Tag files downloaded!", border_style="green"))
    console.print(downloaded_files)


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
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    """Checks the service tags of an Azure IP."""
    if verbose:
        state["verbose"] = True
    else:
        print()


if __name__ == "__main__":
    app()
