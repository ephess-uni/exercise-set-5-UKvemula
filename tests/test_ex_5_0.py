"""test_ex_5_0.py"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from ex_5_0 import line_count

def test_ex_5_0_writes_to_correct_value_to_stdout(capsys):
    infile_fixture = os.path.join(
        os.path.dirname(__file__),
        "fixtures",
        "ex_5_0_fixture.txt",
    )
    assert line_count(infile_fixture) == 4
