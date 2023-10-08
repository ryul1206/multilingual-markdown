<!---------------------------->
<!-- multilingual suffix: en, fr, ko, ja -->
<!---------------------------->
<!-- [en] -->
# Using Juptyer Notebook
<!-- [fr] -->
# Utilisation de Juptyer Notebook
<!-- [ko] -->
# Juptyer Notebook 사용하기
<!-- [ja] -->
# Jupyter Notebook 使用する
<!-- [common] -->

!!! note ""

<!-- [en] -->
    English |
    [**Français**](/fr/advanced-usage/cli-jupyter-notebook) |
    [**한국어**](/ko/advanced-usage/cli-jupyter-notebook) |
    [**日本語**](/ja/advanced-usage/cli-jupyter-notebook)
<!-- [fr] -->
    [**English**](/advanced-usage/cli-jupyter-notebook) |
    Français |
    [**한국어**](/ko/advanced-usage/cli-jupyter-notebook) |
    [**日本語**](/ja/advanced-usage/cli-jupyter-notebook)
<!-- [ko] -->
    [**English**](/advanced-usage/cli-jupyter-notebook) |
    [**Français**](/fr/advanced-usage/cli-jupyter-notebook) |
    한국어 |
    [**日本語**](/ja/advanced-usage/cli-jupyter-notebook)
<!-- [ja] -->
    [**English**](/advanced-usage/cli-jupyter-notebook) |
    [**Français**](/fr/advanced-usage/cli-jupyter-notebook) |
    [**한국어**](/ko/advanced-usage/cli-jupyter-notebook) |
    日本語
<!-- [common] -->

!!! quote ""

<!-- [en] -->
    This feature is available from v2.0.0.
<!-- [fr] -->
    Cette fonctionnalité est disponible à partir de la v2.0.0.
<!-- [ko] -->
    v2.0.0부터 추가된 기능입니다.
<!-- [ja] -->
    v2.0.0 から使える機能です。
<!-- [common] -->

<!-- [ko] -->
- Jupyter notebook 파일도 markdown 파일과 동일하게 MMG의 모든 기능을 사용할 수 있습니다.
- Markdown 파일과 마찬가지로 jupyter notebook 파일도 `*.base.ipynb` 파일을 만들어야 합니다.
- MMG는 jupyter notebook에서 markdown cell만 추출하여 헤더와 키워드를 인식합니다.
- 헤더는 cell과 상관없이 notebook 파일 전체에서 하나만 있어야 합니다.
- 모든 code cell은 `common`의 code block으로 간주됩니다.
<!-- [ja] -->
- Jupyter Notebook ファイルも markdown ファイルと同じように MMG の全ての機能を使えます。
- Markdown ファイルと同じように jupyter notebook ファイルも `*.base.ipynb` ファイルを作らなければなりません。
- MMG は jupyter notebook から markdown cell のみを抽出してヘッダーとキーワードを認識します。
- ヘッダーは cell と関係なく notebook ファイル全体で一つだけ存在しなければなりません。
- 全ての code cell は `common` の code block として扱われます。
<!-- [en] -->
- Jupyter notebook files can use all the features of MMG just like markdown files.
- Just like markdown files, jupyter notebook files must also create a `*.base.ipynb` file.
- MMG extracts only markdown cells from jupyter notebook and recognizes headers and keywords.
- There must be only one header in the entire notebook file, regardless of the cell.
- All code cells are treated as `common` code blocks.
<!-- [fr] -->
- Les fichiers Jupyter notebook peuvent utiliser toutes les fonctionnalités de MMG comme les fichiers markdown.
- Tout comme les fichiers markdown, les fichiers jupyter notebook doivent également créer un fichier `*.base.ipynb`.
- MMG extrait uniquement les cellules markdown du jupyter notebook et reconnaît les en-têtes et les mots-clés.
- Il ne doit y avoir qu'un seul en-tête dans l'ensemble du fichier notebook, indépendamment de la cellule.
- Toutes les cellules de code sont traitées comme des blocs de code `common`.
<!-- [common] -->

<!-- [ko] -->
GitHub 저장소에 있는 `sample_jupyter.base.ipynb`으로 테스트해보세요. (파일 경로: [./examples/cli-examples/sample_jupyter.base.ipynb](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/cli-examples))
<!-- [ja] -->
GitHub のリポジトリにある `sample_jupyter.base.ipynb` でテストしてください。 (ファイルパス: [./examples/cli-examples/sample_jupyter.base.ipynb](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/cli-examples))
<!-- [en] -->
Test it with `sample_jupyter.base.ipynb` in the GitHub repository. (File path: [./examples/cli-examples/sample_jupyter.base.ipynb](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/cli-examples))
<!-- [fr] -->
Testez-le avec `sample_jupyter.base.ipynb` dans le dépôt GitHub. (Chemin du fichier: [./examples/cli-examples/sample_jupyter.base.ipynb](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/cli-examples))
<!-- [common] -->

```sh
$ mmg .\sample_jupyter.base.ipynb -vv
----------------------
 ✅ sample_jupyter.base.ipynb
    Tag count: {'en-US': 3, 'fr-FR': 3, 'ko-KR': 3, 'ja-JP': 3}
----------------------
 => 1 base file was found.
    Do you want to convert these files? [y/N]
```
