from xonsh.built_ins import XonshSession


def _load_xontrib_(xsh: XonshSession, **_):

    # If your xontrib was made only for interactive mode it's good practice to check this before executing.
    if XSH.env.get("XONSH_INTERACTIVE"):
        var = xsh.env.get("VAR", "default")
        print("Autoloading xontrib: {{ project_repo_name }}")

        {% if has_events %}
        from .event_hooks import listen_cd
        xsh.builtins.events.on_chdir(listen_cd)
        {% endif %}
        {% if has_aliases %}
        from .aliases import git_log
        xsh.aliases["gl"] = git_log
        {% endif %}
