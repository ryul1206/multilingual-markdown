from typing import List, Dict
import os
import json
import markdown  # Markdown to HTML
import nbconvert  # Jupyter Notebook to HTML
import nbformat  # Dict to Jupyter Notebook
from mmg.base_item import FileItem


def save_md(path, md_doc: List[str]):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_doc))


def save_jn(path, jupyter_notebook: Dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(jupyter_notebook, f, indent=2)


def save_html(path, html: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def save_pdf(path, html: str):
    # For Windows, import weasyprint only when GTK is available.
    # Please refer to the following link for more information:
    #   - https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows
    #   - https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#troubleshooting
    try:
        import weasyprint  # HTML to PDF
    except ModuleNotFoundError:
        raise ImportError(
            "WeasyPrint is not installed. Try `pip install mmg[pdf]` to install it.\n"
            "If you are a Windows user, you also need to install GTK3. "
            "Please refer to the following link for more information:\n"
            "* https://mmg.ryul1206.dev/unstable/misc/troubleshooting/#weasyprint-cannot-import-external-libraries"
        )
    except OSError:
        raise ImportError(
            "GTK3 is not available. If you are a Windows user, please install GTK3 and try again.\n"
            "Please refer to the following link for more information:\n"
            "* https://mmg.ryul1206.dev/unstable/misc/troubleshooting/#weasyprint-cannot-import-external-libraries"
        )
    # Save PDF
    html = weasyprint.HTML(string=html)
    html.write_pdf(path)


def handle_as_is(target_item: FileItem, content: any):
    if target_item.extension == "md":
        save_md(target_item.norm_path, content)
    elif target_item.extension == "ipynb":
        save_jn(target_item.norm_path, content)


def handle_html_or_pdf(target_item: FileItem, input_format: str, css: str, content: any):
    """
    Saves the provided content into a HTML file or a PDF file.

    Args:
        target_item (FileItem): Holds the file information of the target file.
        input_format (str): The format of the input content - either "md" or "ipynb".
        css (str): This parameter indicates the styling used for the HTML conversion.
            It can be a path to a CSS file, or one of the two preset values: "github-light" or "github-dark".
            This option is mandatory, regardless of the output format.
            This is because, even for PDF output, the content is first converted to HTML, then to PDF.
        content (any): This can be a List[str] for markdown content, or a Dict for a jupyter notebook.

    Raises:
        ValueError: Raised when an unsupported output format is specified.
    """
    # Convert to HTML
    if input_format == "md":
        html = convert_md_to_html("\n".join(content), css=css)
    elif input_format == "ipynb":
        html = convert_jupyter_to_html(content)
    # Save
    if target_item.extension == "html":
        save_html(target_item.norm_path, html)
    elif target_item.extension == "pdf":
        save_pdf(target_item.norm_path, html)


def convert_md_to_html(md: str, css: str):
    html = markdown.markdown(md, extensions=["fenced_code", "codehilite", "md_in_html"])
    # Get path of css file
    if css == "github-light" or css == "github-dark":
        this_dir = os.path.dirname(os.path.abspath(__file__))
        css_path = os.path.join(this_dir, "css", f"{css}.css")
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()
    else:
        current_dir = os.getcwd()
        css_path = os.path.join(current_dir, css)
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()
    # Add css
    html = f"<style>{css_content}</style><article class='markdown-body'>{html}</article>"
    return html


def convert_jupyter_to_html(notebook: Dict):
    # Read
    nb_str = json.dumps(notebook)
    nb: nbformat.NotebookNode = nbformat.reads(nb_str, as_version=4)
    # Validate
    try:
        nbformat.validate(nb)
    except nbformat.ValidationError as e:
        raise e
    # Convert
    html_exporter = nbconvert.HTMLExporter()
    html_data, resources = html_exporter.from_notebook_node(nb)
    return html_data
