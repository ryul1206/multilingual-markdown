<!---------------------------->
<!-- multilingual suffix: en, fr, ko, ja -->
<!---------------------------->
<!-- [en] -->
# Installation
<!-- [fr] -->
# Installation
<!-- [ko] -->
# 설치
<!-- [ja] -->
# 設置
<!-- [common] -->

!!! note ""

<!-- [en] -->
    English |
    [**Français**](site:/fr/getting-started/installation) |
    [**한국어**](site:/ko/getting-started/installation) |
    [**日本語**](site:/ja/getting-started/installation)
<!-- [fr] -->
    [**English**](site:/getting-started/installation) |
    Français |
    [**한국어**](site:/ko/getting-started/installation) |
    [**日本語**](site:/ja/getting-started/installation)
<!-- [ko] -->
    [**English**](site:/getting-started/installation) |
    [**Français**](site:/fr/getting-started/installation) |
    한국어 |
    [**日本語**](site:/ja/getting-started/installation)
<!-- [ja] -->
    [**English**](site:/getting-started/installation) |
    [**Français**](site:/fr/getting-started/installation) |
    [**한국어**](site:/ko/getting-started/installation) |
    日本語
<!-- [common] -->

## Linux

```sh
pip3 install mmg
```

<!-- [en] -->
If you want to generate PDFs with mmg, make sure to install with the `pdf` option:
<!-- [fr] -->
Si vous souhaitez générer des PDF avec mmg, installez-le avec l’option `pdf` :
<!-- [ko] -->
만약 mmg로 PDF를 생성할 거라면 `pdf` 옵션을 줘서 설치해야 합니다.
<!-- [ja] -->
mmgでPDFを生成する場合は、`pdf`オプションを付けてインストールしてください。
<!-- [common] -->

```sh
pip3 install mmg[pdf]
```

## macOS

```sh
pip3 install mmg
```

<!-- [en] -->
If you want to generate PDFs with mmg, make sure to install with the `pdf` option:
<!-- [fr] -->
Si vous souhaitez générer des PDF avec mmg, installez-le avec l’option `pdf` :
<!-- [ko] -->
만약 mmg로 PDF를 생성할 거라면 `pdf` 옵션을 줘서 설치해야 합니다.
<!-- [ja] -->
mmgでPDFを生成する場合は、`pdf`オプションを付けてインストールしてください。
<!-- [common] -->

```sh
pip3 install mmg[pdf]
```

<!-- [en] -->
If you have any issues with [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#macos), install it with the following command. WeasyPrint is only used to create PDFs.
<!-- [fr] -->
Si vous rencontrez des problèmes avec [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#macos), installez-le avec la commande suivante. WeasyPrint est uniquement utilisé pour créer des PDF.
<!-- [ko] -->
만약 [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#macos)와 관련된 문제가 발생한다면, 아래 명령어으로 설치해주세요. WeasyPrint는 PDF를 생성할 때에만 사용됩니다.
<!-- [ja] -->
[WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#macos)で問題が発生した場合は、次のコマンドでインストールしてください。WeasyPrintはPDFの作成にのみ使用されます。
<!-- [common] -->

```sh
brew install weasyprint
```

## Windows

<!-- [en] -->
Python is not installed by default on Windows. Please install Python first, then install MMG using the Python package manager pip.
<!-- [fr] -->
Python n'est pas installé par défaut sur Windows. Veuillez d'abord installer Python, puis installez MMG à l'aide du gestionnaire de paquets Python pip.
<!-- [ko] -->
윈도우에는 파이썬이 기본으로 설치되어 있지 않습니다. 파이썬을 설치한 후 파이썬 패키지 관리자 pip로 MMG를 설치해주세요.
<!-- [ja] -->
WindowsにはPythonがデフォルトでインストールされていません。Pythonをインストールした後、PythonパッケージマネージャーpipでMMGをインストールしてください。
<!-- [common] -->

```powershell
pip3 install mmg
```

<!-- [en] -->
If you installed Python from the [Microsoft Store](https://apps.microsoft.com/), you may see the following warning when installing MMG. (The displayed path may vary for each user.)
<!-- [fr] -->
Si vous avez installé Python depuis le [Microsoft Store](https://apps.microsoft.com/), vous pouvez voir l'avertissement suivant lors de l'installation de MMG. (Le chemin affiché peut varier selon l'utilisateur.)
<!-- [ko] -->
[Microsoft Store](https://apps.microsoft.com/)에서 파이썬을 설치했다면, MMG 설치 시 다음과 같은 경고가 나타날 수 있습니다. (표시되는 경로는 사용자마다 다를 수 있습니다.)
<!-- [ja] -->
[Microsoft Store](https://apps.microsoft.com/)からPythonをインストールした場合、MMGのインストール時に次の警告が表示される場合があります。（表示されるパスはユーザーごとに異なる場合があります。）
<!-- [common] -->

```powershell
$ pip3 install mmg
...
  WARNING: The script mmg.exe is installed in 'C:\Users\...\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed mmg-2.0.1
```

<!-- [en] -->
If you see this warning, it means the `mmg` command cannot be found in the terminal. Please add the path shown in the warning message to the `PATH` environment variable. Instructions for adding to PATH can be found in the [Troubleshooting](https://mmg.ryul1206.dev/2.0/misc/troubleshooting/) documentation.
<!-- [fr] -->
Si vous voyez cet avertissement, cela signifie que la commande `mmg` ne peut pas être trouvée dans le terminal. Veuillez ajouter le chemin indiqué dans le message d'avertissement à la variable d'environnement `PATH`. Les instructions pour ajouter au PATH se trouvent dans la documentation [Dépannage](https://mmg.ryul1206.dev/2.0/fr/misc/troubleshooting/).
<!-- [ko] -->
이 경고가 나타나면, 터미널에서 `mmg` 명령어를 찾지 못하는 상태입니다. 경고 문구에 안내된 경로를 환경변수 `PATH`에 추가해주세요. 추가하는 방법은 [문제 해결](https://mmg.ryul1206.dev/2.0/ko/misc/troubleshooting/) 문서에 적어두었습니다.
<!-- [ja] -->
この警告が表示された場合、ターミナルで`mmg`コマンドが見つからない状態です。警告メッセージに表示されているパスを環境変数`PATH`に追加してください。追加方法は[トラブルシューティング](https://mmg.ryul1206.dev/2.0/ja/misc/troubleshooting/)ドキュメントに記載されています。
<!-- [common] -->

<!-- [en] -->
If you want to generate PDFs with mmg, make sure to install with the `pdf` option:
<!-- [fr] -->
Si vous souhaitez générer des PDF avec mmg, installez-le avec l’option `pdf` :
<!-- [ko] -->
만약 mmg로 PDF를 생성할 거라면 `pdf` 옵션을 줘서 설치해야 합니다.
<!-- [ja] -->
mmgでPDFを生成する場合は、`pdf`オプションを付けてインストールしてください。
<!-- [common] -->

```sh
pip3 install mmg[pdf]
```

<!-- [en] -->
Additionally, MMG uses [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows) to create PDFs. WeasyPrint requires the GTK library, so download and run the latest [GTK3 installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases). **If you are not interested in creating PDFs, you can skip this step.** Other features of MMG are available without GTK.
<!-- [fr] -->
En plus, MMG utilise [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows) pour créer des PDF. WeasyPrint nécessite la bibliothèque GTK, alors téléchargez et exécutez le dernier [installateur GTK3](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases). **Si vous n'êtes pas intéressé par la création de PDF, vous pouvez ignorer cette étape.** Les autres fonctionnalités de MMG sont disponibles sans GTK.
<!-- [ko] -->
추가적으로, MMG는 [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)를 사용하여 PDF를 생성합니다. WeasyPrint는 GTK 라이브러리가 있어야 작동하므로, 최신 [GTK3 설치 파일](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)을 다운로드하고 실행하세요. **PDF 생성 기능을 사용하지 않는다면 이 단계을 건너뛰어도 됩니다.** GTK가 없더라도 MMG의 다른 기능들은 정상적으로 쓸 수 있습니다.
<!-- [ja] -->
追加的に、MMGは[WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)を使用してPDFを作成します。WeasyPrintはGTKライブラリが必要なので、最新の[GTK3インストーラー](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)をダウンロードして実行します。**PDFを作成することに興味がない場合は、このステップをスキップできます。** GTKがなくても、MMGの他の機能は使用できます。
<!-- [common] -->

## Unstable Version (dev branch)

<!-- [en] -->
!!! example "The dev branch is unstable and may not work properly."

    The dev branch is used to test experimental features or fix bugs before releasing a new version.
    Also, the API may change without notice before the release of a new major version.
    Therefore, the dev branch is unstable and may not work properly, and execution is not guaranteed.
    For general use, please use the [official release version](https://github.com/ryul1206/multilingual-markdown/releases).
<!-- [fr] -->
!!! example "La branche dev est instable et peut ne pas fonctionner correctement."

    La branche dev est utilisée pour tester les fonctionnalités expérimentales ou corriger les bugs avant la sortie d'une nouvelle version.
    De plus, l'API peut changer sans préavis avant la sortie d'une nouvelle version majeure.
    Par conséquent, la branche dev est instable et peut ne pas fonctionner correctement, et l'exécution n'est pas garantie.
    Pour une utilisation générale, veuillez utiliser la [version officielle](https://github.com/ryul1206/multilingual-markdown/releases).
<!-- [ko] -->
!!! example "dev 브랜치는 불안정하며 제대로 작동하지 않을 수 있습니다."

    dev 브랜치는 새로운 버전을 출시하기 전에 실험적인 기능을 테스트하거나 버그를 수정하는 데 사용됩니다.
    뿐만 아니라, 새로운 major 버전의 출시 전에는 예고 없이 API가 변경될 수 있습니다.
    따라서 dev 브랜치는 불안정하며 제대로 작동하지 않을 수 있고, 실행을 보장하지 않습니다.
    일반적인 사용을 위해서는 [정식 릴리즈 버전](https://github.com/ryul1206/multilingual-markdown/releases)을 사용해주세요.
<!-- [ja] -->
!!! example "devブランチは不安定で正常に動作しない場合があります。"

    devブランチは、新しいバージョンをリリースする前に実験的な機能をテストしたり、バグを修正したりするために使用されます。
    また、新しいメジャーバージョンをリリースする前にAPIが予告なく変更される場合があります。
    したがって、devブランチは不安定で正常に動作せず、実行は保証されません。
    一般的な使用には、[公式リリースバージョン](https://github.com/ryul1206/multilingual-markdown/releases)を使用してください。
<!-- [common] -->

<!-- [en] -->
The dev branch can be installed with the following command. Please refer to the [unstable version documentation](https://mmg.ryul1206.dev/unstable/) for the documentation of the dev branch. **The documentation for the unstable version may change at any time and may not match the code in the actual dev branch.**
<!-- [fr] -->
La branche dev peut être installée avec la commande suivante. Veuillez vous référer à la [documentation de la version instable](https://mmg.ryul1206.dev/unstable/fr/) pour la documentation de la branche dev. **La documentation de la version instable peut changer à tout moment et peut ne pas correspondre au code de la branche dev réelle.**
<!-- [ko] -->
다음 명령어를 사용하면 dev 브랜치를 설치할 수 있습니다. dev 브랜치의 문서는 [unstable 버전의 문서](https://mmg.ryul1206.dev/unstable/ko/)를 참고해주세요. **unstable 버전의 문서는 언제든지 변경될 수 있으며, 실제 dev 브랜치의 코드와 불일치할 수 있습니다.**
<!-- [ja] -->
devブランチは次のコマンドでインストールできます。devブランチのドキュメントについては、[不安定なバージョンのドキュメント](https://mmg.ryul1206.dev/unstable/ja/)を参照してください。**不安定なバージョンのドキュメントは、いつでも変更される可能性があり、実際のdevブランチのコードと一致しない場合があります。**
<!-- [common] -->

```sh
pip install git+https://github.com/ryul1206/multilingual-markdown.git@dev
```
