from git import Repo
import os
import tempfile
import shutil

def add_from_git(git_url):
    with tempfile.TemporaryDirectory() as tmpdirname:
        dir = clone(git_url, tmpdirname)
        theme_dir = get_themes_dirs(dir)
        install_theme(theme_dir)

def is_theme_or_icon():
    pass

def clone(git_url, tmpdirname):
    """
    Clones a repo to a temp dir
    """
    repo_name = os.path.splitext(os.path.basename(git_url))[0]
    repo = Repo.clone_from(git_url, os.path.join(tmpdirname, repo_name), branch = 'master')
    return os.path.join(os.path.dirname(repo.git_dir))

def get_themes_dirs(dirname):
    theme_dir = None
    if os.path.exists(os.path.join(dirname, 'index.theme')):
        theme_dir = dirname
    return theme_dir


def install_theme(theme_dir):
    if not os.path.exists(theme_dir):
        if theme_dir != None:
            shutil.move(theme_dir, os.path.join(os.environ['HOME'], '.themes/'))
    else:
        print("Existe")