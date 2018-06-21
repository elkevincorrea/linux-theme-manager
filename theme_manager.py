import sys
from enum import Enum
import git_theme
import click

class Mode(Enum):
    GIT = "git"

@click.group()
def cli():
    pass

@cli.command()
@click.argument('theme_path')
def add(theme_path):
    """
    Add a theme given a THEME_PATH which must be a git url
    """
    git_theme.add_from_git(theme_path)