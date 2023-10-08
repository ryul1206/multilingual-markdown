<!---------------------------->
<!-- multilingual suffix: en, fr, ko, ja -->
<!---------------------------->
<!-- [en] -->
# Recursive Option
<!-- [fr] -->
# Option Récursive
<!-- [ko] -->
# 재귀 옵션
<!-- [ja] -->
# 再帰オプション
<!-- [common] -->

!!! note ""

<!-- [en] -->
    English |
    [**Français**](/fr/basic-usage/cli-recursive) |
    [**한국어**](/ko/basic-usage/cli-recursive) |
    [**日本語**](/ja/basic-usage/cli-recursive)
<!-- [fr] -->
    [**English**](/basic-usage/cli-recursive) |
    Français |
    [**한국어**](/ko/basic-usage/cli-recursive) |
    [**日本語**](/ja/basic-usage/cli-recursive)
<!-- [ko] -->
    [**English**](/basic-usage/cli-recursive) |
    [**Français**](/fr/basic-usage/cli-recursive) |
    한국어 |
    [**日本語**](/ja/basic-usage/cli-recursive)
<!-- [ja] -->
    [**English**](/basic-usage/cli-recursive) |
    [**Français**](/fr/basic-usage/cli-recursive) |
    [**한국어**](/ko/basic-usage/cli-recursive) |
    日本語
<!-- [common] -->

<!-- [en] -->
If you want to convert all base files in the current directory and subdirectories, use the `--recursive` or `-r` option.
<!-- [fr] -->
Si vous souhaitez convertir tous les fichiers de base du répertoire actuel et des sous-répertoires, utilisez l'option `--recursive` ou `-r`.
<!-- [ko] -->
현재 디렉토리와 하위 디렉토리에 있는 모든 베이스 파일을 변환하고 싶다면, `--recursive` 또는 `-r` 옵션을 사용하세요.
<!-- [ja] -->
現在のディレクトリとサブディレクトリのすべてのベースファイルを変換したい場合は、`--recursive`または`-r`オプションを使用します。
<!-- [common] -->

```sh
mmg --recursive
```

<!-- [en] -->
For example, let's assume that the current path is as follows.
<!-- [fr] -->
Soyons par exemple que le chemin actuel est le suivant.
<!-- [ko] -->
예를 들어, 현재 경로가 다음과 같다고 가정해봅시다.
<!-- [ja] -->
たとえば、現在のパスが次のとおりであるとします。
<!-- [common] -->

```text
.
├─ docs/
│  └─ Retriever.base.md
├─ jupyter/
│  └─ Collie.base.ipynb
└─ Corgi.base.md
```

<!-- [en] -->
Using the recursive option, you can convert all base files in the current directory and subdirectories.
<!-- [fr] -->
En utilisant l'option récursive, vous pouvez convertir tous les fichiers de base du répertoire actuel et des sous-répertoires.
<!-- [ko] -->
재귀 옵션을 사용하면, 현재 디렉토리와 하위 디렉토리에 있는 모든 베이스 파일을 변환할 수 있습니다.
<!-- [ja] -->
再帰オプションを使用すると、現在のディレクトリとサブディレクトリのすべてのベースファイルを変換できます。
<!-- [common] -->

```sh
$ mmg -r
----------------------
 ✅ Corgi.base.md
 ✅ docs\Retriever.base.md
 ✅ jupyter\Collie.base.ipynb
----------------------
 => 3 base files were found.
    Do you want to convert these files? [y/N]
```

<!-- [en] -->
You can also use the recursive option when you pass a file as an argument, and you can also use it with the `--output` option.
(About the `--output` option, see [here](/basic-usage/cli-html-pdf).)
However, it cannot be used with the [batch processing option](/advanced-usage/cli-batch-processing).
If you use `--recursive` and `--batch` together, `--batch` is ignored, so you cannot use them together.
<!-- [fr] -->
Vous pouvez également utiliser l'option récursive lorsque vous passez un fichier en argument, et vous pouvez également l'utiliser avec l'option `--output`.
(A propos de l'option `--output`, voir [ici](/fr/basic-usage/cli-html-pdf).)
Cependant, il ne peut pas être utilisé avec l'option [traitement par lots](/fr/advanced-usage/cli-batch-processing).
Si vous utilisez `--recursive` et `--batch` ensemble, `--batch` est ignoré, vous ne pouvez donc pas les utiliser ensemble.
<!-- [ko] -->
재귀 옵션은 파일을 인자로 받을 때도 함께 사용할 수 있고, `--output` 옵션도 함께 사용할 수도 있습니다.
(`--output` 옵션에 대해서는 [여기](/ko/basic-usage/cli-html-pdf)를 보아주세요.)
하지만 [일괄 처리 옵션](/ko/advanced-usage/cli-batch-processing)과 함께 사용할 수는 없습니다.
`--recursive`와 `--batch`를 함께 사용하면, `--batch`가 무시되기 때문에 함께 사용할 수 없습니다.
<!-- [ja] -->
再帰オプションは、ファイルを引数として渡すときにも使用でき、`--output`オプションとも使用できます。
(`--output`オプションについては[こちら](/ja/basic-usage/cli-html-pdf)をご覧ください。)
ただし、[バッチ処理オプション](/ja/advanced-usage/cli-batch-processing)とは併用できません。
`--recursive`と`--batch`を併用すると、`--batch`は無視されるため、併用できません。
<!-- [common] -->
