<p align="center">
A <a href="https://github.com/audreyr/cookiecutter">cookiecutter</a> template for <a href="https://github.com/xonsh/xonsh">xonsh</a> contributions called <a href="https://xon.sh/xontribs.html">xontribs</a>.
</p>

<p align="center">  
If you like the template click ⭐ on the repo.
</p>

## Why use this template?

This template includes good pack of prebuilt files: 

* xontrib promotion instructions in the README 
* `setup.py` file to make and install PyPi package easily 
* `.gitattributes` file to enable Github syntax highlighting for `*.xsh` files
* `.gitignore` file with standard list of directories to ignore
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
$ cookiecutter gh:xonsh/xontrib-cookiecutter 
full_name [Your name]: Snail
email [Your address email]: snail
github_username [Your github username]: snail
project_name [Name of the project (for humans, without xontrib- prefix)]: my-super-xontrib
project_slug [my-super-xontrib]: 
project_short_description [A short description of the project]: It's my super xontrib!
version [0.1.0]: 

$ tree xontrib-my-super-xontrib
xontrib-my-super-xontrib
├── LICENSE
├── MANIFEST.in
├── README.rst
├── requirements.txt
├── setup.cfg
├── setup.py
└── xontrib
    └── my-super-xontrib.xsh

$ pip install -U xontrib-my-super-xontrib
Successfully installed xontrib-my-super-xontrib-0.1.0
  
$ xontrib load my-super-xontrib
This is my-super-xontrib!
```
