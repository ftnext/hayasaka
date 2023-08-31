from selenium.webdriver import FirefoxOptions


def build_options() -> FirefoxOptions:
    options = FirefoxOptions()
    options.add_argument("--width=800")
    options.add_argument("--height=485")  # ブラウザウィンドウ上部が85px分ある

    return options
