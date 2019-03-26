CONTROLLER_STARTER = None
CONTROLLER_CRYSALIS_TABBIN = None
CONTROLLER_WIDGET_TABBIN = None

__all__ = ["set_controller_starter", "get_controller_starter",
           "get_controller_crysalis", "set_controller_crysalis",
           "set_controller_widget_tabbin", "get_controller_widget_tabbin",
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