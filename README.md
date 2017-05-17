# Py-backwards packager

Setuptools integration with [py-backwards](https://github.com/nvbn/py-backwards).

## Usage

Install py-backwards-packager:

```bash
pip install py-backwards-packager
```

Change `setup` import in `setup.py` to:
 
```python
try:
    from py_backwards_packager import setup
except ImportError:
    from setuptools import setup
```

By default all targets enabled, but you can limit them with:
 
```python
setup(...,
      py_backwards_targets=['2.7', '3.3'])
```

After that your code will be automatically compiled on
`sdist`, `bdist` and `bdist_wheel`.

## License MIT
