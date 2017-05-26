import pytest
from subprocess import call
from pathlib import Path
from py_backwards.const import TARGETS

# TODO: test also on 3.0, 3.1 and 3.2
targets = [version for version, target in TARGETS.items()
           if target < (3, 0) or target > (3, 2)]


@pytest.fixture(autouse=True)
def build_package():
    package_root = Path(__file__).parent.joinpath('package').as_posix()
    call(['python', 'setup.py', 'clean', '--all'], cwd=package_root)
    call(['python', 'setup.py', 'bdist_wheel', '--universal'],
         cwd=package_root)


@pytest.mark.parametrize('target', targets)
def test(spawnu, TIMEOUT, target):
    proc = spawnu('py_backwards_packager/python-{}'.format(target),
                  'FROM python:{}'.format(target),
                  'bash')

    proc.sendline(
        'pip install src/tests/package/dist/package-0.1-py2.py3-none-any.whl')
    assert proc.expect_exact([TIMEOUT, 'Successfully installed package-0.1'])

    proc.sendline('app')
    assert proc.expect_exact([TIMEOUT, 'main {}'.format(target)])

    proc.sendline('deep-app')
    assert proc.expect_exact([TIMEOUT, 'deep {}'.format(target)])

    proc.sendline('python -m package.main')
    assert proc.expect_exact([TIMEOUT, 'main {}'.format(target)])

    proc.sendline('python -m package.deep.main')
    assert proc.expect_exact([TIMEOUT, 'deep {}'.format(target)])
