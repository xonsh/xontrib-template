import os.path
import sys

import pytest

from .helpers import get_all_files, get_expected_files
import subprocess as sp

@pytest.mark.parametrize("autoloading", [False, True])
@pytest.mark.parametrize("builder", [
    "setuptools", "poetry"
])
def test_it_generates(bake_cookie, builder, autoloading):
    out = bake_cookie(package_manager=builder, enable_autoloading=autoloading)
    expected = get_expected_files(builder, autoloading)
    files = set(get_all_files(out.dst_path, ))
    assert files == expected

    pip = [sys.executable, "-m", "pip"]
    pkg = "xontrib-my-prompt"
    # check it is installable with pip
    sp.check_call([*pip, "install", os.path.join(out.dst_path, pkg), "-t", os.path.join(out.dst_path, "installed")])
