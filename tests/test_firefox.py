from __future__ import annotations

from unittest.mock import ANY, patch

from selenium.webdriver import FirefoxOptions

from hayasaka import firefox


def assert_options_arguments(option, expected_arguments: set[str]) -> None:
    assert isinstance(option, FirefoxOptions)
    assert set(option.arguments) == expected_arguments


def test_build_options():
    actual = firefox.build_options()

    assert_options_arguments(actual, {"--width=800", "--height=485"})


@patch("hayasaka.firefox._take_screenshot")
@patch("helium_cylinder.decorators.start_firefox")
def test_take_screenshot(start_firefox, _take_screenshot):
    firefox.take_screenshot("https://example.com/awesome", "save/to/path.png")

    start_firefox.assert_called_once_with(options=ANY, headless=True)
    assert_options_arguments(
        start_firefox.call_args.kwargs["options"],
        {"--width=800", "--height=485"},
    )
    _take_screenshot.assert_called_once_with(
        "https://example.com/awesome", "save/to/path.png"
    )
