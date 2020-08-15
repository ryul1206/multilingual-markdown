# Multilingual Markdown Generator

🚀 **version 0.1.0**

[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/ryul1206/multilingual-markdown/badge/master)](https://www.codefactor.io/repository/github/ryul1206/multilingual-markdown/overview/master)

</div>

🌏 [English](README.md), [Français](README.fr.md), [한국어](README.kr.md)

---

**Table of Contents** ⚡

1. [Overview ](#Overview-)
    1. [How It Works](#How-It-Works)
    1. [Features](#Features)
1. [Installation](#Installation)
1. [How to Use](#How-to-Use)
    1. [(1) File Designation](#1-File-Designation)
    1. [(2) Recursive Option](#2-Recursive-Option)
    1. [More explanations](#More-explanations)
1. [Command Tags](#Command-Tags)
    1. [Headers](#Headers)
    1. [Badges](#Badges)
    1. [Main Text](#Main-Text)
1. [Contribution](#Contribution)
    1. [Contributors](#Contributors)

## Overview 🔎

### How It Works
![how it works](how-it-works.png)

### Features

- Auto suffix to file name
- No suffix option (for one main language)
- UTF-8 encoding. So *maybe* this will support almost all languages. :) 🍷
- Auto table of contents
    - Table of contents level options
    - Table of contents emoji **on-off** options

## Installation

First, install the required Python3 packages.

```sh
pip3 install click --user
```

Download `multilang_md.py` as a hidden file on your home directory with the command below:

```sh
cd
curl -fsSL https://raw.githubusercontent.com/ryul1206/multilingual-markdown/master/multilang_md.py > .multilang_md.py
```

Then, register the following alias in your shell. Just add the following to the end of `~/.bashrc` or `~/.zshrc`.

```sh
# vim ~/.bashrc
alias mmg="python3 ~/.multilang_md.py"
```

Now when you open a new terminal you can use the new command `mmg`.

```sh
mmg --help
```

## How to Use

Make `{something}.base.md` files. See [README.base.md](README.base.md) and [example.base.md](example/example.base.md) for examples, and [Command Tags](#Command-Tags) for rules.

**(Note) A wrong format of base-file will break generated style.**

### (1) File Designation

Enter the `*.base.md` files that you want to create in multiple languages as arguments to the `mmg` command.

```sh
mmg FileName.base.md
```

Multiple arguments are separated by spaces.

```sh
mmg Foo.base.md Bar.base.md Baz.base.md
```

### (2) Recursive Option

If you want to convert all base files in the current directory and subdirectories, use the `--recursive` or `-r` option.
The recursive option searches all subfolders based on where the command is entered.
You cannot specify a folder as an argument yet.

```sh
mmg --recursive
```

### More explanations

- You can find the `{something}.{suffix}.md` files in the same directory. For example:
    - By default: `{something}.en.md`, `{something}.kr.md`, `{something}.es.md`, ...
    - When no-suffix option on `en`: `{something}.md`, `{something}.kr.md`, `{something}.es.md`, ...
- Since this generator overwrites the auto-generated files each time, you do not have to delete them every time when you modify the `{something}.base.md`. Just run step 2 again.

## Command Tags

### Headers

Headers must be declared before the body begins.

1. **Suffix Declaration**

    Declare the language you want to use. The following example declares `en` and `kr` and others as keywords. These keywords are used as suffixes.

    ```markdown
    <!-- multilangual suffix: en, kr, fr, es, jp, cn -->
    ```

1. **Hidden Suffix** (Optional)

    The `no suffix` option can prevent the suffix from being appended when creating the file. In other words, setting `no suffix` to `en` will generate `FileName.md` instead of `FileName.en.md`. This is useful because the main `README` in **GitHub** is not recognized when it has a suffix.

    ```markdown
    <!-- no suffix: en -->
    ```

### Badges

[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-yellow.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-green.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-blue.svg)](https://github.com/ryul1206/multilingual-markdown)
...

```markdown
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
```

### Main Text

Everything that the parser reads after the tag below is recognized as the main text. (So you have to write the header before main).

1. **Keywords**

    1. Language Classification

        The tags that distinguish languages are written in the form `<!-- [keyword] -->`. If one keyword is recognized, it will be recognized as that keyword until another keyword is seen.

        ```markdown
        <!-- [en] -->
        <!-- [kr] -->
        <!-- [fr] -->
        <!-- [es] -->
        <!-- [jp] -->
        <!-- [cn] -->
        ...
        ```

    1. Common Section

        You can use the 'common' keyword to create a common entry for all files to be generated.

        ```markdown
        <!-- [common] -->
        ```

    1. Ignored Section

        Sometimes you do not want to include some items such as comments or TODOs in the files to be generated. If so, use the `ignore` keyword.

        ```markdown
        <!-- [ignore] -->
        ```

1. **Table of contents**

    The tags below are automatically replaced to the table of contents by the generator. The level of the table of contents can be determined through the `level` option. The highest-level of title(`# title`) is level 1 because it is `<h1>` in HTML.

    **(Note) If you skip the title level of the markdown marked with `#`, an error will occur. In other words, the subtitle of `##` must be `###`.**

    ```markdown
    <!-- [[ multilangual toc: level=2~3 ]] -->
    ```

    1. **`level` option**
        - There are four ways to mark `level`. You can change the numbers below.
            - `level=2`: Make the 2nd level to table of contents.
            - `level=2~`: Make the 2nd ~ 9th level to table of contents.
            - `level=~4`: Make the 1st ~ 4th level to table of contents.
            - `level=2~4`: Make the 2nd ~ 4th level to table of contents.
        - You can write the `table of contents` tags multiple times in one document, and also put different `level` options each time.
        - **CAUTION💥**: If you omit this `level`, the parser will not recognize it.
        - **CAUTION💥**: The `table of contents` tag automatically changes the current keyword to `common`. So this tag is also implicitly in `common`.
    2. **`no-emoji` option**
        - In rare cases, you may want to subtract emoji from the table of contents while inserting emoji in the title.😱 If you are in this situation, apply the `no-emoji` option as shown below.😎

        ```markdown
        <!-- [[ multilangual toc: level=2~3 no-emoji ]] -->
        ```

## Contribution

I would appreciate anything you send. (e.g. translations, simple improvements, bug reports, and so on.)

> Especially I would be very grateful if you could translate this `README.md` document into your language not listed here and give it to me.

### Contributors

> The contributor list is available in English only.

- [Francis Piérot](https://github.com/bkg2018) - French translation ([#1](https://github.com/ryul1206/multilingual-markdown/pull/1))
