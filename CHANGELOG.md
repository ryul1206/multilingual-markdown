# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

<!--
알파벳 순서
Added 새로운 기능
Changed 기존 기능의 변경사항
Deprecated 곧 지워질 기능
Removed 지금 지워진 기능
Fixed 버그 픽스
Security 취약점이 있는 경우
-->

To do

- Better emoji detection (https://stackoverflow.com/questions/43146528/how-to-extract-all-the-emojis-from-text)

## [1.0.a2] - 2021-06-17

- **Fixed** - Fix 'import-im6.q16' errors caused by missing shebang.

## [1.0.a1] - 2021-06-17

- **Added** - `pip install` from the Python Package Index.
- **Added** - More CLI features: check, verbose, version, and yes parameter for confirmation.
- **Added** - Detect a failure of ToC level [PR #2](https://github.com/ryul1206/multilingual-markdown/pull/2) by [**@mathben**](https://github.com/mathben)
- **Added** - Detect an error of missing language keywords. [PR #2](https://github.com/ryul1206/multilingual-markdown/pull/2) by [**@mathben**](https://github.com/mathben)
- **Changed** - Update README pip installation with requirements.txt [PR #2](https://github.com/ryul1206/multilingual-markdown/pull/2) by [**@mathben**](https://github.com/mathben)
- **Fixed** - Correct `mmg` completion message to distinguish between singular and plural.
- **Fixed** - Fix regex pattern to recognize [IETF language tags](https://en.wikipedia.org/wiki/IETF_language_tag)

## [0.2.0] - 2020-08-16

- **Added** - New CLI command by [Click package](https://click.palletsprojects.com/en/7.x/). `mmg --help`
- **Changed** - All Python exceptions changed to [Click exceptions](https://click.palletsprojects.com/en/7.x/api/#exceptions).
- **Changed** - More detailed README. (Installation method, CLI usage, and some warnings.)

## [0.1.0] - 2020-07-26

- **Added** - Initial python module. (`multilang_md,py`)
- **Added** - Added french translation to README and example. [PR #1](https://github.com/ryul1206/multilingual-markdown/pull/1) by [**@bkg2018**](https://github.com/bkg2018)

[unreleased]: https://github.com/ryul1206/multilingual-markdown/compare/v1.0.a2...develop
[1.0.a2]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v1.0.a2
[1.0.a1]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v1.0.a1
[0.2.0]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v0.2.0
[0.1.0]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v0.1.0
