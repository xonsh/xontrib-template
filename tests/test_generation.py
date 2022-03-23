from pathlib import Path


def get_all_files(path: "Path | str", parent: Path):
    if isinstance(path, str):
        path = Path(path)
    for p in path.iterdir():
        if p.is_file():
            yield str(p.relative_to(parent))
        else:
            yield from get_all_files(p, path)


def test_pip(bake_cookie, tmp_path):
    out_path = bake_cookie()
    files = set(get_all_files(out_path, tmp_path))
    assert files == {
        "xontrib-my-prompt/LICENSE",
        "xontrib-my-prompt/requirements.txt",
        "xontrib-my-prompt/MANIFEST.in",
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
