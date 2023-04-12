# secretelf

[![PyPI - Version](https://img.shields.io/pypi/v/secretelf.svg)](https://pypi.org/project/secretelf)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/secretelf.svg)](https://pypi.org/project/secretelf)

-----

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install secretelf
```

## Usage
Just pass the secretd binary file to the `secretelf iaskeys command`

```console
$ secretelf iaskeys tests/vectors/secretd
API KEY:  be5e574b2d4ce101eaf374c5a6ba6f40
SPID:     6C7BCCC92E1C7308084D737230F38022
```

```console
$ secretelf --help
Usage: secretelf [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  iaskeys
```

```console
$ secretelf iaskeys --help
Usage: secretelf iaskeys [OPTIONS] BINARY

Options:
  --help  Show this message and exit.
```

## License

`secretelf` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
