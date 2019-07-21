# 다국어 마크다운 생성기

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)

[English](README.md), [한국어](README.kr.md)

**Table of contents**

1. [How it works](#How-it-works)
1. [기능](#기능)
1. [사용법](#사용법)

## How it works
![how it works](how-it-works.png)

## 기능

- 자동 목차
- 파일 이름 뒤에 자동 접미사
- 접미사 생략 옵션 (한 개 언어만 가능)
- UTF-8 인코딩

> The output encoding is **'utf-8'**

## 사용법

1. `{파일이름}.base.md` 파일을 만듭니다.
2. 프로젝트 루트 위치에서 파이썬 파일을 실행합니다. 그러면 알아서 하위폴더의 마크다운들을 찾아낼 것입니다.

    ```bash
    python multilang_md.py
    ```

3. 각 폴더의 동일한 위치에서 `{파일이름}.{접미사}.md`으로 된 파일들을 볼 수 있습니다. 예를 들어:
    - 기본: `{파일이름}.en.md`, `{파일이름}.kr.md`, `{파일이름}.es.md`, ...
    - `en`에 접미사 생략 옵션: `{파일이름}.md`, `{파일이름}.kr.md`, `{파일이름}.es.md`, ...
