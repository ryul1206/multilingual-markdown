# Sample Document

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)

[English](example.en-US.md),
[Français](example.fr-FR.md),
[한국어](example.ko-KR.md),
[日本語](example.ja-JP.md)

![lets go now](lets-go-now.jpg)

This document is the output from the `base` document.

```sh
$ cd example
$ mmg example.base.md
----------------------
./example.base.md
    en-US: ./example.en-US.md
    fr-FR: ./example.fr-FR.md
    ko-KR: ./example.ko-KR.md
    ja-JP: ./example.ja-JP.md
----------------------
 => 1 base markdown was converted.
```

**Table of contents**
1. [This is heading 2](#This-is-heading-2)
    1. [This is heading 3](#This-is-heading-3)

## This is heading 2

### This is heading 3

```bash
This is a code block.
```

