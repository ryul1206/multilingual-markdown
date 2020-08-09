# Générateur de Markdown Multilingue

[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown.svg)
![GitHub](https://img.shields.io/github/license/ryul1206/multilingual-markdown.svg)

🚀 **version 0.1**
🌏 [English](README.md), [Français](README.fr.md), [한국어](README.kr.md)

---

**Table des matières** ⚡

1. [Fonctionnement ](#Fonctionnement-)
1. [Fonctionnalités](#Fonctionnalités)
1. [Badges](#Badges)
1. [Mode d'emploi](#Mode-demploi)
1. [Marqueurs](#Marqueurs)
    1. [Titres](#Titres)
    1. [Corps de texte](#Corps-de-texte)
1. [Contributors](#Contributors)
    1. [Contribution](#Contribution)

## Fonctionnement 🔎
![how it works](how-it-works.png)

## Fonctionnalités

- Suffixe automatique des noms de fichier
- Possibilité d'omettre le suffixe (pour la langue principale)
- Encodage UTF-8. Cela *devrait* supporter presque toutes les langues. :) 🍷
- Table des matières automatique
    - Niveaux de titres au choix
    - Emojis en option

## Badges

[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-yellow.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-green.svg)](https://github.com/ryul1206/multilingual-markdown)
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-blue.svg)](https://github.com/ryul1206/multilingual-markdown)
...

```markdown
[![Multilingual Markdown Generator](https://img.shields.io/badge/markdown-multilingual%20🌐-ff69b4.svg)](https://github.com/ryul1206/multilingual-markdown)
```

## Mode d'emploi

1. Saisissez les fichiers multilingues avec une extension `.base.md`. Voir les exemples [README.base.md](README.base.md) et [example.base.md](example/example.base.md) et reportez-vous à [Marqueurs](#marqueurs) pour les règles.
2. Exécutez le script Python `multilang_md.py` à la racine de votre projet : il recherchera tous les Markdown dans les répertoires inférieurs.

  ```bash
  python multilang_md.py
  ```

3. Vous trouverez les fichiers `{quelquechose}.{suffixe}.md` dans le même répertoire que celui de base qui leur correspond. Par example :

    - par défaut : `{quelquechose}.en.md`, `{quelquechose}.kr.md`, `{quelquechose}.fr.md`, ...
    - option no-suffix pour `en`: `{quelquechose}.md`, `{quelquechose}.kr.md`, `{quelquechose}.fr.md`, ...

4. Le générateur écrase les fichiers générés à chaque exécution, il est donc inutile de les supprimer après avoir modifié `{fichier}.base.md`. Reprenez simplement au point 2. Ne modifiez pas les fichiers de chaque langue, les modifications disparaitraient à la prochaine exécution du script.

## Marqueurs

### Titres

Les titres doivent être déclarés avant le corps de texte.

1. **Déclaration des suffixes**

    Déclarez les langues que vous souhaitez utiliser. Dans l'exemple suivant, on déclare les mots-clés `en`, `kr` et `fr` et quelque autres. Ces mots-clés seront utilisés comme suffixes des noms de fichier et comme marqueurs dans les fichiers `base.md`.

    ```markdown
    <!-- multilangual suffix: en, kr, fr, es, jp, cn -->
    ```

1. **Suffixe invisible** (facultatif)

    L'option `no suffix` évite l'ajout de l'un des suffixes lors de la création des fichiers. Ainsi, appliquer `no suffix`à la langue `en` génèrera *`fichier`*`.md` au lieu de *`fichier`*`.en.md`. Cela est utile par exemple pour le `README` obligatoire dans  **GitHub** qui n sera pas reconnu s'il a un suffixe (par exemple `README.en.md`).

    ```markdown
    <!-- no suffix: en -->
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

    ```markdown
    <!-- [[ multilangual toc: level=2~3 ]] -->
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
        - En de rares occasions, vous pouvez souhaiter mettre un emoji dans un titre sans qu'il apparaisse dans la table des matières 😱. dans ce cas, utilisez l'option `no-emoji` comme indiqué ci-dessous 😎

        ```markdown
        <!-- [[ multilangual toc: level=2~3 no-emoji ]] -->
        ```

## Contributors

> La liste des contributeurs est en Anglais seulement.

- [Francis Piérot](https://github.com/bkg2018) - French translation ([fr])

### Contribution

Toute contribution sera grandement appréciée. (ex: traductions, améliorations, signalements de bugs etc.)

> Je serai particulièrement reconnaissant si vous pouviez traduire ce `README.md` dans votre langue et me l'envoyer.

