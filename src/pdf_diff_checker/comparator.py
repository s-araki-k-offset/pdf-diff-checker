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