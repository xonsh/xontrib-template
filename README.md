<p align="center">
A <a href="https://github.com/audreyr/cookiecutter">cookiecutter</a> template for <a href="https://github.com/xonsh/xonsh">xonsh</a> contributions called <a href="https://xon.sh/xontribs.html">xontribs</a>.
</p>

<p align="center">  
If you like the template click ⭐ on the repo.
</p>

## Why use this template?

This template includes good pack of prebuilt files: 

* `README` with the info and xontrib promotion instructions
* `setup.py` file to make and install PyPi package easily 
* `.gitattributes` file to enable Github syntax highlighting for `*.xsh` files
* `.gitignore` file with standard list of directories to ignore
* `.github/workflow/push-test.yml` to automatically test the code using Github Actions
* `MANIFEST.in` file to make Conda feedstock easily
* `LICENSE` file with standard MIT license
* `requirements.txt` file to make reference to xonsh on Github and promote xontrib

## Create new xontrib

To create a `xontrib` from this template just run:
```bash
pip install cookiecutter
cookiecutter gh:xonsh/xontrib-cookiecutter
```

## Example
```bash
cookiecutter gh:xonsh/xontrib-cookiecutter 
# full_name [Your name]: Conch Snail
# email [your@email.address]: snail@conch.sea
# github_username [Your github username]: snail
# project_name [Short project name (i.e. my-prompt)]: my-prompt
# project_repo_name [xontrib-my-prompt]: 
# project_package_name [my_prompt]: 
# project_short_description [A short description of the project]: My super prompt.
# version [0.1.0]: 

tree xontrib-my-prompt
# xontrib-my-prompt/
# ├── LICENSE
# ├── MANIFEST.in
# ├── README.md
# ├── requirements.txt
# ├── setup.py
# └── xontrib
#     └── my_prompt.xsh

pip install -U xontrib-my-prompt/
# Successfully installed xontrib-my-super-xontrib-0.1.0
  
xontrib load my_prompt
# This is xontrib-my-prompt!
```

# Alternatives
- Poetry version of the template - https://github.com/jnoortheen/xontrib-cookiecutter-poetry
