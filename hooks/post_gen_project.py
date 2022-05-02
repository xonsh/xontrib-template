"""This is run after project generation"""
import shutil

pkg_manager = "{{ cookiecutter.package_manager }}"
disable_commit_hooks = "{{ cookiecutter.enable_pre_commit_hooks }}" == "no"
disable_release = "{{ cookiecutter.enable_auto_release }}" == "no"

from pathlib import Path


def get_all_files(path: "Path | str"):
    if isinstance(path, str):
        path = Path(path)
    for p in path.iterdir():
        if p.is_file():
            yield p
        else:
            yield from get_all_files(p)


def remove(file):
    print(f"Removing {file} ")
    file.unlink()


for file in get_all_files(Path.cwd()):
    if pkg_manager != "pip" and file.name in {
        "setup.py",
    }:
        # remove pip based setup
        remove(file)
    if disable_commit_hooks and (file.name == ".pre-commit-config.yaml"):
        remove(file)
    if disable_release and file.name in {"release.yml", "release-drafter.yml"}:
        remove(file)
    # remove any .jinja2 extensions from file names
    if file.suffix.endswith("jinja2"):
        shutil.move(file, file.name.rstrip(file.suffix))
