
# Sample Document

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)

[English](example.md),
[Français](example.fr-FR.md),
[한국어](example.ko-KR.md),
[日本語](example.ja-JP.md)

![lets go now](lets-go-now.jpg)

This document is the output from the `sample.base.md`.

```sh
$ mmg sample.base.md
----------------------
 ✅ ./sample.base.md
----------------------
 => 1 base markdown was found.
    Your verbosity is 0. Try the `--verbose` option for more details.
Do you want to convert these files? [y/N] y
----------------------
./sample.base.md
        en-US: ./sample.md
        fr-FR: ./sample.fr-FR.md
        ko-KR: ./sample.ko-KR.md
        ja-JP: ./sample.ja-JP.md
----------------------
 => 1 base file has been converted.
```

**Table of contents**
1. [This is heading 2](#this-is-heading-2)
    1. [This is heading 3](#this-is-heading-3)

## This is heading 2

### This is heading 3

```bash
This is a code block.
```
