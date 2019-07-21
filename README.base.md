<!---------------------------->
<!-- multilangual suffix: en, kr  -->
<!-- no suffix: en -->
<!---------------------------->

<!-- [en] -->
# Multilingual Markdown Generator
<!-- [kr] -->
# 다국어 마크다운 생성기
<!-- [common] -->

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)

[English](README.md), [한국어](README.kr.md)

<!-- [en] -->
**Table of contents**
<!-- [kr] -->
**목차**
<!-- [common] -->

<!-- [[ multilangual toc: level=2~3 ]] -->

<!-- [en] -->
## How It Works
<!-- [kr] -->
## 작동 방식
<!-- [common] -->
![how it works](how-it-works.png)

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

<!-- [en] -->
## How to Use
<!-- [kr] -->
## 사용법
<!-- [common] -->

<!-- [en] -->
1. Make `{something}.base.md` files. See [README.base.md](README.base.md) and [example.base.md](example/example.base.md) for examples, and [Command Tags](#Command-Tags) for rules.
<!-- [kr] -->
1. `{파일이름}.base.md` 파일을 만듭니다. 예제는 [README.base.md](README.base.md) 와 [example.base.md](example/example.base.md) 를 참고하시고, 작성하는 규칙은 [명령어 태그](#명령어-태그)를 참고하십시오.
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

<!-- [en] -->
4. Since this generator overwrites the auto-generated files each time, you do not have to delete them every time when you modify the `base`. Just run step 2 again.
<!-- [kr] -->
4. 이 생성기는 자동생성된 파일을 매번 덮어쓰기 때문에, `base` 파일을 수정하더라도 매번 지울 필요가 없습니다. 그저 방금 전 2단계를 다시 실행하면 됩니다.
<!-- [common] -->

<!-- [en] -->
## Command Tags
<!-- [kr] -->
## 명령어 태그
<!-- [common] -->

<!-- [en] -->
### Headers

Headers must be declared before the body begins.
<!-- [kr] -->
### 헤더

헤더는 반드시 본문이 시작하기 전에 선언되어야 합니다.
<!-- [common] -->

<!-- [en] -->
1. **Suffix Declaration**

    Declare the language you want to use. The following example declares `en` and `kr` as keywords. These keywords are used as suffixes.
<!-- [kr] -->
1. **접미사 선언**

    사용할 언어를 선언하십시오. 다음 예제는 `en`과 `kr`을 키워드로 선언하였습니다. 이 키워드들은 접미사로 사용됩니다.
<!-- [common] -->

    ```markdown
    <!-- multilangual suffix: en, kr  -->
    ```

<!-- [en] -->
2. **Hidden Suffix** (Optional)

    The `no suffix` option can prevent the suffix from being appended when creating the file. In other words, setting `no suffix` to `en` will generate `FileName.md` instead of `FileName.en.md`. This is useful because the main `README` in **GitHub** is not recognized when it has a suffix.
<!-- [kr] -->
2. **접미사 숨기기** (필수 아님)

    `no suffix` 옵션은 파일을 생성할 때 접미사가 붙는 것을 방지할 수 있습니다. 다시 말하자면 `no suffix`를 `en`으로 설정하면 `파일이름.en.md`가 아니라 `파일이름.md`가 생성됩니다. **GitHub**에서 메인 `README`는 접미사가 붙으면 인식이 안되기 때문에 이 기능이 유용합니다.
<!-- [common] -->

    ```markdown
    <!-- no suffix: en -->
    ```

<!-- [en] -->
### Main Text

Everything that the parser reads after the tag below is recognized as the main text. (So ​​you have to write the header before main).
<!-- [kr] -->
### 본문

파서가 아래의 태그들를 읽는 순간부터 그 이후에 읽는 모든 것은 메인 텍스트로 인식합니다. (그래서 헤더를 메인 이전에 적어야 합니다.)
<!-- [common] -->

<!-- [en] -->
1. **Keywords**
<!-- [kr] -->
1. **키워드**
<!-- [common] -->

<!-- [en] -->
    1. Language Classification

        The tags that distinguish languages ​​are written in the form `<!-- [keyword] -->`. If one keyword is recognized, it will be recognized as that keyword until another keyword is seen.
<!-- [kr] -->
    1. 언어 분류

        언어를 구분하는 태그는 `<!-- [키워드] -->` 같은 형태로 작성합니다. 하나의 키워드가 인식되면 다른 키워드가 나타날 때까지 해당 키워드로 인식됩니다.
<!-- [common] -->

        ```markdown
        <!-- [en] -->
        <!-- [kr] -->
        <!-- [fr] -->
        <!-- [es] -->
        <!-- [jp] -->
        <!-- [cn] -->
        ...
        ```

<!-- [en] -->
    1. Common Section

        You can use the 'common' keyword to create a common entry for all files to be generated.
<!-- [kr] -->
    1. 공통 영역

        생성될 모든 파일에 공통적으로 들어갈 내용은 `common` 키워드를 사용하여 작성하면 됩니다.
<!-- [common] -->

        ```markdown
        <!-- [common] -->
        ```

<!-- [en] -->
    1. Ignored Section

        Sometimes you do not want to include some items such as comments or TODOs in the files to be generated. If so, use the `ignore` keyword.
<!-- [kr] -->
    1. 무시되는 영역

        주석이나 TODO와 같은 몇 가지 항목들은 생성될 파일에 포함하고 싶지 않는 경우가 있습니다. 그런 경우 `ignore` 키워드를 사용하세요.
<!-- [common] -->

        ```markdown
        <!-- [ignore] -->
        ```

<!-- [en] -->
1. **Table of contents**

    The tags below are automatically replaced to the table of contents by the generator. The level of the table of contents can be determined through the `level` option. The highest-level of title(`# title`) is level 1 because it is `<h1>` in HTML.
<!-- [kr] -->
1. **목차**

    아래 태그는 생성기에 의해 목차로 자동교체됩니다. 목차의 수준은 `level` 부분을 통해 정할 수 있습니다. 가장 큰 제목(`# 제목`)은 html에서 `<h1>`이기 때문에 `level 1`입니다.
<!-- [common] -->

    ```markdown
    <!-- [[ multilangual toc: level=2~3 ]] -->
    ```

<!-- [en] -->
    - There are four ways to mark `level`. You can change the numbers below.
        - `level=2`: Make the 2nd level to table of contents.
        - `level=2~`: Make the 2nd ~ 9th level to table of contents.
        - `level=~4`: Make the 1st ~ 4th level to table of contents.
        - `level=2~4`: Make the 2nd ~ 4th level to table of contents.
    - You can write the `table of contents` tags multiple times in one document, and also put different `level` options each time.
    - **CAUTION**: If you omit this `level` or leave it as `level =`(spacing), the parser will not recognize it.
    - **CAUTION**: The `table of contents` tag automatically changes the current keyword to `common`. So this tag is also implicitly in `common`.
<!-- [kr] -->
    - `level`을 표기하는 방법은 총 4가지입니다. 여러분의 필요에 따라 숫자는 바꾸시면 됩니다.
        - `level=2`: 2수준의 제목만 목차로 만듭니다.
        - `level=2~`: 2~9수준의 제목만 목차로 만듭니다.
        - `level=~4`: 1~4수준의 제목만 목차로 만듭니다.
        - `level=2~4`: 2~4수준의 제목만 목차로 만듭니다.
    - 하나의 문서에서 `table of contents` 태그는 여러번 쓸 수 있고, 매번 다른 `level` 옵션을 줄 수도 있습니다.
    - **주의**: 만약 `level`을 생략하거나 `level =`과 같이 띄어쓰면 파서가 인식하지 못합니다.
    - **주의**: 목차 태그는 자동으로 현재 키워드를 `common`으로 변경합니다. 그래서 목차 태그 또한 암묵적으로 `common`에 속합니다.
<!-- [common] -->
