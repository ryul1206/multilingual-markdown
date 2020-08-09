<!---------------------------->
<!-- multilangual suffix: en, kr, fr  -->
<!-- no suffix: en -->
<!---------------------------->

<!-- [en] -->
# Multilingual Markdown Generator
<!-- [kr] -->
# 다국어 마크다운 생성기
<!-- [fr] -->
# Générateur de Markdown Multilingue
<!-- [common] -->

[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)

🚀 **version 0.1**
🌏 [English](README.md), [한국어](README.kr.md), [Français](README.fr.md)

---

<!-- [en] -->
**Table of Contents** ⚡
<!-- [kr] -->
**목차** ⚡
<!-- [fr] -->
**Table des matières** ⚡
<!-- [common] -->

<!-- [[ multilangual toc: level=2~3 no-emoji ]] -->

<!-- [en] -->
## How It Works 🔎
<!-- [kr] -->
## 작동 방식 🔎
<!-- [fr] -->
## Fonctionnement 🔎
<!-- [common] -->
![how it works](how-it-works.png)

<!-- [en] -->
## Features

- Auto suffix to file name
- No suffix option (for one main language)
- UTF-8 encoding. So *maybe* this will support almost all languages. :) 🍷
- Auto table of contents
    - Table of contents level options
    - Table of contents emoji **on-off** options
<!-- [kr] -->
## 기능

- 파일 이름 뒤에 자동 접미사
- 접미사 생략 옵션 (한 개 언어만 가능)
- UTF-8 인코딩. 따라서 *아마도* 거의 모든 언어를 지원할겁니다. :) 🍷
- 자동 목차
    - 목차로 만들 제목수준 설정 가능
    - 목차에서 이모티콘 **표시/생략** 설정 가능
<!-- [fr] -->
## Fonctionnalités

- Suffixe automatique des noms de fichier
- Possibilité d'omettre le suffixe (pour la langue principale)
- Encodage UTF-8. Cela *devrait* supporter presque toutes les langues. :) 🍷
- Table des matières automatique
    - Niveaux de titres au choix
    - Emojis en option
<!-- [common] -->

<!-- [en] -->
## Badges
<!-- [kr] -->
## 뱃지 달기
<!-- [fr] -->
## Badges
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

## How to Use
<!-- [kr] -->
## 사용법
<!-- [fr] -->
## Mode d'emploi
<!-- [common] -->

<!-- [en] -->
  1. Make `{something}.base.md` files. See [README.base.md](README.base.md) and [example.base.md](example/example.base.md) for examples, and [Command Tags](#Command-Tags) for rules.
<!-- [kr] -->
  1. `{파일이름}.base.md` 파일을 만듭니다. 예제는 [README.base.md](README.base.md) 와 [example.base.md](example/example.base.md) 를 참고하시고, 작성하는 규칙은 [명령어 태그](#명령어-태그)를 참고하십시오.
<!-- [fr] -->
  1. Saisissez les fichiers multilingues avec une extension `.base.md`. Voir les exemples [README.base.md](README.base.md) et [example.base.md](example/example.base.md) et reportez-vous à [Marqueurs](#marqueurs) pour les règles.

<!-- [en] -->
  2. Run this python file on your project root. Then, this will search all markdowns recursively.
<!-- [kr] -->
  2. 프로젝트 루트 위치에서 파이썬 파일을 실행합니다. 그러면 알아서 하위폴더의 마크다운들을 찾아낼 것입니다.
<!-- [fr] -->
  2. Exécutez le script Python `multilang_md.py` à la racine de votre projet : il recherchera tous les Markdown dans les répertoires inférieurs.
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
<!-- [fr] -->
  3. Vous trouverez les fichiers `{quelquechose}.{suffixe}.md` dans le même répertoire que celui de base qui leur correspond. Par example :

    - par défaut : `{quelquechose}.en.md`, `{quelquechose}.kr.md`, `{quelquechose}.fr.md`, ...
    - option no-suffix pour `en`: `{quelquechose}.md`, `{quelquechose}.kr.md`, `{quelquechose}.fr.md`, ...
<!-- [common] -->

<!-- [en] -->
  4. Since this generator overwrites the auto-generated files each time, you do not have to delete them every time when you modify the `{something}.base.md`. Just run step 2 again.
<!-- [kr] -->
  4. 이 생성기는 자동생성된 파일을 매번 덮어쓰기 때문에, `{파일이름}.base.md` 파일을 수정하더라도 매번 지울 필요가 없습니다. 그저 방금 전 2단계를 다시 실행하면 됩니다.
<!-- [fr] -->
  4. Le générateur écrase les fichiers générés à chaque exécution, il est donc inutile de les supprimer après avoir modifié `{fichier}.base.md`. Reprenez simplement au point 2. Ne modifiez pas les fichiers de chaque langue, les modifications disparaitraient à la prochaine exécution du script.
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
    <!-- multilangual suffix: en, kr, fr, es, jp, cn -->
    ```

<!-- [en] -->
  2. **Hidden Suffix** (Optional)

    The `no suffix` option can prevent the suffix from being appended when creating the file. In other words, setting `no suffix` to `en` will generate `FileName.md` instead of `FileName.en.md`. This is useful because the main `README` in **GitHub** is not recognized when it has a suffix.
<!-- [kr] -->
  2. **접미사 숨기기** (필수 아님)

    `no suffix` 옵션은 파일을 생성할 때 접미사가 붙는 것을 방지할 수 있습니다. 다시 말하자면 `no suffix`를 `en`으로 설정하면 `파일이름.en.md`가 아니라 `파일이름.md`가 생성됩니다. **GitHub**에서 메인 `README`는 접미사가 붙으면 인식이 안되기 때문에 이 기능이 유용합니다.

<!-- [fr] -->
  2. **Suffixe invisible** (facultatif)

    L'option `no suffix` évite l'ajout de l'un des suffixes lors de la création des fichiers. Ainsi, appliquer `no suffix`à la langue `en` génèrera *`fichier`*`.md` au lieu de *`fichier`*`.en.md`. Cela est utile par exemple pour le `README` obligatoire dans  **GitHub** qui n sera pas reconnu s'il a un suffixe (par exemple `README.en.md`).

<!-- [common] -->

    ```markdown
    <!-- no suffix: en -->
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
<!-- [kr] -->
  1. **목차**

    아래 태그는 생성기에 의해 목차로 자동교체됩니다. 목차의 수준은 `level` 부분을 통해 정할 수 있습니다. 가장 큰 제목(`# 제목`)은 html에서 `<h1>`이기 때문에 `level 1`입니다.
<!-- [fr] -->
  1. **Table des matières**

    Les marqueurs sont automatiquement placés dans la table des matières par le générateur. Le niveau de titre auquel commence la table des matières peut être indiqué avec l'option `level`. Le niveau le plus haut est 1, ce qui correspond aux titres Markdown `# titre` et aux tags HTML `<H1>`.
<!-- [common] -->

    ```markdown
    <!-- [[ multilangual toc: level=2~3 ]] -->
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
        - In rare cases, you may want to subtract emoji from the table of contents while inserting emoji in the title.😱 If you are in this situation, apply the `no-emoji` option as shown below.😎
<!-- [kr] -->
    2. **`no-emoji` 옵션**
        - 드문 경우지만 제목에는 이모티콘을 넣으면서 목차에서는 이모티콘을 지우고 싶을 때가 있습니다.😱 만약 당신이 이와 같은 상황이라면, 아래와 같이 `no-emoji` 옵션을 적용하세요.😎
<!-- [fr] -->
    2. **Option `no-emoji`**
        - En de rares occasions, vous pouvez souhaiter mettre un emoji dans un titre sans qu'il apparaisse dans la table des matières 😱. dans ce cas, utilisez l'option `no-emoji` comme indiqué ci-dessous 😎
<!-- [common] -->

        ```markdown
        <!-- [[ multilangual toc: level=2~3 no-emoji ]] -->
        ```

<!-- [en] -->
## Contributing
<!-- [kr] -->
## 기여하기
<!-- [fr] -->
## Contribution
<!-- [common] -->

<!-- [en] -->
I would appreciate anything you send. (e.g. translations, simple improvements, bug reports, and so on.)

> Especially I would be very grateful if you could translate this `README.md` document into your language not listed here and give it to me.
<!-- [fr] -->
Toute contribution sera grandement appréciée. (ex: traductions, améliorations, signalements de bugs etc.)

> Je serai particulièrement reconnaissant si vous pouviez traduire ce `README.md` dans votre langue et me l'envoyer.

<!-- [kr] -->
번역, 단순한 개선, 버그 제보 등 어떠한 것이라도 소중히 받습니다.

> 특히 이 `README.md` 문서를 여기에 없는 다른 언어로 번역해주신다면 매우 감사드립니다.
<!-- [common] -->

<!-- [ignore] -->
### Contributors

<!-- [en] -->
> The contributor list is available in English only.
<!-- [kr] -->
> 기여자 명단은 영어로만 제공됩니다.
<!-- [fr] -->
> La liste des contributeurs est en Anglais seulement.

<!-- [common] -->

Francis Piérot - French translation ([fr])
