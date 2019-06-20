import subprocess


def test_flake8_output():
    result = subprocess.run(
        ["flake8", "--config", "integrate/setup.cfg", "integrate"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0

    assert result.stdout == (
        "integrate/__init__.py:2:7: T400 Badly formatted TODO. Use TODO(name)[ticket_number]\n"
        "integrate/__init__.py:11:25: T400 Badly formatted TODO. Use TODO(name)[ticket_number]\n"
    )
