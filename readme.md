# azureipcheck

<div align="center">
    <img src="https://img.shields.io/pypi/v/azureipcheck"/>
    <img src="https://img.shields.io/pypi/pyversions/azureipcheck"/>
    <img src="https://img.shields.io/pypi/l/azureipcheck"/>
    <a href="https://twitter.com/mcohmi"><img src="https://img.shields.io/twitter/follow/mcohmi.svg?style=plastic"/></a><br>
</div>

A Python [Typer-based](https://github.com/tiangolo/typer) CLI tool to check IP addresses against Azure services. It also uses [Rich](https://github.com/willmcgugan/rich) for some dope console output. Additionally, it makes use of [Clumper](https://github.com/koaning/clumper) for parsing through the Azure Service Tag JSON files.


## Installation

The recommended method of installation is with [pipx](https://github.com/pipxproject/pipx). 

```
pipx install azureipcheck
```

However, you can install the normal way from PyPi with `python3 -m pip install azureipcheck`.

## Usage

You should first run `azureipcheck update` to download the latest Service Tag JSON files. After downloading the files locally, you can run `azureipcheck check <ip>`, where `ip` can be a single address or CIDR (i.e., `51.8.227.233` or `51.8.227.233/24`). 

Checking a CIDR does not check every IP in the network provided. It simply checks to see if the network is in a subnet of any of the Azure network ranges. Therefore `51.8.227.233/24` may return matches but `51.8.227.233/8` would not. 


### Built With
- Typer: https://github.com/tiangolo/typer
- Rich: https://github.com/willmcgugan/rich
- Clumper: https://github.com/koaning/clumper
- Gazpacho: https://github.com/maxhumber/gazpacho
- Cookiecutter-RichTyper: https://github.com/daddycocoaman/cookiecutter-richtyper

Inspired by https://github.com/deanobalino/azureip


