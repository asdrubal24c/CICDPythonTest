import subprocess
import sys

from src.main import add


def test_add_integers():
    assert add(2, 3) == 5


def test_add_floats():
    assert add(1.5, 2.5) == 4.0


def test_cli_add():
    # Run the module as a script: python -m src.main add 2 3
    p = subprocess.run(
        [sys.executable, "-m", "src.main", "add", "2", "3"],
        capture_output=True,
        text=True,
    )
    assert p.returncode == 0
    assert p.stdout.strip() == "5"
