from app.imports.common import *
from .version import version

__all__ = ["get_debugging_level", "set_debugging_level", "get_window_title", "get_window_statusbar_timeout"]

# configuring the window title
WINDOW_TITLE = "Tabbin filter - v{} ".format(version)

# status bar timeour
WINDOW_STATUSBAR_TIMEOUT = 5000.

# configuring the default debug level
# can be overwritten by the controller
DEBUGGING_LEVEL = DEBUG

def get_debugging_level():
    global  DEBUGGING_LEVEL
    return DEBUGGING_LEVEL

def set_debugging_level(level=DEBUG):
    global  DEBUGGING_LEVEL
    DEBUGGING_LEVEL = level

def get_window_title():
    global WINDOW_TITLE
    return WINDOW_TITLE

def get_window_statusbar_timeout():
    global WINDOW_STATUSBAR_TIMEOUT
    return WINDOW_STATUSBAR_TIMEOUT