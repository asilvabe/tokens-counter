"""Page-by-page PDF text extraction for low memory usage."""

from typing import Iterator

import fitz


def iter_pages(path: str) -> Iterator[str]:
    """Yield the text of each PDF page without loading the full document."""
    with fitz.open(path) as doc:
        for page in doc:
            yield page.get_text()
