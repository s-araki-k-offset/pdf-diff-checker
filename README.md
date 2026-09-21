# PDF Diff Checker

[日本語版 README](README_ja.md)

A command-line tool for comparing text differences between two PDF files.

PDF Diff Checker extracts text from each page of two PDFs and displays changed pages using a unified diff format.

## Features

- Extract text from PDF files with PyMuPDF
- Compare PDFs page by page
- Detect added or removed pages
- Display line-by-line text differences
- Command-line interface
- Automated tests with pytest

## Requirements

- Python 3.12+

## Installation

Clone the repository:

```bash
git clone https://github.com/s-araki-k-offset/pdf-diff-checker.git
cd pdf-diff-checker
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the package:

```bash
pip install -e ".[dev]"
```

## Usage

Compare two PDF files:

```bash
pdf-diff-checker before.pdf after.pdf
```

Example output:

```diff
--- Page 1 ---
--- before
+++ after
@@ -1,3 +1,3 @@
 Product: Sample A
-Price: 1,000 yen
+Price: 1,200 yen
 Release date: 2026-09-21
```

## Testing

Run the test suite with:

```bash
pytest
```

## Project Structure

```text
pdf-diff-checker/
├── src/
│   └── pdf_diff_checker/
│       ├── cli.py
│       ├── comparator.py
│       └── extractor.py
├── tests/
├── README.md
└── pyproject.toml
```

## Status

This project is under development.

Planned improvements include:

- More readable diff output
- Text normalization
- Improved handling of PDF text layout
- HTML diff reports