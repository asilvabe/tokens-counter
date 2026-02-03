"""Command-line interface."""

import argparse
import sys
import time
from pathlib import Path

from .counter import count_tokens_in_pdf, DEFAULT_ENCODING


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Count tokens in a PDF file.",
    )
    parser.add_argument(
        "pdf",
        type=Path,
        help="Path to the PDF file.",
    )
    parser.add_argument(
        "-e", "--encoding",
        default=DEFAULT_ENCODING,
        help=f"tiktoken encoding to use (default: {DEFAULT_ENCODING}).",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show per-page token breakdown.",
    )
    return parser


def main() -> None:
    args = _build_parser().parse_args()

    if not args.pdf.is_file():
        print(f"Error: '{args.pdf}' is not a valid file.", file=sys.stderr)
        sys.exit(1)

    if args.pdf.suffix.lower() != ".pdf":
        print(f"Error: '{args.pdf}' is not a .pdf file.", file=sys.stderr)
        sys.exit(1)

    file_size_mb = args.pdf.stat().st_size / (1024 * 1024)
    print(f"File    : {args.pdf}")
    print(f"Size    : {file_size_mb:.2f} MB")
    print(f"Encoding: {args.encoding}")
    print("-" * 40)

    start = time.perf_counter()
    result = count_tokens_in_pdf(str(args.pdf), args.encoding)
    elapsed = time.perf_counter() - start

    print(f"Pages   : {result['total_pages']}")
    print(f"Tokens  : {result['total_tokens']:,}")
    print(f"Time    : {elapsed:.2f}s")

    if args.verbose:
        print("-" * 40)
        print("Tokens per page:")
        for i, t in enumerate(result["tokens_per_page"], 1):
            print(f"  Page {i:>4}: {t:>8,} tokens")


if __name__ == "__main__":
    main()
