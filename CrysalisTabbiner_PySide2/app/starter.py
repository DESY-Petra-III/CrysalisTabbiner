from app.imports.common import *
from app.controller import *
from app.gui.mainwindow import *
from app.threading import *

class App(QtWidgets.QApplication):
    def __init__(self, *argv, **kwargs):
        QtWidgets.QApplication.__init__(self, *argv, **kwargs)

class Starter(QtCore.QObject, Tester):

    KEY_SETTINGS_MAINWINDOW = "MainWindow"
    KEY_SETTINGS_SIZE = "size"
    KEY_SETTINGS_POSITION = "position"
    KEY_SETTINGS_FOLDER = "last_folder"

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
        self.last_input_file = None
        self.last_output_file = None

        # settings session
        app = QtWidgets.QApplication.instance()

        self.settings = QtCore.QSettings()

        # path and other settings
        current_path = os.path.split(__file__)[0]
        icon_path = os.path.join(current_path, "images", "icon.png")
        set_path_images(icon_path)

        # main window
        self._mwindow = MainWindow(self)
        self._mwindow.setIcon(icon_path)

        # threading
        self.thcontrol = ThreadingController()

        # cleaning up
        app.lastWindowClosed.connect(self.cleanup)

        # update settings
        self._read_settings()

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

    def cleanup(self):
        """
        Cleanup event to trigger on the problems
        :return:
        """
        self.info("Cleaning up")

    def _read_settings(self):
        """
        Reads the settings from the file
        :return:
        """
        self.settings.beginGroup(self.KEY_SETTINGS_MAINWINDOW)

        size = None
        key = self.KEY_SETTINGS_SIZE
        def_size = QtCore.QSize(800, 600)
        try:
            size = self.settings.value(key, def_size).toSize()
        except AttributeError:
            size = self.settings.value(key, def_size)

        position = None
        key = self.KEY_SETTINGS_POSITION
        def_position = QtCore.QPoint(100, 100)
        try:
            position = self.settings.value(key, def_position).toPoint()
        except AttributeError:
            position = self.settings.value(key, def_position)


        if not isinstance(size, QtCore.QSize):
            size = def_size

        if not isinstance(position, QtCore.QPoint):
            position = def_position

        key = self.KEY_SETTINGS_FOLDER
        last_path = self.settings.value(key, "/")

        self.info(size)
        self.info(position)

        self._mwindow.resize(size)
        self._mwindow.move(position)

        if last_path != "/":
            self._mwindow.centralWidget().controller.actionSelectFolder(last_path)

        self.settings.endGroup()

    def _write_settings(self, size, position):
        """
        Writes the settings on application exit (main window closed)
        :param size:
        :param position:
        :return:
        """
        self.info("Saving Settings")

        self.settings.beginGroup(self.KEY_SETTINGS_MAINWINDOW)

        self.settings.setValue(self.KEY_SETTINGS_SIZE, size)
        self.settings.setValue(self.KEY_SETTINGS_POSITION, position)

        last_path = self._mwindow.centralWidget().controller.current_watch_folder
        if last_path is not None and os.path.isdir(last_path):
            pass
        else:
            last_path = "/"
        self.settings.setValue(self.KEY_SETTINGS_FOLDER, last_path)

        self.settings.endGroup()
        self.settings.sync()

    def signSetClipboard(self, value):
        """
        Sets the cliupboard of the application to a specific value
        :return:
        """
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(str(value))