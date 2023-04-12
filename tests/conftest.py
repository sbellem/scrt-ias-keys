# SPDX-FileCopyrightText: 2023-present Sylvain Bellemare <sbellem@gmail.com>
#
# SPDX-License-Identifier: MIT

import shutil
from collections import namedtuple
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from click.testing import CliRunner as __CliRunner


@pytest.fixture(scope="session")
def plugin_dir():
    with TemporaryDirectory() as d:
        directory = Path(d, "plugin")
        shutil.copytree(Path.cwd(), directory, ignore=shutil.ignore_patterns(".git"))

        yield directory.resolve()


@pytest.fixture
def new_project(tmp_path, plugin_dir, monkeypatch):
    project_dir = tmp_path / "my-app"
    project_dir.mkdir()

    project_file = project_dir / "pyproject.toml"
    project_file.write_text(
        f"""\
[build-system]
requires = ["hatchling", "hatch-plugin-name @ {plugin_dir.as_uri()}"]
build-backend = "hatchling.build"

[project]
name = "my-app"
version = "0.1.0"
""",
        encoding="utf-8",
    )

    package_dir = project_dir / "src" / "my_app"
    package_dir.mkdir(parents=True)

    package_root = package_dir / "__init__.py"
    package_root.write_text("")

    monkeypatch.chdir(project_dir)

    return project_dir


# Taken from https://github.com/ofek/hatch-showcase/blob/master/tests/conftest.py
class CliRunner(__CliRunner):
    def __init__(self, command):
        super().__init__()
        self._command = command

    def __call__(self, *args, **kwargs):
        # Exceptions should always be handled
        kwargs.setdefault("catch_exceptions", False)

        return self.invoke(self._command, args, **kwargs)


@pytest.fixture(scope="session")
def secretelf():
    from secretelf import cli

    return CliRunner(cli.secretelf)


@pytest.fixture
def ias_api_key():
    return "be5e574b2d4ce101eaf374c5a6ba6f40"


@pytest.fixture
def ias_spid():
    return "6C7BCCC92E1C7308084D737230F38022"


@pytest.fixture
def ias_keys(ias_api_key, ias_spid):
    IASKeys = namedtuple("IASKeys", ("api_key", "spid"))
    return IASKeys(ias_api_key, ias_spid)
