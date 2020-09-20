from pathlib import Path

from eopkg_automate import extract_action_from_path

import pytest

BASE_PATH = Path(__file__).resolve().parent


@pytest.mark.parametrize('path, expected_string', [
    (Path(f'{BASE_PATH}/package_lists/package_group_install.txt'), 'group_install'),
    (Path(f'{BASE_PATH}/package_lists/package_install.txt'), 'install'),
    (Path(f'{BASE_PATH}/package_lists/package_remove.txt'), 'remove'),
    (Path(f'{BASE_PATH}/package_lists/package_update.txt'), 'update'),
])
def test__extract_action_from_path__should_return_expected_values(path: Path, expected_string: str):
    action = extract_action_from_path(path)
    assert action == expected_string
