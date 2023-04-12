# SPDX-FileCopyrightText: 2023-present Sylvain Bellemare <sbellem@gmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

def test(secretelf, ias_keys):
    result = secretelf("iaskeys", "tests/vectors/secretd")

    assert result.exit_code == 0, result.output
    assert result.output == f"API KEY: \t{ias_keys.api_key}\nSPID: \t\t{ias_keys.spid}\n"
