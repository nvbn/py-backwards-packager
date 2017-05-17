import setuptools
import sys
from tempfile import TemporaryDirectory
from contextlib import contextmanager
import os
from py_backwards.compiler import compile_files
from py_backwards.const import TARGETS
from . import const


def _get_bootstrap_content():
    root = os.path.abspath(os.path.dirname(__file__))
    bootstrap = os.path.join(root, 'bootstrap.py')
    with open(bootstrap) as f:
        return f.read()


bootstrap = _get_bootstrap_content()


def _target_to_module(target):
    return '_compiled_{}'.format(target.replace('.', '_'))


def _compile_packages(setup_kwargs, targets, tmp_dir):
    for package in setup_kwargs['packages']:
        if '.' in package:
            continue

        package_path = os.path.join(tmp_dir, package)
        for target in targets:
            path = os.path.join(package_path, _target_to_module(target),
                                package)
            compile_files(package, path, TARGETS[target])
        with open(os.path.join(package_path, '__init__.py'), 'w') as f:
            f.write(bootstrap)


def _get_new_packages(packages, targets):
    for package in packages:
        for target in targets:
            if '.' in package:
                parts = package.split('.')
                yield '{}.{}.{}.{}'.format(parts[0],
                                           _target_to_module(target),
                                           parts[0],
                                           '.'.join(parts[1:]))
            else:
                yield '{}.{}.{}'.format(package,
                                        _target_to_module(target),
                                        package)


@contextmanager
def _compiled(setup_kwargs, targets):
    with TemporaryDirectory(dir='.') as tmp_dir:
        _compile_packages(setup_kwargs, targets, tmp_dir)
        packages = list(_get_new_packages(setup_kwargs['packages'],
                                          targets))
        yield dict(setup_kwargs,
                   package_dir={'': tmp_dir},
                   packages=setup_kwargs['packages'] + packages)


def setup(py_backwards_targets=list(TARGETS.keys()), **setup_kwargs):
    if not const.COMMANDS.intersection(sys.argv):
        return setuptools.setup(**setup_kwargs)

    with _compiled(setup_kwargs, py_backwards_targets) as updated_kwargs:
        return setuptools.setup(**updated_kwargs)
