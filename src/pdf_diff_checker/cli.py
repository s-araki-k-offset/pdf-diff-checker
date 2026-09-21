import argparse
from pathlib import Path

from pdf_diff_checker.comparator import create_text_diff
from pdf_diff_checker.extractor import extract_text


def main():
    parser = argparse.ArgumentParser(
        description="Compare text differences between two PDF files."
    )
    parser.add_argument("before", type=Path, help="Original PDF file")
    parser.add_argument("after", type=Path, help="Modified PDF file")

    args = parser.parse_args()

    before_pages = extract_text(args.before)
    after_pages = extract_text(args.after)

    for page_number, (before, after) in enumerate(
        zip(before_pages, after_pages),
        start=1,
    ):
        diff = create_text_diff(before, after)

        if diff:
            print(f"\n--- Page {page_number} ---")
            print("\n".join(diff))


if __name__ == "__main__":
    main()