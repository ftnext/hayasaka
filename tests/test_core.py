from unittest.mock import call, patch

from hayasaka import core


@patch("hayasaka.core.kill_browser")
@patch("hayasaka.core.get_driver")
@patch("hayasaka.core.go_to")
@patch("hayasaka.core.start_firefox")
@patch("hayasaka.core.FirefoxOptions")
def test_take_screenshot(
    FirefoxOptions, start_firefox, go_to, get_driver, kill_browser
):
    options = FirefoxOptions.return_value
    driver = get_driver.return_value

    core.take_screenshot("https://example.com/awesome", "save/to/path.png")

    FirefoxOptions.assert_called_once_with()
    options.add_argument.assert_has_calls(
        [call("--width=800"), call("--height=485")]
    )
    start_firefox.assert_called_once_with(options=options, headless=True)
    go_to.assert_called_once_with("https://example.com/awesome")
    get_driver.assert_called_once_with()
    driver.save_screenshot.assert_called_once_with("save/to/path.png")
    kill_browser.assert_called_once_with()
