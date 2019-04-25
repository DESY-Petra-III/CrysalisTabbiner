# configuration of the watch stats
CONTROLLER_WATCHDOG_DEPTH = 5

# references
CONTROLLER_STARTER = None
CONTROLLER_CRYSALIS_TABBIN = None
CONTROLLER_WIDGET_TABBIN = None

# path for the images
PATH_IMAGES = None

__all__ = ["set_controller_starter", "get_controller_starter",
           "get_controller_crysalis", "set_controller_crysalis",
           "set_controller_widget_tabbin", "get_controller_widget_tabbin",
           "get_controller_watchdog_depth", "set_controller_watchdog_depth",
           "set_path_images", "get_path_images"
           ]

def set_controller_starter(value):
    global CONTROLLER_STARTER
    CONTROLLER_STARTER = value

def get_controller_starter():
    global CONTROLLER_STARTER
    return CONTROLLER_STARTER

def set_controller_crysalis(value):
    global CONTROLLER_CRYSALIS_TABBIN
    CONTROLLER_CRYSALIS_TABBIN = value

def get_controller_crysalis():
    global CONTROLLER_CRYSALIS_TABBIN
    return CONTROLLER_CRYSALIS_TABBIN

def set_controller_widget_tabbin(value):
    global CONTROLLER_WIDGET_TABBIN
    CONTROLLER_WIDGET_TABBIN = value

def get_controller_widget_tabbin():
    global CONTROLLER_WIDGET_TABBIN
    return CONTROLLER_WIDGET_TABBIN

def set_controller_watchdog_depth(value):
    global CONTROLLER_WATCHDOG_DEPTH
    CONTROLLER_WATCHDOG_DEPTH = value

def get_controller_watchdog_depth():
    global CONTROLLER_WATCHDOG_DEPTH
    return CONTROLLER_WATCHDOG_DEPTH

def set_path_images(value):
    global PATH_IMAGES
    PATH_IMAGES = value

def get_path_images():
    global PATH_IMAGES
    return PATH_IMAGES