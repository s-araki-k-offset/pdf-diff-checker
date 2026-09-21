# PDF Diff Checker

2つのPDFファイルからテキストを抽出し、差分を比較するためのコマンドラインツールです。

PDFをページ単位で比較し、変更されたテキストをunified diff形式で表示します。

[English README](README.md)

## 主な機能

- PyMuPDFを使用したPDFテキスト抽出
- ページ単位でのPDF比較
- ページの追加・削除を検出
- 行単位のテキスト差分表示
- コマンドラインから実行可能
- pytestによる自動テスト

## 動作環境

- Python 3.12以上

## インストール

リポジトリをクローンします。

```bash
git clone https://github.com/s-araki-k-offset/pdf-diff-checker.git
cd pdf-diff-checker
```

仮想環境を作成して有効化します。

```bash
python -m venv .venv
source .venv/bin/activate
```

パッケージをインストールします。

```bash
pip install -e ".[dev]"
```

## 使い方

比較する2つのPDFを指定します。

```bash
pdf-diff-checker before.pdf after.pdf
```

出力例：

```diff
--- Page 1 ---
--- before
+++ after
@@ -1,3 +1,3 @@
 商品名：サンプル商品A
-価格：1,000円
+価格：1,200円
 発売日：2026年9月21日
```

この例では、1ページ目の価格が「1,000円」から「1,200円」に変更されたことを示しています。

## テスト

pytestでテストを実行できます。

```bash
pytest
```

## プロジェクト構成

```text
pdf-diff-checker/
├── src/
│   └── pdf_diff_checker/
│       ├── cli.py
│       ├── comparator.py
│       └── extractor.py
├── tests/
├── README.md
├── README_ja.md
└── pyproject.toml
```

## 開発状況

現在開発中です。

今後、以下の機能追加・改善を予定しています。

- 差分表示の改善
- PDFから抽出したテキストの正規化
- PDF内の文字配置への対応改善
- HTML形式の差分レポート