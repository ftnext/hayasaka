import sys

from selenium.webdriver import FirefoxOptions

from hayasaka import firefox

if sys.version_info < (3, 9):
    from typing import Iterable
else:
    from collections.abc import Iterable


def assert_options_arguments(
    option, expected_arguments: Iterable[str]
) -> None:
    assert isinstance(option, FirefoxOptions)
    assert set(option.arguments) == set(expected_arguments)


def test_build_options():
    actual = firefox.build_options()

    assert_options_arguments(actual, {"--width=800", "--height=485"})
