<p align="center">
A <a href="https://github.com/audreyr/cookiecutter">cookiecutter</a> template for <a href="https://github.com/xonsh/xonsh">xonsh</a> contributions called <a href="https://xon.sh/xontribs.html">xontribs</a>.
</p>

<p align="center">  
If you like the template click ⭐ on the repo.
</p>

## Why use this template?

This template includes good pack of prebuilt files: 

* `README` with the info and xontrib promotion instructions
* [`PEP 621`](https://peps.python.org/pep-0621/) or `poetry` based `pyproject.toml` file to make and install PyPi package easily 
* `.gitattributes` file to enable Github syntax highlighting for `*.xsh` files
* `.gitignore` file with standard list of directories to ignore
* `.github/workflow/push-test.yml` to automatically test the code using Github Actions
* `.github/*_template.md` files to create Github templates for the text of issue and PR.
* `MANIFEST.in` file to make Conda feedstock easily
* `LICENSE` file with standard MIT license

## Create new xontrib

This template uses [copier](https://copier.readthedocs.io/en/stable/). We can install it as a CLI using [pipx](https://pypa.github.io/pipx/):

```bash
pipx install copier
pipx inject copier jinja2-time
pipx inject copier cookiecutter
```

Now to create your new `xontrib`:

```bash
copier gh:xonsh/xontrib-template .
```

## Advent of [PEP-621](https://peps.python.org/pep-0621/) 

Older projects can use the following tools to upgrade their setup to use pyproject.toml

* https://github.com/asottile/setup-py-upgrade
* https://ini2toml.readthedocs.io/en/latest/setuptools_pep621.html
* https://validate-pyproject.readthedocs.io/
* https://github.com/denkiwakame/py-tiny-pkg

## Example
```bash
cookiecutter gh:xonsh/xontrib-cookiecutter 
# full_name [Snail From Conch]: <ENTER>
# email [your@email.address]: <ENTER>
# github_username [snail]: <ENTER>
# project_name [my-prompt]: <ENTER>
# project_repo_name [xontrib-my-prompt]: <ENTER> 
# project_package_name [my_prompt]: <ENTER>
# project_short_description [A short description of the project.]: <ENTER> 
# version [0.1.0]: <ENTER>


tree -a xontrib-my-prompt/
# xontrib-my-prompt/
# ├── .gitattributes
# ├── .github
# │    └── workflows
# │         └── push-test.yml
# ├── .gitignore
# ├── LICENSE
# ├── MANIFEST.in
# ├── README.md
# ├── requirements.txt
# ├── setup.py
# └── xontrib
#     └── my_prompt.xsh

```
