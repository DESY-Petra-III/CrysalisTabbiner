from app.imports.common import *
from app.controller.tabbin import *
from app.gui.ui.ui_widget import *

__all__ = ["CentralWidget"]

class CentralWidget(QtWidgets.QWidget, Ui_Form, Tester):
    def __init__(self, debug_mode=None):
        QtWidgets.QWidget.__init__(self)
        Ui_Form.__init__(self)
        Tester.__init__(self, debug_mode=debug_mode)

        self.setupUi(self)

        self.controller = TabbinController(self, debug_mode=debug_mode, parent=self)

    def actionSelectInputFile(self):
        """
        Passes the action to the controller - select input file
        :return:
        """
        self.controller.actionSelectInputFile()

    def actionUpdateFile(self):
        """
        Passes the action to the controller - update file
        :return:
        """
        self.controller.actionUpdateFile()

    def actionSelectOutputFile(self):
        """
        Passes the action to the controller - select output file
        :return:
        """
        self.controller.actionSelectOutputFile()

    def actionProcessFile(self):
        """
        Passes the action to the controller - process file
        :return:
        """
        self.controller.actionProcessFile()

    def actionMakeSamePath(self):
        """
        Passes the action to the controller - make input and the output the same
        :return:
        """
        self.controller.actionMakeSamePath()

    def actionSelectFolder(self):
        """
        Selects a folder for a watchdog
        :return:
        """
        self.controller.actionSelectFolder()

    def actionUpdateBtnWatchdogFile(self):
        """
        Select the recently updated file
        :return:
        """
        self.info("{}actionUpdateBtnWatchdogFile".format(self.__class__.__name__))
        self.controller.actionUpdateBtnWatchdogFile()