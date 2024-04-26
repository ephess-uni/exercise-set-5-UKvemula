import os
from subprocess import run, PIPE

def test_ex_5_1_has_description(capfd):
    run_command = run(['python', 'ex_5_1.py', '-h'], stdout=PIPE, stderr=PIPE, text=True)
    assert "prints the number of lines" in run_command.stdout.lower()

def test_ex_5_1_prints_correct_line_count(capfd):
    infile_fixture = os.path.join(
        os.path.dirname(__file__),
        "fixtures",
        "ex_5_0_fixture.txt",
    )
    run_command = run(['python', 'ex_5_1.py', infile_fixture], stdout=PIPE, stderr=PIPE, text=True)
    expected_output = f"Number of lines in {infile_fixture}: 4"
    assert run_command.stdout.strip() == expected_output
