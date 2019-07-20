<!---------------------------->
<!-- multilangual suffix: en, kr  -->
<!-- no suffix: en -->
<!---------------------------->

<!-- [en] -->
# Multilingual Markdown Generator
<!-- [kr] -->
# 다국어 마크다운 생성기
<!-- [common] -->

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)

[English](README.md), [한국어](README.kr.md)

**Table of contents**

<!-- [[ multilangual toc: level=2~3 ]] -->

![one-does-not-simply-speak-only-one-language](example/one-does-not-simply-speak-only-one-language.jpg)

<!-- [en] -->
## Features

- Auto table of contents
- Auto suffix to file name
- No suffix option (for one main language)
- UTF-8 encoding
<!-- [kr] -->
## 기능

- 자동 목차
- 파일 이름 뒤에 자동 접미사
- 접미사 생략 옵션 (한 개 언어만 가능)
- UTF-8 인코딩
<!-- [common] -->

> The output encoding is **'utf-8'**

<!-- [en] -->
## How to use
<!-- [kr] -->
## 사용법
<!-- [common] -->

<!-- [en] -->
1. Make `{something}.base.md` file
<!-- [kr] -->
1. `{파일이름}.base.md` 파일을 만듭니다.
<!-- [en] -->
2. Run this python file on your project root. Then, this will search all markdowns recursively.
<!-- [kr] -->
2. 프로젝트 루트 위치에서 파이썬 파일을 실행합니다. 그러면 알아서 하위폴더의 마크다운들을 찾아낼 것입니다.
<!-- [common] -->

    ```bash
    python multilang_md.py
    ```

<!-- [en] -->
3. You can find the `{something}.{suffix}.md` files in the same directory. For example:
    - default: `{something}.en.md`, `{something}.kr.md`, `{something}.es.md`, ...
    - no-suffix option to `en`: `{something}.md`, `{something}.kr.md`, `{something}.es.md`, ...
<!-- [kr] -->
3. 각 폴더의 동일한 위치에서 `{파일이름}.{접미사}.md`으로 된 파일들을 볼 수 있습니다. 예를 들어:
    - 기본: `{파일이름}.en.md`, `{파일이름}.kr.md`, `{파일이름}.es.md`, ...
    - `en`에 접미사 생략 옵션: `{파일이름}.md`, `{파일이름}.kr.md`, `{파일이름}.es.md`, ...
<!-- [common] -->
