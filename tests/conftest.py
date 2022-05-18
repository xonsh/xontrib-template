from pathlib import Path

from pytest import fixture
import copier


@fixture
def bake_cookie(tmpdir):
    def bake(**ctx):
        data = dict(full_name="Full Name", github_username="gh_user", email="example@example.com",
                    project_name="sample", project_repo_name="xontrib-sample", project_package_name="sample",
                    pure_py=True, version="0.1.0", enable_pre_commit_hooks=True,
                    project_short_description="description", )
        data.update(ctx)
        template = Path(__file__).parent.parent
        assert template.exists(), "Not the root path"
        return copier.run_copy(
            str(template),
            dst_path=tmpdir,
            data=data,
        )

    return bake
