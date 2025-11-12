# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
알파벳 순서
Added 새로운 기능
Fixed 버그 픽스
Changed 기존 기능의 변경사항
Deprecated 곧 지워질 기능
Improved 기능 개선
Removed 지금 지워진 기능
Security 취약점이 있는 경우
-->

## [Upcoming Release][unreleased]

## [2.1.0] - 2025-11-12

Temporarily marked Python 3.14 as unsupported until upstream dependencies add compatibility.

- **Added** - Add support for including a preamble at the top of each generated document via the `--preamble` CLI option ([#34](https://github.com/ryul1206/multilingual-markdown/issues/34))
   - Users can now add copyright or informational headers. You can include a `<FILE_NAME>` placeholder in the preamble text to automatically insert the file name.
   - When enabled, the preamble will be added to each output file during conversion.
- **Added** - Support for additional markdown extensions (experimental):
   - .markdown, .mkd (Markdown variants)
   - .mdx (MDX - Markdown + JSX)
   - .rmd (R Markdown)
   - .mmd (MultiMarkdown)
   - .qmd (Quarto)
- **Changed** - Move `WeasyPrint` from required dependencies to optional dependencies (Resolves [#33](https://github.com/ryul1206/multilingual-markdown/issues/33))
   - Now install PDF export support via:

     ```bash
     pip install mmg[pdf]
     ```

   - This change reduces unnecessary dependencies for users who don’t need PDF generation.
- **Changed** - Now the `-y` (`--yes`) option can also be used when running in batch mode with the `--batch` flag. ([#31](https://github.com/ryul1206/multilingual-markdown/issues/31))
- **Improved** - Update CLI help message to show all supported file extensions
- **Improved** - Refactor regex pattern compilation for better performance by moving it to module level

Please refer to the [CHANGELOG in the dev branch](https://github.com/ryul1206/multilingual-markdown/blob/dev/CHANGELOG.md) for upcoming release changes.

## [2.0.1] - 2025-04-03

- **Fixed** - Fix incorrect CLI messages [#30](https://github.com/ryul1206/multilingual-markdown/issues/30)
- **Fixed** - Resolve issue with missing pyyaml package
- **Changed** - Migrate from Poetry to UV
- **Security** - Update dependencies; resolve [#29](https://github.com/ryul1206/multilingual-markdown/issues/29) and [#28](https://github.com/ryul1206/multilingual-markdown/issues/28)

## [2.0.0] - 2023-10-09

- **Added** - Add batch processing mode with YAML file. Please refer to [mmg.yaml](mmg.yml) file for usage.
- **Added** - Simple Python API for script usage [#13](https://github.com/ryul1206/multilingual-markdown/issues/13)
- **Added** - Add automated testing for stability and reliability [#18](https://github.com/ryul1206/multilingual-markdown/issues/18)
- **Added** - Add "Validation Only" command to the mmg CLI [#20](https://github.com/ryul1206/multilingual-markdown/issues/20)
- **Added** - Add "Skip Validation" command to the mmg CLI.
- **Added** - Support Jupyter Notebook(.ipynb) [#13](https://github.com/ryul1206/multilingual-markdown/issues/13)
- **Added** - Support for HTML, PDF output formats [#19](https://github.com/ryul1206/multilingual-markdown/issues/19)
- **Added** - Publish documentation to Github Pages (http://mmg.ryul1206.dev/) [#17](https://github.com/ryul1206/multilingual-markdown/issues/17)
- **Changed** - Use [Poetry](https://python-poetry.org/) for Python package management [#16](https://github.com/ryul1206/multilingual-markdown/issues/16)
- **Fixed** - Bug in `remove_emoji` function that fails to remove all emojis [#23](https://github.com/ryul1206/multilingual-markdown/issues/23)
- **Fixed** - Fixes and enhancements for code block tracking [#24](https://github.com/ryul1206/multilingual-markdown/issues/24)
- **Improved** - From version 2.0, skipping header levels will no longer cause an error when generating a table of contents. In versions 1.X, if header 2 was skipped and header 3 followed immediately, an error occurred when creating the table of contents. However, we have removed this restriction as it was deemed inconvenient. Instead, in such cases, the skipped header 3 will not be displayed in the table of contents.
- **Removed** - Drop support for Python 3.6
   - Python 3.6 EOL is 23 Dec 2021
   - Poetry requires Python 3.7 or higher

## [1.0.3] - 2023-04-16

- **Fixed** - Bug fix for `--yes` flag. #21 by [@ryukzak](https://github.com/ryukzak)
- **Fixed** - Fix broken URL for CodeFactor badge in README
- **Fixed** - Resolve PowerShell bug for specific file names

## [1.0.2] - 2022-06-19

- **Changed** - Change the verbosity level of some display information.
- **Fixed** - Fix [#10](https://github.com/ryul1206/multilingual-markdown/issues/10): The CLI is not working on the Windows PowerShell.
- **Removed** - Delete unnecessary sentences.

   ```sh
   Do you want to convert these files? [y/N]
   Please respond with 'yes' or 'no' (or 'y' or 'n').  # <--- THIS LINE WAS DELETED.
   ```

## [1.0.1] - 2021-07-02

- **Added** - Japanese README
- **Changed** - Move the log's check icon to the front.
- **Fixed** - Fix [#4](https://github.com/ryul1206/multilingual-markdown/issues/4): ToC contents are broken when a header(#) has a link.

## [1.0.a2] - 2021-06-17

- **Fixed** - Fix 'import-im6.q16' errors caused by missing shebang.
- **Fixed** - Fix an infinite loop bug when select no in query_yes_no.

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

[unreleased]: https://github.com/ryul1206/multilingual-markdown/compare/v2.1.0...develop
[2.1.0]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v2.1.0
[2.0.1]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v2.0.1
[2.0.0]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v2.0.0
[1.0.3]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v1.0.3
[1.0.2]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v1.0.2
[1.0.1]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v1.0.1
[1.0.a2]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v1.0.a2
[1.0.a1]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v1.0.a1
[0.2.0]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v0.2.0
[0.1.0]: https://github.com/ryul1206/multilingual-markdown/releases/tag/v0.1.0
