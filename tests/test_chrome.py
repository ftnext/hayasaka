from selenium.webdriver import ChromeOptions

from hayasaka import chrome


def test_build_options():
    actual = chrome.build_options()

    assert isinstance(actual, ChromeOptions)
    assert set(actual.arguments) == {"--window-size=400,200"}
