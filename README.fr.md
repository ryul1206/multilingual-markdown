# Générateur de Markdown Multilingue

Ce package fournit une interface de ligne de commande pour gérer les contenus multilingues et générer des démarques i18n à partir d'un seul fichier de base.

[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/ryul1206/multilingual-markdown/badge)](https://www.codefactor.io/repository/github/ryul1206/multilingual-markdown)

🚀 **version 1.0.3**
🌏
[**English**](https://github.com/ryul1206/multilingual-markdown/blob/master/README.md) |
Français |
[**한국어**](https://github.com/ryul1206/multilingual-markdown/blob/master/README.kr.md) |
[**日本語**](https://github.com/ryul1206/multilingual-markdown/blob/master/README.jp.md)

Disponible dans Bash, Zsh et Windows PowerShell.

---

**Table des matières** ⚡

1. [Aperçu ](#Aperçu-)
    1. [Fonctionnement](#Fonctionnement)
    1. [Fonctionnalités](#Fonctionnalités)
1. [Installer](#Installer)
    1. [Comment corriger une erreur "Commande introuvable"](#Comment-corriger-une-erreur-Commande-introuvable)
1. [Mises à jour](#Mises-à-jour)
1. [Désinstaller](#Désinstaller)
1. [Mode d'emploi](#Mode-demploi)
    1. [(0) Créer un fichier de démarques de base](#0-Créer-un-fichier-de-démarques-de-base)
    1. [(1) Spécification du fichier cible](#1-Spécification-du-fichier-cible)
    1. [(2) Option Récursive](#2-Option-Récursive)
    1. [(3) Validation du Fichier de Base](#3-Validation-du-Fichier-de-Base)
    1. [(4) Plus d'explications](#4-Plus-dexplications)
1. [Marqueurs](#Marqueurs)
    1. [Titres](#Titres)
    1. [Badges](#Badges)
    1. [Corps de texte](#Corps-de-texte)
1. [Contribution](#Contribution)
    1. [Comment construire localement pour le développement](#Comment-construire-localement-pour-le-développement)
    1. [Changelog](#Changelog)
    1. [Contributors](#Contributors)

## Aperçu 🔎

### Fonctionnement
![how it works](how-it-works.png)

### Fonctionnalités

- Suffixe automatique des noms de fichier
  - [Étiquette d'identification de langues IETF](https://fr.wikipedia.org/wiki/%C3%89tiquette_d%27identification_de_langues_IETF) ​sont également disponibles
  - Possibilité d'omettre le suffixe (pour la langue principale)
- Encodage UTF-8. Cela *devrait* supporter presque toutes les langues. :) 🍷
- Table des matières automatique
    - Niveaux de titres au choix
    - Emojis en option

## Installer

```sh
pip3 install mmg --user
```

Maintenant, lorsque vous ouvrez un nouveau terminal, vous pouvez utiliser la nouvelle commande `mmg`.

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

### Comment corriger une erreur "Commande introuvable"

**Ubuntu Bash/Zsh**

- Cause : Cette erreur se produit si la variable `PATH` ne contient pas le chemin `$HOME/.local/bin` où la commande `mmg` est installée.
- Solution : Ouvrez le fichier `~/.bashrc` ou `~/.zshrc` et ajoutez `$HOME/.local/bin` à `PATH`.
    ```
    export PATH="$HOME/.local/bin:$PATH"
    ```

**Windows PowerShell**

Vous pouvez résoudre le problème en créant les modules PS dans l'ordre décrit ci-dessous.

1. Vous pouvez vérifier les chemins PSModule en utilisant la commande `$env:PSModulePath` dans PowerShell. Collez le dossier PSmmg de ce référentiel dans l'un des chemins PSModule. Par exemple, `C:\Program Files\WindowsPowerShell\Modules\PSmmg\PSmmg.psm1` doit exister.
2. Exécutez PowerShell en mode administrateur et modifiez la politique d'exécution.
    ```
    Set-ExecutionPolicy RemoteSigned
    ```
3. Redémarrez maintenant PowerShell et vous pouvez utiliser la commande `mmg`.

**Alternative indépendante du système d'exploitation**

```
python -m mmgcli [options]
```

## Mises à jour

```sh
pip3 install mmg --upgrade --user
```

## Désinstaller

```sh
pip3 uninstall mmg
```

## Mode d'emploi

### (0) Créer un fichier de démarques de base

Saisissez les fichiers multilingues avec une extension `.base.md`. Voir les exemples [README.base.md](README.base.md) et [example.base.md](example/example.base.md) et reportez-vous à [Marqueurs](#marqueurs) pour les règles.

**(Remarque) Un format incorrect de fichier de base cassera le style généré.**

### (1) Spécification du fichier cible

Entrez les fichiers `* .base.md` que vous souhaitez créer dans plusieurs langues comme arguments de la commande` mmg`.

```sh
mmg FileName.base.md
```

Les arguments multiples sont séparés par des espaces.

```sh
mmg Foo.base.md Bar.base.md Baz.base.md
```

### (2) Option Récursive

Si vous voulez convertir tous les fichiers de base dans le répertoire courant et les sous-répertoires, utilisez l'option `--recursive` ou` -r`.
L'option récursive recherche tous les sous-dossiers en fonction de l'endroit où la commande est entrée.
Vous ne pouvez pas encore spécifier un dossier comme argument.

```sh
mmg --recursive
```

### (3) Validation du Fichier de Base

Lorsque votre fichier peut avoir un problème.
(Normal est indiqué en vert et anormal en rouge.)

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

Lorsque vos fichiers sont ok.

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

### (4) Plus d'explications

- Vous trouverez les fichiers `{quelquechose}.{suffixe}.md` dans le même répertoire que celui de base qui leur correspond. Par example :
    - Par défaut : `{quelquechose}.en.md`, `{quelquechose}.kr.md`, `{quelquechose}.fr.md`, ...
    - Lorsque option no-suffix pour `en`: `{quelquechose}.md`, `{quelquechose}.kr.md`, `{quelquechose}.fr.md`, ...
- Le générateur écrase les fichiers générés à chaque exécution, il est donc inutile de les supprimer après avoir modifié `{fichier}.base.md`. Reprenez simplement au point 2. Ne modifiez pas les fichiers de chaque langue, les modifications disparaitraient à la prochaine exécution du script.

## Marqueurs

### Titres

Les titres doivent être déclarés avant le corps de texte.

1. **Déclaration des suffixes**

    Déclarez les langues que vous souhaitez utiliser. Dans l'exemple suivant, on déclare les mots-clés `en`, `kr` et `fr` et quelque autres. Ces mots-clés seront utilisés comme suffixes des noms de fichier et comme marqueurs dans les fichiers `base.md`.

    ```markdown
    <!-- multilingual suffix: en, kr, fr, es, jp, cn -->
    ```

1. **Suffixe invisible** (facultatif)

    L'option `no suffix` évite l'ajout de l'un des suffixes lors de la création des fichiers. Ainsi, appliquer `no suffix`à la langue `en` génèrera *`fichier`*`.md` au lieu de *`fichier`*`.en.md`. Cela est utile par exemple pour le `README` obligatoire dans  **GitHub** qui n sera pas reconnu s'il a un suffixe (par exemple `README.en.md`).

    ```markdown
    <!-- no suffix: en -->
    ```

### Badges

[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-yellow.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-green.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-blue.svg)](https://github.com/ryul1206/multilingual-markdown)
...

```markdown
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
```

### Corps de texte

Tout ce qui suit le marqueur est interprété comme corps principal de texte, donc vous devez placer les titres avant le texte.

1. **Mots-clés**
    1. Classification de langue

        Les marqueurs qui distinguent les languages sont écrits sous la forme `<!-- [marqueur] -->`. Si un marqueur est reconnu, il sera retenu jusqu'à ce qu'un autre soit reconnu.

        ```markdown
        <!-- [en] -->
        <!-- [kr] -->
        <!-- [fr] -->
        <!-- [es] -->
        <!-- [jp] -->
        <!-- [cn] -->
        ...
        ```

    1. Section commune

        Vous pouvez utiliser le mot-clé 'common' pour une partie de texte commune à toutes les langues, par exemple pour des illustrations.

        ```markdown
        <!-- [common] -->
        ```

    1. Section ignorée

        Vous pouvez exclure des parties du texte telles que les blocs de commentaires ou les TODO avec le mot-clé `ignore`.

        ```markdown
        <!-- [ignore] -->
        ```

1. **Table des matières**

    Les marqueurs sont automatiquement placés dans la table des matières par le générateur. Le niveau de titre auquel commence la table des matières peut être indiqué avec l'option `level`. Le niveau le plus haut est 1, ce qui correspond aux titres Markdown `# titre` et aux tags HTML `<H1>`.

    **(Remarque) Si vous sautez le niveau de titre de la démarque marquée avec `#`, une erreur se produira. En d'autres termes, le sous-titre de `##` doit être `###`.**

    ```markdown
    <!-- [[ multilingual toc: level=2~3 ]] -->
    ```

    1. **Option `level`**
        - Les niveaux acceptés dans la table des matières par l'option `level` vont de 1 à 9 et sont indiqués avec un niveau de départ et un niveau de fin séparés par une tilde `~`. Si vous ne spécifiez pas le premier numéro, les niveaux commenceront au premier et si vous ne spécifiez pas le second numéro, les niveaux seront pris jusqu'au neuvième. Adaptez les nombres des exemples suivants selon vos besoins.
            - `level=2`: Mettre uniquement le niveau 2 dans la table des matières.
            - `level=2~`: Mettre les niveaux 2 à 9 dans la table des matières.
            - `level=~4`: Mettre les niveaux 1 à 4 dans la table des matières.
            - `level=2~4`: Mettre les niveaux 2 à 4 dans la table des matières..
        - Vous pouvez écrire les marqueurs de la table des matières plusieurs fois dans le document et spécifier différentes options `level` à chaque fois.
        - **ATTENTION💥**: si vous ommettez `level` le script ignorera la commande.
        - **ATTENTION💥**: le marqueur `table of contents` change automatiquement le marqueur de section pour `common` donc les commandes de la table des matières concernent toutes les langues, et vous devez réindiquer un marqueur de langue par la suite.
    2. **Option `no-emoji`**
        - Vous pouvez souhaiter mettre un emoji dans un titre sans qu'il apparaisse dans la table des matières.😱 dans ce cas, utilisez l'option `no-emoji` comme indiqué ci-dessous 😎

        ```markdown
        <!-- [[ multilingual toc: level=2~3 no-emoji ]] -->
        ```

## Contribution

Toute contribution sera grandement appréciée. (ex: traductions, améliorations, signalements de bugs etc.)

### Comment construire localement pour le développement

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

> La liste des contributeurs est en Anglais seulement.

- [@bkg2018 (Francis Piérot)](https://github.com/bkg2018): Added french translation to README and example. [PR #1](https://github.com/ryul1206/multilingual-markdown/pull/1)
- [@mathben (Mathieu Benoit)](https://github.com/mathben): Update README pip installation with requirements.txt [PR #2](https://github.com/ryul1206/multilingual-markdown/pull/2)
