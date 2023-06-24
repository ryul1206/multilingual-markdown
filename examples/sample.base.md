<!---------------------------->
<!-- multilingual suffix: en-US, fr-FR, ko-KR, ja-JP -->
<!-- no suffix: en-US -->
<!---------------------------->

<!-- [en-US] -->
# Sample Document
<!-- [ko-KR] -->
# 예제 문서
<!-- [fr-FR] -->
# Document exemple
<!-- [ja-JP] -->
# サンプルドキュメント
<!-- [common] -->

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)

[English](example.md),
[Français](example.fr-FR.md),
[한국어](example.ko-KR.md),
[日本語](example.ja-JP.md)

![lets go now](lets-go-now.jpg)

<!-- [en-US] -->
This document is the output from the `sample.base.md`.
<!-- [ko-KR] -->
이 문서는 `sample.base.md`로 부터 생성된 결과입니다.
<!-- [fr-FR] -->
Ce document est généré à partir du `sample.base.md`.
<!-- [ja-JP] -->
この記事は、`sample.base.md`から生成された結果です。
<!-- [common] -->

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

<!-- [ignore] -->
- **This section will be ignored.**
- **이 영역은 무시될 것입니다.**
- **Cette partie sera ignorée**
- **この領域は無視されます。**

<!-- [en-US] -->
**Table of contents**
<!-- [ko-KR] -->
**목차**
<!-- [fr-FR] -->
**Table des matières**
<!-- [ja-JP] -->
**目次**

<!-- [[ multilingual toc: level=2~3 ]] -->

<!-- [en-US] -->
## This is heading 2

### This is heading 3

```bash
This is a code block.
```

<!-- [ko-KR] -->
## 제목 수준 2

### 제목 수준 3

```bash
이것은 코드 블럭입니다.
```

<!-- [fr-FR] -->
## Ceci est un titre 2

### Ceci est un titre 3

```bash
Ceci est un bloc de code.
```

<!-- [ja-JP] -->
## タイトルレベル 2

### タイトルレベル 3

```bash
これはコードブロックです。
```
