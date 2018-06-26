from git import Repo
import os
import tempfile
import shutil
import click

def add_from_git(git_url):
    with tempfile.TemporaryDirectory() as tmpdirname:
        temp_dir = clone(git_url, tmpdirname)
        theme_dirs = get_themes_dirs(temp_dir)
        for theme_dir in theme_dirs:
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
    theme_dirs = []
    if os.path.exists(os.path.join(dirname, 'index.theme')):
        theme_dirs.append(dirname)
    else:
        source_dirs = next(os.walk(dirname))[1]
        for maybe_theme in source_dirs:
            if os.path.exists(os.path.join(dirname, maybe_theme, 'index.theme')):
                theme_dirs.append(os.path.join(dirname, maybe_theme))
    return theme_dirs

def install_theme(theme_dir):
    """
    Install a theme for the current user
    """
    target_dir = os.path.join(os.environ['HOME'], '.themes/' if not is_icon(theme_dir) else '.icons/')
    if not os.path.exists(os.path.join(target_dir, os.path.basename(theme_dir))):
        shutil.move(theme_dir, target_dir)
    else:
        click.secho("The theme {0} already exists".format(os.path.basename(theme_dir)), fg="yellow")