from app.imports.common import *
from app.controller import *
from app.gui.mainwindow import *
from app.threading import *

class App(QtWidgets.QApplication):
    def __init__(self, *argv, **kwargs):
        QtWidgets.QApplication.__init__(self, *argv, **kwargs)

class Starter(QtCore.QObject, Tester):
    def __init__(self):
        QtCore.QObject.__init__(self)
        Tester.__init__(self, debug_mode=None)

        # save the controller
        set_controller_starter(self)

        self._init_timer()

    def _init_timer(self):
        """
        Initializes the timer to make sure we start the event loop
        :return:
        """
        self._timer = QtCore.QTimer()
        self._timer.setInterval(200)
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self.Initialization)
        self._timer.start()

    def _cleanup_timer(self):
        """Cleans up unnecessary timer"""
        self._timer.deleteLater()

    def Initialization(self):
        """
        Application initialization
        :return:
        """
        self._cleanup_timer()

        self.init_variables()

    def init_variables(self):
        """
        Initializing useful variables
        :return:
        """
        self.debug("Initializing variables")

        self.current_dir = None
        self.last_file = None

        # threading
        self._th_watch = None

        # main window
        self._mwindow = MainWindow(self)

        # threading
        self.thcontrol = ThreadingController()

    def signChangeWindowTitle(self, input_file="", output_file=""):
        """
        Sets the window title for the main window
        :param input_file:
        :param output_file:
        :return:
        """
        title = get_window_title()

        if len(input_file) > 0 or len(output_file)>0:
            title = title + " : "

        if len(input_file) > 0:
            title = title + " {} ".format(input_file)
        if len(output_file) > 0:
            title = title + "=> {} ".format(output_file)

        self._mwindow.setWindowTitle(title)

    def signSetStatus(self, msg):
        """
        Sets the main window status message
        :return:
        """
        sb = self._mwindow.statusBar()
        sb.clearMessage()
        sb.showMessage(msg, get_window_statusbar_timeout())


