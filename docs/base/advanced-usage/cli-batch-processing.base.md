<!---------------------------->
<!-- multilingual suffix: en, fr, ko, ja -->
<!---------------------------->
<!-- [en] -->
# Batch Processing with YAML File
<!-- [fr] -->
# Traitement par lots avec Fichier YAML
<!-- [ko] -->
# YAML 파일을 사용한 일괄 처리
<!-- [ja] -->
# YAML ファイルを使用したバッチ処理
<!-- [common] -->

!!! note ""

<!-- [en] -->
    English |
    [**Français**](site:/fr/advanced-usage/cli-batch-processing) |
    [**한국어**](site:/ko/advanced-usage/cli-batch-processing) |
    [**日本語**](site:/ja/advanced-usage/cli-batch-processing)
<!-- [fr] -->
    [**English**](site:/advanced-usage/cli-batch-processing) |
    Français |
    [**한국어**](site:/ko/advanced-usage/cli-batch-processing) |
    [**日本語**](site:/ja/advanced-usage/cli-batch-processing)
<!-- [ko] -->
    [**English**](site:/advanced-usage/cli-batch-processing) |
    [**Français**](site:/fr/advanced-usage/cli-batch-processing) |
    한국어 |
    [**日本語**](site:/ja/advanced-usage/cli-batch-processing)
<!-- [ja] -->
    [**English**](site:/advanced-usage/cli-batch-processing) |
    [**Français**](site:/fr/advanced-usage/cli-batch-processing) |
    [**한국어**](site:/ko/advanced-usage/cli-batch-processing) |
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
YAML 파일에는 보다 복잡한 MMG 작업을 정의할 수 있습니다.
<!-- [ja] -->
YAML ファイルにはより複雑な MMG の処理を定義できます。
<!-- [en] -->
You can define more complex MMG operations in YAML files.
<!-- [fr] -->
Vous pouvez définir des opérations MMG plus complexes dans des fichiers YAML.
<!-- [common] -->

<!-- [ko] -->
- 지정된 폴더에 로그 파일을 남길 수 있습니다.
- 사용자 정의 태그를 파일의 접미사로 사용하지 않고, 폴더 이름으로 사용할 수 있습니다. 예를 들어, `foo.en.md`와 `foo.fr.md` 대신, `en/foo.md`와 `fr/foo.md`를 생성할 수 있습니다.
- 생성될 파일의 디렉토리를 지정할 수 있습니다.
<!-- [ja] -->
- 指定したフォルダにログファイルを残せます。
- ユーザー定義タグをファイルの接尾辞ではなく、フォルダ名として使えます。例えば、`foo.en.md` と `foo.fr.md` の代わりに、`en/foo.md` と `fr/foo.md` を生成できます。
- 生成されるファイルのディレクトリを指定できます。
<!-- [en] -->
- You can leave log files in the specified folder.
- You can use user-defined tags as folder names instead of file suffixes. For example, you can generate `en/foo.md` and `fr/foo.md` instead of `foo.en.md` and `foo.fr.md`.
- You can specify the directory of the generated file.
<!-- [fr] -->
- Vous pouvez laisser des fichiers journaux dans le dossier spécifié.
- Vous pouvez utiliser des tags définis par l'utilisateur comme noms de dossier au lieu des suffixes de fichier. Par exemple, vous pouvez générer `en/foo.md` et `fr/foo.md` au lieu de `foo.en.md` et `foo.fr.md`.
- Vous pouvez spécifier le répertoire du fichier généré.
<!-- [common] -->

<!-- [ko] -->
지금 보고 계신 페이지도 `mmg.yaml`을 사용하여 [MkDocs static i18n plugin](https://github.com/ultrabug/mkdocs-static-i18n)이 인식할 수 있는 형식으로 변환되었습니다.
<!-- [ja] -->
今ご覧のページも `mmg.yaml` を使用して [MkDocs static i18n plugin](https://github.com/ultrabug/mkdocs-static-i18n) が認識できる形式に変換されました。
<!-- [en] -->
This page you are viewing now has also been converted to a format that can be recognized by [MkDocs static i18n plugin](https://github.com/ultrabug/mkdocs-static-i18n) using `mmg.yaml`.
<!-- [fr] -->
Cette page que vous consultez maintenant a également été convertie dans un format pouvant être reconnu par [MkDocs static i18n plugin](https://github.com/ultrabug/mkdocs-static-i18n) en utilisant `mmg.yaml`.
<!-- [common] -->

<!-- [ko] -->
## 사용법
<!-- [ja] -->
## 使い方
<!-- [en] -->
## Usage
<!-- [fr] -->
## Utilisation
<!-- [common] -->

<!-- [ko] -->
작업을 정의한 파일이 `my_first_job.yaml`라면, 다음과 같이 실행할 수 있습니다.
<!-- [ja] -->
作業を定義したファイルが `my_first_job.yaml` なら、次のように実行できます。
<!-- [en] -->
If you define a job in a file named `my_first_job.yaml`, you can run it as follows.
<!-- [fr] -->
Si vous définissez un travail dans un fichier nommé `my_first_job.yaml`, vous pouvez l'exécuter comme suit.
<!-- [common] -->

```sh
mmg -b my_first_job.yaml
```

<!-- [ko] -->
## YAML 파일 예제
<!-- [ja] -->
## YAML ファイルの例
<!-- [en] -->
## YAML File Example
<!-- [fr] -->
## Exemple de fichier YAML
<!-- [common] -->

`my_first_job.yaml`:

```yaml
convert_without_ask: true
# If false (default), ask for confirmation before converting.
# If true, it is same as `mmg ** --yes`.`

verbose: 2
# 0: quiet(default), 1: normal, 2: verbose

log_dir: "logs"
# Log files will be placed in this folder.
# If the folder does not exist, error will occur.
# If comment out, log files will not be generated.

# The `tags_as` can be "folder" or "suffix"
#   - "folder" is for the folder docs structure.
#   - "suffix" is for the suffix docs structure
# Please refer to the following link for details.
# https://ultrabug.github.io/mkdocs-static-i18n/getting-started/quick-start/

jobs:
  - name: "MkDocs pages"        # Job name (optional)
    tag_as: "folder"            # "folder" or "suffix" (required)
    source: "docs/base"         # Source folder containing the files to convert (required)
    recursive: true             # If true, recursively search for files in subfolders (default: true)
    output_dir: "docs"          # Generated files will be placed in this folder (required)

  - name: "README.md"           # Job name (optional)
    tag_as: "suffix"            # "folder" or "suffix" (required)
    source: "README.base.md"    # Source file to convert (required)
    output_dir: "./"            # Generated file will be placed in this folder (required)
```

<!-- [ko] -->
## 옵션 무시 및 강제 적용
<!-- [ja] -->
## オプションの強制適用
<!-- [en] -->
## Force Option Override
<!-- [fr] -->
## Forcer la substitution d’option
<!-- [common] -->

!!! quote ""

<!-- [en] -->
    This feature is available from v2.1.0.
<!-- [fr] -->
    Cette fonctionnalité est disponible à partir de la v2.1.0.
<!-- [ko] -->
    v2.1.0부터 추가된 기능입니다.
<!-- [ja] -->
    v2.1.0 から使える機能です。
<!-- [common] -->

<!-- [ko] -->
명령어 실행 시 `--yes` 옵션을 추가하면, YAML 파일에서 `convert_without_ask`가 `false`로 설정되어 있어도 실제로는 `true`인 것처럼 동작합니다.
<!-- [ja] -->
コマンド実行時に `--yes` オプションを追加すると、YAML ファイルで `convert_without_ask` が `false` に設定されていても、実質的に `true` として動作します。
<!-- [en] -->
When you add the `--yes` option at the command line, the tool always behaves as if `convert_without_ask` is set to `true` in the YAML file, even when it is set to `false`.
<!-- [fr] -->
Lorsque vous exécutez la commande avec l’option `--yes`, l’outil se comporte toujours comme si `convert_without_ask` était défini sur `true` dans le fichier YAML, même si sa valeur est `false`.
<!-- [common] -->

```sh
mmg -b my_first_job.yaml --yes
```
