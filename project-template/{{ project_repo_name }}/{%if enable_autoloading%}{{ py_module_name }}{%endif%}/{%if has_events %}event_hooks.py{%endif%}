def activate_env(path:str):
    # lazy import to reduce startup cost
    from xontrib.voxapi import Vox

    vox = Vox()
    vox.activate(path)

def listen_cd(olddir, newdir, **_):
    activate_env(newdir)
