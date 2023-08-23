from pathlib import Path
from urllib.parse import urlparse


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
