from hayasaka.cli import parse_args
from hayasaka.firefox import take_screenshot


def main():
    args = parse_args()
    take_screenshot(args.uri_or_path, args.screenshot_path)
    print(f"Got the best shot: {args.screenshot_path}")


if __name__ == "__main__":
    main()
