from unittest.mock import patch

from hayasaka import core


@patch("hayasaka.core.kill_browser")
@patch("hayasaka.core.get_driver")
@patch("hayasaka.core.go_to")
def test_take_screenshot(go_to, get_driver, kill_browser):
    driver = get_driver.return_value

    core.take_screenshot("https://example.com/awesome", "save/to/path.png")

    go_to.assert_called_once_with("https://example.com/awesome")
    get_driver.assert_called_once_with()
    driver.save_screenshot.assert_called_once_with("save/to/path.png")
    kill_browser.assert_called_once_with()
