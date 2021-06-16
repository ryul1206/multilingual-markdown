<!---------------------------->
<!-- multilingual suffix: en, fr, kr -->
<!-- no suffix: en -->
<!---------------------------->

<!-- [en] -->
# Multilingual Markdown Generator

This package provides a command-line interface to manage multilingual contents and generate i18n markdown from a single base file.
<!-- [fr] -->
# Générateur de Markdown Multilingue

Ce package fournit une interface de ligne de commande pour gérer les contenus multilingues et générer des démarques i18n à partir d'un seul fichier de base.
<!-- [kr] -->
# 다국어 마크다운 생성기

이 패키지는 다국어 콘텐츠를 관리하고, 단일 기본 파일로부터 i18n 마크 다운을 생성하는 명령 줄 인터페이스(CLI)를 제공합니다.
<!-- [common] -->

[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/ryul1206/multilingual-markdown/badge/master)](https://www.codefactor.io/repository/github/ryul1206/multilingual-markdown/overview/master)

🚀 **version 1.0-alpha.1** 🌏
[English](https://github.com/ryul1206/multilingual-markdown/blob/master/README.md),
[Français](https://github.com/ryul1206/multilingual-markdown/blob/master/README.fr.md),
[한국어](https://github.com/ryul1206/multilingual-markdown/blob/master/README.kr.md)

---

<!-- [en] -->
**Table of Contents** ⚡
<!-- [kr] -->
**목차** ⚡
<!-- [fr] -->
**Table des matières** ⚡
<!-- [common] -->

<!-- [[ multilingual toc: level=2~3 no-emoji ]] -->

<!-- [en] -->
## Overview 🔎
<!-- [fr] -->
## Aperçu 🔎
<!-- [kr] -->
## 개요 🔎
<!-- [common] -->

<!-- [en] -->
### How It Works
<!-- [fr] -->
### Fonctionnement
<!-- [kr] -->
### 작동 방식
<!-- [common] -->
![how it works](how-it-works.png)

<!-- [en] -->
### Features

- Auto suffix to file name
- No suffix option (for one main language)
- UTF-8 encoding. So *maybe* this will support almost all languages. :) 🍷
- Auto table of contents
    - Table of contents level options
    - Table of contents emoji **on-off** options
<!-- [kr] -->
### 기능들

- 파일 이름 뒤에 자동 접미사
- 접미사 생략 옵션 (한 개 언어만 가능)
- UTF-8 인코딩. 따라서 *아마도* 거의 모든 언어를 지원할겁니다. :) 🍷
- 자동 목차
    - 목차로 만들 제목수준 설정 가능
    - 목차에서 이모티콘 **표시/생략** 설정 가능
<!-- [fr] -->
### Fonctionnalités

- Suffixe automatique des noms de fichier
- Possibilité d'omettre le suffixe (pour la langue principale)
- Encodage UTF-8. Cela *devrait* supporter presque toutes les langues. :) 🍷
- Table des matières automatique
    - Niveaux de titres au choix
    - Emojis en option
<!-- [common] -->

<!-- [en] -->
## Install
<!-- [fr] -->
## Installer
<!-- [kr] -->
## 설치
<!-- [common] -->

```sh
pip3 install mmg --user
```

<!-- [en] -->
Now when you open a new terminal you can use the new command `mmg`.
<!-- [fr] -->
Maintenant, lorsque vous ouvrez un nouveau terminal, vous pouvez utiliser la nouvelle commande `mmg`.
<!-- [kr] -->
이제 새터미널을 열면 새로운 명령어 `mmg`를 사용할 수 있습니다.
<!-- [common] -->

```sh
$ mmg --help
mmg [OPTIONS] [FILENAMES]...

Options:
  --version                 Show the current version.
  -r, --recursive           This recursive option searches all subfolders
                            based on current directory and converts all base
                            files.
  -y, --yes                 Confirm the action without prompting
  -c, --check / -s, --skip  Check the number of language tags of each file
                            (defualt: --check)
  -v, --verbose             For example, -v:1, -vv:2, -vvv:3  [x>=0]
  --help                    Show this message and exit.
```

<!-- [en] -->
## Update
<!-- [fr] -->
## Mises à jour
<!-- [kr] -->
## 업데이트
<!-- [common] -->

```sh
pip3 install mmg --upgrade --user
```

<!-- [en] -->
## Uninstall
<!-- [fr] -->
## Désinstaller
<!-- [kr] -->
## 제거
<!-- [common] -->

```sh
pip3 uninstall mmg
```

<!-- [en] -->
## How to Use
<!-- [fr] -->
## Mode d'emploi
<!-- [kr] -->
## 사용법
<!-- [common] -->

<!-- [en] -->
Make `{something}.base.md` files. See [README.base.md](README.base.md) and [example.base.md](example/example.base.md) for examples, and [Command Tags](#Command-Tags) for rules.

**(Note) A wrong format of base-file will break generated style.**
<!-- [fr] -->
Saisissez les fichiers multilingues avec une extension `.base.md`. Voir les exemples [README.base.md](README.base.md) et [example.base.md](example/example.base.md) et reportez-vous à [Marqueurs](#marqueurs) pour les règles.

**(Remarque) Un format incorrect de fichier de base cassera le style généré.**
<!-- [kr] -->
`{파일이름}.base.md` 파일을 만듭니다. 예제는 [README.base.md](README.base.md) 와 [example.base.md](example/example.base.md) 를 참고하시고, 작성하는 규칙은 [명령어 태그](#명령어-태그)를 참고하십시오.

**(경고) 베이스 파일 형식이 잘못되면 생성된 스타일이 깨집니다.**
<!-- [common] -->

<!-- [en] -->
### (1) File Designation
<!-- [fr] -->
### (1) Spécification du fichier cible
<!-- [kr] -->
### (1) 파일 지정
<!-- [common] -->

<!-- [en] -->
Enter the `*.base.md` files that you want to create in multiple languages as arguments to the `mmg` command.
<!-- [fr] -->
Entrez les fichiers `* .base.md` que vous souhaitez créer dans plusieurs langues comme arguments de la commande` mmg`.
<!-- [kr] -->
다국어로 생성하고 싶은 `*.base.md` 파일을 `mmg` 명령에 인자(arguments)로 넣어줍니다.
<!-- [common] -->

```sh
mmg FileName.base.md
```

<!-- [en] -->
Multiple arguments are separated by spaces.
<!-- [fr] -->
Les arguments multiples sont séparés par des espaces.
<!-- [kr] -->
여러 인자는 띄어쓰기로 구분합니다.
<!-- [common] -->

```sh
mmg Foo.base.md Bar.base.md Baz.base.md
```

<!-- [en] -->
### (2) Recursive Option
<!-- [fr] -->
### (2) Option Récursive
<!-- [kr] -->
### (2) 재귀 옵션 (recursive option)
<!-- [common] -->

<!-- [en] -->
If you want to convert all base files in the current directory and subdirectories, use the `--recursive` or `-r` option.
The recursive option searches all subfolders based on where the command is entered.
You cannot specify a folder as an argument yet.
<!-- [fr] -->
Si vous voulez convertir tous les fichiers de base dans le répertoire courant et les sous-répertoires, utilisez l'option `--recursive` ou` -r`.
L'option récursive recherche tous les sous-dossiers en fonction de l'endroit où la commande est entrée.
Vous ne pouvez pas encore spécifier un dossier comme argument.
<!-- [kr] -->
현재 디렉토리와 하위 디렉토리에 있는 모든 베이스 파일을 변환하고 싶다면 `--recursive` 또는 `-r` 옵션을 사용하세요.
recursive option은 명령어가 입력된 위치를 기준으로 모든 하위 폴더를 탐색합니다.
아직은 인자로 폴더를 지정할 수 없습니다.
<!-- [common] -->

```sh
mmg --recursive
```

<!-- [en] -->
### (3) Base File Validation

When your file may have a problem.
(Normal is shown in green and abnormal in red.)
<!-- [fr] -->
### (3) Validation du Fichier de Base

Lorsque votre fichier peut avoir un problème.
(Normal est indiqué en vert et anormal en rouge.)
<!-- [kr] -->
### (3) 베이스 파일 유효성 검사

문제가 있는 것으로 의심되는 경우.
(정상은 녹색으로, 비정상은 빨간색으로 표시됩니다.)
<!-- [common] -->

```sh
$ mmg -r --verbose
----------------------
 + .\README.base.md
        [O] Tag count: {'en': 37, 'fr': 37, 'kr': 37}
 + .\example\example.base.md
        [X] 4 language(s) not translated.
            Tag count: {'en-US': 4, 'fr-FR': 4, 'ko-KR': 5, 'ja-JP': 4, '<Unknown>': 1}
        Line 28: This language reappeared before all languages appeared once.
        Line 36: A common area appeared before all languages come out.
        Line 57: Unknown suffix detected.
        Line 59: This language reappeared before all languages appeared once.
----------------------
 => 2 base markdowns were found.
Do you want to convert these files? [y/N]
```

<!-- [en] -->
When your files are ok.
<!-- [fr] -->
Lorsque vos fichiers sont ok.
<!-- [kr] -->
문제점이 없다면
<!-- [common] -->

```sh
$ mmg -r --verbose
----------------------
 + .\README.base.md
        [O] Tag count: {'en': 37, 'fr': 37, 'kr': 37}
 + .\example\example.base.md
        [O] Tag count: {'en-US': 4, 'fr-FR': 4, 'ko-KR': 4, 'ja-JP': 4}
----------------------
 => 2 base markdowns were found.
Do you want to convert these files? [y/N]
```

<!-- [en] -->
### (4) More explanations
<!-- [fr] -->
### (4) Plus d'explications
<!-- [kr] -->
### (4) 부연 설명
<!-- [common] -->

<!-- [en] -->
- You can find the `{something}.{suffix}.md` files in the same directory. For example:
    - By default: `{something}.en.md`, `{something}.kr.md`, `{something}.es.md`, ...
    - When no-suffix option on `en`: `{something}.md`, `{something}.kr.md`, `{something}.es.md`, ...
- Since this generator overwrites the auto-generated files each time, you do not have to delete them every time when you modify the `{something}.base.md`. Just run step 2 again.
<!-- [fr] -->
- Vous trouverez les fichiers `{quelquechose}.{suffixe}.md` dans le même répertoire que celui de base qui leur correspond. Par example :
    - Par défaut : `{quelquechose}.en.md`, `{quelquechose}.kr.md`, `{quelquechose}.fr.md`, ...
    - Lorsque option no-suffix pour `en`: `{quelquechose}.md`, `{quelquechose}.kr.md`, `{quelquechose}.fr.md`, ...
- Le générateur écrase les fichiers générés à chaque exécution, il est donc inutile de les supprimer après avoir modifié `{fichier}.base.md`. Reprenez simplement au point 2. Ne modifiez pas les fichiers de chaque langue, les modifications disparaitraient à la prochaine exécution du script.
<!-- [kr] -->
- 각 폴더의 동일한 위치에서 `{파일이름}.{접미사}.md`으로 된 파일들을 볼 수 있습니다. 예를 들어:
    - 기본일 때: `{파일이름}.en.md`, `{파일이름}.kr.md`, `{파일이름}.es.md`, ...
    - `en`에 접미사 생략 옵션일 때: `{파일이름}.md`, `{파일이름}.kr.md`, `{파일이름}.es.md`, ...
- 이 생성기는 자동생성된 파일을 매번 덮어쓰기 때문에, `{파일이름}.base.md` 파일을 수정하더라도 매번 지울 필요가 없습니다. 그저 방금 전 2단계를 다시 실행하면 됩니다.
<!-- [common] -->

<!-- [en] -->
## Command Tags
<!-- [kr] -->
## 명령어 태그
<!-- [fr] -->
## Marqueurs
<!-- [common] -->

<!-- [en] -->
### Headers

Headers must be declared before the body begins.
<!-- [kr] -->
### 헤더

헤더는 반드시 본문이 시작하기 전에 선언되어야 합니다.
<!-- [fr] -->
### Titres

Les titres doivent être déclarés avant le corps de texte.
<!-- [common] -->

<!-- [en] -->
1. **Suffix Declaration**

    Declare the language you want to use. The following example declares `en` and `kr` and others as keywords. These keywords are used as suffixes.
<!-- [kr] -->
1. **접미사 선언**

    사용할 언어를 선언하십시오. 다음 예제는 `en`과 `kr`을 키워드로 선언하였습니다. 이 키워드들은 접미사로 사용됩니다.
<!-- [fr] -->
1. **Déclaration des suffixes**

    Déclarez les langues que vous souhaitez utiliser. Dans l'exemple suivant, on déclare les mots-clés `en`, `kr` et `fr` et quelque autres. Ces mots-clés seront utilisés comme suffixes des noms de fichier et comme marqueurs dans les fichiers `base.md`.
<!-- [common] -->

    ```markdown
    <!-- multilingual suffix: en, kr, fr, es, jp, cn -->
    ```

<!-- [en] -->
1. **Hidden Suffix** (Optional)

    The `no suffix` option can prevent the suffix from being appended when creating the file. In other words, setting `no suffix` to `en` will generate `FileName.md` instead of `FileName.en.md`. This is useful because the main `README` in **GitHub** is not recognized when it has a suffix.
<!-- [kr] -->
1. **접미사 숨기기** (필수 아님)

    `no suffix` 옵션은 파일을 생성할 때 접미사가 붙는 것을 방지할 수 있습니다. 다시 말하자면 `no suffix`를 `en`으로 설정하면 `파일이름.en.md`가 아니라 `파일이름.md`가 생성됩니다. **GitHub**에서 메인 `README`는 접미사가 붙으면 인식이 안되기 때문에 이 기능이 유용합니다.
<!-- [fr] -->
1. **Suffixe invisible** (facultatif)

    L'option `no suffix` évite l'ajout de l'un des suffixes lors de la création des fichiers. Ainsi, appliquer `no suffix`à la langue `en` génèrera *`fichier`*`.md` au lieu de *`fichier`*`.en.md`. Cela est utile par exemple pour le `README` obligatoire dans  **GitHub** qui n sera pas reconnu s'il a un suffixe (par exemple `README.en.md`).
<!-- [common] -->

    ```markdown
    <!-- no suffix: en -->
    ```

<!-- [en] -->
### Badges
<!-- [kr] -->
### 뱃지 달기
<!-- [fr] -->
### Badges
<!-- [common] -->

[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-yellow.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-green.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-blue.svg)](https://github.com/ryul1206/multilingual-markdown)
...

```markdown
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
```

<!-- [en] -->
### Main Text

Everything that the parser reads after the tag below is recognized as the main text. (So you have to write the header before main).
<!-- [kr] -->
### 본문

파서가 아래의 태그들를 읽는 순간부터 그 이후에 읽는 모든 것은 메인 텍스트로 인식합니다. (그래서 헤더를 메인 이전에 적어야 합니다.)
<!-- [fr] -->
### Corps de texte

Tout ce qui suit le marqueur est interprété comme corps principal de texte, donc vous devez placer les titres avant le texte.
<!-- [common] -->

<!-- [en] -->
1. **Keywords**
<!-- [kr] -->
1. **키워드**
<!-- [fr] -->
1. **Mots-clés**
<!-- [common] -->
<!-- [en] -->
    1. Language Classification

        The tags that distinguish languages are written in the form `<!-- [keyword] -->`. If one keyword is recognized, it will be recognized as that keyword until another keyword is seen.
<!-- [kr] -->
    1. 언어 분류

        언어를 구분하는 태그는 `<!-- [키워드] -->` 같은 형태로 작성합니다. 하나의 키워드가 인식되면 다른 키워드가 나타날 때까지 해당 키워드로 인식됩니다.
<!-- [fr] -->
    1. Classification de langue

        Les marqueurs qui distinguent les languages sont écrits sous la forme `<!-- [marqueur] -->`. Si un marqueur est reconnu, il sera retenu jusqu'à ce qu'un autre soit reconnu.
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
<!-- [fr] -->
    1. Section commune

        Vous pouvez utiliser le mot-clé 'common' pour une partie de texte commune à toutes les langues, par exemple pour des illustrations.
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
<!-- [fr] -->
    1. Section ignorée

        Vous pouvez exclure des parties du texte telles que les blocs de commentaires ou les TODO avec le mot-clé `ignore`.
<!-- [common] -->

        ```markdown
        <!-- [ignore] -->
        ```

<!-- [en] -->
1. **Table of contents**

    The tags below are automatically replaced to the table of contents by the generator. The level of the table of contents can be determined through the `level` option. The highest-level of title(`# title`) is level 1 because it is `<h1>` in HTML.

    **(Note) If you skip the title level of the markdown marked with `#`, an error will occur. In other words, the subtitle of `##` must be `###`.**
<!-- [kr] -->
1. **목차**

    아래 태그는 생성기에 의해 목차로 자동교체됩니다. 목차의 수준은 `level` 부분을 통해 정할 수 있습니다. 가장 큰 제목(`# 제목`)은 html에서 `<h1>`이기 때문에 `level 1`입니다.

    **(주의) `#`으로 표시하는 마크다운의 제목수준을 건너뛰면 에러가 발생합니다. 다시말해, `##`의 하위 제목은 `###` 이여야 합니다.**
<!-- [fr] -->
1. **Table des matières**

    Les marqueurs sont automatiquement placés dans la table des matières par le générateur. Le niveau de titre auquel commence la table des matières peut être indiqué avec l'option `level`. Le niveau le plus haut est 1, ce qui correspond aux titres Markdown `# titre` et aux tags HTML `<H1>`.

    **(Remarque) Si vous sautez le niveau de titre de la démarque marquée avec `#`, une erreur se produira. En d'autres termes, le sous-titre de `##` doit être `###`.**
<!-- [common] -->

    ```markdown
    <!-- [[ multilingual toc: level=2~3 ]] -->
    ```

<!-- [en] -->
    1. **`level` option**
        - There are four ways to mark `level`. You can change the numbers below.
            - `level=2`: Make the 2nd level to table of contents.
            - `level=2~`: Make the 2nd ~ 9th level to table of contents.
            - `level=~4`: Make the 1st ~ 4th level to table of contents.
            - `level=2~4`: Make the 2nd ~ 4th level to table of contents.
        - You can write the `table of contents` tags multiple times in one document, and also put different `level` options each time.
        - **CAUTION💥**: If you omit this `level`, the parser will not recognize it.
        - **CAUTION💥**: The `table of contents` tag automatically changes the current keyword to `common`. So this tag is also implicitly in `common`.
<!-- [kr] -->
    1. **`level` 옵션**
        - `level`을 표기하는 방법은 총 4가지입니다. 여러분의 필요에 따라 숫자는 바꾸시면 됩니다.
            - `level=2`: 2수준의 제목만 목차로 만듭니다.
            - `level=2~`: 2~9수준의 제목만 목차로 만듭니다.
            - `level=~4`: 1~4수준의 제목만 목차로 만듭니다.
            - `level=2~4`: 2~4수준의 제목만 목차로 만듭니다.
        - 하나의 문서에서 `table of contents` 태그는 여러번 쓸 수 있고, 매번 다른 `level` 옵션을 줄 수도 있습니다.
        - **주의💥**: 만약 `level`을 생략하면 파서가 인식하지 못합니다.
        - **주의💥**: 목차 태그는 자동으로 현재 키워드를 `common`으로 변경합니다. 그래서 목차 태그 또한 암묵적으로 `common`에 속합니다.
<!-- [fr] -->
    1. **Option `level`**
        - Les niveaux acceptés dans la table des matières par l'option `level` vont de 1 à 9 et sont indiqués avec un niveau de départ et un niveau de fin séparés par une tilde `~`. Si vous ne spécifiez pas le premier numéro, les niveaux commenceront au premier et si vous ne spécifiez pas le second numéro, les niveaux seront pris jusqu'au neuvième. Adaptez les nombres des exemples suivants selon vos besoins.
            - `level=2`: Mettre uniquement le niveau 2 dans la table des matières.
            - `level=2~`: Mettre les niveaux 2 à 9 dans la table des matières.
            - `level=~4`: Mettre les niveaux 1 à 4 dans la table des matières.
            - `level=2~4`: Mettre les niveaux 2 à 4 dans la table des matières..
        - Vous pouvez écrire les marqueurs de la table des matières plusieurs fois dans le document et spécifier différentes options `level` à chaque fois.
        - **ATTENTION💥**: si vous ommettez `level` le script ignorera la commande.
        - **ATTENTION💥**: le marqueur `table of contents` change automatiquement le marqueur de section pour `common` donc les commandes de la table des matières concernent toutes les langues, et vous devez réindiquer un marqueur de langue par la suite.
<!-- [en] -->
    2. **`no-emoji` option**
        - You may want to subtract emoji from the table of contents while inserting emoji in a section title.😱 If you are in this situation, apply the `no-emoji` option as shown below.😎
<!-- [kr] -->
    2. **`no-emoji` 옵션**
        - 섹션 제목에는 이모티콘을 넣으면서 목차에서는 이모티콘을 지우고 싶을 때가 있습니다.😱 만약 당신이 이와 같은 상황이라면, 아래와 같이 `no-emoji` 옵션을 적용하세요.😎
<!-- [fr] -->
    2. **Option `no-emoji`**
        - Vous pouvez souhaiter mettre un emoji dans un titre sans qu'il apparaisse dans la table des matières.😱 dans ce cas, utilisez l'option `no-emoji` comme indiqué ci-dessous 😎
<!-- [common] -->

        ```markdown
        <!-- [[ multilingual toc: level=2~3 no-emoji ]] -->
        ```

<!-- [en] -->
## Contribution
<!-- [fr] -->
## Contribution
<!-- [kr] -->
## 기여
<!-- [common] -->

<!-- [en] -->
I would appreciate anything you send. (e.g. translations, simple improvements, bug reports, and so on.) Especially I would be very grateful if you could translate this `README.md` document into your language not listed here and give it to me.
<!-- [fr] -->
Toute contribution sera grandement appréciée. (ex: traductions, améliorations, signalements de bugs etc.) Je serai particulièrement reconnaissant si vous pouviez traduire ce `README.md` dans votre langue et me l'envoyer.
<!-- [kr] -->
번역, 단순한 개선, 버그 제보 등 어떠한 것이라도 소중히 받습니다. 특히 이 `README.md` 문서를 여기에 없는 다른 언어로 번역해주신다면 매우 감사드립니다.
<!-- [common] -->

<!-- [en] -->
### How to build locally for development
<!-- [fr] -->
### Comment construire localement pour le développement
<!-- [kr] -->
### 개발을 위해 local로 빌드하는 방법
<!-- [common] -->

- Linux and MacOS
  - Required packages: `pip3 install -r requirements_dev.txt --user`
  - Install: `python3 setup.py install --user --record temp.txt`
  - Usage: `mmg [OPTIONS] [FILENAMES]...`
  - Uninstall: `xargs rm -rf < temp.txt`
- Windows (Not recommended)
  - Required packages: `pip3 install -r .\requirements_dev.txt --user`
  - Install: `python3 setup.py install --user --record temp.txt`
  - Usage: `python3 -m mmgcli [OPTIONS] [FILENAMES]...`
  - Uninstall (PowerShell): `Get-Content .\temp.txt | Remove-Item`

### [Changelog](https://github.com/ryul1206/multilingual-markdown/blob/master/CHANGELOG.md)

### Contributors

<!-- [en] -->
> The contributor list is available in English only.
<!-- [kr] -->
> 기여자 명단은 영어로만 제공됩니다.
<!-- [fr] -->
> La liste des contributeurs est en Anglais seulement.
<!-- [common] -->

- [@bkg2018 (Francis Piérot)](https://github.com/bkg2018): Added french translation to README and example. [PR #1](https://github.com/ryul1206/multilingual-markdown/pull/1)
- [@mathben (Mathieu Benoit)](https://github.com/mathben): Update README pip installation with requirements.txt [PR #2](https://github.com/ryul1206/multilingual-markdown/pull/2)
