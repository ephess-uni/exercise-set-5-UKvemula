import os
from subprocess import run, PIPE
import pytest

MODULE_PATH = os.path.join(os.path.dirname(__file__), '..', 'src', 'ex_5_1.py')


def test_ex_5_1_has_description(capfd):
    run_command = run(['python', MODULE_PATH, '-h'], stdout=PIPE, stderr=PIPE, text=True)
    assert "prints the number of lines" in run_command.stdout.lower()


def test_ex_5_1_prints_correct_line_count(capfd):
    infile_fixture = os.path.join(
        os.path.dirname(__file__),
        "fixtures",
        "ex_5_0_fixture.txt",
    )
    run_command = run(['python', MODULE_PATH, infile_fixture], stdout=PIPE, stderr=PIPE, text=True)
    assert run_command.stdout.strip() == f"Number of lines in {infile_fixture}: 4"
