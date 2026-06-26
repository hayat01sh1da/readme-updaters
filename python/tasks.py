import os
import sys

from invoke import Context, task

_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_ROOT, 'src'))

from application import Application  # noqa: E402


@task
def update_readme(c: Context) -> None:
    """Update README.md with The Latest Output from The Application"""
    print('========== Start Updating README ===========')
    Application.run()
    print('========== Finished Updating README ===========')


@task(default=True)
def test(c: Context) -> None:
    """Run all tests"""
    c.run('pytest .')
