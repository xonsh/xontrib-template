from xonsh.built_ins import XonshSession


def _load_xontrib_(xsh: XonshSession, **_):
    # Some code in Using Python API:
    var = xsh.env.get("VAR", "default")
    result = xsh.subproc_captured_stdout(['echo', '1'])
    print(result, var)
