from helium import get_driver, go_to, kill_browser, start_firefox
from selenium.webdriver import FirefoxOptions


def take_screenshot(url: str, save_path: str) -> None:
    options = FirefoxOptions()
    options.add_argument("--width=800")
    options.add_argument("--height=485")  # ブラウザウィンドウ上部が85px分ある

    start_firefox(options=options, headless=True)
    go_to(url)
    get_driver().save_screenshot(save_path)
    kill_browser()
