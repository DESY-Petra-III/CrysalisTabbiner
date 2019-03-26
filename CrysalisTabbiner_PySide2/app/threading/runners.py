from app.imports.common import *
from app.controller import *

__all__ = ["ThreadingController", "TabbinRunnableOpen", "TabbinRunnableProcess"]

class ThreadingController(QtCore.QThreadPool, Tester):
    MAX_THREAD_COUNT = 5

    signstatus = QtCore.Signal(str)

    def __init__(self, debug_mode=None):
        QtCore.QThreadPool.__init__(self)
        Tester.__init__(self, debug_mode=debug_mode)

        self._starter = get_controller_starter()
        self.setParent(self._starter)

        self.setMaxThreadCount(self.MAX_THREAD_COUNT)

class Emmitter(QtCore.QObject, Tester):

    signtabbincontroller = QtCore.Signal(object)
    signstatus = QtCore.Signal(str)

    def __init__(self, debug_mode=None):
        QtCore.QObject.__init__(self)
        Tester.__init__(self, debug_mode=debug_mode)

class TabbinRunnableAbstract(QtCore.QRunnable, Tester):
    """
    Runnable executing the work
    """

    def __init__(self, debug_mode=None):
        QtCore.QRunnable.__init__(self)
        Tester.__init__(self, debug_mode=debug_mode)

        self.emmiter = Emmitter()

        self._starter = get_controller_starter()
        self._crysalis = get_controller_crysalis()
        self._tabbin = get_controller_widget_tabbin()

        self.emmiter.signtabbincontroller.connect(self._tabbin.signTabbinController)
        self.emmiter.signstatus.connect(self._starter.signSetStatus)

        self.setAutoDelete(True)

class TabbinRunnableOpen(TabbinRunnableAbstract):
    """
    Runnable executing the work of file reading
    """

    def __init__(self, filepath, binning, debug_mode=None):
        TabbinRunnableAbstract.__init__(self, debug_mode=debug_mode)

        self.filepath = filepath
        self.binning = binning

    def run(self):
        if os.path.isfile(self.filepath):
            d, f = os.path.split(self.filepath)
            self.emmiter.signstatus.emit("Opening file ({})".format(f))

            tc = self._crysalis.getTabbin()
            tc.read_file(self.filepath, binning=self.binning)

            self.emmiter.signtabbincontroller.emit(tc)
        else:
            self.emmiter.signstatus.emit("Invalid file ({})".format(self.filepath))
            self.emmiter.signtabbincontroller.emit(int(0))

        self.emmiter.deleteLater()


class TabbinRunnableProcess(TabbinRunnableAbstract):
    """
    Runnable executing the work of file writing
    """
    def __init__(self, tc, filepath, group, radius, debug_mode=None):
        TabbinRunnableAbstract.__init__(self, debug_mode=debug_mode)

        self.tc = tc
        self.filepath = filepath
        self.group = group
        self.radius = radius

    def run(self):
        if not os.path.isdir(self.filepath):
            d,f = os.path.split(self.filepath)
            self.emmiter.signstatus.emit("Writing the file ({})".format(f))

            self.tc.mod_list_pixelmultiframe(self.filepath,
                                  group=self.group, radius=self.radius)

            self.emmiter.signstatus.emit("File writing ({}) is finished".format(f))
            self.emmiter.signtabbincontroller.emit(int(0))
        else:
            self.emmiter.signstatus.emit("Invalid file ({})".format(self.filepath))
            self.emmiter.signtabbincontroller.emit(int(0))

        self.emmiter.deleteLater()