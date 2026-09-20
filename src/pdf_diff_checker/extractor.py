from pathlib import Path

import pymupdf


def extract_text(pdf_path: Path) -> list[str]:
    """Extract text from each page of a PDF file."""
    pages = []

    with pymupdf.open(pdf_path) as document:
        for page in document:
            pages.append(page.get_text())

    return pages
