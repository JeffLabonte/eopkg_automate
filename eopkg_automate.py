#!/usr/bin/python3

from pathlib import Path
from glob import glob
from subprocess import Popen, PIPE
from typing import List, Optional


MESSAGE_REQUIRE_LIST = """
You need to specify the packages you want to install, remove, upgrade, group install.
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


def get_packages(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def run_command(action: str, packages: List):
    if action == 'update':
        command = ['sudo', *COMMANDS_MAPPING[action]]
    else:
        command = ['sudo', *COMMANDS_MAPPING[action], *packages]
    cli_call = Popen(command, stdout=PIPE, stderr=PIPE)
    command_string = ' '.join(command)
    print(f'Executing:\n {command_string}\n')
    msg, err = cli_call.communicate()
    if msg:
        print(msg.decode('utf-8'))


def main(package_lists_path: List):
    for path in package_lists_path:
        action = extract_action_from_path(path)
        packages = get_packages(path)

        if action != 'update' and not packages:
            continue

        run_command(action, packages)


if __name__ == '__main__':
    package_lists_path = get_package_lists_path()
    if package_lists_path:
        main(
            package_lists_path=package_lists_path,
        )
    else:
        print(MESSAGE_REQUIRE_LIST)
