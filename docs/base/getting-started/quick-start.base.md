<!---------------------------->
<!-- multilingual suffix: en, fr, ko, ja -->
<!---------------------------->
<!-- [en] -->
# Quick Start with Examples
<!-- [fr] -->
# Démarrage rapide avec des Exemples
<!-- [ko] -->
# 빠른 시작을 위한 예제
<!-- [ja] -->
# クイックスタートのための例
<!-- [common] -->

!!! note ""

<!-- [en] -->
    English |
    [**Français**](/fr/getting-started/quick-start) |
    [**한국어**](/ko/getting-started/quick-start) |
    [**日本語**](/ja/getting-started/quick-start)
<!-- [fr] -->
    [**English**](/getting-started/quick-start) |
    Français |
    [**한국어**](/ko/getting-started/quick-start) |
    [**日本語**](/ja/getting-started/quick-start)
<!-- [ko] -->
    [**English**](/getting-started/quick-start) |
    [**Français**](/fr/getting-started/quick-start) |
    한국어 |
    [**日本語**](/ja/getting-started/quick-start)
<!-- [ja] -->
    [**English**](/getting-started/quick-start) |
    [**Français**](/fr/getting-started/quick-start) |
    [**한국어**](/ko/getting-started/quick-start) |
    日本語
<!-- [common] -->

<!-- [en] -->
This page explains the most basic way to create and convert a Base file.
<!-- [fr] -->
Cette page explique la façon la plus basique de créer et convertir un fichier Base.
<!-- [ko] -->
이 페이지에서는 Base 파일을 만들고 변환하는 가장 기초적인 방법을 설명합니다.
<!-- [ja] -->
このページでは、Baseファイルを作成し、変換する最も基本的な方法について説明します。
<!-- [common] -->

<!-- [en] -->
## Step 1. Create a Base File
<!-- [fr] -->
## Étape 1. Créer un Fichier Base
<!-- [ko] -->
## 1 단계. Base 파일 만들기
<!-- [ja] -->
## Step 1. Baseファイルを作成する
<!-- [common] -->

<!-- [en] -->
Create a file named `foo.base.md`. You can name it whatever you want.
<!-- [fr] -->
Créez un fichier nommé `foo.base.md`. Vous pouvez le nommer comme vous voulez.
<!-- [ko] -->
다음과 같이 `foo.base.md` 파일을 만듭니다. 파일 이름은 자유롭게 바꾸셔도 됩니다.
<!-- [ja] -->
`foo.base.md`というファイルを作成します。ファイル名は自由に変更しても構いません。
<!-- [common] -->

````md
<!---------------------------->
<!-- multilingual suffix: en, fr, ko, ja -->
<!---------------------------->
# Hello, World!

<!-- [en] -->
You can see this written in other languages: `foo.en.md`, `foo.fr.md`, `foo.ja.md`
<!-- [fr] -->
Ceci s'écrit en français comme "Bonjour, le monde !".
<!-- [ko] -->
이것은 한국어로 "안녕, 세상아!"라고 쓴 것입니다.
<!-- [ja] -->
これは日本語で「こんにちは、世のああ！」と書いたものです。
<!-- [common] -->

```md
Thank you for using MMG!
<!-- [en] -->
Tags within code blocks are treated as plain text.
```
````

<!-- [en] -->
Please refer to the ["Create a Base File"](/basic-usage/create-base-file) page for features not introduced here.

Now you are ready to use MMG!
Let's create `en`, `fr`, `ko`, `ja` files in the next step.
<!-- [fr] -->
Veuillez vous référer à la page ["Créer un Fichier Base"](/fr/basic-usage/create-base-file) pour les fonctionnalités non présentées ici.

Vous êtes maintenant prêt à utiliser MMG !
Créons les fichiers `en`, `fr`, `ko`, `ja` à l'étape suivante.
<!-- [ko] -->
여기서 소개하지 않은 기능들은 ["베이스 파일 만들기"](/ko/basic-usage/create-base-file) 페이지를 참고하세요.

이제 MMG를 사용할 준비가 되었습니다!
다음 단계에서는 `en`, `fr`, `ko`, `ja` 파일을 생성해보겠습니다.
<!-- [ja] -->
ここでは紹介していない機能は、["Baseファイルを作成する"](/ja/basic-usage/create-base-file)ページを参照してください。

これでMMGを使用する準備が整いました！
次のステップでは、`en`、`fr`、`ko`、`ja`ファイルを作成します。
<!-- [common] -->

<!-- [en] -->
## Step 2. Convert using MMG
<!-- [fr] -->
## Étape 2. Convertir avec MMG
<!-- [ko] -->
## 2 단계. MMG를 사용하여 변환하기
<!-- [ja] -->
## Step 2. MMGを使用して変換する
<!-- [common] -->

<!-- [en] -->
Run the following command to perform the conversion.
Check that `foo.en.md`, `foo.fr.md`, `foo.ko.md`, `foo.ja.md` files are created in the same path as `foo.base.md`.
<!-- [fr] -->
Exécutez la commande suivante pour effectuer la conversion.
Vérifiez que les fichiers `foo.en.md`, `foo.fr.md`, `foo.ko.md`, `foo.ja.md` sont créés dans le même chemin que `foo.base.md`.
<!-- [ko] -->
다음 명령어를 입력하여 변환을 수행합니다.
`foo.base.md`와 동일한 경로에 `foo.en.md`, `foo.fr.md`, `foo.ko.md`, `foo.ja.md` 파일이 생성되었는지 확인하세요.
<!-- [ja] -->
変換を実行するには、次のコマンドを実行します。
`foo.base.md`と同じパスに`foo.en.md`、`foo.fr.md`、`foo.ko.md`、`foo.ja.md`ファイルが作成されていることを確認してください。
<!-- [common] -->

<!-- [en] -->
!!! warning "Cautions"

    MMG overwrites existing files when creating files. Therefore, you do not need to delete the created files even if you modify the Base file. Instead, **any modifications made in the created file will be lost**, so please modify contents in the Base file.
<!-- [fr] -->
!!! warning "Précautions"

    MMG écrase les fichiers existants lors de la création de fichiers. Par conséquent, vous n'avez pas besoin de supprimer les fichiers créés même si vous modifiez le fichier Base. Au lieu de cela, **toute modification apportée au fichier créé sera perdue**, alors veuillez modifier le contenu dans le fichier Base.
<!-- [ko] -->
!!! warning "주의 사항"

    MMG는 파일을 생성할 때, 이미 존재하는 파일을 매번 덮어씁니다. 따라서, Base 파일을 수정하더라도 생성된 파일을 매번 지울 필요가 없습니다. 대신 **생성된 파일에서 수정한 내용은 사라지므로**, 수정은 Base 파일에서 하기 바랍니다.
<!-- [ja] -->
!!! warning "注意事項"

    MMGは、ファイルを作成するときに既存のファイルを上書きします。したがって、Baseファイルを変更しても、作成されたファイルを削除する必要はありません。代わりに、**作成されたファイルで行った変更は失われる**ため、Baseファイルでコンテンツを変更してください。
<!-- [common] -->

```sh
mmg foo.base.md
```

<!-- [en] -->
For example, the contents of `foo.en.md` are as follows.
<!-- [fr] -->
Par exemple, le contenu de `foo.fr.md` est le suivant.
<!-- [ko] -->
예를 들어, `foo.en.md`의 내용은 다음과 같습니다.
<!-- [ja] -->
例えば、`foo.ja.md`の内容は次のようになります。
<!-- [common] -->

````md
# Hello, World!

You can see this written in other languages: `foo.en.md`, `foo.fr.md`, `foo.ja.md`

```md
Thank you for using MMG!
<!-- [en] -->
Tags within code blocks are treated as plain text.
```
````

<!-- [en] -->
Also check `foo.fr.md`. You can see that MMG correctly classifies the content according to each tag.

````md
# Hello, World!

Ceci s'écrit en français comme "Bonjour, le monde !".

```md
Thank you for using MMG!
<!-- [en] -->
Tags within code blocks are treated as plain text.
```
````
<!-- [fr] -->
Vérifiez également `foo.fr.md`. Vous pouvez voir que MMG classe correctement le contenu en fonction de chaque balise.

````md
# Hello, World!

Ceci s'écrit en français comme "Bonjour, le monde !".

```md
Thank you for using MMG!
<!-- [en] -->
Tags within code blocks are treated as plain text.
```
````
<!-- [ko] -->
`foo.ko.md`도 확인해보세요. MMG가 각 태그에 따라 제대로 내용을 분류하는 것을 확인할 수 있습니다.

````md
# Hello, World!

이것은 한국어로 "안녕, 세상아!"라고 쓴 것입니다.

```md
Thank you for using MMG!
<!-- [en] -->
Tags within code blocks are treated as plain text.
```
````
<!-- [ja] -->
`foo.ja.md`も確認してください。MMGが各タグに応じてコンテンツを正しく分類していることがわかります。

````md
# Hello, World!

これは日本語で「こんにちは、世のああ！」と書いたものです。

```md
Thank you for using MMG!
<!-- [en] -->
Tags within code blocks are treated as plain text.
```
````
<!-- [common] -->

<!-- [en] -->
## How to Convert Multiple Files at Once
<!-- [fr] -->
## Comment Convertir Plusieurs Fichiers à la Fois
<!-- [ko] -->
## 한 번에 여러 파일 변환하기
<!-- [ja] -->
## 一度に複数のファイルを変換する方法
<!-- [common] -->

<!-- [en] -->
MMG has three ways to process multiple files at once.
<!-- [fr] -->
MMG a trois façons de traiter plusieurs fichiers à la fois.
<!-- [ko] -->
MMG가 여러 파일을 한 번에 처리하는 방식에는 세 가지가 있습니다.
<!-- [ja] -->
MMGには、複数のファイルを一度に処理する方法が3つあります。
<!-- [common] -->

<!-- [en] -->
- (Method 1) Input multiple files as arguments
- (Method 2) Recursively search all subpaths from the current path
- (Method 3) Define tasks in a YAML file and process them in batch
<!-- [fr] -->
- (Méthode 1) Entrer plusieurs fichiers en tant qu'arguments
- (Méthode 2) Rechercher récursivement tous les sous-chemins depuis le chemin actuel
- (Méthode 3) Définir des tâches dans un fichier YAML et les traiter en lot
<!-- [ko] -->
- (방법 1) 인자로 여러 파일을 입력하는 방식
- (방법 2) 현재 경로에서 모든 하위 경로를 재귀적으로 탐색하는 방식
- (방법 3) YAML 파일에 작업을 정의하여 일괄 처리하는 방식
<!-- [ja] -->
- (方法1) 複数のファイルを引数として入力する
- (方法2) 現在のパスからすべてのサブパスを再帰的に検索する
- (方法3) YAMLファイルでタスクを定義し、バッチで処理する
<!-- [common] -->

<!-- [en] -->
For the first method, you can input multiple files separated by spaces.
<!-- [fr] -->
Pour la première méthode, vous pouvez entrer plusieurs fichiers séparés par des espaces.
<!-- [ko] -->
첫 번째 방법의 경우, 띄워쓰기로 구분하여 여러 파일을 입력하면 됩니다.
<!-- [ja] -->
最初の方法では、スペースで区切って複数のファイルを入力できます。
<!-- [common] -->

```sh
mmg Foo.base.md Bar.base.md Baz.base.md
```

<!-- [en] -->
For the second method, use the `--recursive` or `-r` option, which can also be used with the first method.
Please refer to the [recursive option](/basic-usage/cli-recursive) for more information.
<!-- [fr] -->
Pour la deuxième méthode, utilisez l'option `--recursive` ou `-r`, qui peut également être utilisée avec la première méthode.
Veuillez vous référer à l'[option récursive](/fr/basic-usage/cli-recursive) pour plus d'informations.
<!-- [ko] -->
두 번째 방법의 경우, `--recursive` 또는 `-r` 옵션을 사용하면 되고, 첫 번째 방법과 함께 사용할 수도 있습니다.
자세한 내용은 [재귀 옵션](/ko/basic-usage/cli-recursive)을 참고하세요.
<!-- [ja] -->
2番目の方法では、最初の方法と同様に、`--recursive`または`-r`オプションを使用します。
詳細については、[再帰オプション](/ja/basic-usage/cli-recursive)を参照してください。
<!-- [common] -->

<!-- [en] -->
Finally, for the third method, please refer to the [batch processing with YAML file](/advanced-usage/cli-batch-processing) page.
<!-- [fr] -->
Enfin, pour la troisième méthode, veuillez vous référer à la page [traitement par lots avec fichier YAML](/fr/advanced-usage/cli-batch-processing).
<!-- [ko] -->
마지막으로 세 번째 방법에 대해서는 [YAML 파일을 사용한 일괄 처리](/ko/advanced-usage/cli-batch-processing) 페이지를 참고하세요.
<!-- [ja] -->
最後に、3番目の方法については、[YAMLファイルを使用したバッチ処理](/ja/advanced-usage/cli-batch-processing)ページを参照してください。
<!-- [common] -->
