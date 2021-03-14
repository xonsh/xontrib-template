import xonsh


__all__ = ()

print('This is {{cookiecutter.project_slug}}!')


# Good start! Get more documentation -> https://xon.sh/contents.html#guides


# Note! If you will write the xontrib on Python it will work faster 
# until https://github.com/xonsh/xonsh/issues/3953 hasn't released yet.
# To use Python:
#  1. rename this file from `xsh` to `py`
#  2. replace `xsh` to `py` in `setup.py`
#  3. rewrite the code using xonsh Python API i.e.:
#   * `__xonsh__.env.get('VAR', 'default')` instead of `${...}.get('VAR', 'default')`
#   * `__xonsh__.subproc_captured_stdout(['echo', '1'])` instead of `$(echo 1)`
