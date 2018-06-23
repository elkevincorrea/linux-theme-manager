from git import Repo
import os
import tempfile
import shutil
import click

def add_from_git(git_url):
    with tempfile.TemporaryDirectory() as tmpdirname:
        dir = clone(git_url, tmpdirname)
        theme_dir = get_themes_dirs(dir)
        if theme_dir != None:
            install_theme(theme_dir)

def is_icon(theme_dir):
    with open(os.path.join(theme_dir, 'index.theme')) as index_theme:
        first_line = index_theme.readline()
        return str(first_line).find("[Icon Theme]") != -1
            

def clone(git_url, tmpdirname):
    """
    Clones a repo to a temp dir
    """
    repo_name = os.path.splitext(os.path.basename(git_url))[0]
    repo = Repo.clone_from(git_url, os.path.join(tmpdirname, repo_name), branch = 'master')
    return os.path.dirname(repo.git_dir)

def get_themes_dirs(dirname):
    theme_dir = None
    if os.path.exists(os.path.join(dirname, 'index.theme')):
        theme_dir = dirname
    return theme_dir

def install_theme(theme_dir):
    """
    Install a theme for the current user
    """
    target_dir = os.path.join(os.environ['HOME'], '.themes/' if not is_icon(theme_dir) else '.icons/')
    if not os.path.exists(os.path.join(target_dir, os.path.basename(theme_dir))):
        shutil.move(theme_dir, target_dir)
    else:
        click.secho("The theme already exists", fg="yellow")