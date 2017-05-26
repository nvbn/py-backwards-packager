#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = '0.2'

install_requires = ['py-backwards']
extras_require = {':python_version<"3.4"': ['pathlib2'],
                  ':python_version<"3.5"': ['typing']}

setup(name='py-backwards-packager',
      version=VERSION,
      description="Setuptools integration with py-backwards",
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/py-backwards-packager',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'example*', 'tests*']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require=extras_require,
      entry_points={'console_scripts': [
          'py-backwards-packager = py_backwards_packager.main:main']})
