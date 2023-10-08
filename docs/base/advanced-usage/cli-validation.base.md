<!---------------------------->
<!-- multilingual suffix: en, fr, ko, ja -->
<!---------------------------->
<!-- [en] -->
# Base File Validation
<!-- [fr] -->
# Validation du Fichier de Base
<!-- [ko] -->
# Base 파일 유효성 검사
<!-- [ja] -->
# ベースファイルの検証
<!-- [common] -->

!!! note ""

<!-- [en] -->
    English |
    [**Français**](/fr/advanced-usage/cli-validation) |
    [**한국어**](/ko/advanced-usage/cli-validation) |
    [**日本語**](/ja/advanced-usage/cli-validation)
<!-- [fr] -->
    [**English**](/advanced-usage/cli-validation) |
    Français |
    [**한국어**](/ko/advanced-usage/cli-validation) |
    [**日本語**](/ja/advanced-usage/cli-validation)
<!-- [ko] -->
    [**English**](/advanced-usage/cli-validation) |
    [**Français**](/fr/advanced-usage/cli-validation) |
    한국어 |
    [**日本語**](/ja/advanced-usage/cli-validation)
<!-- [ja] -->
    [**English**](/advanced-usage/cli-validation) |
    [**Français**](/fr/advanced-usage/cli-validation) |
    [**한국어**](/ko/advanced-usage/cli-validation) |
    日本語
<!-- [common] -->

<!-- [ko] -->
## 어떤 것을 검사합니까?
<!-- [ja] -->
## 何を検証しますか？
<!-- [en] -->
## What is validated?
<!-- [fr] -->
## Qu'est-ce qui est validé ?
<!-- [common] -->

<!-- [ko] -->
MMG는 주로 다음의 내용을 검사합니다.
<!-- [ja] -->
MMG は主に以下の内容を検証します。
<!-- [en] -->
MMG mainly validates the following contents.
<!-- [fr] -->
MMG vérifie principalement les contenus suivants.
<!-- [common] -->

<!-- [ko] -->
- 사용자가 사용한 각 태그의 개수가 동일한지 여부
- 모든 태그가 한 번씩 나타나기 전에, 중복된 태그가 다시 나타나는지 여부
- 미리 지정된 태그가 아닌 태그가 있는지 여부
- `no-suffix` 옵션이 제대로 설정되었는지 여부
<!-- [ja] -->
- 使用者が使用した各タグの数が同じかどうか
- すべてのタグが一度ずつ現れる前に、重複したタグが再び現れるかどうか
- 事前に指定されたタグ以外のタグがあるかどうか
- `no-suffix` オプションが正しく設定されているかどうか
<!-- [en] -->
- Whether the number of each tag used by the user is the same
- Whether a duplicate tag appears again before all tags appear once
- Whether there are tags other than the tags specified in advance
- Whether the `no-suffix` option is set correctly
<!-- [fr] -->
- Si le nombre de chaque tag utilisé par l'utilisateur est le même
- Si un tag en double apparaît à nouveau avant que tous les tags n'apparaissent une fois
- S'il y a des tags autres que les tags spécifiés à l'avance
- Si l'option `no-suffix` est correctement définie
<!-- [common] -->

<!-- [ko] -->
검사를 통과하지 못하면, 이 페이지에서 설명할 Verbosity 설정을 통해 사용자에게 검사를 통과하지 못한 이유를 알려줄 수 있습니다.
검사를 통과하지 못했더라도 강제로 변환할 수 있습니다.
<!-- [ja] -->
検証に合格しない場合は、このページで説明する Verbosity 設定を通じて、使用者に検証に合格しない理由を知らせることができます。
検証に合格しなくても強制的に変換することができます。
<!-- [en] -->
If the validation fails, you can use the verbosity setting described on this page to let the user know why the validation failed.
Even if the validation fails, you can force the conversion.
<!-- [fr] -->
Si la validation échoue, vous pouvez utiliser le paramètre de verbosité décrit sur cette page pour informer l'utilisateur de la raison de l'échec de la validation.
Même si la validation échoue, vous pouvez forcer la conversion.
<!-- [common] -->

<!-- [ko] -->
### 사용된 태그의 개수가 동일한지 여부
<!-- [ja] -->
### 使用されたタグの数が同じかどうか
<!-- [en] -->
### Whether the number of tags used is the same
<!-- [fr] -->
### Si le nombre de tags utilisés est le même
<!-- [common] -->

<!-- [ko] -->
사용자가 빠트린 태그가 있는지 확인하기 위해, MMG는 사용자가 사용한 각 태그의 개수를 세어서 비교합니다.
<!-- [ja] -->
使用者が抜けているタグがあるかどうかを確認するために、MMG は使用者が使用した各タグの数を数えて比較します。
<!-- [en] -->
To check if the user has missed a tag, MMG counts the number of each tag used by the user and compares it.
<!-- [fr] -->
Pour vérifier si l'utilisateur a manqué une balise, MMG compte le numéro de chaque balise utilisée par l'utilisateur et le compare.
<!-- [common] -->

<!-- [ko] -->
=== "Validation 실패"

    B를 빠트렸기 때문에 검사를 통과하지 못합니다.
<!-- [ja] -->
=== "Validation 失敗"

    B を抜けたため、検証に合格しません。
<!-- [en] -->
=== "Validation fails"

    The validation fails because B is missing.
<!-- [fr] -->
=== "La validation échoue"

    La validation échoue car B est manquant.
<!-- [common] -->

    ```markdown
    <!-- multilingual suffix: A, B, C -->

    <!-- [A] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <!-- [C] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    ```

<!-- [ko] -->
=== "Validation 통과"
<!-- [ja] -->
=== "Validation 通過"
<!-- [en] -->
=== "Validation passes"
<!-- [fr] -->
=== "La validation réussit"
<!-- [common] -->

    ```markdown
    <!-- multilingual suffix: A, B, C -->

    <!-- [A] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <!-- [B] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <!-- [C] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    ```

<!-- [ko] -->
### 모든 태그가 한 번씩 나타나기 전에, 중복된 태그가 다시 나타나는지 여부
<!-- [ja] -->
### すべてのタグが一度ずつ現れる前に、重複したタグが再び現れるかどうか
<!-- [en] -->
### Whether a duplicate tag appears again before all tags appear once
<!-- [fr] -->
### Si un tag en double apparaît à nouveau avant que tous les tags n'apparaissent une fois
<!-- [common] -->

<!-- [ko] -->
문서 전체를 볼 때, 모든 태그들이 동일한 횟수로 사용되었더라도, 모든 태그들이 세트로 묶여서 나타나지 않으면 검사를 통과하지 못합니다.
<!-- [ja] -->
ドキュメント全体を見ると、すべてのタグが同じ回数使われていたとしても、すべてのタグがセットでまとめて現れない場合は、検証に合格しません。
<!-- [en] -->
Even if all tags are used the same number of times throughout the document, the validation will fail if any tags do not appear by set.
<!-- [fr] -->
Même si tous les tags sont utilisés le même nombre de fois dans tout le document, la validation échouera si certains tags n'apparaissent pas par ensemble.
<!-- [common] -->

<!-- [ko] -->
이렇게 검사하는 이유는 모든 태그들이 균일하게 등장하지 않으면, 사용자가 어떤 태그를 빠트렸는지 알기 어렵기 때문입니다.
심지어 사용된 태그의 개수가 동일하기 때문에, 문서가 길어진다면 더더욱 알기 어렵습니다.
이 검사를 통해, 잠재적으로 발생할 수 있는 문제를 미리 방지할 수 있습니다.
<!-- [ja] -->
このように検証する理由は、すべてのタグが均一に現れない場合、使用者がどのタグを抜けたかを知るのが難しいためです。
しかも使用されたタグの数が同じであるため、ドキュメントが長くなるとなおさら知るのが難しいです。
この検証を通じて、潜在的に発生する可能性のある問題を事前に防ぐことができます。
<!-- [en] -->
The reason for this validation is that if all tags do not appear uniformly, it is difficult for the user to know which tag is missing.
Even if the number of tags used is the same, it is even more difficult to know if the document is long.
Through this validation, potential problems can be prevented in advance.
<!-- [fr] -->
La raison de cette validation est que si toutes les balises n’apparaissent pas uniformément, il est difficile pour l’utilisateur de savoir quelle balise manque.
Même si le nombre de balises utilisées est le même, il est encore plus difficile de savoir si le document est long.
Grâce à cette validation, les problèmes potentiels peuvent être évités à l’avance.
<!-- [common] -->

<!-- [ko] -->
=== "Validation 실패"

    A, B, C에 빠진 내용이 없으므로, MMG가 생성할 내용에는 문제가 없습니다.
    하지만, A와 B가 나타난 후에, A가 다시 나타났기 때문에 검사를 통과하지 못합니다.
<!-- [ja] -->
=== "Validation 失敗"

    A, B, C に抜けた内容がないため、MMG が生成する内容には問題がありません。
    しかし、A と B が現れた後、A が再び現れたため、検証に合格しません。
<!-- [en] -->
=== "Validation fails"

    There is no missing content in A, B, and C, so there is no problem with the content MMG will generate.
    However, since A appears again after A and B appear, the validation fails.
<!-- [fr] -->
=== "La validation échoue"

    Il n’y a pas de contenu manquant dans A, B et C, donc il n’y a pas de problème avec le contenu que MMG va générer.
    Cependant, comme A apparaît à nouveau après que A et B apparaissent, la validation échoue.
<!-- [common] -->

    ```markdown
    <!-- multilingual suffix: A, B, C -->

    <!-- [A] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <!-- [B] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

    <!-- [A] -->
    Aenean in ultrices metus, in semper mi.
    <!-- [B] -->
    Aenean in ultrices metus, in semper mi.

    <!-- [C] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <!-- [C] -->
    Aenean in ultrices metus, in semper mi.
    ```

<!-- [ko] -->
=== "Validation 통과"

    A, B, C가 반드시 순서대로 나타날 필요는 없습니다.
<!-- [ja] -->
=== "Validation 通過"

    A, B, C が必ずしも順番に現れる必要はありません。
<!-- [en] -->
=== "Validation passes"

    A, B, and C do not necessarily have to appear in order.
<!-- [fr] -->
=== "La validation réussit"

    A, B et C n’ont pas nécessairement à apparaître dans l’ordre.
<!-- [common] -->

    ```markdown
    <!-- multilingual suffix: A, B, C -->

    <!-- [C] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <!-- [A] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <!-- [B] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

    <!-- [A] -->
    Aenean in ultrices metus, in semper mi.
    <!-- [B] -->
    Aenean in ultrices metus, in semper mi.
    <!-- [C] -->
    Aenean in ultrices metus, in semper mi.
    ```

<!-- [ko] -->
### 미리 지정된 태그가 아닌 태그가 있는지 여부
<!-- [ja] -->
### 事前に指定されたタグ以外のタグがあるかどうか
<!-- [en] -->
### Whether there are tags other than the tags specified in advance
<!-- [fr] -->
### S'il y a des tags autres que les tags spécifiés à l'avance
<!-- [common] -->

<!-- [ko] -->
사용자는 언제든 오타를 낼 수 있으므로, MMG가 사용자 정의 태그를 읽을 때, 헤더에 선언된 태그인지 확인합니다.

=== "Validation 실패"

    `ko`를 `kr`로 잘못 입력했고, `ja`도 `jp`로 잘못 입력했기 때문에 검사를 통과하지 못합니다.
<!-- [ja] -->
使用者はいつでもタイプミスをする可能性があるため、MMG が使用者定義タグを読むとき、ヘッダーに宣言されたタグかどうかを確認します。

=== "Validation 失敗"

    `ko` を `kr` と間違って入力し、`ja` も `jp` と間違って入力したため、検証に合格しません。
<!-- [en] -->
Since the user can make a typo at any time, MMG checks whether the tag is declared in the header when reading the user-defined tag.

=== "Validation fails"

    The validation fails because `ko` was incorrectly entered as `kr` and `ja` was also incorrectly entered as `jp`.
<!-- [fr] -->
Comme l’utilisateur peut faire une faute de frappe à tout moment, MMG vérifie si la balise est déclarée dans l’en-tête lors de la lecture de la balise définie par l’utilisateur.

=== "La validation échoue"

    La validation échoue car `ko` a été entré incorrectement comme `kr` et `ja` a également été entré incorrectement comme `jp`.
<!-- [common] -->

    ```markdown
    <!-- multilingual suffix: ko, ja -->

    <!-- [kr] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <!-- [jp] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    ```

<!-- [ko] -->
=== "Validation 통과"
<!-- [ja] -->
=== "Validation 通過"
<!-- [en] -->
=== "Validation passes"
<!-- [fr] -->
=== "La validation réussit"
<!-- [common] -->

    ```markdown
    <!-- multilingual suffix: ko, ja -->

    <!-- [ko] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <!-- [ja] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    ```

<!-- [ko] -->
### `no-suffix` 옵션이 제대로 설정되었는지 여부
<!-- [ja] -->
### `no-suffix` オプションが正しく設定されているかどうか
<!-- [en] -->
### Whether the `no-suffix` option is set correctly
<!-- [fr] -->
### Si l'option `no-suffix` est correctement définie
<!-- [common] -->

<!-- [ko] -->
=== "Validation 실패"

    `en-US`는 사용자 정의 태그가 아니므로 검사를 통과하지 못합니다.
<!-- [ja] -->
=== "Validation 失敗"

    `en-US` は使用者定義タグではないため、検証に合格しません。
<!-- [en] -->
=== "Validation fails"

    `en-US` is not a user-defined tag, so the validation fails.
<!-- [fr] -->
=== "La validation échoue"

    `en-US` n’est pas une balise définie par l’utilisateur, donc la validation échoue.
<!-- [common] -->

    ```markdown
    <!-- multilingual suffix: ko, ja -->
    <!-- no suffix: en-US -->

    <!-- [kr] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <!-- [jp] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    ```

<!-- [ko] -->
=== "Validation 통과"
<!-- [ja] -->
=== "Validation 通過"
<!-- [en] -->
=== "Validation passes"
<!-- [fr] -->
=== "La validation réussit"
<!-- [common] -->

    ```markdown
    <!-- multilingual suffix: ko, ja -->
    <!-- no suffix: ko -->

    <!-- [ko] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <!-- [ja] -->
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    ```

<!-- [ko] -->
## Verbosity 설정
<!-- [ja] -->
## Verbosity 設定
<!-- [en] -->
## Verbosity setting
<!-- [fr] -->
## Réglage de la verbosité
<!-- [common] -->

<!-- [ko] -->
!!! info "안내"

    GitHub 저장소에 verbosity 설정을 시험해볼 수 있는 예제 파일이 있으니 사용해보세요.
    (예제 파일 위치: [./examples/validation-examples](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/validation-examples))
<!-- [ja] -->
!!! info "Note"

    GitHub リポジトリに Verbosity 設定を試験できる例題ファイルがあるので、使ってみてください。
    (例題ファイルの位置: [./examples/validation-examples](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/validation-examples))
<!-- [en] -->
!!! info "Note"

    There are example files that can test the verbosity setting in the GitHub repository, so please use them.
    (Example file location: [./examples/validation-examples](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/validation-examples))
<!-- [fr] -->
!!! info "Note"

    Il existe des fichiers d’exemple qui peuvent tester le réglage de la verbosité dans le dépôt GitHub, alors veuillez les utiliser.
    (Emplacement du fichier d’exemple: [./examples/validation-examples](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/validation-examples))
<!-- [common] -->

<!-- [ko] -->
Verbosity는 0이 기본값이기 때문에, 평소의 MMG는 검사 결과만을 출력합니다.
<!-- [ja] -->
Verbosity は 0 がデフォルト値なので、普段の MMG は検証結果だけを出力します。
<!-- [en] -->
Since 0 is the default value, the usual MMG only outputs the validation results.
<!-- [fr] -->
Comme 0 est la valeur par défaut, le MMG habituel ne produit que les résultats de validation.
<!-- [common] -->

```sh
$ mmg -r
----------------------
 ❌ bad_md.base.md
 ✅ good_md.base.md
 ❌ bad_jupyter.base.ipynb
----------------------
 => 3 base files were found.
    Do you want to convert these files? [y/N]
```

<!-- [ko] -->
하지만 Verbosity 설정을 하면, 검사를 통과하지 못한 이유를 알 수 있습니다.
<!-- [ja] -->
しかし Verbosity 設定をすると、検証に合格しない理由を知ることができます。
<!-- [en] -->
However, if you set the verbosity, you can find out why the validation failed.
<!-- [fr] -->
Cependant, si vous réglez la verbosité, vous pouvez savoir pourquoi la validation a échoué.
<!-- [common] -->

<!-- [ko] -->
### Verbosity 1 (`--verbose` 또는 `-v`)
<!-- [ja] -->
### Verbosity 1 (`--verbose` または `-v`)
<!-- [en] -->
### Verbosity 1 (`--verbose` or `-v`)
<!-- [fr] -->
### Verbosity 1 (`--verbose` ou `-v`)
<!-- [common] -->

<!-- [ko] -->
Verbosity가 1이면, 태그 개수가 추가로 출력됩니다. 이를 통해, 빠트린 태그나 오타의 유무를 빠르게 확인할 수 있습니다.
<!-- [ja] -->
Verbosity が 1 なら、タグの数が追加で出力されます。これによって、抜けたタグやタイプミスの有無を素早く確認することができます。
<!-- [en] -->
If the verbosity is 1, the number of tags is output additionally. This allows you to quickly check for missing tags or typos.
<!-- [fr] -->
Si la verbosité est 1, le nombre de balises est également affiché. Cela vous permet de vérifier rapidement les balises manquantes ou les fautes de frappe.
<!-- [common] -->

```sh
$ mmg -r -v
----------------------
 ❌ bad_md.base.md
    3 language(s) not translated.
    Tag count: {'A': 4, 'B': 2, 'C': 2, '<Unknown>': 1}
 ✅ good_md.base.md
    Tag count: {'A': 3, 'B': 3, 'C': 3}
 ❌ bad_jupyter.base.ipynb
    1 language(s) not translated.
    Tag count: {'en-US': 2, 'fr-FR': 2, 'ko-KR': 2, 'ja-JP': 2, '<Unknown>': 1}
----------------------
 => 3 base files were found.
    Do you want to convert these files? [y/N]
```

<!-- [ko] -->
### Verbosity 2 (`--verbose --verbose` 또는 `-vv`)
<!-- [ja] -->
### Verbosity 2 (`--verbose --verbose` または `-vv`)
<!-- [en] -->
### Verbosity 2 (`--verbose --verbose` or `-vv`)
<!-- [fr] -->
### Verbosity 2 (`--verbose --verbose` ou `-vv`)
<!-- [common] -->

<!-- [ko] -->
Verbosity를 2로 설정하면, 구체적으로 몇 번째 줄이 어떤 이유로 검사를 통과하지 못했는지 알 수 있습니다.
특히, jupyter notebook의 경우, 어떤 셀의 어떤 줄이 검사를 통과하지 못했는지 알 수 있기 때문에, 렌더링된 셀을 하나하나 확인할 필요가 없습니다.
<!-- [ja] -->
Verbosity を 2 に設定すると、具体的に何行目がどの理由で検証に合格しなかったかを知ることができます。
特に、jupyter notebook の場合、どのセルのどの行が検証に合格しなかったかを知ることができるため、レンダリングされたセルを一つ一つ確認する必要がありません。
<!-- [en] -->
If you set the verbosity to 2, you can find out exactly which line failed the validation for what reason.
In particular, in the case of jupyter notebook, you can find out which line of which cell failed the validation, so you don't have to check each rendered cell.
<!-- [fr] -->
Si vous réglez la verbosité sur 2, vous pouvez savoir exactement quelle ligne a échoué la validation pour quelle raison.
En particulier, dans le cas du cahier jupyter, vous pouvez savoir quelle ligne de quelle cellule a échoué la validation, vous n’avez donc pas à vérifier chaque cellule rendue.
<!-- [common] -->

```sh
$ mmg -r -vv
----------------------
 ❌ bad_md.base.md
    3 language(s) not translated.
    Tag count: {'A': 4, 'B': 2, 'C': 2, '<Unknown>': 1}
        Config: no_suffix 'en-US' is not in lang_tags.
        Line 10: Unknown tag 'D' detected.
        Line 12: 'common' appeared before all tags appeared once.
        Line 18: 'A' appeared again before all tags appeared once.
        Line 22: 'common' appeared before all tags appeared once.
        Line 28: 'common' appeared before all tags appeared once.
        Line 34: 'common' appeared before all tags appeared once.
 ✅ good_md.base.md
    Tag count: {'A': 3, 'B': 3, 'C': 3}
 ❌ bad_jupyter.base.ipynb
    1 language(s) not translated.
    Tag count: {'en-US': 2, 'fr-FR': 2, 'ko-KR': 2, 'ja-JP': 2, '<Unknown>': 1}
        Cell 4, Line 3: Unknown tag 'English' detected.
----------------------
 => 3 base files were found.
    Do you want to convert these files? [y/N]
```

<!-- [ko] -->
## 유효성 검사 건너뛰기
<!-- [ja] -->
## 検証をスキップする
<!-- [en] -->
## Skip validation
<!-- [fr] -->
## Ignorer la validation
<!-- [common] -->

<!-- [ko] -->
`-s` 또는 `--skip-validation` 옵션을 사용하면, 유효성 검사를 건너뛸 수 있습니다.
이때, markdown 파일은 📄로 표시되고, jupyter notebook 파일은 📒로 표시됩니다.
<!-- [ja] -->
`-s` または `--skip-validation` オプションを使うと、検証をスキップすることができます。
このとき、markdown ファイルは 📄 で表示され、jupyter notebook ファイルは 📒 で表示されます。
<!-- [en] -->
You can skip validation by using the `-s` or `--skip-validation` option.
In this case, markdown files are displayed as 📄 and jupyter notebook files are displayed as 📒.
<!-- [fr] -->
Vous pouvez ignorer la validation en utilisant l’option `-s` ou `--skip-validation`.
Dans ce cas, les fichiers markdown sont affichés comme 📄 et les fichiers jupyter notebook sont affichés comme 📒.
<!-- [common] -->

```sh
$ mmg -r -s
----------------------
 📄 bad.base.md
 📄 good.base.md
 📒 sample_jupyter.base.ipynb
----------------------
 => 3 base files were found.
    Do you want to convert these files? [y/N]
```

<!-- [ko] -->
## CI/CD를 위한 유효성 검사 only 모드 (파일 생성 비활성화)
<!-- [ja] -->
## CI/CD のための検証 only モード (ファイル生成無効化)
<!-- [en] -->
## Validation only mode for CI/CD (file creation disabled)
<!-- [fr] -->
## Mode de validation uniquement pour CI/CD (création de fichiers désactivée)
<!-- [common] -->

!!! quote ""

<!-- [ko] -->
    v2.0.0부터 추가된 기능입니다.
<!-- [ja] -->
    v2.0.0 から使える機能です。
<!-- [en] -->
    This feature is available from v2.0.0.
<!-- [fr] -->
    Cette fonctionnalité est disponible à partir de la v2.0.0.
<!-- [common] -->

<!-- [ko] -->
이 모드는 유효성 검사만 수행하고, 변환된 파일을 생성하지 않습니다.
이 모드는 CI/CD를 위해 만들어졌기 때문에, 검사를 통과하지 못하면 `sys.exit(1)`을 호출합니다.
검사를 통과하면 `sys.exit(0)`을 호출합니다.
이를 이용하여, 유효성 검사의 결과에 따라 CI/CD 파이프라인의 분기를 나눌 수 있습니다.
<!-- [ja] -->
このモードは検証のみを行い、変換されたファイルを生成しません。
このモードは CI/CD のために作られたため、検証に合格しない場合は `sys.exit(1)` を呼び出します。
検証に合格すると `sys.exit(0)` を呼び出します。
これを利用して、検証の結果によって CI/CD パイプラインの分岐を分けることができます。
<!-- [en] -->
This mode only performs validation and does not generate converted files.
It calls `sys.exit(1)` if it fails the validation because it was created for CI/CD.
It calls `sys.exit(0)` if it passes the validation.
This can be used to branch the CI/CD pipeline depending on the results of the validation.
<!-- [fr] -->
Ce mode ne fait que valider et ne génère pas de fichiers convertis.
Il appelle `sys.exit(1)` s’il échoue à la validation car il a été créé pour CI/CD.
Il appelle `sys.exit(0)` s’il réussit la validation.
Cela peut être utilisé pour diviser le pipeline CI/CD en fonction des résultats de la validation.
<!-- [common] -->

```sh
mmg -r --validation-only
----------------------
 ❌ bad_md.base.md
 ✅ good_md.base.md
 ❌ bad_jupyter.base.ipynb
----------------------
 => 3 base files were found.
 => Some files are unhealthy.
```

<!-- [ko] -->
Verbosity 설정을 통해, 검사를 통과하지 못한 이유도 CI/CD 로그에 남길 수 있습니다.
<!-- [ja] -->
Verbosity 設定を通じて、検証に合格しない理由も CI/CD ログに残すことができます。
<!-- [en] -->
Through the verbosity setting, you can also leave the reason for failing the validation in the CI/CD log.
<!-- [fr] -->
Grâce au réglage de la verbosité, vous pouvez également laisser la raison de l’échec de la validation dans le journal CI/CD.
<!-- [common] -->

```sh
$ mmg -r --validation-only -vv
----------------------
 ❌ bad_md.base.md
    3 language(s) not translated.
    Tag count: {'A': 4, 'B': 2, 'C': 2, '<Unknown>': 1}
        Config: no_suffix 'en-US' is not in lang_tags.
        Line 10: Unknown tag 'D' detected.
        Line 12: 'common' appeared before all tags appeared once.
        Line 18: 'A' appeared again before all tags appeared once.
        Line 22: 'common' appeared before all tags appeared once.
        Line 28: 'common' appeared before all tags appeared once.
        Line 34: 'common' appeared before all tags appeared once.
 ✅ good_md.base.md
    Tag count: {'A': 3, 'B': 3, 'C': 3}
 ❌ bad_jupyter.base.ipynb
    1 language(s) not translated.
    Tag count: {'en-US': 2, 'fr-FR': 2, 'ko-KR': 2, 'ja-JP': 2, '<Unknown>': 1}
        Cell 4, Line 3: Unknown tag 'English' detected.
----------------------
 => 3 base files were found.
 => Some files are unhealthy.
```
