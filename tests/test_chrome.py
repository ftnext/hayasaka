from __future__ import annotations

from selenium.webdriver import ChromeOptions

from hayasaka import chrome


def assert_options_arguments(option, expected_arguments: set[str]) -> None:
    assert isinstance(option, ChromeOptions)
    assert set(option.arguments) == expected_arguments


def test_build_options():
    actual = chrome.build_options()

    assert_options_arguments(actual, {"--window-size=400,200"})
