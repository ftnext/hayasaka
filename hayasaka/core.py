from helium import get_driver, go_to, kill_browser


def take_screenshot(url: str, save_path: str):
    go_to(url)
    get_driver().save_screenshot(save_path)
    kill_browser()
