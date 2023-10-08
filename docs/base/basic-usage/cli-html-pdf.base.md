<!---------------------------->
<!-- multilingual suffix: en, fr, ko, ja -->
<!---------------------------->
<!-- [en] -->
# HTML, PDF Output
<!-- [fr] -->
# Sortie HTML, PDF
<!-- [ko] -->
# HTML, PDF 출력
<!-- [ja] -->
# HTML, PDF 出力
<!-- [common] -->

!!! note ""

<!-- [en] -->
    English |
    [**Français**](/fr/basic-usage/cli-html-pdf) |
    [**한국어**](/ko/basic-usage/cli-html-pdf) |
    [**日本語**](/ja/basic-usage/cli-html-pdf)
<!-- [fr] -->
    [**English**](/basic-usage/cli-html-pdf) |
    Français |
    [**한국어**](/ko/basic-usage/cli-html-pdf) |
    [**日本語**](/ja/basic-usage/cli-html-pdf)
<!-- [ko] -->
    [**English**](/basic-usage/cli-html-pdf) |
    [**Français**](/fr/basic-usage/cli-html-pdf) |
    한국어 |
    [**日本語**](/ja/basic-usage/cli-html-pdf)
<!-- [ja] -->
    [**English**](/basic-usage/cli-html-pdf) |
    [**Français**](/fr/basic-usage/cli-html-pdf) |
    [**한국어**](/ko/basic-usage/cli-html-pdf) |
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

<!-- [en] -->
MMG supports HTML and PDF output. You can specify it using the `--output-format` or `-o` option.
<!-- [fr] -->
MMG prend en charge la sortie HTML et PDF. Vous pouvez le spécifier en utilisant l'option `--output-format` ou `-o`.
<!-- [ko] -->
MMG는 HTML, PDF 출력을 지원합니다. `--output-format` 또는 `-o` 옵션을 사용하여 지정할 수 있습니다.
<!-- [ja] -->
MMG は HTML と PDF の出力をサポートしています。`--output-format` または `-o` オプションで指定できます。
<!-- [common] -->

<!-- [en] -->
- `--output-format html`: HTML output
- `--output-format pdf`: PDF output
- `--output-format as-is`: Output in the same format as the original file (default)
<!-- [fr] -->
- `--output-format html`: Sortie HTML
- `--output-format pdf`: Sortie PDF
- `--output-format as-is`: Sortie dans le même format que le fichier d'origine (par défaut)
<!-- [ko] -->
- `--output-format html`: HTML 출력
- `--output-format pdf`: PDF 출력
- `--output-format as-is`: 원본 파일과 같은 형식으로 출력 (기본값)
<!-- [ja] -->
- `--output-format html`: HTML 出力
- `--output-format pdf`: PDF 出力
- `--output-format as-is`: 元のファイルと同じ形式で出力 (デフォルト)
<!-- [common] -->

```sh
mmg foo.md --output-format pdf
```

<!-- [en] -->
You can also use it with the [recursive option](/basic-usage/cli-recursive-option), and you can specify the style of HTML and PDF by adding the `--css` option.
For easy styling, two themes, `github-light` and `github-dark`, are provided by default.
<!-- [fr] -->
Vous pouvez également l'utiliser avec l'[option récursive](/fr/basic-usage/cli-recursive-option), et vous pouvez spécifier le style de HTML et PDF en ajoutant l'option `--css`.
Pour un style facile, deux thèmes, `github-light` et `github-dark`, sont fournis par défaut.
<!-- [ko] -->
뿐만 아니라, [재귀 옵션](/ko/basic-usage/cli-recursive-option)과 함께 사용할 수도 있고, `--css` 옵션을 추가하여 HTML과 PDF의 스타일을 지정할 수도 있습니다.
스타일을 쉽게 지정할 수 있도록, `github-light`와 `github-dark` 두 가지 테마를 기본으로 제공합니다.
<!-- [ja] -->
[再帰オプション](/ja/basic-usage/cli-recursive-option)とも一緒に使用でき、`--css` オプションを追加することで HTML と PDF のスタイルを指定できます。
簡単にスタイリングするために、`github-light` と `github-dark` の 2 つのテーマがデフォルトで用意されています。
<!-- [common] -->

<!-- [en] -->
- `--css github-light`: GitHub Light style (default)
- `--css github-dark`: GitHub Dark style
- `--css YOUR_CSS_FILE.css`: Custom CSS file
<!-- [fr] -->
- `--css github-light`: Style GitHub Light (par défaut)
- `--css github-dark`: Style GitHub Dark
- `--css YOUR_CSS_FILE.css`: Fichier CSS personnalisé
<!-- [ko] -->
- `--css github-light`: GitHub Light 스타일 (기본값)
- `--css github-dark`: GitHub Dark 스타일
- `--css YOUR_CSS_FILE.css`: 사용자 정의 CSS 파일
<!-- [ja] -->
- `--css github-light`: GitHub Light スタイル (デフォルト)
- `--css github-dark`: GitHub Dark スタイル
- `--css YOUR_CSS_FILE.css`: カスタム CSS ファイル
<!-- [common] -->

```sh
mmg -r -o pdf --css github-dark
```

<!-- [en] -->
To generate HTMLs, MMG uses the [markdown package](https://github.com/Python-Markdown/markdown) for markdown files and the [nbconvert package](https://github.com/jupyter/nbconvert) for jupyter notebook files.
And when generating PDFs, it first converts to HTML and then converts to PDF.
<!-- [fr] -->
Pour générer des HTML, MMG utilise le [package markdown](https://github.com/Python-Markdown/markdown) pour les fichiers markdown et le [package nbconvert](https://github.com/jupyter/nbconvert) pour les fichiers jupyter notebook.
Et lors de la génération de PDF, il convertit d'abord en HTML puis en PDF.
<!-- [ko] -->
MMG는 HTML을 생성할 때, markdown 파일에는 [markdown 패키지](https://github.com/Python-Markdown/markdown)를 사용하고, jupyter notebook 파일에는 [nbconvert 패키지](https://github.com/jupyter/nbconvert)를 사용합니다.
그리고 PDF를 생성하는 경우에도 우선 HTML로 변환한 후 PDF로 변환합니다.
<!-- [ja] -->
MMG は HTML を生成するとき、markdown ファイルには [markdown パッケージ](https://github.com/Python-Markdown/markdown)を使用し、jupyter notebook ファイルには [nbconvert パッケージ](https://github.com/jupyter/nbconvert)を使用します。
そして PDF を生成する場合も、まず HTML に変換してから PDF に変換します。
<!-- [common] -->

<!-- [en] -->
Therefore, if you want to include HTML tags in markdown, you need to add the `markdown` attribute to the HTML tag as follows so that the [markdown package](https://github.com/Python-Markdown/markdown) can work properly.
See [Markdown in HTML Extension](https://python-markdown.github.io/extensions/md_in_html/) for details.
<!-- [fr] -->
Par conséquent, si vous souhaitez inclure des balises HTML dans le markdown, vous devez ajouter l'attribut `markdown` à la balise HTML comme suit afin que le [package markdown](https://github.com/Python-Markdown/markdown) puisse fonctionner correctement.
Voir [Markdown in HTML Extension](https://python-markdown.github.io/extensions/md_in_html/) pour plus de détails.
<!-- [ko] -->
그러므로 만약 markdown에 HTML 태그를 포함하고자 하는 경우, [markdown 패키지](https://github.com/Python-Markdown/markdown)가 제대로 동작할 수 있도록 다음과 같이 HTML 태그에 `markdown` 속성을 추가해야 합니다.
자세한 내용은 [Markdown in HTML 확장](https://python-markdown.github.io/extensions/md_in_html/)을 참고하세요.
<!-- [ja] -->
そのため、markdown に HTML タグを含めたい場合、[markdown パッケージ](https://github.com/Python-Markdown/markdown)が正しく動作するように、次のように HTML タグに `markdown` 属性を追加する必要があります。
詳細は [Markdown in HTML Extension](https://python-markdown.github.io/extensions/md_in_html/) を参照してください。
<!-- [common] -->

```markdown
<div align="center" markdown>
Hello, world!
</div>
```
