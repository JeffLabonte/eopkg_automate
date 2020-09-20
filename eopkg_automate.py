#!/usr/bin/python3

from pathlib import Path
from glob import glob
from subprocess import Popen
from typing import List


MESSAGE_REQUIRE_LIST = """
You need to specify the packages you want to install, remove, up, group install.
"""


COMMANDS_MAPPING = {
    'install': ['eopkg', 'it'],
    'remove': ['eopkg', 'rm'],
    'group_install': ['eopkg', 'it', '-c'],
    'update': ['eopkg', 'up'],
}


def extract_action_from_path(path: Path) -> str:
    filename =  str(path).split('/')[-1]
    after_underscore_index = filename.find('_') + 1
    dot_index = filename.find('.')
    return filename[after_underscore_index:dot_index]


def get_package_lists_path() -> List:
    return [p for p in glob('package_lists/package_*.txt', recursive=True) if '.template' not in p]



def main(package_lists_path: List):
    for path in package_lists_path:
        pass
        


if __name__ == '__main__':
    package_lists_path = get_package_lists()
    if package_lists_path:
        main(
            package_lists_path=package_lists_path,
        )
    else:
        print(MESSAGE_REQUIRE_LIST)
