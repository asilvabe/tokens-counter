"""Core token counting logic using tiktoken."""

import tiktoken

from .pdf_reader import iter_pages

DEFAULT_ENCODING = "cl100k_base"


def count_tokens_in_pdf(path: str, encoding_name: str = DEFAULT_ENCODING) -> dict:
    """Count tokens in a PDF, processing page by page.

    Returns:
        dict with total_tokens, total_pages and tokens_per_page.
    """
    enc = tiktoken.get_encoding(encoding_name)
    tokens_per_page: list[int] = []

    for page_text in iter_pages(path):
        tokens_per_page.append(len(enc.encode(page_text)))

    return {
        "total_tokens": sum(tokens_per_page),
        "total_pages": len(tokens_per_page),
        "tokens_per_page": tokens_per_page,
    }
