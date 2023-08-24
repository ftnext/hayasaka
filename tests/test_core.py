from unittest.mock import patch

from selenium.webdriver import FirefoxOptions

from hayasaka import core


@patch("hayasaka.core.kill_browser")
@patch("hayasaka.core.get_driver")
@patch("hayasaka.core.go_to")
@patch("hayasaka.core.start_firefox")
@patch("hayasaka.core.build_options")
def test_take_screenshot(
    build_options, start_firefox, go_to, get_driver, kill_browser
):
    options = build_options.return_value
    driver = get_driver.return_value

    core.take_screenshot("https://example.com/awesome", "save/to/path.png")

    build_options.assert_called_once_with()
    start_firefox.assert_called_once_with(options=options, headless=True)
    go_to.assert_called_once_with("https://example.com/awesome")
    get_driver.assert_called_once_with()
    driver.save_screenshot.assert_called_once_with("save/to/path.png")
    kill_browser.assert_called_once_with()


def test_build_options():
    actual = core.build_options()

    assert isinstance(actual, FirefoxOptions)
    assert set(actual.arguments) == {"--width=800", "--height=485"}
