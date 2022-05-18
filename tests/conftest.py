from pathlib import Path

from pytest import fixture
import copier


@fixture
def bake_cookie(tmpdir):
    def bake(**ctx):
        template = Path(__file__).parent.parent
        assert template.exists(), "Not the root path"
        return copier.run_copy(
            str(template),
            dst_path=tmpdir,
            data=ctx,
        )

    return bake
