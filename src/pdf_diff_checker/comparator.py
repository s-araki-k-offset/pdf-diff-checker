from difflib import unified_diff
from itertools import zip_longest


def find_different_pages(
    before_pages: list[str],
    after_pages: list[str],
) -> list[int]:
    """Return page numbers whose text differs."""
    different_pages = []

    for page_number, (before, after) in enumerate(
        zip_longest(before_pages, after_pages),
        start=1,
    ):
        if before != after:
            different_pages.append(page_number)

    return different_pages

def create_text_diff(before: str, after: str) -> list[str]:
    """Return line-by-line differences between two texts."""
    return list(
        unified_diff(
            before.splitlines(),
            after.splitlines(),
            fromfile="before",
            tofile="after",
            lineterm="",
        )
    )

def compare_pages(
    before_pages: list[str],
    after_pages: list[str],
) -> list[tuple[int, list[str]]]:
    """Return text differences for each changed page."""
    differences = []

    for page_number, (before, after) in enumerate(
        zip_longest(before_pages, after_pages, fillvalue=""),
        start=1,
    ):
        diff = create_text_diff(before, after)

        if diff:
            differences.append((page_number, diff))

    return differences
