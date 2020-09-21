from eopkg_automate import get_actions_args

import pytest


class FakeArguments:
    pass


@pytest.mark.parametrize(
    "attribute_to_true, expected_action",
    [
        (
            "install",
            "install",
        ),
        (
            "remove",
            "remove",
        ),
    ],
)
def test__get_action_args_with_args__should_return_expected_action(attribute_to_true, expected_action):
    arguments = FakeArguments()
    setattr(arguments, "install", True if attribute_to_true == "install" else False)
    setattr(arguments, "remove", True if attribute_to_true == "remove" else False)
    setattr(arguments, "file", "/home/test/")

    assert get_actions_args(arguments) == expected_action


def test__get_action_args_without_file__should_raise_system_error():
    with pytest.raises(SystemError):
        get_actions_args(FakeArguments())
