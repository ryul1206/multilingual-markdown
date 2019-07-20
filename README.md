# multilingual-markdown

multilingual markdown generator, auto table of contents, no-suffix options

1. Make `{something}.base.md` file
2. Run this python file. Then, this will search all markdowns recursively.

    ```bash
    python multilang_md.py
    ```

3. You can find the `{something}.lang.md` files in the same directory. For example:
    - default: `{something}.en.md`, `{something}.kr.md`, `{something}.es.md`, ...
    - no-suffix option to `en`: `{something}.md`, `{something}.kr.md`, `{something}.es.md`, ...
