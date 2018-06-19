import sys
from enum import Enum
import git_theme

class Mode(Enum):
    GIT = "git"

class Commands(Enum):
    ADD = "add"

def init():
    print("Hello World!")
    print(sys.argv[1:])
    command = sys.argv[2]
    mode = sys.argv[1]
    if Commands(command) == Commands.ADD and Mode(mode) == Mode.GIT:
        git_theme.add_from_git(sys.argv[3])

init()