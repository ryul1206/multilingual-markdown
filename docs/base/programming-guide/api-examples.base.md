<!---------------------------->
<!-- multilingual suffix: en, fr, ko, ja -->
<!---------------------------->
<!-- [en] -->
# API Usage Examples
<!-- [fr] -->
# Exemples d'Utilisation de l'API
<!-- [ko] -->
# API 사용 예제
<!-- [ja] -->
# API 使用例
<!-- [common] -->

!!! note ""

<!-- [en] -->
    English |
    [**Français**](site:/fr/programming-guide/api-examples) |
    [**한국어**](site:/ko/programming-guide/api-examples) |
    [**日本語**](site:/ja/programming-guide/api-examples)
<!-- [fr] -->
    [**English**](site:/programming-guide/api-examples) |
    Français |
    [**한국어**](site:/ko/programming-guide/api-examples) |
    [**日本語**](site:/ja/programming-guide/api-examples)
<!-- [ko] -->
    [**English**](site:/programming-guide/api-examples) |
    [**Français**](site:/fr/programming-guide/api-examples) |
    한국어 |
    [**日本語**](site:/ja/programming-guide/api-examples)
<!-- [ja] -->
    [**English**](site:/programming-guide/api-examples) |
    [**Français**](site:/fr/programming-guide/api-examples) |
    [**한국어**](site:/ko/programming-guide/api-examples) |
    日本語
<!-- [common] -->

<!-- [ko] -->
- 모든 예제는 [GitHub](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/api-examples)에서 확인할 수 있습니다.
- 이 페이지에서 사용되는 MMG API의 레퍼런스는 [Python API](site:/ko/programming-guide/python-api)에서 확인할 수 있습니다.
<!-- [ja] -->
- 全ての例は[GitHub](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/api-examples)で確認できます。
- このページで使用されるMMG APIのリファレンスは[Python API](site:/ja/programming-guide/python-api)で確認できます。
<!-- [en] -->
- All examples can be found on [GitHub](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/api-examples).
- The reference of MMG API used in this page can be found in [Python API](site:/programming-guide/python-api).
<!-- [fr] -->
- Tous les exemples peuvent être trouvés sur [GitHub](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/api-examples).
- La référence de l'API MMG utilisée dans cette page peut être trouvée dans [Python API](site:/fr/programming-guide/python-api).
<!-- [common] -->

## api_example_convert_file.py

<!-- [ko] -->
파일을 불러와 변환하는 예제입니다.
<!-- [ja] -->
ファイルを読み込んで変換する例です。
<!-- [en] -->
This example loads a file and converts it.
<!-- [fr] -->
Cet exemple charge un fichier et le convertit.
<!-- [common] -->

See on [GitHub](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/api-examples/api_example_convert_file.py)

```py
from typing import Dict
import os
import mmg.api as mmg


def main():
    # Read a markdown file as a string
    base_file = os.path.join(os.path.dirname(__file__), "./sample.base.md")
    base_file = os.path.abspath(base_file)
    print(f"Reading file: {base_file}")

    with open(base_file, "r", encoding="utf-8") as f:
        base_md: str = f.read()

    # Convert markdown string
    converted_mds: Dict[str, str] = mmg.convert(base_md)
    for tag, txt in converted_mds.items():
        print(f"\n>> Tag: {tag}")
        print(txt)


if __name__ == "__main__":
    main()
```

??? success "Output Text"

    ```txt
    >> Tag: A
    # Heading A

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in ultrices metus, in semper mi.

    Footer here.

    >> Tag: B
    # Heading B

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in ultrices metus, in semper mi.

    Footer here.

    >> Tag: C
    # Heading C

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in ultrices metus, in semper mi.

    Footer here.
    ```

## api_example_convert_string.py

<!-- [ko] -->
Python string을 변환하는 예제입니다.
<!-- [ja] -->
Python stringを変換する例です。
<!-- [en] -->
This example converts a Python string.
<!-- [fr] -->
Cet exemple convertit une chaîne Python.
<!-- [common] -->

See on [GitHub](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/api-examples/api_example_convert_string.py)

```py
from typing import Dict
import mmg.api as mmg

base_md: str = """
<!---------------------------->
<!-- multilingual suffix: A, B, C -->
<!---------------------------->
<!-- [A] -->
# Sample Document A

Hello, A!
<!-- [B] -->
# Sample Document B

Hello, B!
<!-- [C] -->
# Sample Document C

Hello, C!
<!-- [common] -->
Thank you for using mmg!
"""


def main():
    converted_mds: Dict[str, str] = mmg.convert(base_md)
    for tag, txt in converted_mds.items():
        print(f"\n>> Tag: {tag}")
        print(txt)


if __name__ == "__main__":
    main()
```

??? success "Output Text"

    ```txt
    >> Tag: A

    # Sample Document A

    Hello, A!
    Thank you for using mmg!

    >> Tag: B

    # Sample Document B

    Hello, B!
    Thank you for using mmg!

    >> Tag: C

    # Sample Document C

    Hello, C!
    Thank you for using mmg!
    ```

## api_example_convert_with_cfg.py

<!-- [ko] -->
헤더가 없는 Python string을 변환하는 예제입니다
헤더 대신, `Config` 객체를 직접 사용합니다.
<!-- [ja] -->
ヘッダーのないPython stringを変換する例です。
ヘッダーの代わりに、`Config`オブジェクトを直接使用します。
<!-- [en] -->
This example converts a Python string without a header.
Instead of a header, it directly uses a `Config` object.
<!-- [fr] -->
Cet exemple convertit une chaîne Python sans en-tête.
Au lieu d'un en-tête, il utilise directement un objet `Config`.
<!-- [common] -->

See on [GitHub](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/api-examples/api_example_convert_with_cfg.py)

```py
from typing import Dict
import mmg.api as mmg

base_md: str = """
<!-- [A] -->
# Sample Document A

Hello, A!
<!-- [B] -->
# Sample Document B

Hello, B!
<!-- [C] -->
# Sample Document C

Hello, C!
<!-- [common] -->
Thank you for using mmg!
"""


def main():
    cfg = mmg.Config(lang_tags=["A", "B", "C"])
    print(f"Config: {cfg}")

    converted_mds: Dict[str, str] = mmg.convert(base_md, cfg=cfg)
    for tag, txt in converted_mds.items():
        print(f"\n>> Tag: {tag}")
        print(txt)


if __name__ == "__main__":
    main()
```

??? success "Output Text"

    ```txt
    >> Tag: A

    # Sample Document A

    Hello, A!
    Thank you for using mmg!

    >> Tag: B

    # Sample Document B

    Hello, B!
    Thank you for using mmg!

    >> Tag: C

    # Sample Document C

    Hello, C!
    Thank you for using mmg!
    ```

## api_example_create_toc.py

<!-- [ko] -->
목차를 생성하는 예제입니다.
<!-- [ja] -->
目次を生成する例です。
<!-- [en] -->
This example creates a table of contents.
<!-- [fr] -->
Cet exemple crée une table des matières.
<!-- [common] -->

See on [GitHub](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/api-examples/api_example_create_toc.py)

```py
from typing import List
from mmg.utils import REGEX_PATTERN
from mmg.toc import create_toc, parse_toc_options

base_md: str = """
# 🔎 Header 1

Here are some examples of the table of contents.

**Table of Contents with Emoji**

<!-- [[ multilingual toc: level=2~3 ]] -->

**Table of Contents without Emoji**

<!-- [[ multilingual toc: level=2~3 no-emoji ]] -->

## 📝 Header 2

Foo

### 🌈 Header 3

Bar
"""


def main():
    doc = base_md.splitlines()
    for line in doc:
        if REGEX_PATTERN["auto_toc"].match(line):
            toc_options = parse_toc_options(line)
            toc: List[str] = create_toc(toc_options, doc)
            toc: str = "\n".join(toc)
            print(f">> Toc (no-emoji: {toc_options[2]}):\n{toc}\n")


if __name__ == "__main__":
    main()
```

??? success "Output Text"

    ```txt
    >> Toc (no-emoji: False):
    1. [📝 Header 2](#-header-2)
        1. [🌈 Header 3](#-header-3)

    >> Toc (no-emoji: True):
    1. [Header 2](#-header-2)
        1. [Header 3](#-header-3)
    ```

## api_example_health_check.py

<!-- [ko] -->
유효성 검사를 수행하는 예제입니다.
<!-- [ja] -->
バリデーションを実行する例です。
<!-- [en] -->
This example validates a base string.
<!-- [fr] -->
Cet exemple valide une chaîne de base.
<!-- [common] -->

See on [GitHub](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/api-examples/api_example_health_check.py)

```py
from mmg.health import HealthChecker, HealthStatus

base_md: str = """
<!---------------------------->
<!-- multilingual suffix: A, B, C -->
<!---------------------------->
<!-- [A] -->
# Sample Document A

Hello, A!
<!-- [B] -->
# Sample Document B

Hello, B!
<!-- [C] -->
# Sample Document C

Hello, C!
<!-- [common] -->
Thank you for using mmg!
"""


def main():
    hc = HealthChecker()
    status: HealthStatus = hc.health_check(base_md.splitlines())

    print(f" - Health check: {status.name}")
    print(" - Health messages:")
    for msg in hc.warning_messages:
        print(f"\t[WARN] {msg}")
    for msg in hc.error_messages:
        print(f"\t[ERR ] {msg}")
    print(f" - Tag list: {hc.tag_count}")


if __name__ == "__main__":
    main()
```

??? success "Output Text"

    ```txt
     - Health check: HEALTHY
     - Health messages:
     - Tag list: {'A': 1, 'B': 1, 'C': 1}
    ```

## api_example_reserved_tags.py

<!-- [ko] -->
예약된 태그 목록을 확인하는 예제입니다. 예약된 태그는 사용자 정의 태그로 사용할 수 없습니다.
<!-- [ja] -->
予約されたタグのリストを確認する例です。予約されたタグは、ユーザー定義のタグとして使用できません。
<!-- [en] -->
This example checks the list of reserved tags. Reserved tags cannot be used as user-defined tags.
<!-- [fr] -->
Cet exemple vérifie la liste des balises réservées. Les balises réservées ne peuvent pas être utilisées comme balises définies par l'utilisateur.
<!-- [common] -->

See on [GitHub](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/api-examples/api_example_reserved_tags.py)

```py
# import mmg.api as mmg
from mmg.config import RESERVED_KEYWORDS


def main():
    print(RESERVED_KEYWORDS)


if __name__ == "__main__":
    main()
```

??? success "Output Text"

    ```txt
    ['common', 'ignore', '<Unknown>']
    ```

## api_example_save_file.py

<!-- [ko] -->
변환한 결과를 파일로 저장하는 예제입니다.
**이 예제는 실제로 `A.md`, `B.md`, `C.md` 파일을 현재 디렉토리에 생성합니다.**
<!-- [ja] -->
変換した結果をファイルに保存する例です。
**この例は、実際に`A.md`、`B.md`、`C.md`ファイルを現在のディレクトリに作成します。**
<!-- [en] -->
This example saves the converted result to a file.
**This example actually creates `A.md`, `B.md`, `C.md` files in the current directory.**
<!-- [fr] -->
Cet exemple enregistre le résultat converti dans un fichier.
**Cet exemple crée réellement les fichiers `A.md`, `B.md`, `C.md` dans le répertoire actuel.**
<!-- [common] -->

See on [GitHub](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/api-examples/api_example_save_file.py)

```py
import os
from typing import Dict
import mmg.api as mmg

base_md: str = """
<!---------------------------->
<!-- multilingual suffix: A, B, C -->
<!---------------------------->
<!-- [A] -->
# Sample Document A

Hello, A!
<!-- [B] -->
# Sample Document B

Hello, B!
<!-- [C] -->
# Sample Document C

Hello, C!
<!-- [common] -->
Thank you for using mmg!
"""


def main(fake: bool = True):
    converted_mds: Dict[str, str] = mmg.convert(base_md)
    if fake:
        print(f"Fake mode: skip saving file. Detected tags: {converted_mds.keys()}")
        return
    for tag, txt in converted_mds.items():
        file_name = os.path.join(os.path.dirname(__file__), f"./{tag}.md")
        file_name = os.path.abspath(file_name)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(txt)


if __name__ == "__main__":
    main(fake=False)
```

No output text.

## api_example_save_file_no_suffix_option.py

<!-- [ko] -->
변환한 결과를 파일로 저장할 때, `no suffix` 옵션을 사용하는 예제입니다.
**이 예제는 실제로 `README.A`, `README.B`, `README` 파일을 현재 디렉토리에 생성합니다.**
<!-- [ja] -->
変換した結果をファイルに保存するとき、`no suffix`オプションを使用する例です。
**この例は、実際に`README.A`、`README.B`、`README`ファイルを現在のディレクトリに作成します。**
<!-- [en] -->
This example uses the `no suffix` option when saving the converted result to a file.
**This example actually creates `README.A`, `README.B`, `README` files in the current directory.**
<!-- [fr] -->
Cet exemple utilise l'option `no suffix` lors de l'enregistrement du résultat converti dans un fichier.
**Cet exemple crée réellement les fichiers `README.A`, `README.B`, `README` dans le répertoire actuel.**
<!-- [common] -->

See on [GitHub](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/api-examples/api_example_save_file_no_suffix_option.py)

```py
import os
from typing import Dict, List
from mmg.config import Config, extract_config_from_md
import mmg.api as mmg

base_md: str = """
<!---------------------------->
<!-- multilingual suffix: A, B, C -->
<!-- no suffix: C -->
<!---------------------------->
<!-- [A] -->
# Sample Document A

Hello, A!
<!-- [B] -->
# Sample Document B

Hello, B!
<!-- [C] -->
# Sample Document C

Hello, C!
<!-- [common] -->
Thank you for using mmg!
"""


def main(fake: bool = True):

    converted_mds: Dict[str, str] = mmg.convert(base_md)

    base_doc: List[str] = base_md.splitlines()
    cfg: Config = extract_config_from_md(base_doc)

    if fake:
        print(f"Fake mode: skip saving file. Detected tags: {converted_mds.keys()}")
        return
    for tag, txt in converted_mds.items():
        file_name = f"./README.{tag}.md" if tag != cfg.no_suffix else "./README.md"
        file_name = os.path.join(os.path.dirname(__file__), file_name)
        file_name = os.path.abspath(file_name)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(txt)


if __name__ == "__main__":
    main(fake=False)
```

No output text.

## api_example_set_cfg.py

<!-- [ko] -->
`Config` 객체를 다루는 예제입니다.
<!-- [ja] -->
`Config`オブジェクトを扱う例です。
<!-- [en] -->
This example handles `Config` objects.
<!-- [fr] -->
Cet exemple gère les objets `Config`.
<!-- [common] -->

See on [GitHub](https://github.com/ryul1206/multilingual-markdown/tree/main/examples/api-examples/api_example_set_cfg.py)

```py
from mmg.api import Config


def main():
    cfg1 = Config()
    cfg1.lang_tags = ["en", "fr", "kr", "jp"]  # Language tags are also used as suffixes.
    cfg1.no_suffix = "en"                      # Used only when saving files.
    print(f"cfg1: {cfg1}")

    cfg2 = Config(
        lang_tags=["en", "fr", "kr", "jp"],
        no_suffix="en",
    )
    print(f"cfg2: {cfg2}")


if __name__ == "__main__":
    main()
```

??? success "Output Text"

    ```txt
    cfg1: Config(lang_tags=['en', 'fr', 'kr', 'jp'], no_suffix='en')
    cfg2: Config(lang_tags=['en', 'fr', 'kr', 'jp'], no_suffix='en')
    ```
