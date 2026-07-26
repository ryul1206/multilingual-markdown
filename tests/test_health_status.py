"""Tests that an error found in a base file actually fails the validation gate.

`DocChecker` used to record its verdict on an attribute of its own instance that nobody
read, so `HealthChecker` stayed HEALTHY no matter what `DocChecker` reported. A typo in
a language tag therefore dropped a whole section from the output while
`mmg --validation-only` still exited 0 in CI and in the pre-commit hook.

Warnings keep their previous meaning: an unbalanced tag is worth reporting but still
converts, so it must not fail the gate.
"""

import pytest
from mmg.health import HealthChecker, HealthStatus


HEADER = "<!-- multilingual suffix: en, fr -->"


def check_md(lines):
    hc = HealthChecker()
    status = hc.health_check(lines, extension="md")
    return hc, status


def notebook(lines):
    """One notebook holding each line of `lines` in its own markdown cell."""
    return {
        "cells": [{"cell_type": "markdown", "metadata": {}, "source": [line + "\n"]} for line in lines],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5,
    }


healthy_doc = [HEADER, "<!-- [en] -->", "Hello", "<!-- [fr] -->", "Bonjour"]

unhealthy_docs = {
    # A typo'd tag is dropped as <Unknown>, so its content never reaches any output file.
    "unknown tag": [HEADER, "<!-- [en] -->", "Hello", "<!-- [fr] -->", "Bonjour", "<!-- [zz] -->", "Dropped"],
    # A ToC marker without a level option cannot be rendered.
    "bad toc option": [HEADER, "<!-- [[ multilingual toc: no-emoji ]] -->", "<!-- [en] -->", "a", "<!-- [fr] -->", "b"],
}


def test_a_healthy_doc_stays_healthy():
    hc, status = check_md(healthy_doc)
    assert status == HealthStatus.HEALTHY
    assert hc.is_healthy
    assert hc.error_messages == []


@pytest.mark.parametrize("name", sorted(unhealthy_docs))
def test_an_error_makes_the_file_unhealthy(name):
    hc, status = check_md(unhealthy_docs[name])
    assert hc.error_messages, f"[{name}] The error was not reported at all."
    assert status == HealthStatus.UNHEALTHY, f"[{name}] Reported {hc.error_messages} but still passed the gate."
    assert not hc.is_healthy, f"[{name}] {hc.error_messages}"


@pytest.mark.parametrize("name", sorted(unhealthy_docs))
def test_an_error_makes_the_notebook_unhealthy(name):
    hc = HealthChecker()
    status = hc.health_check(notebook(unhealthy_docs[name]), extension="ipynb")
    assert hc.error_messages, f"[{name}] The error was not reported at all."
    assert status == HealthStatus.UNHEALTHY, f"[{name}] Reported {hc.error_messages} but still passed the gate."


def test_a_warning_alone_does_not_fail_the_gate():
    """An unbalanced tag is reported, but the file still converts."""
    doc = [HEADER, "<!-- [en] -->", "Hello", "<!-- [en] -->", "Hello again", "<!-- [fr] -->", "Bonjour"]
    hc, status = check_md(doc)
    assert hc.warning_messages, "The unbalanced tag should have been reported."
    assert hc.error_messages == []
    assert status == HealthStatus.HEALTHY


def test_error_line_numbers_start_from_one():
    """A ToC error used to be reported one line early, unlike every other error."""
    hc, _ = check_md(unhealthy_docs["bad toc option"])
    assert str(hc.error_messages[0]).startswith("Line 2:"), hc.error_messages


if __name__ == "__main__":
    pytest.main()
