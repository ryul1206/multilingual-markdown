
<div align="center" markdown>
   <img src="https://github.com/ryul1206/multilingual-markdown/assets/19263912/7cfded93-4c64-428a-b027-76a621de92a6" width="500" alt="Multilingual Markdown Generator" />
</div>

<div align="center" markdown>

# [多言語マークダウンジェネレータ](https://mmg.ryul1206.dev/latest/ja)

このパッケージは、単一のデフォルトのファイルから多言語コンテンツを管理してi18nマークダウンを生成するコマンドラインインタフェース（CLI）を提供しています。

[![PyPI - Version](https://img.shields.io/pypi/v/mmg?color)](https://pypi.org/project/mmg/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mmg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown)
[![PyPI - License](https://img.shields.io/pypi/l/mmg)](https://github.com/ryul1206/multilingual-markdown/blob/main/LICENSE)

[![PyPI - Downloads](https://img.shields.io/pypi/dm/mmg)](https://pypi.org/project/mmg/)
[![PyPI Downloads](https://static.pepy.tech/badge/mmg)](https://pepy.tech/projects/mmg)

🌏
[**English**](https://github.com/ryul1206/multilingual-markdown/blob/main/README.md) |
[**Français**](https://github.com/ryul1206/multilingual-markdown/blob/main/README.fr.md) |
[**한국어**](https://github.com/ryul1206/multilingual-markdown/blob/main/README.ko.md) |
日本語

Bash, Zsh, WindowsPowerShellで使用できます。

</div>

---

**目次** ⚡

1. [概要](#概要-)
    1. [作動方式](#作動方式)
    1. [特徴](#特徴)
1. [設置](#設置-)
    1. [Linux](#linux)
    1. [macOS](#macos)
    1. [Windows](#windows)
1. [使用方法](#使用方法-)
1. [トラブルシューティング](#トラブルシューティング-)
1. [Changelog](#changelog-)
1. [貢献された方々](#貢献された方々-)

## 概要 🔎

### 作動方式

1 つの Base ファイルのみを管理することで、コンテンツの翻訳漏れや不一致によるエラーを減らすことができます。
また、単一ファイルで編集できるため、[Copilot](https://github.com/features/copilot) などの AI ツールの自動補完機能による便利な翻訳を期待できます。

Markdown:

<div align="center">
   <img src="https://github.com/ryul1206/multilingual-markdown/assets/19263912/fd88420e-ddd1-403c-a9df-3429ec8095e3" width="800" alt="How It Works: Markdown" />
</div>

Jupyter Notebook:

<div align="center">
   <img src="https://github.com/ryul1206/multilingual-markdown/assets/19263912/ff2ef5d9-da9f-4d91-9618-fb933802bf69" width="900" alt="How It Works: Jupyter Notebook" />
</div>

### 特徴

次の機能をサポートします。

- **Markdown、Jupyter Notebook（`.ipynb`）を入力形式で使用する**
- **As-is(そのまま)、HTML、PDF出力形式**
- Bash、Zsh、Windows PowerShell用のコマンドラインインターフェイス
- Python API
- `-r`オプションを使用した再帰巡回モード（As-is、HTML、PDFの両方をサポート）
- YAMLファイルを使用したバッチモード（As-isのみサポート）
- [IETF言語タグ](https://ja.wikipedia.org/wiki/IETF%E8%A8%80%E8%AA%9E%E3%82%BF%E3%82%B0)
- UTF-8エンコーディング
- レベルと絵文字オプションを含む目次の自動生成（MarkdownとJupyter Notebookの両方をサポート）
- Baseファイルの検証(言語別のタグ数の確認)
- CI / CDのための検証のみモード（ファイル生成を無効にする）

## 設置 📦

### Linux

```sh
pip3 install mmg
```

### macOS

```sh
pip3 install mmg
```

[WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#macos)で問題が発生した場合は、次のコマンドでインストールしてください。WeasyPrintはPDFの作成にのみ使用されます。

```sh
brew install weasyprint
```

### Windows

1. MMGは[WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)を使用してPDFを作成します。WeasyPrintはGTKライブラリが必要なので、最新の[GTK3インストーラー](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)をダウンロードして実行します。**PDFを作成することに興味がない場合は、このステップをスキップできます。** GTKがなくても、MMGの他の機能は使用できます。
2. Pipを使用してMMGをインストールします。

    ```sh
    pip3 install mmg
    ```

## 使用方法 💡

詳細な使用方法と例は、[ドキュメント](https://mmg.ryul1206.dev/latest/ja/)を参照してください。

```sh
$ mmg --help
Usage: mmg [OPTIONS] [FILE_NAMES]...

  FILE_NAMES: Base file names to convert. `*.base.md` or `*.base.ipynb` are
  available.

  Here are some examples:

      mmg *.base.md

      mmg *.base.ipynb

      mmg *.base.md *.base.ipynb -o pdf --css github-dark

      mmg --recursive

      mmg --recursive --validation-only

      mmg --batch mmg.yml

Options:
  -r, --recursive                 This will search all subfolders based on
                                  current directory.
  -b, --batch FILE                YAML file path for batch conversion.
                                  (Default: None)
  -o, --output-format [as-is|html|pdf]
                                  Output format. (Default: as-is)
  --css TEXT                      CSS file path or preset('github-
                                  light'/'github-dark'). Only for the HTML/PDF
                                  output. (Default: github-light)
  -y, --yes                       This will confirm the conversion without
                                  asking. (Default: False)
  -s, --skip-validation           Skip the health check. (Default: False)
  --validation-only               Only check the health. (Default: False)
  -v, --verbose                   Verbosity level from 0 to 2. --verbose:1,
                                  -v:1, -vv:2 (Default: 0)
  --version                       Show the current version.
  --help                          Show this message and exit.
```

## トラブルシューティング 💊

[トラブルシューティング](https://mmg.ryul1206.dev/latest/ja/misc/troubleshooting/)ページを参照してください。

## Changelog 📝

[CHANGELOG.md](https://github.com/ryul1206/multilingual-markdown/blob/develop/CHANGELOG.md)

## 貢献された方々 🤝

<a href="https://github.com/ryul1206/multilingual-markdown/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ryul1206/multilingual-markdown" />
</a>

[contrib.rocks](https://contrib.rocks)で作りました。

貢献方法に興味がある方は、[貢献ガイド](https://mmg.ryul1206.dev/latest/ja/contributing/)を参照してください。