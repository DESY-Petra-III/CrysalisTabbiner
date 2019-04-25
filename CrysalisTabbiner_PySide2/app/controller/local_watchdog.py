__all__ = ["WatchdogController"]

from app.imports.common import *

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class WatchdogHandler(QtCore.QObject, FileSystemEventHandler, Tester):
    """Logs all the events captured."""

    signfilelistupdate = QtCore.Signal(str, bool)

    def __init__(self, parent, *args, **kwargs):
        QtCore.QObject.__init__(self, parent)
        FileSystemEventHandler.__init__(self, *args, **kwargs)
        Tester.__init__(self)

        self.parent = parent

        self.signfilelistupdate.connect(self.parent.updateWatchdogFileList)

    def on_created(self, event):
        super(WatchdogHandler, self).on_created(event)

        if event.is_directory:
            what = 'directory'
        else:
            what = 'file'

            fp = event.src_path
            if self.test_file(fp):
                self.info("Created {}: {}".format(what, fp))
                self.signfilelistupdate.emit(fp, True)

    def on_deleted(self, event):
        super(WatchdogHandler, self).on_deleted(event)

        if event.is_directory:
            what = 'directory'
        else:
            what = 'file'

            fp = event.src_path
            if self.test_file(fp):
                self.info("Deleted {}: {}".format(what, fp))
                self.signfilelistupdate.emit(fp, False)

    def on_modified(self, event):
        super(WatchdogHandler, self).on_modified(event)

        if event.is_directory:
            what = 'directory'
        else:
            what = 'file'

            fp = event.src_path
            if self.test_file(fp):
                self.debug("Modified {}: {}".format(what, fp))
                self.signfilelistupdate.emit(fp, True)

    def test_file(self, path):
        """
        Tests if the file corresponds to a proper file mask
        :return:
        """
        res = False

        fp = os.path.split(path)[1]

        if len(fp) > 0:
            test_patt = re.compile("[^\.]+.tabbin", re.IGNORECASE)
            if test_patt.match(fp):
                res = True
        return res

    def cleanup(self):
        """
        Cleansup the signal connections
        :return:
        """
        self.signfilelistupdate.disconnect(self.parent.updateWatchdogFileList)


class WatchdogController(QtCore.QObject, Tester):
    """
    Class controlling the watchdog
    """
    signfilelistupdate = QtCore.Signal(str, bool)

    def __init__(self, parent=None, debug_mode=None):
        QtCore.QObject.__init__(self, parent=parent)
        Tester.__init__(self, debug_mode=debug_mode)

        self.parent = parent

        if self.parent is not None:
            self.signfilelistupdate.connect(parent.updateWatchdogFileList)

        self.observer = None
        self.handler = None
        self.path = None

    def startObserver(self, path):
        """
        Starts the watch dog observer
        :return:
        """
        if self.path == path or not os.path.isdir(str(path)):
            return

        self.stopObserver()
        self.path = path

        self.observer = Observer()
        self.handler = WatchdogHandler(self)

        self.observer.schedule(self.handler, path, recursive=True)

        self.observer.start()

    def stopObserver(self):
        """
        Stops the observer
        :return:
        """
        if self.observer is not None:
            self.observer.stop()
            self.observer.join()

            self.observer = None
            self.handler.cleanup()
            self.handler.deleteLater()
            self.handler = None

    def cleanup(self):
        """
        Cleaning up procedure
        :return:
        """
        self.stopObserver()

    def updateWatchdogFileList(self, path, badddeleteflag):
        """
        Updates the information on the watchdog filelist
        :return:
        """
        self.debug("New fileupdate ({} : {})".format(path, badddeleteflag))
        if self.parent is not None:
            self.signfilelistupdate.emit(path, badddeleteflag)
