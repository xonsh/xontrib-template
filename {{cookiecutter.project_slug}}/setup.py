from setuptools import setup

setup(
    name='{{cookiecutter.project_slug}}',
    version='{{cookiecutter.version}}',
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}',
    license='MIT',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    description='{{cookiecutter.short_description}}',
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
)
