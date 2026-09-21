from pdf_diff_checker.comparator import create_text_diff, find_different_pages


def test_find_different_pages():
    before_pages = [
        "商品A 1,000円",
        "商品B 2,000円",
    ]

    after_pages = [
        "商品A 1,200円",
        "商品B 2,000円",
    ]

    different_pages = find_different_pages(before_pages, after_pages)

    assert different_pages == [1]

def test_find_different_pages_when_pages_are_identical():
    before_pages = [
        "商品A 1,000円",
        "商品B 2,000円",
    ]

    after_pages = [
        "商品A 1,000円",
        "商品B 2,000円",
    ]

    different_pages = find_different_pages(before_pages, after_pages)

    assert different_pages == []

def test_find_different_pages_when_page_counts_differ():
    before_pages = [
        "Page 1",
        "Page 2",
    ]

    after_pages = [
        "Page 1",
        "Page 2",
        "Page 3",
    ]

    different_pages = find_different_pages(before_pages, after_pages)

    assert different_pages == [3]

def test_find_different_pages_when_page_is_removed():
    before_pages = [
        "Page 1",
        "Page 2",
        "Page 3",
    ]

    after_pages = [
        "Page 1",
        "Page 2",
    ]

    different_pages = find_different_pages(before_pages, after_pages)

    assert different_pages == [3]

def test_create_text_diff():
    before = """商品名：サンプル商品A
価格：1,000円
発売日：2026年9月21日"""

    after = """商品名：サンプル商品A
価格：1,200円
発売日：2026年9月21日"""

    diff = create_text_diff(before, after)

    assert "-価格：1,000円" in diff
    assert "+価格：1,200円" in diff
