#!/usr/bin/env python3
# import sys
import codecs
import os
import re
import setuptools


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), "r").read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


with open(os.path.join(here, "requirements.txt"), encoding="utf-8") as f:
    install_requires = [pkg.replace("\n", "") for pkg in f.readlines()]


setup_options = dict(
    name="mmg",
    version=find_version("mmgcli", "__init__.py"),
    description="Command Line Interface to Generate i18n Markdown",
    author="Hong-ryul Jung",
    author_email="jung.hr.1206@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryul1206/multilingual-markdown",
    scripts=["bin/mmg"],
    packages=setuptools.find_packages(exclude=["example", "tests*", "PSmmg"]),
    install_requires=install_requires,
    license="MIT",
    python_requires=">=3.6, <4",
    keywords=["i18n", "markdown", "cli"],
    # https://pypi.org/classifiers/
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        # 'Operating System :: MacOS',
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Localization",
        "Topic :: Text Processing :: Markup :: Markdown",
    ],
)


setuptools.setup(**setup_options)
