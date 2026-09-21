import sys

import pymupdf

from pdf_diff_checker.cli import main


def create_pdf(path, texts):
    document = pymupdf.open()

    for text in texts:
        page = document.new_page()
        page.insert_text((72, 72), text)

    document.save(path)
    document.close()


def test_cli(tmp_path, monkeypatch, capsys):
    before_path = tmp_path / "before.pdf"
    after_path = tmp_path / "after.pdf"

    create_pdf(
        before_path,
        [
            "Page 1",
            "Price: 1,000 yen",
        ],
    )

    create_pdf(
        after_path,
        [
            "Page 1",
            "Price: 1,200 yen",
        ],
    )

    monkeypatch.setattr(
        sys,
        "argv",
        ["pdf-diff-checker", str(before_path), str(after_path)],
    )

    main()

    captured = capsys.readouterr()

    assert "--- Page 2 ---" in captured.out
    assert "-Price: 1,000 yen" in captured.out
    assert "+Price: 1,200 yen" in captured.out

def test_cli_when_after_has_extra_page(tmp_path, monkeypatch, capsys):
    before_path = tmp_path / "before.pdf"
    after_path = tmp_path / "after.pdf"

    create_pdf(
        before_path,
        [
            "Page 1",
            "Page 2",
        ],
    )

    create_pdf(
        after_path,
        [
            "Page 1",
            "Page 2",
            "Page 3",
        ],
    )

    monkeypatch.setattr(
        sys,
        "argv",
        ["pdf-diff-checker", str(before_path), str(after_path)],
    )

    main()

    captured = capsys.readouterr()

    assert "--- Page 3 ---" in captured.out
