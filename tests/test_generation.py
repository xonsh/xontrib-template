import pytest

from .helpers import get_all_files, get_expected_files


@pytest.mark.parametrize("autoloading", [False, True])
@pytest.mark.parametrize("builder", [
    "setuptools", "poetry"
])
def test_it_generates(bake_cookie, builder, autoloading):
    out = bake_cookie(package_manager=builder, enable_autoloading=autoloading)
    expected_fields = get_expected_files(builder, autoloading)
    files = set(get_all_files(out.dst_path, ))
    assert files == expected_fields
