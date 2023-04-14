import builtins
import importlib
import io
import sys

import pytest
from pytest import MonkeyPatch


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ("1", ["2"]),
        ("2", ["2", "3"]),
        ("3", ["2", "3", "5"]),
        ("4", ["2", "3", "5", "7"]),
        ("5", ["2", "3", "5", "7", "11"]),
        ("6", ["2", "3", "5", "7", "11", "13"]),
        ("20", ["2", "3", "5", "7", "11", "13", "17", "19", "23", "29",
         "31", "37", "41", "43", "47", "53", "59", "61", "67", "71"])
    ],
)
def test_primes(monkeypatch: MonkeyPatch, test_input: str, expected_output: list[str]):
    mocked_input = lambda prompt="": test_input

    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    for output in expected_output:
        assert output in mocked_stdout.getvalue().strip()


def test_one(monkeypatch: MonkeyPatch):
    mocked_input = lambda prompt="": "2"

    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert "1" not in mocked_stdout.getvalue().strip()
