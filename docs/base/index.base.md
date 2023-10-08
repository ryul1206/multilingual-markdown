<!---------------------------->
<!-- multilingual suffix: en, fr, ko, ja -->
<!---------------------------->

<div align="center">
   <img src="/assets/mmg-logo-dark.jpg" width="500" alt="Multilingual Markdown Generator" />
</div>
&nbsp;

<!-- [en] -->
# Multilingual Markdown Generator
<!-- [fr] -->
# Générateur de Markdown Multilingue
<!-- [ko] -->
# 다국어 마크다운 생성기
<!-- [ja] -->
# 多言語マークダウンジェネレータ
<!-- [common] -->

<!-- [en] -->
This package provides a command-line interface to manage multilingual contents and generate i18n markdown from a single base file.
<!-- [fr] -->
Ce package fournit une interface de ligne de commande pour gérer les contenus multilingues et générer des démarques i18n à partir d'un seul fichier de base.
<!-- [ko] -->
이 패키지는 단일 기본 파일로부터 다국어 콘텐츠를 관리하고, i18n 마크 다운을 생성하는 명령 줄 인터페이스 (CLI)를 제공합니다.
<!-- [ja] -->
このパッケージは、単一のデフォルトのファイルから多言語コンテンツを管理してi18nマークダウンを生成するコマンドラインインタフェース（CLI）を提供しています。
<!-- [common] -->

<!-- [en] -->
Available in Bash, Zsh, and Windows PowerShell.
<!-- [fr] -->
Disponible dans Bash, Zsh et Windows PowerShell.
<!-- [ko] -->
Bash, Zsh, Windows PowerShell에서 사용할 수 있습니다.
<!-- [ja] -->
Bash, Zsh, WindowsPowerShellで使用できます。
<!-- [common] -->

---

!!! note ""

<!-- [en] -->
    English | [**Français**](/fr) | [**한국어**](/ko) | [**日本語**](/ja)
<!-- [fr] -->
    [**English**](/) | Français | [**한국어**](/ko) | [**日本語**](/ja)
<!-- [ko] -->
    [**English**](/) | [**Français**](/fr) | 한국어 | [**日本語**](/ja)
<!-- [ja] -->
    [**English**](/) | [**Français**](/fr) | [**한국어**](/ko) | 日本語
<!-- [common] -->

<!-- [en] -->
## How It Works 💡

By managing only one Base file, we can reduce the number of errors caused by missing or mismatched translations.
Additionally, thanks to editing in a single file, we can expect convenient translation with the auto-completion function of AI tools such as [Copilot](https://github.com/features/copilot).
<!-- [fr] -->
## Comment Ça Fonctionne 💡

En gérant un seul fichier Base, nous pouvons réduire le nombre d'erreurs causées par des traductions manquantes ou incohérentes.
De plus, grâce à l'édition dans un seul fichier, nous pouvons nous attendre à une traduction pratique avec la fonction de complétion automatique des outils AI tels que [Copilot](https://github.com/features/copilot).
<!-- [ko] -->
## 작동 방식 💡

Base 파일 하나만 관리하기 때문에, 콘텐츠 번역이 누락되거나 불일치되는 실수를 줄일 수 있습니다.
또한 단일 파일에서 편집하는 덕분에, [Copilot](https://github.com/features/copilot)과 같은 AI 도구의 자동 완성 기능으로 편리한 번역을 기대할 수 있습니다.
<!-- [ja] -->
### 作動方式 💡

1 つの Base ファイルのみを管理することで、コンテンツの翻訳漏れや不一致によるエラーを減らすことができます。
また、単一ファイルで編集できるため、[Copilot](https://github.com/features/copilot) などの AI ツールの自動補完機能による便利な翻訳を期待できます。
<!-- [common] -->

Markdown:

<div align="center">
   <img src="/assets/how-it-works-md.png" width="800" alt="How It Works: Markdown" />
</div>

Jupyter Notebook:

<div align="center">
   <img src="/assets/how-it-works-ipynb.png" width="900" alt="How It Works: Jupyter Notebook" />
</div>

<!-- [en] -->
## Features ✨

Supports the following features:

- **Markdown, Jupyter Notebook(`.ipynb`) as input formats**
- **As-is, HTML, PDF as ouput formats**
- Command-line interface for Bash, Zsh, Windows PowerShell
- Python API
- Recursive traversal mode with `-r` option (As-is, HTML, PDF are all supported)
- Batch processing mode with YAML file (Only `As-is` is supported)
- [IETF language tags](https://en.wikipedia.org/wiki/IETF_language_tag)
- UTF-8 encoding
- Automatic generation of table of contents with level and emoji options (Markdown and Jupyter Notebook are both supported)
- Base file validation (Check the number of tags of each language)
- Validation only mode for CI/CD (Disable file generation)
<!-- [ko] -->
## 특징 ✨

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
<!-- [ja] -->
## 特徴 ✨

次の機能をサポートします。

- **Markdown、Jupyter Notebook（`.ipynb`）を入力形式で使用する**
- **As-is(そのまま)、HTML、PDF出力形式**
- Bash、Zsh、Windows PowerShell用のコマンドラインインターフェイス
- Python API
- `-r`オプションを使用した再帰巡回モード（As-is、HTML、PDFの両方をサポート）
- YAMLファイルを使用したバッチモード（As-isのみサポート）
- [IETF言語タグ](https://ja.wikipedia.org/wiki/IETF%E8%A8%80%E8%AA%9E%E3%82%BF%E3%82%B0)
- UTF-8エンコーディング
- レベルと絵文字オプションを含む目次の自動生成（MarkdownとJupyter Notebookの両方をサポート）
- Baseファイルの検証(言語別のタグ数の確認)
- CI / CDのための検証のみモード（ファイル生成を無効にする）
<!-- [fr] -->
## Caractéristiques ✨

Prend en charge les fonctionnalités suivantes :

- **Markdown, Jupyter Notebook(`.ipynb`) comme formats d'entrée**
- **Tel quel, HTML, PDF comme formats de sortie**
- Interface de ligne de commande pour Bash, Zsh, Windows PowerShell
- API Python
- Mode de parcours récursif avec l'option `-r` (tels quels, HTML, PDF sont tous pris en charge)
- Mode de traitement par lots avec fichier YAML (seul `tel quel` est pris en charge)
- [Étiquette d'identification de langues IETF](https://fr.wikipedia.org/wiki/%C3%89tiquette_d%27identification_de_langues_IETF)
- Encodage UTF-8
- Génération automatique de table des matières avec options de niveau et options de emoji (Markdown et Jupyter Notebook sont tous deux pris en charge)
- Validation du fichier de base (Vérifier le nombre de balises de chaque langue)
- Mode validation uniquement pour CI/CD (désactiver la génération de fichiers)
<!-- [common] -->

<!-- [en] -->
## User Guide 📖
<!-- [fr] -->
## Guide de l'Utilisateur 📖
<!-- [ko] -->
## 사용자 가이드 📖
<!-- [ja] -->
## ユーザーガイド 📖
<!-- [common] -->

<!-- [en] -->
### Getting Started

1. [Installation](/getting-started/installation)
2. [Quick Start with Examples](/getting-started/quick-start)
3. [Upgrade and Uninstall](/getting-started/upgrade-and-uninstall)
<!-- [fr] -->
### Commencer

1. [Installation](/fr/getting-started/installation)
2. [Démarrage rapide avec des Exemples](/fr/getting-started/quick-start)
3. [Mettre à niveau et Désinstaller](/fr/getting-started/upgrade-and-uninstall)
<!-- [ko] -->
### 시작하기

1. [설치](/ko/getting-started/installation)
2. [빠른 시작을 위한 예제](/ko/getting-started/quick-start)
3. [업그레이드 및 제거](/ko/getting-started/upgrade-and-uninstall)
<!-- [ja] -->
### はじめに

1. [設置](/ja/getting-started/installation)
2. [クイックスタートのための例](/ja/getting-started/quick-start)
3. [アップグレードと削除](/ja/getting-started/upgrade-and-uninstall)
<!-- [common] -->

<!-- [en] -->
### Basic Usage (CLI)

1. [Create Base File](/basic-usage/create-base-file)
2. [Recursive Option](/basic-usage/cli-recursive-option)
3. [HTML, PDF Output](/basic-usage/cli-html-pdf)
<!-- [fr] -->
### Utilisation de Base (CLI)

1. [Créer un Fichier de Base](/fr/basic-usage/create-base-file)
2. [Option Récursive](/fr/basic-usage/cli-recursive-option)
3. [Sortie HTML, PDF](/fr/basic-usage/cli-html-pdf)
<!-- [ko] -->
### 기본 사용법 (CLI)

1. [Base 파일 생성](/ko/basic-usage/create-base-file)
2. [재귀 옵션](/ko/basic-usage/cli-recursive-option)
3. [HTML, PDF 출력](/ko/basic-usage/cli-html-pdf)
<!-- [ja] -->
### 基本的な使い方 (CLI)

1. [ベースファイルの作成](/ja/basic-usage/create-base-file)
2. [再帰オプション](/ja/basic-usage/cli-recursive-option)
3. [HTML, PDF 出力](/ja/basic-usage/cli-html-pdf)
<!-- [common] -->

<!-- [en] -->
### Advanced Usage (CLI)

1. [Base File Validation](/advanced-usage/cli-validation)
2. [Using Juptyer Notebook](/advanced-usage/cli-jupyter-notebook)
3. [Batch Processing with YAML File](/advanced-usage/cli-batch-processing)
<!-- [fr] -->
### Utilisation Avancée (CLI)

1. [Validation du Fichier de Base](/fr/advanced-usage/cli-validation)
2. [Utilisation de Juptyer Notebook](/fr/advanced-usage/cli-jupyter-notebook)
3. [Traitement par lots avec Fichier YAML](/fr/advanced-usage/cli-batch-processing)
<!-- [ko] -->
### 고급 사용법 (CLI)

1. [Base 파일 유효성 검사](/ko/advanced-usage/cli-validation)
2. [Juptyer Notebook 사용하기](/ko/advanced-usage/cli-jupyter-notebook)
3. [YAML 파일을 사용한 일괄 처리](/ko/advanced-usage/cli-batch-processing)
<!-- [ja] -->
### 高度な使い方 (CLI)

1. [ベースファイルの検証](/ja/advanced-usage/cli-validation)
2. [Jupyter Notebook 使用する](/ja/advanced-usage/cli-jupyter-notebook)
3. [YAML ファイルを使用したバッチ処理](/ja/advanced-usage/cli-batch-processing)
<!-- [common] -->

<!-- [en] -->
### Programming Guide

1. [Python API](/programming-guide/python-api)
2. [API Usage Examples](/programming-guide/api-examples)
3. [Advanced Reference](/programming-guide/advanced-reference)
<!-- [fr] -->
### Guide de Programmation

1. [Python API](/fr/programming-guide/python-api)
2. [Exemples d'Utilisation de l'API](/fr/programming-guide/api-examples)
3. [Advanced Reference](/fr/programming-guide/advanced-reference)
<!-- [ko] -->
### 프로그래밍 가이드

1. [Python API](/ko/programming-guide/python-api)
2. [API 사용 예제](/ko/programming-guide/api-examples)
3. [Advanced Reference](/ko/programming-guide/advanced-reference)
<!-- [ja] -->
### プログラミングガイド

1. [Python API](/ja/programming-guide/python-api)
2. [API 使用例](/ja/programming-guide/api-examples)
3. [Advanced Reference](/ja/programming-guide/advanced-reference)
<!-- [common] -->

<!-- [en] -->
### Miscellaneous

1. [Troubleshooting](/misc/troubleshooting)
2. [Contribution Guide](/misc/contributing)
3. [Changelog](https://github.com/ryul1206/multilingual-markdown/blob/dev/CHANGELOG.md)
4. [License](/LICENSE)
<!-- [fr] -->
### Divers

1. [Dépannage](/fr/misc/troubleshooting)
2. [Guide de Contribution](/fr/misc/contributing)
3. [Changelog](https://github.com/ryul1206/multilingual-markdown/blob/dev/CHANGELOG.md)
4. [Licence](/fr/LICENSE)
<!-- [ko] -->
### 기타

1. [문제 해결](/ko/misc/troubleshooting)
2. [기여 가이드](/ko/misc/contributing)
3. [Changelog](https://github.com/ryul1206/multilingual-markdown/blob/dev/CHANGELOG.md)
4. [라이선스](/ko/LICENSE)
<!-- [ja] -->
### その他

1. [トラブルシューティング](/ja/misc/troubleshooting)
2. [貢献ガイド](/ja/misc/contributing)
3. [Changelog](https://github.com/ryul1206/multilingual-markdown/blob/dev/CHANGELOG.md)
4. [ライセンス](/ja/LICENSE)
<!-- [common] -->

<!-- [en] -->
## Contributors 🤝
<!-- [fr] -->
## Contributeurs 🤝
<!-- [ko] -->
## 기여하신 분들 🤝
<!-- [ja] -->
## 貢献された方々 🤝
<!-- [common] -->

<a href="https://github.com/ryul1206/multilingual-markdown/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ryul1206/multilingual-markdown" />
</a>

<!-- [en] -->
Made with [contrib.rocks](https://contrib.rocks).

If you are interested in how to contribute, please refer to the [contribution guide](/contributing).
<!-- [fr] -->
Réalisé avec [contrib.rocks](https://contrib.rocks).

Si vous êtes intéressé par la façon de contribuer, veuillez vous référer au [guide de contribution](/fr/contributing).
<!-- [ko] -->
[contrib.rocks](https://contrib.rocks)로 만들었습니다.

기여 방법에 관심이 있으시다면, [기여 가이드](/ko/contributing)를 참고해주세요.
<!-- [ja] -->
[contrib.rocks](https://contrib.rocks)で作りました。

貢献方法に興味がある方は、[貢献ガイド](/ja/contributing)を参照してください。
<!-- [common] -->
