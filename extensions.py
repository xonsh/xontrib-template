# copied from https://github.com/pawamoy/copier-pdm/blob/main/extensions.py
# Thanks to the original author

import re
import subprocess
import unicodedata
from datetime import date

from jinja2.ext import Extension


def git_user_name() -> str:
    return subprocess.getoutput("git config user.name").strip()


def git_user_email() -> str:
    return subprocess.getoutput("git config user.email").strip()


def slugify(value, separator="-"):
    value = (
        unicodedata.normalize("NFKD", str(value))
        .encode("ascii", "ignore")
        .decode("ascii")
    )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-_\s]+", separator, value).strip("-_")


class GitExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.globals["git_user_name"] = git_user_name
        environment.globals["git_user_email"] = git_user_email


class SlugifyExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["slugify"] = slugify


class CurrentYearExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.globals["current_year"] = date.today().year
