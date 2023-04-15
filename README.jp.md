# 多言語マークダウンジェネレータ

このパッケージは、単一のデフォルトのファイルから多言語コンテンツを管理してi18nマークダウンを生成するコマンドラインインタフェース（CLI）を提供しています。

[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/ryul1206/multilingual-markdown/badge)](https://www.codefactor.io/repository/github/ryul1206/multilingual-markdown)

🚀 **version 1.0.3**
🌏
[**English**](https://github.com/ryul1206/multilingual-markdown/blob/master/README.md) |
[**Français**](https://github.com/ryul1206/multilingual-markdown/blob/master/README.fr.md) |
[**한국어**](https://github.com/ryul1206/multilingual-markdown/blob/master/README.kr.md) |
日本語

Bash, Zsh, WindowsPowerShellで使用できます。

---

**目次** ⚡

1. [概要 ](#概要-)
    1. [作動方式](#作動方式)
    1. [技能](#技能)
1. [設置](#設置)
    1. ["コマンドが見つかりません"エラーを修正する方法](#コマンドが見つかりませんエラーを修正する方法)
1. [アップデート](#アップデート)
1. [削除](#削除)
1. [使用方法](#使用方法)
    1. [（0）ベースマークダウンファイル作成](#（0）ベースマークダウンファイル作成)
    1. [（1）ファイルを指定](#（1）ファイルを指定)
    1. [（2）再帰オプション（recursive option）](#（2）再帰オプション（recursive-option）)
    1. [（4）より多くの説明](#（4）より多くの説明)
1. [コマンドタグ](#コマンドタグ)
    1. [ヘッダ](#ヘッダ)
    1. [バッジ付け](#バッジ付け)
    1. [本文](#本文)
1. [貢献](#貢献)
    1. [開発のためのlocalに構築する方法](#開発のためのlocalに構築する方法)
    1. [Changelog](#Changelog)
    1. [Contributors](#Contributors)

## 概要 🔎

### 作動方式
![how it works](how-it-works.png)

### 技能

- ファイル名の後に自動接尾辞
  - [IETF言語タグ](https://ja.wikipedia.org/wiki/IETF%E8%A8%80%E8%AA%9E%E3%82%BF%E3%82%B0) 使用可能
  - 接尾辞省略オプション(1ヶ国語のみ)
- UTF-8エンコード。 ですので、*たぶん*ほぼすべての言語をサポートします。 :) 🍷
- 自動目次
    - 目次で作成するタイトルレベル設定可能
    - 目次で絵文字を **"表示/省略"** 設定可能

## 設置

```sh
pip3 install mmg --user
```

これで、新ターミナルを開けると新しいコマンド「mmg」が使えます。

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

### "コマンドが見つかりません"エラーを修正する方法

**Ubuntu Bash/Zsh**

- 原因:`mmg`コマンドがインストールされる'$HOME/.local/bin'経路が'PATH'に含まれていないと発生します。
- 解決:`/.bashrc`または`/.zshrc`ファイルを開き、`PATH`に`$HOME/.local/bin`を追加します。
    ```
    export PATH="$HOME/.local/bin:$PATH"
    ```

**Windows PowerShell**

以下に説明した順にPSモジュールを作成すると、問題を解決することができます。

1. PowerShellで`$env:PSModulePath`コマンドを使えばPSModule経路を確認することができる。ここのリポジトリのPSmmgフォルダをPSModuleの一つに貼り付けます。例えば、`C:\ProgramFiles\WindowsPowerShell\Modules\PSmmg\PSmmg.psm1`が必要です。
2. PowerShellを管理者モードで実行し、実行ポリシーを変更します。
    ```
    Set-ExecutionPolicy RemoteSigned
    ```
3. PowerShellを再起動すると、`mmg`命令を書くことができます。

**OSにこだわらない代案**

```
python -m mmgcli [options]
```

## アップデート

```sh
pip3 install mmg --upgrade --user
```

## 削除

```sh
pip3 uninstall mmg
```

## 使用方法

### （0）ベースマークダウンファイル作成

`{ファイル名}.base.md`ファイルを作成します。例では、[README.base.md](README.base.md)と[example.base.md](example/example.base.md)を参照し、作成するルールは、[コマンドタグ](#コマンドタグ)を参照してください。

**（警告）ベースのファイル形式が間違っている場合生成されたスタイルが壊れます。**

### （1）ファイルを指定

多言語で作成したい`*.base.md`ファイルを`mmg`コマンド引数（arguments）で入れてくれます。

```sh
mmg FileName.base.md
```

複数の引数は、間隔で区切ります。

```sh
mmg Foo.base.md Bar.base.md Baz.base.md
```

### （2）再帰オプション（recursive option）

現在のディレクトリおよびサブディレクトリにあるすべてのデータベースファイルを変換したい場合は`--recursive`、または`-r`オプションを使用します。recursive optionはコマンドが入力された位置を基準にすべてのサブフォルダを移動します。まだ引数としてフォルダを指定することができません。

```sh
mmg --recursive
```

###（3）データベースファイルの検証

問題があると疑われる場合。（通常は緑色で、異常は赤で表示されます。）

- Verbosity 0
    ```text
    $ mmg -r
    ----------------------
    ✅ .\README.base.md
    ❌ .\example\example.base.md
    ----------------------
    => 2 base markdowns were found.
        Your verbosity is 0. Try the `--verbose` option for more details.
    Do you want to convert these files? [y/N]
    ```
- Verbosity 1 (`--verbose`)
    ```text
    $ mmg -r -v
    ----------------------
    ✅ .\README.base.md
        Tag count: {'en': 37, 'fr': 37, 'kr': 37}
    ❌ .\example\example.base.md
        4 language(s) not translated.
        Tag count: {'en-US': 4, 'fr-FR': 4, 'ko-KR': 5, 'ja-JP': 4, '<Unknown>': 1}
    ----------------------
    => 2 base markdowns were found.
    Do you want to convert these files? [y/N]
    ```
- Verbosity 2
    ```text
    $ mmg -r -vv
    ----------------------
    ✅ .\README.base.md
        Tag count: {'en': 37, 'fr': 37, 'kr': 37}
    ❌ .\example\example.base.md
        4 language(s) not translated.
        Tag count: {'en-US': 4, 'fr-FR': 4, 'ko-KR': 5, 'ja-JP': 4, '<Unknown>': 1}
            Line 28: This language reappeared before all languages appeared once.
            Line 36: A common area appeared before all languages come out.
            Line 57: Unknown suffix detected.
            Line 59: This language reappeared before all languages appeared once.
    ----------------------
    => 2 base markdowns were found.
    Do you want to convert these files? [y/N]
    ```

問題がなければ、

```text
$ mmg -r --verbose
----------------------
✅ .\README.base.md
    Tag count: {'en': 37, 'fr': 37, 'kr': 37}
✅ .\example\example.base.md
    Tag count: {'en-US': 4, 'fr-FR': 4, 'ko-KR': 4, 'ja-JP': 4}i
----------------------
=> 2 base markdowns were found.
    Your verbosity is 0. Try the `--verbose` option for more details.
Do you want to convert these files? [y/N]
```

### （4）より多くの説明

- 各フォルダの同じ場所で`{ファイル名}.{接尾辞}.md`になったファイルを見ることができます。例えば：
  - 基本のとき：`{ファイル名}.en.md`、`{ファイル名}.kr.md`、`{ファイル名}.es.md`、...
  - `en`サフィックス省略オプションのとき：`{ファイル名}.md`、`{ファイル名}.kr.md`、`{ファイル名}.es.md`、...
- このジェネレータは、自動生成されたファイルを毎回上書きされるため、`{ファイル名}.base.md`ファイルを変更しても、毎回消去する必要がありません。ただ先ほどステップ2を再度実行します。

## コマンドタグ

### ヘッダ

ヘッダは、必ず本体を開始する前に宣言する必要があります。

1. **サフィックス宣言**

    使用する言語を宣言します。次の例では、enとkrをキーワードで宣言しました。このキーワードは、接尾辞として使用されます。

    ```markdown
    <!-- multilingual suffix: en, kr, fr, es, jp, cn -->
    ```

1. **サフィックスを非表示**（必須ではない）

    `no suffix`オプションは、ファイルを作成するときにサフィックスがつくのを防ぐことができます。言い換えればno suffixをenに設定すると、`ファイル名.en.md`ではなく、`ファイル名.md`が生成されます。**GitHub**からメイン`README`はサフィックスが付く認識にならないので、この機能が便利です。

    ```markdown
    <!-- no suffix: en -->
    ```

### バッジ付け

[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-yellow.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-green.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-blue.svg)](https://github.com/ryul1206/multilingual-markdown)
...

```markdown
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
```

### 本文

パーサが下のタグ立ち寄る読む瞬間から、その後に読むすべてはメインテキストとして認識します。（だからヘッダをメインの前に書かなければならいます。）

1. **キーワード**
    1. 言語分類

        言語を区別するタグは、`<!-- [キーワード] -->`同じ形で作成します。一つのキーワードが認識されると、他のキーワードが表示されるまで、そのキーワードとして認識されます。

        ```markdown
        <!-- [en] -->
        <!-- [kr] -->
        <!-- [fr] -->
        <!-- [es] -->
        <!-- [jp] -->
        <!-- [cn] -->
        ...
        ```

    1. 共通領域

        生成されるすべてのファイルに共通に入る内容は`common`、キーワードを使用して作成します。

        ```markdown
        <!-- [common] -->
        ```

    1. 無視される領域

        コメントやTODOなどのいくつかの項目は、生成されるファイルに含ましたくない場合があります。そのような場合`ignore`、キーワードを使用します。

        ```markdown
        <!-- [ignore] -->
        ```

1. **目次**

    次のタグは、ジェネレータによって本文に自動的に置き換えられます。目次のレベルは、`level`部分を介してすることができます。最大のタイトル（`# 題目`）はhtmlで`<h1>`あるため`level 1`です。

    **（注意）`#`に表示するマークダウンの見出しレベルをスキップエラーが発生します。つまり、`##`サブタイトルは`###`でなければします。**

    ```markdown
    <!-- [[ multilingual toc: level=2~3 ]] -->
    ```

    1. **`level`オプション**
        - `level`を表記する方法は、合計4つあります。お客様のニーズに応じて、数字は変えたらされます。
            - `level=2`：2レベルの見出しのみ目次にします。
            - `level=2~`：2〜9レベルの見出しのみ目次にします。
            - `level=~4`：1〜4レベルの見出しのみ目次にします。
            - `level=2~4`：2〜4レベルの見出しのみ目次にします。
        - 1つの記事で`table of contents`タグは何度も書くことができ、毎回異なる`level`オプションを与えることもできます。
        - **注意💥**：もし`level`を省略すると、パーサが認識しない。
        - **注意💥**：目次タグは、自動的に現在のキーワードを`common`変更します。だから目次タグも暗黙的に`common`に属します。
    2. **`no-emoji`オプション**
        - セクションのタイトルには、絵文字を入れながら、目次では、絵文字を消したいときがあります。😱 もしあなたがこのような状況であれば、以下のように`no-emoji`オプションを適用します。😎

        ```markdown
        <!-- [[ multilingual toc: level=2~3 no-emoji ]] -->
        ```

## 貢献

翻訳、単純な改善、バグ情報提供などいかなるものでも大切に受けます。

### 開発のためのlocalに構築する方法

- Linux and MacOS
  - Required packages: `pip3 install -r requirements_dev.txt --user`
  - Install: `python3 setup.py install --user --record temp.txt`
  - Usage: `mmg [OPTIONS] [FILENAMES]...`
  - Uninstall: `xargs rm -rf < temp.txt`
- Windows
  - Required packages: `pip3 install -r .\requirements_dev.txt --user`
  - Install: `python3 setup.py install --user --record temp.txt`
  - Usage: `python3 -m mmgcli [OPTIONS] [FILENAMES]...`
  - Uninstall (PowerShell): `python3 -m pip uninstall mmg`

### [Changelog](https://github.com/ryul1206/multilingual-markdown/blob/develop/CHANGELOG.md)

### Contributors

> 貢献リストは英語のみで提供されます。

- [@bkg2018 (Francis Piérot)](https://github.com/bkg2018): Added french translation to README and example. [PR #1](https://github.com/ryul1206/multilingual-markdown/pull/1)
- [@mathben (Mathieu Benoit)](https://github.com/mathben): Update README pip installation with requirements.txt [PR #2](https://github.com/ryul1206/multilingual-markdown/pull/2)
