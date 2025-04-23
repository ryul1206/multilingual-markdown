
<div align="center" markdown>
   <img src="https://github.com/ryul1206/multilingual-markdown/assets/19263912/7cfded93-4c64-428a-b027-76a621de92a6" width="500" alt="Multilingual Markdown Generator" />
</div>

<div align="center" markdown>

# [다국어 마크다운 생성기](https://mmg.ryul1206.dev/latest/ko)

이 패키지는 단일 기본 파일로부터 다국어 콘텐츠를 관리하고, i18n 마크 다운을 생성하는 명령 줄 인터페이스 (CLI)를 제공합니다.

[![PyPI - Version](https://img.shields.io/pypi/v/mmg?color)](https://pypi.org/project/mmg/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mmg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown)
[![PyPI - License](https://img.shields.io/pypi/l/mmg)](https://github.com/ryul1206/multilingual-markdown/blob/main/LICENSE)

[![PyPI - Downloads](https://img.shields.io/pypi/dm/mmg)](https://pypi.org/project/mmg/)
[![PyPI Downloads](https://static.pepy.tech/badge/mmg)](https://pepy.tech/projects/mmg)

🌏
[**English**](https://github.com/ryul1206/multilingual-markdown/blob/main/README.md) |
[**Français**](https://github.com/ryul1206/multilingual-markdown/blob/main/README.fr.md) |
한국어 |
[**日本語**](https://github.com/ryul1206/multilingual-markdown/blob/main/README.ja.md)

Bash, Zsh, Windows PowerShell에서 사용할 수 있습니다.

</div>

---

**목차** ⚡

1. [개요](#개요-)
    1. [작동 방식](#작동-방식)
    1. [특징](#특징)
1. [설치](#설치-)
    1. [Linux](#linux)
    1. [macOS](#macos)
    1. [Windows](#windows)
1. [사용법](#사용법-)
1. [문제 해결](#문제-해결-)
1. [Changelog](#changelog-)
1. [기여하신 분들](#기여하신-분들-)

## 개요 🔎

### 작동 방식

Base 파일 하나만 관리하기 때문에, 콘텐츠 번역이 누락되거나 불일치되는 실수를 줄일 수 있습니다.
또한 단일 파일에서 편집하는 덕분에, [Copilot](https://github.com/features/copilot)과 같은 AI 도구의 자동 완성 기능으로 편리한 번역을 기대할 수 있습니다.

Markdown:

<div align="center">
   <img src="https://github.com/ryul1206/multilingual-markdown/assets/19263912/fd88420e-ddd1-403c-a9df-3429ec8095e3" width="800" alt="How It Works: Markdown" />
</div>

Jupyter Notebook:

<div align="center">
   <img src="https://github.com/ryul1206/multilingual-markdown/assets/19263912/ff2ef5d9-da9f-4d91-9618-fb933802bf69" width="900" alt="How It Works: Jupyter Notebook" />
</div>

### 특징

다음 기능을 지원합니다:

- **Markdown, Jupyter Notebook(`.ipynb`)을 입력 형식으로 사용**
- **As-is(있는 그대로), HTML, PDF 출력 형식**
- Bash, Zsh, Windows PowerShell용 명령줄 인터페이스
- 파이썬 API
- `-r` 옵션을 사용한 재귀 순회 모드 (As-is, HTML, PDF 모두 지원됨)
- YAML 파일을 사용한 일괄 처리 모드 (As-is만 지원)
- [IETF 언어 태그](https://ko.wikipedia.org/wiki/IETF_%EC%96%B8%EC%96%B4_%ED%83%9C%EA%B7%B8)
- UTF-8 인코딩
- 레벨 및 이모티콘 옵션이 포함된 목차 자동 생성 (Markdown 및 Jupyter Notebook 모두 지원)
- Base 파일 유효성 검사 (언어별 태그 개수 확인)
- CI/CD를 위한 유효성 검사 only 모드 (파일 생성 비활성화)

## 설치 📦

### Linux

```sh
pip3 install mmg
```

### macOS

```sh
pip3 install mmg
```

만약 [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#macos)와 관련된 문제가 발생한다면, 아래 명령어으로 설치해주세요. WeasyPrint는 PDF를 생성할 때에만 사용됩니다.

```sh
brew install weasyprint
```

### Windows

윈도우에는 파이썬이 기본으로 설치되어 있지 않습니다. 파이썬을 설치한 후 파이썬 패키지 관리자 pip로 MMG를 설치해주세요.

```powershell
pip3 install mmg
```

[Microsoft Store](https://apps.microsoft.com/)에서 파이썬을 설치했다면, MMG 설치 시 다음과 같은 경고가 나타날 수 있습니다. (표시되는 경로는 사용자마다 다를 수 있습니다.)

```powershell
$ pip3 install mmg
...
  WARNING: The script mmg.exe is installed in 'C:\Users\...\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed mmg-2.0.1
```

이 경고가 나타나면, 터미널에서 `mmg` 명령어를 찾지 못하는 상태입니다. 경고 문구에 안내된 경로를 환경변수 `PATH`에 추가해주세요. 추가하는 방법은 [문제 해결](https://mmg.ryul1206.dev/2.0/ko/misc/troubleshooting/) 문서에 적어두었습니다.

추가적으로, MMG는 [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)를 사용하여 PDF를 생성합니다. WeasyPrint는 GTK 라이브러리가 있어야 작동하므로, 최신 [GTK3 설치 파일](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)을 다운로드하고 실행하세요. **PDF 생성 기능을 사용하지 않는다면 이 단계을 건너뛰어도 됩니다.** GTK가 없더라도 MMG의 다른 기능들은 정상적으로 쓸 수 있습니다.

## 사용법 💡

자세한 사용법과 예제는 [문서](https://mmg.ryul1206.dev/latest/ko/)를 참고해주세요.

```sh
$ mmg --help
Usage: mmg [OPTIONS] [FILE_NAMES]...

  FILE_NAMES: Base file names to convert.

  Supported extensions are:
      .md, .markdown, .mkd (Markdown)
      .mdx (MDX - Markdown + JSX) [experimental]
      .rmd (R Markdown) [experimental]
      .mmd (MultiMarkdown) [experimental]
      .qmd (Quarto) [experimental]
      .ipynb (Jupyter Notebook)

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

## 문제 해결 💊

[문제 해결](https://mmg.ryul1206.dev/latest/ko/misc/troubleshooting/) 페이지를 참고해주세요.

## Changelog 📝

[CHANGELOG.md](https://github.com/ryul1206/multilingual-markdown/blob/develop/CHANGELOG.md)

## 기여하신 분들 🤝

<a href="https://github.com/ryul1206/multilingual-markdown/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ryul1206/multilingual-markdown" />
</a>

[contrib.rocks](https://contrib.rocks)로 만들었습니다.

기여 방법에 관심이 있으시다면, [기여 가이드](https://mmg.ryul1206.dev/latest/ko/contributing/)를 참고해주세요.