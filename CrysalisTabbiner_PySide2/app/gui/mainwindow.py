from app.imports.common import *
from app.gui.centralwidget import *
from app.gui.ui.ui_widget import *

__all__ = ["MainWindow"]

class MainWindow(QtWidgets.QMainWindow, Tester):
    def __init__(self, starter, debug_mode=None):
        QtWidgets.QMainWindow.__init__(self)
        Tester.__init__(self, debug_mode=debug_mode)

        self.Initialize(starter)

    def Initialize(self, starter):
        """
        Main initialization script for the main window
        :return:
        """
        # controller
        self.starter = starter

        # central widget
        self.cwidget = CentralWidget()
        self.setCentralWidget(self.cwidget)

        self.cwidget.show()

        # status bar
        self.sb = QtWidgets.QStatusBar(self)
        self.sb.clearMessage()
        self.setStatusBar(self.sb)
        self.sb.show()

        # visuals
        self.setWindowTitle(get_window_title())
        self.setStyleSheet("QMainWindow {background-color: #fff;}")
        self.show()