
# 예제 문서

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)

[English](example.md),
[Français](example.fr-FR.md),
[한국어](example.ko-KR.md),
[日本語](example.ja-JP.md)

![lets go now](lets-go-now.jpg)

이 문서는 `sample.base.md`로 부터 생성된 결과입니다.

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

**목차**
1. [제목 수준 2](#제목-수준-2)
    1. [제목 수준 3](#제목-수준-3)

## 제목 수준 2

### 제목 수준 3

```bash
이것은 코드 블럭입니다.
```
