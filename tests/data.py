COMMON_FILES = {
    '.copier-answers.yml',
    '.editorconfig',
    '.gitattributes',
    '.github/issue_template.md',
    '.github/pull_request_template.md',
    '.github/release-drafter.yml',
    '.github/workflows/release.yml',
    '.github/workflows/test.yml',
    '.gitignore',
    '.pre-commit-config.yaml',
    'LICENSE',
    'README.md',
    'pyproject.toml',
    'tests/__init__.py',
    'tests/test_xontrib.py',
    'xontrib/my_prompt.py'
}

SETUP_TOOLS_FILES = COMMON_FILES.union({
    'setup.py',
})

POETRY_FILES = COMMON_FILES
