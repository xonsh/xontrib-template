"""This is run after project generation"""
import os
import shutil

pkg_manager = "{{ cookiecutter.package_manager }}"

from pathlib import Path


def get_all_files(path: "Path | str"):
    if isinstance(path, str):
        path = Path(path)
    for p in path.iterdir():
        if p.is_file():
            yield p
        else:
            yield from get_all_files(p)


# remove pip based setup
if pkg_manager != "pip":
    print("Pip is not selected")
    for file in ["MANIFEST.in", "requirements.txt", "setup.py"]:
        print(f"Removing {file} ")
        os.unlink(file)

# remove any .jinja2 extensions from file names
for file in get_all_files(Path.cwd()):
    if file.suffix.endswith("jinja2"):
        shutil.move(file, file.name.rstrip(file.suffix))
