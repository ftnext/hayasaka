import argparse

from hayasaka.core import take_screenshot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Example: https://... file://...")
    parser.add_argument("screenshot_path")
    args = parser.parse_args()

    take_screenshot(args.url, args.screenshot_path)


if __name__ == "__main__":
    main()
