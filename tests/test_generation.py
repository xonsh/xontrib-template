import pytest

from .data import SETUP_TOOLS_FILES, POETRY_FILES
from .helpers import get_all_files


@pytest.mark.parametrize("package_manager,files_expected", [
    ["setuptools", SETUP_TOOLS_FILES],
    ["poetry", POETRY_FILES]
])
def test_pip(bake_cookie, package_manager, files_expected):
    out = bake_cookie(package_manager=package_manager)
    files = set(get_all_files(out.dst_path))
    assert files == files_expected
