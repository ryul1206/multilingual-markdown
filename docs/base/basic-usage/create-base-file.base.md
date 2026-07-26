<!---------------------------->
<!-- multilingual suffix: en, fr, ko, ja -->
<!---------------------------->
<!-- [en] -->
# Create a Base File
<!-- [fr] -->
# Créer un Fichier de Base
<!-- [ko] -->
# 베이스 파일 만들기
<!-- [ja] -->
# ベースファイルの作成
<!-- [common] -->

!!! note ""

<!-- [en] -->
    English |
    [**Français**](site:/fr/basic-usage/create-base-file) |
    [**한국어**](site:/ko/basic-usage/create-base-file) |
    [**日本語**](site:/ja/basic-usage/create-base-file)
<!-- [fr] -->
    [**English**](site:/basic-usage/create-base-file) |
    Français |
    [**한국어**](site:/ko/basic-usage/create-base-file) |
    [**日本語**](site:/ja/basic-usage/create-base-file)
<!-- [ko] -->
    [**English**](site:/basic-usage/create-base-file) |
    [**Français**](site:/fr/basic-usage/create-base-file) |
    한국어 |
    [**日本語**](site:/ja/basic-usage/create-base-file)
<!-- [ja] -->
    [**English**](site:/basic-usage/create-base-file) |
    [**Français**](site:/fr/basic-usage/create-base-file) |
    [**한국어**](site:/ko/basic-usage/create-base-file) |
    日本語
<!-- [common] -->

<!-- [en] -->
This page describes the rules for creating a base file.
<!-- [fr] -->
Cette page décrit les règles de création d'un fichier de base.
<!-- [ko] -->
이 페이지에서는 Base 파일을 작성하는 규칙에 대해 상세히 설명합니다.
<!-- [ja] -->
このページでは、ベースファイルを作成する際のルールについて説明します。
<!-- [common] -->

<!-- [en] -->
## Summary
<!-- [fr] -->
## Résumé
<!-- [ko] -->
## 요약
<!-- [ja] -->
## 概要
<!-- [common] -->

<!-- [en] -->
MMG reads markdown files or markdown cells in jupyter notebook and classifies the contents. To do this, MMG uses the following special markdown comments.
<!-- [fr] -->
MMG lit les fichiers markdown ou les cellules markdown dans le notebook jupyter et classe le contenu. Pour ce faire, MMG utilise les commentaires markdown spéciaux suivants.
<!-- [ko] -->
MMG는 markdown 파일이나 jupyter notebook의 markdown 셀을 읽어 내용을 분류하는데, 이를 위해 다음과 같은 특정한 markdown 주석을 사용합니다.
<!-- [ja] -->
MMGはmarkdownファイルやjupyter notebookのmarkdownセルを読み込み、内容を分類します。そのために、MMGは以下の特別なmarkdownコメントを使用します。
<!-- [common] -->

<!-- [en] -->
- Header
    - `<!-- multilingual suffix: keyword1, keyword2, keyword3 -->`: Declare which keywords to use in the future.
    - `<!-- no suffix: keyword -->`: Do not append suffix to the created file for the specified keyword.
- Macro
    - `<!-- [[ multilingual toc: level=2~3 ]] -->`: Automatically generate a table of contents for each keyword at the specified location.
- Body
    - `<!-- [keyword] -->`: Declare which keyword the section belongs to.
    - `<!-- [common] -->`: Declare the content that will be common to all languages.
    - `<!-- [ignore] -->`: Ignore the section.
<!-- [fr] -->
- En-tête
    - `<!-- multilingual suffix: keyword1, keyword2, keyword3 -->`: Déclarez quels mots-clés utiliser à l'avenir.
    - `<!-- no suffix: keyword -->`: Ne pas ajouter de suffixe au fichier créé pour le mot-clé spécifié.
- Macro
    - `<!-- [[ multilingual toc: level=2~3 ]] -->`: Génère automatiquement une table des matières pour chaque mot-clé à l'emplacement spécifié.
- Corps
    - `<!-- [keyword] -->`: Déclarez à quel mot-clé appartient la section.
    - `<!-- [common] -->`: Déclarez le contenu qui sera commun à toutes les langues.
    - `<!-- [ignore] -->`: Ignorez la section.
<!-- [ko] -->
- 헤더
    - `<!-- multilingual suffix: 키워드1, 키워드2, 키워드3 -->`: 앞으로 어떤 키워드를 사용할 것인지 선언합니다.
    - `<!-- no suffix: 키워드 -->`: 지정한 키워드에 대해, 파일을 생성할 때 접미사를 붙이지 않습니다.
- 매크로
    - `<!-- [[ multilingual toc: level=2~3 ]] -->`: 해당 위치에 각 키워드별 목차를 자동으로 생성합니다.
- 본문
    - `<!-- [키워드] -->`: 해당 섹션이 어떤 키워드에 속하는지 선언합니다.
    - `<!-- [common] -->`: 모든 언어에 공통적으로 들어갈 내용을 선언합니다.
    - `<!-- [ignore] -->`: 해당 섹션을 MMG가 무시하도록 합니다.
<!-- [ja] -->
- ヘッダー
    - `<!-- multilingual suffix: keyword1, keyword2, keyword3 -->`: 今後どのキーワードを使用するかを宣言します。
    - `<!-- no suffix: keyword -->`: 指定したキーワードのファイルにサフィックスを付けません。
- マクロ
    - `<!-- [[ multilingual toc: level=2~3 ]] -->`: 指定した場所に各キーワードの目次を自動生成します。
- 本文
    - `<!-- [keyword] -->`: セクションがどのキーワードに属するかを宣言します。
    - `<!-- [common] -->`: すべての言語で共通する内容を宣言します。
    - `<!-- [ignore] -->`: セクションを無視します。
<!-- [common] -->

<!-- [en] -->
!!! info "Note"

    In MMG documents, the terms 'keyword' and 'tag' are used interchangeably.
    In the source code, it is also called as variable name `suffix` or `lang_tags`.
    They all mean the same thing.
<!-- [fr] -->
!!! info "Note"

    Dans les documents MMG, les termes «mot-clé» et «balise» sont utilisés indifféremment.
    Dans le code source, il est également appelé comme nom de variable `suffix` ou `lang_tags`.
    Ils signifient tous la même chose.
<!-- [ko] -->
!!! info "안내"

    MMG 문서에서는 '키워드'와 '태그'를 구분하지 않고 혼용하여 사용합니다.
    소스코드에는 `suffix` 또는 `lang_tags`라는 변수명으로도 쓰입니다.
    모두 같은 의미입니다.
<!-- [ja] -->
!!! info "Note"

    MMGのドキュメントでは、「キーワード」と「タグ」の用語を同じ意味で使用しています。
    ソースコードでは、変数名`suffix`または`lang_tags`としても呼ばれます。
    すべて同じ意味です。
<!-- [common] -->

<!-- [en] -->
## Header
<!-- [fr] -->
## En-tête
<!-- [ko] -->
## 헤더
<!-- [ja] -->
## ヘッダー
<!-- [common] -->

<!-- [en] -->
!!! info "Note"

    Starting from v2.0.0, headers can be declared anywhere in the document. However, in v1.x.x, headers must be declared before the body starts.
<!-- [fr] -->
!!! info "Note"

    À partir de la version 2.0.0, les en-têtes peuvent être déclarés n'importe où dans le document. Cependant, dans la version 1.x.x, les en-têtes doivent être déclarés avant le corps.
<!-- [ko] -->
!!! info "안내"

    v2.0.0부터 헤더는 문서 어디에서 선언해도 상관없습니다. 하지만, v1.x.x에서는 헤더는 반드시 본문이 시작하기 전에 선언되어야 합니다.
<!-- [ja] -->
!!! info "Note"

    v2.0.0から、ヘッダーはドキュメントのどこにでも宣言できます。ただし、v1.x.xでは、ヘッダーは本文の前に宣言する必要があります。
<!-- [common] -->

<!-- [en] -->
### Declare Keywords to Use
<!-- [fr] -->
### Déclarez les mots-clés à utiliser
<!-- [ko] -->
### 사용할 키워드 선언
<!-- [ja] -->
### 使用するキーワードを宣言する
<!-- [common] -->

<!-- [en] -->
Declare the keywords to use. Keywords are separated by commas.
You can use [IETF language tags](https://en.wikipedia.org/wiki/IETF_language_tag) for keywords.
<!-- [fr] -->
Déclarez les mots-clés à utiliser. Les mots-clés sont séparés par des virgules.
Vous pouvez utiliser des [étiquettes de langue IETF](https://fr.wikipedia.org/wiki/%C3%89tiquette_d%27identification_de_langues_IETF) pour les mots-clés.
<!-- [ko] -->
사용할 키워드를 선언합니다. 키워드는 쉼표로 구분합니다.
키워드에는 [IETF 언어 태그](https://ko.wikipedia.org/wiki/IETF_%EC%96%B8%EC%96%B4_%ED%83%9C%EA%B7%B8)를 사용할 수 있습니다.
<!-- [ja] -->
使用するキーワードを宣言します。キーワードはコンマで区切ります。
キーワードには[IETF言語タグ](https://ja.wikipedia.org/wiki/IETF%E8%A8%80%E8%AA%9E%E3%82%BF%E3%82%B0)を使用できます。
<!-- [common] -->

```markdown
<!-- multilingual suffix: en, kr, fr, es, jp, cn -->
```

<!-- [en] -->
### Do Not Append Suffix to the Created File (Optional)
<!-- [fr] -->
### Ne pas ajouter de suffixe au fichier créé (facultatif)
<!-- [ko] -->
### 생성할 파일에 접미사 붙이지 않기 (Optional)
<!-- [ja] -->
### 作成されたファイルにサフィックスを付けない（オプション）
<!-- [common] -->

<!-- [en] -->
If you do not want to append a suffix to the created file, you can declare it as follows.
For example, if you set `no suffix: en`, `filename.en.md` will not be created, but `filename.md` will be created.
In **GitHub**, the main `README` is not recognized if a suffix is attached, so it is recommended to set `no suffix` for the file to be the main `README`.
<!-- [fr] -->
Si vous ne souhaitez pas ajouter de suffixe au fichier créé, vous pouvez le déclarer comme suit.
Par exemple, si vous définissez `no suffix: en`, `fichier.en.md` ne sera pas créé, mais `fichier.md` sera créé.
Dans **GitHub**, le `README` principal n'est pas reconnu si un suffixe est attaché, il est donc recommandé de définir `no suffix` pour le fichier devant être le `README` principal.
<!-- [ko] -->
지정한 키워드에 대해, 파일을 생성할 때 접미사를 붙이지 않습니다.
예를 들어, `no suffix: en`를 설정하면 `파일이름.en.md`가 아니라 `파일이름.md`가 생성됩니다.
**GitHub**에서 메인 `README`는 접미사가 붙으면 인식이 안되기 때문에, 메인 `README`가 될 파일에는 `no suffix`를 설정하는 것이 좋습니다.
<!-- [ja] -->
作成されたファイルにサフィックスを付けたくない場合は、次のように宣言できます。
たとえば、`no suffix: en`を設定すると、`ファイル名.en.md`は作成されず、`ファイル名.md`が作成されます。
**GitHub**では、サフィックスが付いているとメインの`README`が認識されないため、メインの`README`になるファイルには`no suffix`を設定することをお勧めします。
<!-- [common] -->

```markdown
<!-- no suffix: en -->
```

<!-- [en] -->
## Macro
<!-- [fr] -->
## Macro
<!-- [ko] -->
## 매크로
<!-- [ja] -->
## マクロ
<!-- [common] -->

<!-- [en] -->
### Table of Contents Macro
<!-- [fr] -->
### Macro de table des matières
<!-- [ko] -->
### 목차 매크로
<!-- [ja] -->
### 目次マクロ
<!-- [common] -->

<!-- [en] -->
Existing methods for generating a table of contents don't work for base files with content from multiple keywords. That's why MMG provides a macro to do it automatically.
<!-- [fr] -->
Les méthodes existantes pour générer une table des matières ne fonctionnent pas pour les fichiers de base dont le contenu provient de plusieurs mots-clés. C'est pourquoi MMG fournit une macro pour le faire automatiquement.
<!-- [ko] -->
Base 파일에는 여러 키워드의 내용이 섞여 있어서, markdown 목차를 자동으로 생성해주는 기존의 방법들은 사용할 수 없습니다. 그래서 MMG는 목차를 자동으로 생성해주는 매크로를 제공합니다.
<!-- [ja] -->
Baseファイルには、複数のキーワードからのコンテンツが含まれているため、目次を自動生成する既存の方法は機能しません。そのため、MMGは自動的に行うためのマクロを提供しています。
<!-- [common] -->

```markdown
<!-- [[ multilingual toc: level=2~3 ]] -->
```

<!-- [en] -->
#### Level Option
<!-- [fr] -->
#### Option de niveau
<!-- [ko] -->
#### Level 옵션
<!-- [ja] -->
#### レベルオプション
<!-- [common] -->

<!-- [en] -->
<!-- [fr] -->
<!-- [ko] -->
목차에 표시할 제목의 수준은 `level`을 통해 지정할 수 있습니다.
하나의 문서에 목차 매크로는 여러번 쓸 수 있고, 매번 다른 `level` 옵션을 줄 수도 있습니다.
<!-- [ja] -->
<!-- [common] -->

<!-- [en] -->
!!! warning "Cautions"

    - ==The `level` option is required.== If you omit `level`, MMG will treat this macro as a normal comment.
    - The table of contents macro is implicitly assumed to belong to `<!-- [common] -->`. So, when you use the table of contents macro, the current keyword is automatically changed to `common`.
<!-- [fr] -->
!!! warning "Précautions"

    - ==L'option `level` est obligatoire.== Si vous omettez `level`, MMG traitera cette macro comme un commentaire normal.
    - La macro de table des matières est implicitement supposée appartenir à `<!-- [common] -->`. Ainsi, lorsque vous utilisez la macro de table des matières, le mot-clé actuel est automatiquement modifié en `common`.
<!-- [ko] -->
!!! warning "주의 사항"

    - ==이 `level` 옵션은 필수입니다.== 만약 `level`을 생략하면 MMG는 이 매크로를 일반 주석으로 인식합니다.
    - 목차 매크로는 암묵적으로 `<!-- [common] -->`에 속한 것으로 간주됩니다. 그래서 목차 매크로를 사용하면 자동으로 현재 키워드가 `common`으로 변경됩니다.
<!-- [ja] -->
!!! warning "注意事項"

    - ==この`level`オプションは必須です。== `level`を省略すると、MMGはこのマクロを通常のコメントとして認識します。
    - 目次マクロは暗黙的に`<!-- [common] -->`に属するものと見なされます。そのため、目次マクロを使用すると、自動的に現在のキーワードが`common`に変更されます。
<!-- [common] -->

<!-- [en] -->
There are four ways to specify the `level` to display.
<!-- [fr] -->
Il existe quatre façons de spécifier le `level` à afficher.
<!-- [ko] -->
`level`을 표기하는 방법에는 네 가지가 있습니다.
<!-- [ja] -->
`level`を表示する方法は4つあります。
<!-- [common] -->

<!-- [en] -->
- `level=2`: Only level 2 headings are displayed in the table of contents.
- `level=2~`: Level 2 to 9 headings are displayed in the table of contents.
- `level=~4`: Level 1 to 4 headings are displayed in the table of contents.
- `level=2~4`: Level 2 to 4 headings are displayed in the table of contents.
<!-- [fr] -->
- `level=2`: Seuls les titres de niveau 2 sont affichés dans la table des matières.
- `level=2~`: Les titres de niveau 2 à 9 sont affichés dans la table des matières.
- `level=~4`: Les titres de niveau 1 à 4 sont affichés dans la table des matières.
- `level=2~4`: Les titres de niveau 2 à 4 sont affichés dans la table des matières.
<!-- [ko] -->
- `level=2`: 2수준의 제목만 목차로 만듭니다.
- `level=2~`: 2 ~ 9수준의 제목을 목차로 만듭니다.
- `level=~4`: 1 ~ 4수준의 제목을 목차로 만듭니다.
- `level=2~4`: 2 ~ 4수준의 제목을 목차로 만듭니다.
<!-- [ja] -->
- `level=2`: レベル2の見出しだけが目次に表示されます。
- `level=2~`: レベル2から9の見出しが目次に表示されます。
- `level=~4`: レベル1から4の見出しが目次に表示されます。
- `level=2~4`: レベル2から4の見出しが目次に表示されます。
<!-- [common] -->

<!-- [en] -->
#### No-Emoji Option
<!-- [fr] -->
#### Options de suppression des émoticônes
<!-- [ko] -->
#### 이모지 제거 옵션
<!-- [ja] -->
#### 絵文字なしオプション
<!-- [common] -->

<!-- [en] -->
Sometimes you may want to add emoticons to the title but delete them from the table of contents.
If you are in this situation, apply the `no-emoji` option as shown below.
<!-- [fr] -->
Parfois, vous souhaiterez peut-être ajouter des émoticônes au titre mais les supprimer de la table des matières.
Si vous êtes dans cette situation, appliquez l'option `no-emoji` comme indiqué ci-dessous.
<!-- [ko] -->
간혹, 제목에는 이모티콘을 넣으면서 목차에서는 이모티콘을 지우고 싶을 때가 있습니다.
만약 당신이 이와 같은 상황이라면, 아래와 같이 `no-emoji` 옵션을 적용하세요.
<!-- [ja] -->
時には、タイトルに絵文字を入れながら、目次では絵文字を消したい場合があります。
あなたがこのような状況であれば、以下のように `no-emoji`オプションを適用してください。
<!-- [common] -->

```markdown
<!-- [[ multilingual toc: level=2~3 no-emoji ]] -->
```

<!-- [en] -->
If `no-emoji` is applied, only titles without emojis will be displayed in the table of contents.
<!-- [fr] -->
Si `no-emoji` est appliqué, seuls les titres sans émojis seront affichés dans la table des matières.
<!-- [ko] -->
`no-emoji`가 적용되면, 이모티콘을 제외한 제목만 목차에 표시됩니다.
<!-- [ja] -->
`no-emoji`が適用されると、絵文字のないタイトルのみが目次に表示されます。
<!-- [common] -->

=== "With `no-emoji`"

    ```markdown
    **Table of Contents**

    1. [Heading 1](#heading-1-)
    2. [Heading 2](#heading-2-)

    # Heading 1 💎
    # Heading 2 ❤️
    ```

=== "Without `no-emoji`"

    ```markdown
    **Table of Contents**

    1. [Heading 1 💎](#heading-1-)
    2. [Heading 2 ❤️](#heading-2-)

    # Heading 1 💎
    # Heading 2 ❤️
    ```

<!-- [en] -->
#### Anchor Option
<!-- [fr] -->
#### Option d'ancrage
<!-- [ko] -->
#### 앵커 옵션
<!-- [ja] -->
#### アンカーオプション
<!-- [common] -->

<!-- [en] -->
Heading anchors are not standardized: every renderer derives its own heading IDs.
By default MMG writes GitHub-flavored anchors, which are correct on GitHub for both `.md` and `.ipynb` files.
Jupyter, nbconvert and Colab keep the case and the punctuation of a heading instead, so a table of contents built for GitHub does not jump when the same file is opened there.
Use the `anchor` option to pick the renderer you are targeting.
<!-- [fr] -->
Les ancres de titre ne sont pas normalisées : chaque moteur de rendu génère ses propres identifiants de titre.
Par défaut, MMG produit des ancres au format GitHub, correctes sur GitHub aussi bien pour les fichiers `.md` que `.ipynb`.
Jupyter, nbconvert et Colab conservent au contraire la casse et la ponctuation du titre, si bien qu'une table des matières conçue pour GitHub ne fonctionne pas dans ces visionneuses.
L'option `anchor` permet de choisir le moteur de rendu visé.
<!-- [ko] -->
제목 앵커에는 표준이 없어서, 렌더러마다 제목 ID를 만드는 규칙이 다릅니다.
MMG는 기본적으로 GitHub 방식의 앵커를 생성하며, 이는 `.md`와 `.ipynb` 모두 GitHub에서 정확히 동작합니다.
반면 Jupyter, nbconvert, Colab은 제목의 대소문자와 구두점을 그대로 유지하기 때문에, GitHub 기준으로 만든 목차는 이들 뷰어에서 링크가 이동하지 않습니다.
`anchor` 옵션으로 어떤 렌더러를 기준으로 삼을지 선택할 수 있습니다.
<!-- [ja] -->
見出しアンカーは標準化されておらず、レンダラーごとに見出しIDの生成規則が異なります。
MMGは既定でGitHub形式のアンカーを生成し、これは`.md`でも`.ipynb`でもGitHub上で正しく動作します。
一方、Jupyter・nbconvert・Colabは見出しの大文字小文字と句読点をそのまま保持するため、GitHub向けに生成した目次はこれらのビューアーではリンクが移動しません。
`anchor`オプションで、どのレンダラーを対象にするかを選べます。
<!-- [common] -->

```markdown
<!-- [[ multilingual toc: level=2~3, anchor=jupyter ]] -->
```

<!-- [en] -->
- `anchor=github` (default): `# Nombre d'étoiles` becomes `#nombre-détoiles`. Lowercased, punctuation and emojis removed, and a repeated heading gets `-1`, `-2` and so on.
- `anchor=jupyter`: `# Nombre d'étoiles` becomes `#Nombre-d'%C3%A9toiles`. Case, punctuation and emojis are kept, anything outside ASCII is percent-encoded, and a repeated heading keeps the very same anchor — which is what Jupyter itself does.
<!-- [fr] -->
- `anchor=github` (par défaut) : `# Nombre d'étoiles` devient `#nombre-détoiles`. Casse réduite, ponctuation et émojis supprimés, et un titre répété reçoit `-1`, `-2`, etc.
- `anchor=jupyter` : `# Nombre d'étoiles` devient `#Nombre-d'%C3%A9toiles`. Casse, ponctuation et émojis conservés, tout caractère non ASCII est encodé en pourcentage, et un titre répété garde exactement la même ancre — c'est ce que fait Jupyter lui-même.
<!-- [ko] -->
- `anchor=github` (기본값): `# Nombre d'étoiles`가 `#nombre-détoiles`가 됩니다. 소문자로 바꾸고 구두점과 이모지를 제거하며, 제목이 반복되면 `-1`, `-2`처럼 번호가 붙습니다.
- `anchor=jupyter`: `# Nombre d'étoiles`가 `#Nombre-d'%C3%A9toiles`가 됩니다. 대소문자·구두점·이모지를 그대로 두고, ASCII를 벗어나는 문자는 퍼센트 인코딩하며, 제목이 반복되면 앵커도 똑같이 반복됩니다. Jupyter 자체가 그렇게 동작하기 때문입니다.
<!-- [ja] -->
- `anchor=github`（既定値）: `# Nombre d'étoiles` は `#nombre-détoiles` になります。小文字化し、句読点と絵文字を削除し、見出しが重複すると `-1`、`-2` のように番号が付きます。
- `anchor=jupyter`: `# Nombre d'étoiles` は `#Nombre-d'%C3%A9toiles` になります。大文字小文字・句読点・絵文字をそのまま保持し、ASCII 以外の文字はパーセントエンコードされ、見出しが重複してもアンカーは同じままです。Jupyter 自体がそう動作するためです。
<!-- [common] -->

<!-- [en] -->
!!! warning "Cautions"

    - The default is `github`. Choose `anchor=jupyter` only when the generated file is read in a Jupyter-family viewer, because the very same anchor will not jump on GitHub.
    - An unknown value is rejected by the validation. Only `github` and `jupyter` are accepted, in lower case.
<!-- [fr] -->
!!! warning "Précautions"

    - La valeur par défaut est `github`. Ne choisissez `anchor=jupyter` que si le fichier généré est lu dans une visionneuse de la famille Jupyter, car la même ancre ne fonctionnera pas sur GitHub.
    - Une valeur inconnue est rejetée lors de la validation. Seuls `github` et `jupyter` sont acceptés, en minuscules.
<!-- [ko] -->
!!! warning "주의 사항"

    - 기본값은 `github`입니다. 생성된 파일을 Jupyter 계열 뷰어에서 읽을 때만 `anchor=jupyter`를 선택하세요. 똑같은 앵커가 GitHub에서는 이동하지 않습니다.
    - 알 수 없는 값은 검증 단계에서 거부됩니다. `github`과 `jupyter`만, 소문자로 쓸 수 있습니다.
<!-- [ja] -->
!!! warning "注意事項"

    - 既定値は`github`です。生成したファイルをJupyter系のビューアーで読む場合にのみ`anchor=jupyter`を選んでください。同じアンカーはGitHubでは移動しません。
    - 不明な値は検証時に拒否されます。`github`と`jupyter`のみ、小文字で指定できます。
<!-- [common] -->

<!-- [en] -->
## Body
<!-- [fr] -->
## Corps
<!-- [ko] -->
## 본문
<!-- [ja] -->
## 本文
<!-- [common] -->

<!-- [en] -->
Once a keyword is recognized, subsequent content will be recognized with that keyword until another keyword appears.
<!-- [fr] -->
Une fois qu'un mot-clé est reconnu, le contenu suivant sera reconnu avec ce mot-clé jusqu'à ce qu'un autre mot-clé apparaisse.
<!-- [ko] -->
하나의 키워드가 인식되면, 뛰따르는 내용들은 다른 키워드가 나타날 때까지 해당 키워드로 인식됩니다.
<!-- [ja] -->
キーワードが認識されると、その後のコンテンツは、別のキーワードが表示されるまで、そのキーワードで認識されます。
<!-- [common] -->

<!-- [en] -->
### User-Defined Keyword
<!-- [fr] -->
### Mot-clé défini par l'utilisateur
<!-- [ko] -->
### 사용자 정의 키워드
<!-- [ja] -->
### ユーザー定義キーワード
<!-- [common] -->

<!-- [en] -->
Using the keywords declared in the [header](site:/basic-usage/create-base-file/#header), you can declare which keyword the section belongs to.
If you use an undefined keyword by mistake or the number of keywords does not match, MMG will notify you of an error through the [validation feature](site:/advanced-usage/cli-validation).
<!-- [fr] -->
En utilisant les mots-clés déclarés dans l'[en-tête](site:/fr/basic-usage/create-base-file/#en-tete), vous pouvez déclarer à quel mot-clé appartient la section.
Si vous utilisez par erreur un mot-clé non défini ou si le nombre de mots-clés ne correspond pas, MMG vous informera d'une erreur via la [fonction de validation](site:/fr/advanced-usage/cli-validation).
<!-- [ko] -->
앞서 [헤더](site:/ko/basic-usage/create-base-file/#_3)에서 선언한 키워드를 사용하여, 해당 섹션이 어떤 키워드에 속하는지 선언할 수 있습니다.
만약 실수로 정의되지 않은 키워드를 사용하거나 키워드 간의 개수가 맞지 않는다면, MMG는 [유효성 검사 기능](site:/ko/advanced-usage/cli-validation)을 통해 오류를 알려줍니다.
<!-- [ja] -->
[ヘッダー](site:/ja/basic-usage/create-base-file/#_3)で宣言されたキーワードを使用して、セクションがどのキーワードに属するかを宣言できます。
誤って未定義のキーワードを使用した場合や、キーワードの数が一致しない場合は、[検証機能](site:/ja/advanced-usage/cli-validation)を介してエラーが通知されます。
<!-- [common] -->

```markdown
<!-- [en] -->
<!-- [ko] -->
<!-- [fr] -->
<!-- [es] -->
<!-- [ja] -->
<!-- [cn] -->
...
```

<!-- [en] -->
### Common Section
<!-- [fr] -->
### Section commune
<!-- [ko] -->
### 공통 영역
<!-- [ja] -->
### 共通セクション
<!-- [common] -->

<!-- [en] -->
You can declare the content that will be common to all languages.

```markdown
<!-- [common] -->
This content will be shown in all files.
```
<!-- [fr] -->
Vous pouvez déclarer le contenu qui sera commun à toutes les langues.

```markdown
<!-- [common] -->
Ce contenu sera affiché dans tous les fichiers.
```
<!-- [ko] -->
생성될 모든 파일에 공통적으로 들어갈 내용은 `common` 키워드를 사용하여 작성하면 됩니다.

```markdown
<!-- [common] -->
이 영역에 작성된 내용은 생성될 모든 파일에 공통적으로 들어갑니다.
```
<!-- [ja] -->
生成されるすべてのファイルに共通する内容を宣言できます。

```markdown
<!-- [common] -->
この内容はすべてのファイルに表示されます。
```
<!-- [common] -->

<!-- [en] -->
### Ignored Section
<!-- [fr] -->
### Section ignorée
<!-- [ko] -->
### 무시할 영역
<!-- [ja] -->
### 無視されるセクション
<!-- [common] -->

<!-- [en] -->
Sometimes you may want to ignore a section, such as comments or minor memos, from the created file.
In that case, use the `ignore` keyword.

```markdown
<!-- [ignore] -->
This section will not be included in the created file.
```
<!-- [fr] -->
Parfois, vous souhaiterez peut-être ignorer une section, comme des commentaires ou des mémos mineurs, du fichier créé.
Dans ce cas, utilisez le mot-clé `ignore`.

```markdown
<!-- [ignore] -->
Cette section ne sera pas incluse dans le fichier créé.
```
<!-- [ko] -->
주석이나 사소한 메모와 같은 것들은 생성될 파일에 포함하고 싶지 않는 경우가 있습니다.
그런 경우 `ignore` 키워드를 사용하세요.

```markdown
<!-- [ignore] -->
이 영역은 생성될 파일에 포함되지 않습니다.
```
<!-- [ja] -->
コメントやメモなど、作成されたファイルから除外したいセクションがある場合は、`ignore`キーワードを使用します。

```markdown
<!-- [ignore] -->
このセクションは、作成されたファイルに含まれません。
```
<!-- [common] -->
