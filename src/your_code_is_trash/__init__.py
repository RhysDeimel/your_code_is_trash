# your_code_is_trash/__init__.py

"""An example python project structure

Modules exported by this package:

- `calulator`: Provide several sample math calculations.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version('your_code_is_trash')
except PackageNotFoundError:
    # package is not installed
    pass
