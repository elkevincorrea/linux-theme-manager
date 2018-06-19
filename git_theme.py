from git import Repo
import os
import tempfile
import shutil

def add_from_git(git_url):
    print(git_url)
    print(os.path.dirname(__file__))
    clone(git_url)
    

def clone(git_url):
    with tempfile.TemporaryDirectory() as tmpdirname:
        print(tmpdirname)
        repo_name = os.path.splitext(os.path.basename(git_url))[0]
        print(repo_name)
        repo = Repo.clone_from(git_url, os.path.join(tmpdirname, repo_name), branch = 'master')
        print(os.path.dirname(repo.git_dir))
        print(os.path.exists(os.path.join(os.path.dirname(repo.git_dir), 'index.theme')))
        theme_dir = None
        dir = os.path.join(os.path.dirname(repo.git_dir))
        if os.path.exists(os.path.join(dir, 'index.theme')):
            theme_dir = dir

        if theme_dir != None:
            shutil.move(theme_dir, os.path.join(os.environ['HOME'], '.themes/'))
