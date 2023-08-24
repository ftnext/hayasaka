import argparse
from pathlib import Path
from textwrap import dedent
from urllib.parse import urlparse


def parse_args():
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

    return parser.parse_args()


def as_uri(uri_or_path: str) -> str:
    """
    >>> as_uri("http://example.com/slide.html")
    'http://example.com/slide.html'
    >>> as_uri("file:///home/hoge/work/slide.html")
    'file:///home/hoge/work/slide.html'
    >>> as_uri("work/slide.html")
    'file:///.../work/slide.html'
    """
    if _is_uri(uri_or_path):
        return uri_or_path
    return Path(uri_or_path).resolve().as_uri()


def _is_uri(uri_or_path: str) -> bool:
    """
    >>> _is_uri("file:///home/hoge/work/slide.html")
    True
    >>> _is_uri("work/slide.html")
    False
    """
    parsed = urlparse(uri_or_path)
    return bool(parsed.scheme)
