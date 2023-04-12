import pytest

@pytest.skip
def test(secretelf, ias_keys):
    result = secretelf("iaskeys", "binaries/secretd")

    assert result.exit_code == 0, result.output
    assert result.output == f"API KEY: \t{ias_keys.api_key}\nSPID: \t\t{ias_keys.spid}\n"
