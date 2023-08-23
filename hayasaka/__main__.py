import argparse
from textwrap import dedent

from hayasaka.cli import as_uri
from hayasaka.core import take_screenshot


def main():
    parser_help = """
    Save the rendered HTML as an image.

    Examples:

    - from URL

      %(prog)s https://example.com/your/slide.html awesome.png

    - from local HTML file

      %(prog)s your/slide.html awesome.png

      tips: Also supports

      %(prog)s file:///home/.../your/slide.html awesome.png
    """

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=dedent(parser_help),
    )
    parser.add_argument(
        "uri_or_path",
        help=(
            "Specify an HTML file on Web (https://...) "
            "or your computer (file path or file://...)"
        ),
        type=as_uri,
    )
    parser.add_argument("screenshot_path")
    args = parser.parse_args()

    take_screenshot(args.uri_or_path, args.screenshot_path)


if __name__ == "__main__":
    main()
