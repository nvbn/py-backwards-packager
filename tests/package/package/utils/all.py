import os
import re


def get_version():
    path = os.path.abspath(os.path.dirname(__file__))
    version = re.findall(r'_compiled_(\d)_(\d)', path)[0]
    return '{}.{}'.format(*version)

