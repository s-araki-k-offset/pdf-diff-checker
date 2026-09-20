import pymupdf

from pdf_diff_checker.extractor import extract_text


def test_extract_text(tmp_path):
    pdf_path = tmp_path / "sample.pdf"

    document = pymupdf.open()

    page1 = document.new_page()
    page1.insert_text((72, 72), "PDF Diff Checker Sample")

    page2 = document.new_page()
    page2.insert_text((72, 72), "Page 2")

    document.save(pdf_path)
    document.close()

    pages = extract_text(pdf_path)

    assert len(pages) == 2
    assert "PDF Diff Checker Sample" in pages[0]
    assert "Page 2" in pages[1]