from typing import List, Iterator
from dataclasses import dataclass
import os
import re


@dataclass
class FileItem:
    """A dataclass for the file item.

    Attributes:
        norm_path (str): The normalized path of the base file.
        extension (str): The extension of the base file. `md` or `ipynb`.
    """
    norm_path: str
    extension: str

    @property
    def abs_path(self) -> str:
        return os.path.abspath(self.norm_path)

    def __repr__(self):
        return shorten_path(self.norm_path)

    def __hash__(self) -> int:
        return hash(self.abs_path)


def is_base_file(file_name: str) -> bool:
    """Return true if the file is `*.base.md` or `*.base.ipynb`.

    Args:
        file_name (str): The file name to check.

    Returns:
        bool: True if the file is `*.base.md` or `*.base.ipynb`.
    """
    base = re.compile(r"[.]base[.](md|ipynb)$")
    return base.search(file_name) is not None


def base_file_to_item(path: str, file_name: str) -> FileItem:
    """Convert the base file name to the base file item.

    Args:
        path (str): The path of the base file.
        file_name (str): The file name to convert.

    Raises:
        ValueError: If the file name is not a base file.

    Returns:
        FileItem: The base file item.
    """
    if not is_base_file(file_name):
        raise ValueError("The file name, {file_name}, is not a base file. It must be `*.base.md` or `*.base.ipynb`.")
    file_path = os.path.join(path, file_name)
    norm_path = os.path.normpath(file_path)
    extension = file_name.split(".")[-1]
    return FileItem(norm_path, extension)


def walk_base_file(path: str) -> Iterator[FileItem]:
    """Walk the given path and find all base files.

    Args:
        path (str): The path to walk.

    Returns:
        Iterator[FileItem]: The iterator of the base file items.
    """
    for path, _, files in os.walk(path):
        for file_name in files:
            if is_base_file(file_name):
                yield base_file_to_item(path, file_name)


def collect_base_files(file_names: List[str], recursive: bool) -> set[FileItem]:
    """Collect all base files from the given file names and the recursive flag.

    Args:
        file_names (List[str]): The list of file names to collect.
        recursive (bool): The recursive flag.

    Returns:
        set[FileItem]: The set of the base file items.
    """
    base_items: set[FileItem] = set()
    for file_name in file_names:
        # Resolve a PowerShell bug related to file paths with specific names
        # The below line prevents the error when the file_name starts with ".\" or "./".
        if file_name.startswith(".\\") or file_name.startswith("./"):
            file_name = file_name[2:]
        base_items.add(base_file_to_item(".", file_name))
    if recursive:
        for item in walk_base_file("."):
            base_items.add(item)
    return base_items


def shorten_path(path: str, max_length: int = 50) -> str:
    """Shorten the path to a given length.
    https://stackoverflow.com/questions/74300488/pretty-printing-of-paths-in-python

    Args:
        path (str): The path to shorten.
        max_length (int, optional): The maximum length of the path. Defaults to 20.

    Returns:
        str: The shortened path.
    """
    if len(path) < max_length:
        return path  # no need to shorten

    shortened_path = "..."  # add middle item
    paths_to_choose_from = path.split(os.sep)  # split by your custom OS separator. "/" for linux, "\" for windows.
    add_last_path = True
    while len(shortened_path) < max_length:
        if len(paths_to_choose_from) == 0:
            return shortened_path
        if add_last_path:
            shortened_path = shortened_path.replace("...", f"...{os.sep}{paths_to_choose_from[-1]}")
            del paths_to_choose_from[-1]  # delete elem used
            add_last_path = False
        else:
            shortened_path = shortened_path.replace("...", f"{paths_to_choose_from[0]}{os.sep}...")
            del paths_to_choose_from[0]  # delete elem used
            add_last_path = True
    return shortened_path
