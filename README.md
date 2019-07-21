# Multilingual Markdown Generator

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)

[English](README.md), [한국어](README.kr.md)

**Table of contents**

1. [How It Works](#How-It-Works)
1. [Features](#Features)
1. [How to Use](#How-to-Use)
1. [Command Keywords](#Command-Keywords)
    1. [Headers](#Headers)

## How It Works
![how it works](how-it-works.png)

## Features

- Auto table of contents
- Auto suffix to file name
- No suffix option (for one main language)
- UTF-8 encoding

> The output encoding is **'utf-8'**

## How to Use

1. Make `{something}.base.md` file
2. Run this python file on your project root. Then, this will search all markdowns recursively.

    ```bash
    python multilang_md.py
    ```

3. You can find the `{something}.{suffix}.md` files in the same directory. For example:
    - default: `{something}.en.md`, `{something}.kr.md`, `{something}.es.md`, ...
    - no-suffix option to `en`: `{something}.md`, `{something}.kr.md`, `{something}.es.md`, ...

## Command Keywords

### Headers

1. Declare the language you want to use. The following example declares `en` and `kr` as keywords. These keywords are used as suffixes.

    ```markdown
    <!-- multilangual suffix: en, kr  -->
    ```


```markdown
<!-- no suffix: en -->
```

```markdown
```

```markdown
```
```markdown
```
```markdown
```
