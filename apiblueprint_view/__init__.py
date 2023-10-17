import os

from .draughtsman import Draughtsman

_path_linux = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "lib", "libdrafter.so"
)
_path_mac = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "lib", "libdrafter.dylib"
)

try:
    dm = Draughtsman()
except OSError:
    if os.path.isfile(_path_mac):
        dm = Draughtsman(_path_mac)
    elif os.path.isfile(_path_linux):
        dm = Draughtsman(_path_linux)
    else:
        raise Exception("Failed to load libdrafter")
