import argparse

from hayasaka.cli import as_uri
from hayasaka.core import take_screenshot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "uri_or_path", help="Example: https://... file://...", type=as_uri
    )
    parser.add_argument("screenshot_path")
    args = parser.parse_args()

    take_screenshot(args.uri_or_path, args.screenshot_path)


if __name__ == "__main__":
    main()
