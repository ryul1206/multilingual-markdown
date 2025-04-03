<!---------------------------->
<!-- multilingual suffix: en, fr, ko, ja -->
<!---------------------------->
<!-- [en] -->
# Troubleshooting
<!-- [fr] -->
# Dépannage
<!-- [ko] -->
# 문제 해결
<!-- [ja] -->
# トラブルシューティング
<!-- [common] -->

!!! note ""

<!-- [en] -->
    English |
    [**Français**](site:/fr/misc/troubleshooting) |
    [**한국어**](site:/ko/misc/troubleshooting) |
    [**日本語**](site:/ja/misc/troubleshooting)
<!-- [fr] -->
    [**English**](site:/misc/troubleshooting) |
    Français |
    [**한국어**](site:/ko/misc/troubleshooting) |
    [**日本語**](site:/ja/misc/troubleshooting)
<!-- [ko] -->
    [**English**](site:/misc/troubleshooting) |
    [**Français**](site:/fr/misc/troubleshooting) |
    한국어 |
    [**日本語**](site:/ja/misc/troubleshooting)
<!-- [ja] -->
    [**English**](site:/misc/troubleshooting) |
    [**Français**](site:/fr/misc/troubleshooting) |
    [**한국어**](site:/ko/misc/troubleshooting) |
    日本語
<!-- [common] -->

<!-- [en] -->
This page describes solutions to known issues.
<!-- [fr] -->
Cette page décrit les solutions aux problèmes connus.
<!-- [ko] -->
이 페이지에서는 알려진 문제들에 대한 해결 방법을 설명합니다.
<!-- [ja] -->
このページでは、既知の問題の解決策について説明します。
<!-- [common] -->

<!-- [en] -->
## Cannot find `mmg` command in Windows
<!-- [fr] -->
## Impossible de trouver la commande `mmg` sous Windows
<!-- [ko] -->
## Windows에서 `mmg` 명령어를 찾지 못하는 문제
<!-- [ja] -->
## Windowsで`mmg`コマンドが見つからない問題
<!-- [common] -->

```powershell
$ pip3 install mmg
...
  WARNING: The script mmg.exe is installed in 'C:\Users\...\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed mmg-2.0.1
```

<!-- [en] -->
This warning appears because the path to `mmg.exe` installed by pip is not registered in the environment variable `PATH`.
To resolve this, first press the Windows key to open the search box and search for "advanced system settings" and click it.
<!-- [fr] -->
Cet avertissement apparaît car le chemin vers `mmg.exe` installé par pip n'est pas enregistré dans la variable d'environnement `PATH`.
Pour résoudre ce problème, appuyez d'abord sur la touche Windows pour ouvrir la zone de recherche, recherchez "advanced system settings" et cliquez dessus.
<!-- [ko] -->
위와 같은 경고가 나타나는 것은 pip로 설치된 `mmg.exe`의 경로가 환경변수 `PATH`에 등록되지 않아서입니다.
해결하려면 먼저 윈도우키를 눌러 검색창을 열고 "advanced system settings"를 검색해 클릭해주세요.
<!-- [ja] -->
この警告は、pipでインストールされた`mmg.exe`のパスが環境変数`PATH`に登録されていないために表示されます。
解決するには、まずWindowsキーを押して検索ボックスを開き、"advanced system settings"を検索してクリックしてください。
<!-- [common] -->

<div align="center">
   <img src="site:/assets/windows-path-solution1.jpg" width="600" alt="Windows Path Solution 1" />
</div>

<!-- [en] -->
Then click the "Environment Variables" button in the bottom right.
<!-- [fr] -->
Ensuite, cliquez sur le bouton "Variables d'environnement" en bas à droite.
<!-- [ko] -->
그런 다음 오른쪽 아래에 있는 "환경 변수" 버튼을 클릭하세요.
<!-- [ja] -->
次に、右下にある「環境変数」ボタンをクリックしてください。
<!-- [common] -->

<div align="center">
   <img src="site:/assets/windows-path-solution2.jpg" width="450" alt="Windows Path Solution 2" />
</div>

<!-- [en] -->
Select the `PATH` variable as shown in the image below and click the "Edit" button. Click the "New" button to add the path shown in the warning message. **The path may be different for each user, so make sure to add your own path.**
Click "OK" in all windows to complete the setup.
<!-- [fr] -->
Sélectionnez la variable `PATH` comme indiqué dans l'image ci-dessous et cliquez sur le bouton "Modifier". Cliquez sur le bouton "Nouveau" pour ajouter le chemin indiqué dans le message d'avertissement. **Le chemin peut être différent pour chaque utilisateur, assurez-vous donc d'ajouter votre propre chemin.**
Cliquez sur "OK" dans toutes les fenêtres pour terminer la configuration.
<!-- [ko] -->
아래 그림과 같이 `PATH` 변수를 선택하고 "편집" 버튼을 클릭합니다. "새로 만들기" 버튼을 클릭하여 경고 메시지에 나온 경로를 추가해주세요. **경로는 사용자마다 다를 수 있으니 반드시 본인의 경로를 추가하셔야 합니다.**
모든 창에서 "확인" 버튼을 클릭하여 설정을 완료합니다.
<!-- [ja] -->
下の画像のように`PATH`変数を選択し、「編集」ボタンをクリックします。「新規」ボタンをクリックして、警告メッセージに表示されたパスを追加してください。**パスはユーザーごとに異なる場合がありますので、必ず自分のパスを追加してください。**
すべてのウィンドウで「OK」をクリックして設定を完了します。
<!-- [common] -->

<div align="center">
   <img src="site:/assets/windows-path-solution3.jpg" width="800" alt="Windows Path Solution 3" />
</div>

<!-- [en] -->
Now that the path has been added to the `PATH` variable, you can open the command prompt and use the `mmg` command.
<!-- [fr] -->
Maintenant que le chemin a été ajouté à la variable `PATH`, vous pouvez ouvrir l'invite de commande et utiliser la commande `mmg`.
<!-- [ko] -->
이제 `PATH` 변수에 경로가 추가되었으니 명령어 프롬프트를 열어서 `mmg` 명령어를 사용할 수 있습니다.
<!-- [ja] -->
これで`PATH`変数にパスが追加されたので、コマンドプロンプトを開いて`mmg`コマンドを使用できます。
<!-- [common] -->

<!-- [en] -->
## WeasyPrint cannot import external libraries
<!-- [fr] -->
## WeasyPrint ne peut pas importer des bibliothèques externes
<!-- [ko] -->
## WeasyPrint가 외부 라이브러리를 불러오지 못하는 문제
<!-- [ja] -->
## WeasyPrintは外部ライブラリをインポートできません
<!-- [common] -->

<!-- [en] -->
**Symptom**: When you enter the `mmg` command in Windows PowerShell, the following error occurs.
<!-- [fr] -->
**Symptôme**: Lorsque vous entrez la commande `mmg` dans Windows PowerShell, l'erreur suivante se produit.
<!-- [ko] -->
**증상**: Windows PowerShell에서 `mmg` 명령어를 입력하면 다음과 같은 오류가 발생합니다.
<!-- [ja] -->
**症状**: Windows PowerShellで`mmg`コマンドを入力すると、次のエラーが発生します。
<!-- [common] -->

```powershell
PS D:\> mmg --version

-----

WeasyPrint could not import some external libraries. Please carefully follow the installation steps before reporting an issue:
https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation
https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#troubleshooting

-----

Traceback (most recent call last):
  .....
OSError: cannot load library '.....': .....
```

<!-- [en] -->
**Cause**: This is a problem that occurs when GTK is not properly installed on Windows. This can also occur if you install GTK before installing Python.
<!-- [fr] -->
**Cause**: Il s'agit d'un problème qui se produit lorsque GTK n'est pas correctement installé sur Windows. Cela peut également se produire si vous installez GTK avant d'installer Python.
<!-- [ko] -->
**원인**: Windows에 GTK가 제대로 설치되어 있지 않아서 발생하는 문제입니다. Python을 설치하기 전에 GTK를 설치한 경우에도 발생할 수 있습니다.
<!-- [ja] -->
**原因**: これは、WindowsにGTKが正しくインストールされていないと発生する問題です。これは、Pythonをインストールする前にGTKをインストールした場合にも発生する可能性があります。
<!-- [common] -->

<!-- [en] -->
**Solution**: Download and install the latest [GTK3 installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases).
<!-- [fr] -->
**Solution**: Téléchargez et installez le dernier [GTK3 installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases).
<!-- [ko] -->
**해결 방법**: 최신 [GTK3 설치 파일](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)을 다운로드하여 설치합니다.
<!-- [ja] -->
**解決策**: 最新の[GTK3インストーラー](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)をダウンロードしてインストールします。
<!-- [common] -->

<!-- [en] -->
**Reference**: [WeasyPrint > First steps > Installation > Windows](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)
<!-- [fr] -->
**Référence**: [WeasyPrint > First steps > Installation > Windows](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)
<!-- [ko] -->
**참고**: [WeasyPrint > First steps > Installation > Windows](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)
<!-- [ja] -->
**参考**: [WeasyPrint > First steps > Installation > Windows](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)
<!-- [common] -->

<!-- [en] -->
## GLib-GIO-WARNING warning is output on Windows
<!-- [fr] -->
## Avertissement GLib-GIO-WARNING est affiché sur Windows
<!-- [ko] -->
## Windows에서 GLib-GIO-WARNING 경고가 출력됨
<!-- [ja] -->
## WindowsでGLib-GIO-WARNING警告が出力される
<!-- [common] -->

<!-- [en] -->
**Symptom**: When you use `mmg` in Windows PowerShell, the following warning is output.
<!-- [fr] -->
**Symptôme**: Lorsque vous utilisez `mmg` dans Windows PowerShell, l'avertissement suivant est affiché.
<!-- [ko] -->
**증상**: Windows PowerShell에서 `mmg`를 사용하면 다음과 같은 경고가 출력됩니다.
<!-- [ja] -->
**症状**: Windows PowerShellで`mmg`を使用すると、次の警告が出力されます。
<!-- [common] -->

```powershell
GLib-GIO-WARNING **: 13:19:49.232: Unexpectedly, UWP app `*******.*******_0.0.00.0_****__************' (AUMId `*******.*******_************!App') supports 00 extensions but has no verbs
```

<!-- [en] -->
This warning message does not affect the operation of MMG, so you can ignore it.
<!-- [fr] -->
Ce message d'avertissement n'affecte pas le fonctionnement de MMG, vous pouvez donc l'ignorer.
<!-- [ko] -->
이 경고 메시지는 MMG의 작동에 영향을 주지 않으므로, 무시해도 됩니다.
<!-- [ja] -->
この警告メッセージはMMGの動作に影響を与えないため、無視しても構いません。
<!-- [common] -->

<!-- [en] -->
**Solution**: Remove or reinstall the Windows app mentioned in the warning message from [Microsoft Store](https://apps.microsoft.com/).

For example, remove or reinstall the `Clipchamp` app in the following case.
<!-- [fr] -->
**Solution**: Supprimez ou réinstallez l'application Windows mentionnée dans le message d'avertissement depuis [Microsoft Store](https://apps.microsoft.com/).

Par exemple, supprimez ou réinstallez l'application `Clipchamp` dans le cas suivant.
<!-- [ko] -->
**해결 방법**: 경고 메시지에 언급된 Windows 앱을 제거하거나 [Microsoft Store](https://apps.microsoft.com/)에서 재설치합니다.

예를 들어, 다음과 같은 경우에는 `Clipchamp` 앱을 제거하거나 재설치합니다.
<!-- [ja] -->
**解決策**: 警告メッセージに記載されているWindowsアプリを[Microsoft Store](https://apps.microsoft.com/)から削除または再インストールします。

例えば、次の場合は`Clipchamp`アプリを削除または再インストールします。
<!-- [common] -->

```powershell
GLib-GIO-WARNING **: 13:19:49.232: Unexpectedly, UWP app `Clipchamp.Clipchamp_2.7.10.0_neutral__yxz26nhyzhsrt' (AUMId `Clipchamp.Clipchamp_yxz26nhyzhsrt!App') supports 41 extensions but has no verbs
```

<!-- [en] -->
**Reference**: [https://stackoverflow.com/a/71053742/17167856](https://stackoverflow.com/a/71053742/17167856)
<!-- [fr] -->
**Référence**: [https://stackoverflow.com/a/71053742/17167856](https://stackoverflow.com/a/71053742/17167856)
<!-- [ko] -->
**참고**: [https://stackoverflow.com/a/71053742/17167856](https://stackoverflow.com/a/71053742/17167856)
<!-- [ja] -->
**参考**: [https://stackoverflow.com/a/71053742/17167856](https://stackoverflow.com/a/71053742/17167856)
<!-- [common] -->

<!-- [en] -->
## Markdown files are not converted properly when HTML tags are included
<!-- [fr] -->
## Les fichiers Markdown ne sont pas convertis correctement lorsque des balises HTML sont incluses
<!-- [ko] -->
## Markdown에 HTML 태그가 포함된 경우, HTML 또는 PDF 변환이 제대로 되지 않음
<!-- [ja] -->
## MarkdownにHTMLタグが含まれている場合、HTMLまたはPDF変換が正しく行われない
<!-- [common] -->

<!-- [en] -->
To generate HTMLs, MMG uses the [markdown package](https://github.com/Python-Markdown/markdown) for markdown files.
And when generating PDFs, it first converts to HTML and then converts to PDF.
<!-- [fr] -->
Pour générer des HTML, MMG utilise le [package markdown](https://github.com/Python-Markdown/markdown) pour les fichiers markdown.
Et lors de la génération de PDF, il convertit d'abord en HTML puis en PDF.
<!-- [ko] -->
MMG는 HTML을 생성할 때, markdown 파일에는 [markdown 패키지](https://github.com/Python-Markdown/markdown)를 사용합니다.
그리고 PDF를 생성하는 경우에도 우선 HTML로 변환한 후 PDF로 변환합니다.
<!-- [ja] -->
MMG は HTML を生成するとき、markdown ファイルには [markdown パッケージ](https://github.com/Python-Markdown/markdown)を使用します。
そして PDF を生成する場合も、まず HTML に変換してから PDF に変換します。
<!-- [common] -->

<!-- [en] -->
However, when markdown contains HTML tags, it may not be converted properly in the following cases.
The reason for this is that the [markdown package](https://github.com/Python-Markdown/markdown) requires the syntax described in [Markdown in HTML Extension](https://python-markdown.github.io/extensions/md_in_html).
<!-- [fr] -->
Cependant, lorsque le markdown contient des balises HTML, il peut ne pas être converti correctement dans les cas suivants.
La raison en est que le [package markdown](https://github.com/Python-Markdown/markdown) nécessite la syntaxe décrite dans [Markdown in HTML Extension](https://python-markdown.github.io/extensions/md_in_html).
<!-- [ko] -->
따라서 markdown에 HTML 태그가 포함될 때, 아래의 경우에는 제대로 변환이 되지 않을 수 있습니다.
제대로 변환되지 않는 이유는 [markdown 패키지](https://github.com/Python-Markdown/markdown)의 [Markdown in HTML 확장](https://python-markdown.github.io/extensions/md_in_html/)에서 요구하는 문법을 지키지 않았기 때문입니다.
<!-- [ja] -->
しかし、markdown に HTML タグが含まれている場合、次の場合には正しく変換されないことがあります。
これは、[markdown パッケージ](https://github.com/Python-Markdown/markdown)が [Markdown in HTML Extension](https://python-markdown.github.io/extensions/md_in_html) で記述されている構文を要求しているためです。
<!-- [common] -->

```markdown
<div align="center">
Hello, world!
</div>
```

<!-- [en] -->
After you fix it as follows, it will be converted properly.
<!-- [fr] -->
Après l'avoir corrigé comme suit, il sera converti correctement.
<!-- [ko] -->
이를 다음과 같이 고치면 제대로 변환이 됩니다.
<!-- [ja] -->
次のように修正すると、正しく変換されます。
<!-- [common] -->

```markdown
<div align="center" markdown>
Hello, world!
</div>
```
