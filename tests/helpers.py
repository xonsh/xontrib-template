from pathlib import Path

import tomli
from . import data


def get_all_files(path: "Path | str", root: Path = None):
    if isinstance(path, str):
        path = Path(path)
    if root is None:
        childs = list(path.iterdir())
        assert len(childs) == 1
        root = childs[0]
    for p in path.iterdir():
        if p.is_file():
            if p.name == "pyproject.toml":
                validate_pyproject_toml_generated(p)
            yield str(p.relative_to(root))
        else:
            yield from get_all_files(p, root)


def validate_pyproject_toml_generated(path: Path):
    from validate_pyproject import api

    # let's assume that you have access to a `loads` function
    # responsible for parsing a string representing the TOML file
    # (you can check the `toml` or `tomli` projects for that)
    with path.open() as fr:
        pyproject_as_dict = tomli.loads(fr.read())

    # now we can use validate-pyproject
    validator = api.Validator()
    validator(pyproject_as_dict)


def get_expected_files(package_manager: str, autoloading: bool):
    files = data.COMMON_FILES.copy()

    if autoloading:
        files.update(data.AUTO_LOADED)
    else:
        files.update(data.OLD_STYLE)

    if package_manager == "setuptools":
        files.update(data.SETUP_TOOLS_ONLY)

    return files