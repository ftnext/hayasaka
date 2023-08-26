from helium import get_driver, go_to, kill_browser
from helium_cylinder.decorators import using_firefox
from selenium.webdriver import FirefoxOptions


def build_options() -> FirefoxOptions:
    options = FirefoxOptions()
    options.add_argument("--width=800")
    options.add_argument("--height=485")  # ブラウザウィンドウ上部が85px分ある

    return options


@using_firefox(options=build_options(), headless=True)
def take_screenshot(url: str, save_path: str):
    go_to(url)
    get_driver().save_screenshot(save_path)
    kill_browser()
