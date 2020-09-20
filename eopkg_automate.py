#!/usr/bin/python3

from glob import glob
from subprocess import Popen


MESSAGE_REQUIRE_LIST = """
You need to specify the packages you want to install, remove, up, group install.
"""


COMMANDS_MAPPING = {
    'install': ['eopkg', 'it'],
    'remove': ['eopkg', 'rm'],
    'group_install': ['eopkg', 'it', '-c'],
    'update': ['eopkg', 'up'],
}


def get_package_lists():
    return glob('package_lists/*', recursive=True)


def main():
    pass


if __name__ == '__main__':
    if has_lists():
        main()
    else:
        print(MESSAGE_REQUIRE_LIST)
