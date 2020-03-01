import os

from .draughtsman import Draughtsman

_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "lib", "libdrafter.so")

try:
    dm = Draughtsman()
except OSError:
    dm = Draughtsman(_path)
