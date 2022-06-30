from xonsh.built_ins import XonshSession


def _load_xontrib_(xsh: XonshSession, **_):
    # Some code in Using Python API:
    var = xsh.env.get("VAR", "default")
    result = xsh.subproc_captured_stdout(['echo', '1'])
    print(result, var)

    {% if has_events %}
    from .event_hooks import listen_cd
    xsh.builtins.events.on_chdir(listen_cd)
    {% endif %}
    {% if has_aliases %}
    from .aliases import git_log
    xsh.aliases["gl"] = git_log
    {% endif %}
