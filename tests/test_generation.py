from pathlib import Path

import tomli


def get_all_files(path: "Path | str", parent: Path):
    if isinstance(path, str):
        path = Path(path)
    for p in path.iterdir():
        if p.is_file():
            if p.name == "pyproject.toml":
                validate_pyproject_toml_generated(p)
            yield str(p.relative_to(parent))
        else:
            yield from get_all_files(p, path)


def validate_pyproject_toml_generated(path:Path):
    from validate_pyproject import api

    # let's assume that you have access to a `loads` function
    # responsible for parsing a string representing the TOML file
    # (you can check the `toml` or `tomli` projects for that)
    with path.open() as fr:
        pyproject_as_dict = tomli.loads(fr.read())

    # now we can use validate-pyproject
    validator = api.Validator()
    validator(pyproject_as_dict)


def test_pip(bake_cookie, tmp_path):
    out_path = bake_cookie(package_manager="pip")
    files = set(get_all_files(out_path, tmp_path))
    assert files == {
        "xontrib-my-prompt/LICENSE",
        "xontrib/my_prompt.xsh",
        "xontrib-my-prompt/.editorconfig",
        "xontrib-my-prompt/README.md",
        "xontrib-my-prompt/setup.py",
        "xontrib-my-prompt/.gitignore",
        "workflows/test.yml",
        ".github/pull_request_template.md",
        ".github/issue_template.md",
        "xontrib-my-prompt/.gitattributes",
        "xontrib-my-prompt/pyproject.toml",
        ".github/release-drafter.yml",
        "workflows/release.yml",
        "xontrib-my-prompt/.pre-commit-config.yaml",
    }


def test_poetry(bake_cookie, tmp_path):
    out_path = bake_cookie(package_manager="poetry")
    files = set(get_all_files(out_path, tmp_path))
    assert files == {
        "xontrib-my-prompt/LICENSE",
        "xontrib/my_prompt.xsh",
        "xontrib-my-prompt/.editorconfig",
        "xontrib-my-prompt/README.md",
        "xontrib-my-prompt/.gitignore",
        "workflows/test.yml",
        ".github/pull_request_template.md",
        ".github/issue_template.md",
        "xontrib-my-prompt/.gitattributes",
        "xontrib-my-prompt/pyproject.toml",
        "xontrib-my-prompt/.pre-commit-config.yaml",
        ".github/release-drafter.yml",
        "workflows/release.yml",
    }
