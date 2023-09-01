from selenium.webdriver import ChromeOptions


def build_options() -> ChromeOptions:
    options = ChromeOptions()
    options.add_argument("--window-size=400,200")  # 保存される画像のサイズは2倍になる

    return options
