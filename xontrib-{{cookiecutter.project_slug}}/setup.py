#!/usr/bin/env python
import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-{{cookiecutter.project_slug}}',
    version='{{cookiecutter.version}}',
    license='MIT',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    description="{{cookiecutter.project_short_description}}",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=['xonsh'],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    url='https://github.com/{{cookiecutter.github_username}}/xontrib-{{cookiecutter.project_slug}}',
    project_urls={
        "Documentation": "https://github.com/{{cookiecutter.github_username}}/xontrib-{{cookiecutter.project_slug}}/blob/master/README.md",
        "Code": "https://github.com/{{cookiecutter.github_username}}/xontrib-{{cookiecutter.project_slug}}",
        "Issue tracker": "https://github.com/{{cookiecutter.github_username}}/xontrib-{{cookiecutter.project_slug}}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
    ]
)
