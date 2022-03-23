from pathlib import Path

from pytest import fixture
from cookiecutter.main import cookiecutter


@fixture
def bake_cookie(tmpdir):
    def bake(**ctx):
        template = Path(__file__).parent.parent
        assert (template / "cookiecutter.json").exists(), "Not the root path"
        return cookiecutter(
            str(template), no_input=True, extra_context=ctx, output_dir=tmpdir
        )

    return bake
