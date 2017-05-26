from setuptools import find_packages

try:
    from py_backwards_packager import setup
except ImportError:
    from setuptools import setup

VERSION = '0.1'

setup(name='package',
      version=VERSION,
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'example*', 'tests*']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[],
      entry_points={'console_scripts': [
          'app = package.main:main',
          'deep-app = package.deep.main:main']})
