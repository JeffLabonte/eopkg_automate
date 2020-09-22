#!/usr/bin/python3
import argparse

from pathlib import Path
from subprocess import Popen, PIPE
from typing import List


COMMANDS_MAPPING = {
    'install': ['eopkg', 'it', '-y'],
    'remove': ['eopkg', 'rm', '-y'],
    'group_install': ['eopkg', 'it', '-y', '-c'],
    'update': ['eopkg', 'up', '-y'],
}


def get_actions_args(arguments) -> str:
    if not hasattr(arguments, "file"):
        raise SystemError("You need to specify a file for installation or removal")

    return "install" if arguments.install else "remove"


def get_packages_from_path(file_path: str) -> List:
    package_path = Path(file_path).resolve()
    return get_packages(package_path)


def get_packages(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def run_command(command: str):
    cli_call = Popen(command, stdout=PIPE, stderr=PIPE)
    command_string = " ".join(command)
    print(f"Executing:\n {command_string}\n")
    msg, err = cli_call.communicate()
    if msg:
        print(msg.decode("utf-8"))


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="eopkg helper")

    parser.add_argument(
        "--up",
        "-u",
        dest="update",
        action="store_true",
        help="Run update before install or removal",
    )
    parser.add_argument("--file", "-f", type=str, help="Path to your package list to install or remove")

    install_remove_group = parser.add_mutually_exclusive_group()
    install_remove_group.add_argument("--install", "-i", action="store_true", help="List is going to be install")
    install_remove_group.add_argument("--remove", "-rm", action="store_true", help="List is going to be remove")

    return parser


def main():
    parser = create_parser()
    arguments = parser.parse_args()

    if arguments.update:
        command = ["sudo", *COMMANDS_MAPPING["update"]]
        run_command(command=command)

    if arguments.install or arguments.remove:
        action = get_actions_args(arguments)
        packages = get_packages_from_path(arguments.file)
        command = ["sudo", *COMMANDS_MAPPING[action], *packages]
        run_command(command=command)


if __name__ == "__main__":
    main()
