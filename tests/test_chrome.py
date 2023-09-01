from __future__ import annotations

from unittest.mock import ANY, patch

from selenium.webdriver import ChromeOptions

from hayasaka import chrome


def assert_options_arguments(option, expected_arguments: set[str]) -> None:
    assert isinstance(option, ChromeOptions)
    assert set(option.arguments) == expected_arguments


def test_build_options():
    actual = chrome.build_options()

    assert_options_arguments(actual, {"--window-size=400,200"})


@patch("hayasaka.chrome._take_screenshot")
@patch("helium_cylinder.decorators.start_chrome")
def test_take_screenshot(start_chrome, _take_screenshot):
    chrome.take_screenshot("https://example.com/awesome", "save/to/path.png")

    start_chrome.assert_called_once_with(options=ANY, headless=True)
    assert_options_arguments(
        start_chrome.call_args.kwargs["options"], {"--window-size=400,200"}
    )
    _take_screenshot.assert_called_once_with(
        "https://example.com/awesome", "save/to/path.png"
    )
