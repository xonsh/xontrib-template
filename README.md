<p align="center">
A template for creating the <a href="https://github.com/xonsh/xonsh">xonsh</a> contributions called <a href="https://xon.sh/xontribs.html">xontribs</a>.
</p>

<p align="center">
If you like the template click ⭐ on the repo.
</p>

[![asciicast](https://asciinema.org/a/499605.svg)](https://asciinema.org/a/499605)

## Why use this template?

This template includes good pack of prebuilt files:

* `README` with the info and xontrib promotion instructions
* [`PEP 621`](https://peps.python.org/pep-0621/) or `poetry` based `pyproject.toml` file to make and install PyPi package easily
* `.gitattributes` file to enable Github syntax highlighting for `*.xsh` files
* `.gitignore` file with standard list of directories to ignore
* `.github/workflow/push-test.yml` to automatically test the code using Github Actions
* `.github/*_template.md` files to create Github templates for the text of issue and PR.
* `.github/FUNDING.yml` file with template for Github sponsorship button.
* `.pre-commit-config.yaml` file with [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
* `MANIFEST.in` file to make Conda feedstock easily
* `LICENSE` file with standard MIT license
* `tests/` with the test suite

## Create new xontrib

Install [copier](https://copier.readthedocs.io/en/stable/):

```xsh
xpip install copier jinja2-time cookiecutter

# OR using pipx (https://pypa.github.io/pipx/):
pipx install copier
pipx inject copier jinja2-time cookiecutter
```

Create your new xontrib:

```xsh
# copier 9
copier copy --trust gh:xonsh/xontrib-template .

# older versions of copier
copier gh:xonsh/xontrib-template .
```

## Advent of [PEP-621](https://peps.python.org/pep-0621/)

Older projects can use the following tools to upgrade their setup to use pyproject.toml

* https://github.com/asottile/setup-py-upgrade
* https://ini2toml.readthedocs.io/en/latest/setuptools_pep621.html
* https://validate-pyproject.readthedocs.io/
* https://github.com/denkiwakame/py-tiny-pkg

## If you have an idea for xontrib but have no time to implement

* [Create an issue with your idea](https://github.com/xonsh/xontrib-template/issues/new?assignees=&labels=idea&template=idea.md&title=Idea%3A+)
* [Top ideas](https://github.com/xonsh/xontrib-template/issues?q=is%3Aissue+is%3Aopen+label%3Aidea+sort%3Areactions-%2B1-desc)

## Development

- `copier` selects the latest tag when `--vcs-ref` option is not given. So it is important to tag the main branch after important template updates.

### How to fix [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)

If you're using `.pre-commit-config.yaml` and have an error during testing you need fix the code i.e.:

```xsh
xpip install pre-commit-hooks
pre-commit run --all-files black  # or isort, etc
```

## Links

* [Awesome Xontribs](https://github.com/xonsh/awesome-xontribs)
* [Xontribs on GitHub](https://github.com/topics/xontrib)

