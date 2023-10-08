
<div align="center" markdown>
   <img src="./docs/assets/mmg-logo-dark.jpg" width="500" alt="Multilingual Markdown Generator" />
</div>

<div align="center" markdown>

# [Multilingual Markdown Generator](https://mmg.ryul1206.dev/latest/)

This package provides a command-line interface to manage multilingual contents and generate i18n markdown from a single base file.

[![PyPI - Version](https://img.shields.io/pypi/v/mmg?color)](https://pypi.org/project/mmg/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mmg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown)
[![PyPI - License](https://img.shields.io/pypi/l/mmg)](https://github.com/ryul1206/multilingual-markdown/blob/main/LICENSE)

🌏
English |
[**Français**](https://github.com/ryul1206/multilingual-markdown/blob/main/README.fr.md) |
[**한국어**](https://github.com/ryul1206/multilingual-markdown/blob/main/README.ko.md) |
[**日本語**](https://github.com/ryul1206/multilingual-markdown/blob/main/README.ja.md)

Available in Bash, Zsh, and Windows PowerShell.

</div>

---

**Table of Contents** ⚡

1. [Overview](#overview-)
    1. [How It Works](#how-it-works)
    1. [Features](#features)
1. [Installation](#installation-)
    1. [Linux](#linux)
    1. [macOS](#macos)
    1. [Windows](#windows)
1. [How to Use](#how-to-use-)
1. [Troubleshooting](#troubleshooting-)
1. [Changelog](#changelog-)
1. [Contributors](#contributors-)

## Overview 🔎

### How It Works

By managing only one Base file, we can reduce the number of errors caused by missing or mismatched translations.
Additionally, thanks to editing in a single file, we can expect convenient translation with the auto-completion function of AI tools such as [Copilot](https://github.com/features/copilot).

Markdown:

<div align="center">
   <img src="./docs/assets/how-it-works-md.png" width="800" alt="How It Works: Markdown" />
</div>

Jupyter Notebook:

<div align="center">
   <img src="./docs/assets/how-it-works-ipynb.png" width="900" alt="How It Works: Jupyter Notebook" />
</div>

### Features

Supports the following features:

- **Markdown, Jupyter Notebook(`.ipynb`) as input formats**
- **As-is, HTML, PDF as ouput formats**
- Command-line interface for Bash, Zsh, Windows PowerShell
- Python API
- Recursive traversal mode with `-r` option (As-is, HTML, PDF are all supported)
- Batch processing mode with YAML file (Only `As-is` is supported)
- [IETF language tags](https://en.wikipedia.org/wiki/IETF_language_tag)
- UTF-8 encoding
- Automatic generation of table of contents with level and emoji options (Markdown and Jupyter Notebook are both supported)
- Base file validation (Check the number of tags of each language)
- Validation only mode for CI/CD (Disable file generation)

## Installation 📦

### Linux

```sh
pip3 install mmg
```

### macOS

```sh
pip3 install mmg
```

If you have any issues with [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#macos), install it with the following command. WeasyPrint is only used to create PDFs.

```sh
brew install weasyprint
```

### Windows

1. MMG uses [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows) to create PDFs. WeasyPrint requires the GTK library, so download and run the latest [GTK3 installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases). **If you are not interested in creating PDFs, you can skip this step.** Other features of MMG are available without GTK.
2. Install MMG using Pip.

    ```sh
    pip3 install mmg
    ```

## How to Use 💡

Please refer to the [documentation](https://mmg.ryul1206.dev/latest/) for detailed usage and examples.

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

## Troubleshooting 💊

Please refer to the [troubleshooting](https://mmg.ryul1206.dev/latest/misc/troubleshooting/) page on the website.

## Changelog 📝

[CHANGELOG.md](https://github.com/ryul1206/multilingual-markdown/blob/develop/CHANGELOG.md)

## Contributors 🤝

<a href="https://github.com/ryul1206/multilingual-markdown/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ryul1206/multilingual-markdown" />
</a>

Made with [contrib.rocks](https://contrib.rocks).

If you are interested in how to contribute, please refer to the [contribution guide](https://mmg.ryul1206.dev/latest/contributing/).