from pathlib import Path

from pytest import fixture
import copier

@fixture
def bake_cookie(tmpdir):
    def bake(**ctx):
        data = dict(full_name="Full Name", github_username="snail", email="example@example.com",
                    project_name="my-prompt",
                    project_short_description="description", )
        data.update(ctx)
        template = Path(__file__).parent.parent
        assert template.exists(), "Not the root path"
        return copier.copy(
            str(template),
            dst_path=tmpdir,
            data=data,
            defaults=True
        )

    return bake
