from helium_cylinder.decorators import using_chrome
from selenium.webdriver import ChromeOptions

from hayasaka.core import take_screenshot as _take_screenshot


def build_options() -> ChromeOptions:
    options = ChromeOptions()
    options.add_argument("--window-size=400,200")  # 保存される画像のサイズは2倍になる

    return options


@using_chrome(options=build_options(), headless=True)
def take_screenshot(url: str, save_path: str):
    _take_screenshot(url, save_path)
