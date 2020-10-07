<p align="center">
A <a href="https://github.com/audreyr/cookiecutter">cookiecutter</a> template for <a href="https://github.com/xonsh/xonsh">xonsh</a> contributions called <a href="https://xon.sh/xontribs.html">xontribs</a>.
</p>

<p align="center">  
If you like the template click ⭐ on the repo.
</p>

## Create new xontrib

To create xontrib from the template just run:
```bash
pip install cookiecutter
cookiecutter gh:xonsh/xontrib-cookiecutter
```

## Example
```bash
$ cookiecutter gh:anki-code/xontrib-cookiecutter
You've downloaded /home/pc/.cookiecutters/xontrib-cookiecutter before. Is it okay to delete and re-download it? [yes]: 
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