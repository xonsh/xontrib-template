from xonsh.tools import uncapturable


@uncapturable
def git_log(args, stdin=None, stdout=None, stderr=None):
    import subprocess

    cmds = ("git", "log") + tuple(args)
    return subprocess.call(
        cmds,
        stdin=stdin,
        stderr=stderr,
        stdout=stdout,
    )
