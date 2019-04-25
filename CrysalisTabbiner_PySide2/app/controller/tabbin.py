from app.imports.common import *
from app.controller import *
from app.threading import *
from app.controller.local_watchdog import *
from app.imports.crysalis.controller import CrysalisController
from app.imports.crysalis.tabbin import CrysalisTabbinController

__all__ = ["TabbinController"]

class TabbinController(QtCore.QObject, Tester):

    signinputfile = QtCore.Signal(str)
    signoutputfile = QtCore.Signal(str)

    signchangefiles = QtCore.Signal(str, str)

    WATCHDOG_MAXLENGTH = 7

    def __init__(self, widget, parent=None, debug_mode=None):
        QtCore.QObject.__init__(self, parent=parent)
        Tester.__init__(self, debug_mode=debug_mode)

        set_controller_widget_tabbin(self)

        self.widget = widget

        self.dis_all = (
            widget.btn_reopen, widget.btn_openfi,
            widget.sb_binning, widget.btn_process,
            widget.btn_same, widget.sb_group, widget.sb_radius,
            widget.btn_reopen, widget.btn_openfo,
            widget.sb_binning, widget.btn_process,
            widget.btn_same, widget.sb_group, widget.sb_radius
        )

        self.dis_before_input = (
            widget.btn_reopen,
            widget.sb_binning, widget.btn_process,
            widget.btn_same, widget.sb_group, widget.sb_radius
        )

        self.en_before_input = (
            widget.btn_openfi,
        )

        self.dis_before_output = (
            widget.btn_process,
            widget.sb_group, widget.sb_radius
        )

        self.en_before_output = (
            widget.btn_openfo,
        )

        self.dis_before_watchdog = (
            widget.btn_pickupfile,
            widget.cb_filewatchdog
        )

        # starter
        self._starter = get_controller_starter()

        # watchdog controller
        self.watchdog = WatchdogController(parent=self, debug_mode=debug_mode)
        self.watchdog_folder = WatchdogController(parent=self, debug_mode=debug_mode)

        # directory
        self.current_dir = "/"
        self.current_watch_folder = "/"

        # input file
        self.input_file = ""
        self.input_file_full = ""

        # output file
        self.output_file = ""
        self.output_file_full = ""

        # watchdog filelist
        self.wdfilelist = []

        # crysalis controller
        self._crysalis_control = CrysalisController()
        set_controller_crysalis(self._crysalis_control)
        self.tabbindata = None

        # prepare initial layout
        self.prepBeforeInput()
        self.prepBeforeOutput()
        self.prepBeforeWatchDog()

        # prepare signals
        self.signinputfile.connect(self.setInputFile)
        self.signoutputfile.connect(self.setOutputFile)
        self.signchangefiles.connect(self._starter.signChangeWindowTitle)
        self.widget.cb_filewatchdog.currentIndexChanged.connect(self.updateCBWatchdogIndex)

    def prepBeforeInput(self, bflag=False):
        """
        Disables the elements before the file is selected
        :return:
        """
        self.debug("Running {}.prepBeforeInput({})".format(self.__class__.__name__, bflag))
        for el in self.dis_before_input:
            el.setEnabled(bflag)
        for el in self.en_before_input:
            el.setEnabled(True)

    def prepBeforeRunner(self, bflag=False):
        """
        Disables the elements before the file is selected
        :return:
        """
        self.debug("Running {}.prepBeforeRunner".format(self.__class__.__name__))
        for el in self.dis_all:
            el.setEnabled(bflag)

    def prepBeforeWatchDog(self, bflag=False):
        """
        Disables the elements before the file is selected
        :return:
        """
        self.debug("Running {}.prepBeforeWatchDog({})".format(self.__class__.__name__, bflag))
        for el in self.dis_before_watchdog:
            el.setEnabled(bflag)

    def prepAfterRunner(self, dummy=""):
        """
        Enables the elements after runner
        :return:
        """
        self.debug("Running {}.prepAfterRunner ({}:{})".format(self.__class__.__name__,self.input_file, self.output_file))

        if len(self.input_file) > 0:
            self.prepBeforeInput(bflag=True)
        else:
            self.prepBeforeInput()

        if len(self.output_file) > 0:
            self.prepBeforeOutput(bflag=True)
        else:
            self.prepBeforeOutput()

    def prepBeforeOutput(self, bflag=False):
        """
        Prepares the elements before the output file is selected
        :return:
        """
        for el in self.dis_before_output:
            el.setEnabled(bflag)
        for el in self.en_before_output:
            el.setEnabled(True)

    def setInputFile(self, value=""):
        """
        Sets the variables corresponding to the input file
        :return:
        """
        # clear the text
        self.widget.le_fileinput.setText(value)

        if len(value) == 0:
            self.prepBeforeInput()
            self.widget.le_fileinput.setToolTip(value)
        else:
            self.prepBeforeInput(bflag=True)
            self.widget.le_fileinput.setToolTip(self.input_file_full)

            tpath = self.input_file_full
            depth = get_controller_watchdog_depth()
            for i in range(depth):
                tpath = os.path.split(tpath)[0]

            self.debug("The watchdog will use the path ({}) depth ({})".format(tpath, depth))
            self.watchdog.startObserver(tpath)

        self.signchangefiles.emit(self.input_file, self.output_file)

    def setOutputFile(self, value=""):
        """
        Sets the variables corresponding to the input file
        :return:
        """
        # clear the text
        self.widget.le_fileoutput.setText(value)

        if len(value) == 0:
            self.prepBeforeOutput()
            self.widget.le_fileoutput.setToolTip(value)
        else:
            self.prepBeforeInput(bflag=True)
            self.widget.le_fileoutput.setToolTip(self.output_file_full)

        self.signchangefiles.emit(self.input_file, self.output_file)

    def actionSelectInputFile(self):
        self.debug("{}.actionSelectInputFile".format(self.__class__.__name__))
        self.selectFile()

    def actionUpdateFile(self):
        """
        Loads the file data
        :return:
        """
        self.cleanTabbinData()

        self.debug("{}.actionUpdateFile".format(self.__class__.__name__))

        self.prepBeforeRunner()

        binning = self.widget.sb_binning.value()
        runner = TabbinRunnableOpen(self.input_file_full, binning=binning)
        self._starter.thcontrol.tryStart(runner)

    def actionUpdateAndProcessFile(self):
        """
        Loads the file data
        :return:
        """
        self.cleanTabbinData()

        self.info("{}.actionUpdateAndProcessFile".format(self.__class__.__name__))

        binning = self.widget.sb_binning.value()
        group = self.widget.sb_group.value()
        radius = self.widget.sb_radius.value()

        self.prepBeforeRunner()

        runner = TabbinRunnableFullProcess(self.input_file_full, binning, group, radius)
        self._starter.thcontrol.tryStart(runner)

    def actionSelectOutputFile(self):
        """
        Opens the dialog to select the file as an output one
        :return:
        """
        self.debug("{}.actionSelectOutputFile".format(self.__class__.__name__))
        self.selectFile(bsave=True)

    def actionProcessFile(self):
        """
        Process the data and output it
        :return:
        """
        self.debug("{}.actionProcessFile".format(self.__class__.__name__))

        self.prepBeforeRunner()

        group = self.widget.sb_group.value()
        radius = self.widget.sb_radius.value()

        runner = TabbinRunnableProcess(self.tabbindata, self.output_file_full, group, radius)
        self._starter.thcontrol.tryStart(runner)

    def actionMakeSamePath(self):
        """
        Make the paths for the output and the input the same
        :return:
        """
        self.debug("{}.actionMakeSamePath".format(self.__class__.__name__))

        if len(self.input_file) > 0 and len(self.input_file_full) > 0:
            self.output_file = self.input_file
            self.output_file_full = self.input_file_full

            self.setOutputFile(self.output_file)

    def selectFile(self, bsave=False):
        """
        Opens the file dialog to select the file
        :return:
        """
        res = None

        if not bsave:
            res = self._selectInputFile()
            if len(res) > 0:
                self.actionUpdateFile()
        else:
            res = self._selectOutputFile()

    def _selectInputFile(self, filepath=None):
        """
        Function accepting file input from the user
        :return:
        """
        res = None

        self.setTabbinStats()

        path = ''
        try:
            path_test = re.compile("[^\.]+.tabbin")

            if filepath is None:
                for i in range(2):
                    path, selector = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Open Tabbin File",
                                                                           self.current_dir, "Tabbin files (*.tabbin)")
                    if len(path) == 0:
                        continue
                    else:
                        break
            else:
                path = filepath

            # perform the test for the file - should be tabbin and should be valid
            if len(path) == 0:
                raise ValueError
            else:
                d, f = os.path.split(path)
                if path_test.match(f) is None:
                    raise ValueError

                self.input_file = f
                self.input_file_full = path
                self.current_dir = path

                self.signinputfile.emit(f)
        except ValueError:
            path = ''

        res = path
        if len(path) == 0:
            self.setInputFile(path)
        return res

    def _selectOutputFile(self, filepath=None):
        """
        Function accepting file input from the user
        :return:
        """
        res = None

        path = ''
        try:
            path_test = re.compile("[^\.]+.tabbin")

            if filepath is None:
                for i in range(2):
                    path, selector = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Tabbin File",
                                                                           self.current_dir, "Tabbin files (*.tabbin)")
                    if len(path) == 0:
                        continue
                    else:
                        break
            else:
                path = filepath

            # perform the test for the file - should be tabbin and should be valid
            if len(path) == 0:
                raise ValueError
            else:
                d, f = os.path.split(path)
                if path_test.match(f) is None:
                    raise ValueError

                self.output_file = f
                self.output_file_full = path
                self.current_dir = path

                self.signoutputfile.emit(f)
                return
        except ValueError:
            path = ''

        self.setOutputFile(path)
        return res

    def signTabbinController(self, value):
        """
        Recieves a tabbin controller for the file
        :param value:
        :return:
        """
        if isinstance(value, CrysalisTabbinController):
            self.cleanTabbinData()

            self.tabbindata = value

            num_points, version = value.num_points, value.version
            self.setTabbinStats(num_points=num_points, version=version)
        else:
            self.error("The controller is invalid ({})".format(value))
        self.prepAfterRunner()

    def setTabbinStats(self, num_points="", version=""):
        """
        Sets the version and number of points description
        :param num_points:
        :param version:
        :return:
        """
        self.widget.lbl_version.setText("{}".format(version))
        self.widget.lbl_numpoints.setText("{}".format(num_points))

    def cleanTabbinData(self):
        """
        Cleans the tabbin data
        :return:
        """
        if self.tabbindata is not None:
            del self.tabbindata
        self.tabbindata = None

    def closeEvent(self, ev):
        """
        Cleaning up on close
        :param ev:
        :return:
        """
        self.cleanup()

    def cleanup(self):
        """
        Cleaning up the threads and other things
        :return:
        """
        self.watchdog.cleanup()

    def updateWatchdogFileList(self, path, badddeleteflag):
        """
        Updates the information on the watchdog filelist
        :return:
        """

        # do not watch the recycled folder
        if "$recyc" in path.lower():
            return

        bupdated = False

        self.debug("New file update ({} : {})".format(path, badddeleteflag))
        self.debug("Previous lists:\n{}".format(self.wdfilelist))

        if badddeleteflag:  # new file
            if not path in self.wdfilelist:
                self.wdfilelist.insert(0, path)
                bupdated = True
            else:
                self.wdfilelist.pop(self.wdfilelist.index(path))
                self.wdfilelist.insert(0, path)
                bupdated = True

            if len(self.wdfilelist) > self.WATCHDOG_MAXLENGTH:
                self.wdfilelist.pop(-1)
        else:
            if path in self.wdfilelist:
                self.wdfilelist.pop(self.wdfilelist.index(path))
                bupdated = True

        # make a test if the files are existing
        tlist = []
        for el in self.wdfilelist:
            if os.path.exists(el):
                tlist.append(el)
            else:
                bupdated = True

        # test if any of the other files were moved - renamed
        if len(tlist)!= len(self.wdfilelist):
            del self.wdfilelist[:]
            self.wdfilelist = tlist

        # update the combobox
        if bupdated:
            self.widget.cb_filewatchdog.clear()
            for el in self.wdfilelist:
                el = el.replace("\\", "/")

                self.widget.cb_filewatchdog.addItem(self._prep_short_path(el))
                self.widget.cb_filewatchdog.setCurrentIndex(0)

            bdisable = False
            if self.widget.cb_filewatchdog.count() > 0:
                bdisable = True

            self.prepBeforeWatchDog(bflag=bdisable)

    def updateCBWatchdogIndex(self, index):
        """
        Updates the information on the file
        :param index:
        :return:
        """
        if self.widget.cb_filewatchdog.count() > 0:
            fp = self.wdfilelist[index]
            fp = fp.replace("\\", "/")
            self.widget.cb_filewatchdog.setToolTip(fp)

    def actionUpdateBtnWatchdogFile(self):
        """
        Action fired upon a click of the button updating both the input and the output files
        :return:
        """
        if self.widget.cb_filewatchdog.count() > 0:
            index = self.widget.cb_filewatchdog.currentIndex()
            path = self.wdfilelist[index]

            # set both file fields to the same value
            self.info("Step1")
            self._selectInputFile(filepath=path)
            self.info("Step2")
            self._selectOutputFile(filepath=path)

            # process file at the same time
            self.info("Step3")
            self.actionUpdateAndProcessFile()

    def _prep_short_path(self, path, level=None):
        """
        Prepares a shorted version of the path
        :param path:
        :return:
        """
        res = ""
        tlist = []
        tpath = path

        if level is None:
            level = get_controller_watchdog_depth()

        for i in range(level):
            tpath, t1 = os.path.split(tpath)

            tlist.insert(0, t1)

            self.debug("{}/{} {} {} {}".format(i, level, tlist, t1, tpath))

            if len(t1) == 0:
                if i < level-1:
                    tlist.insert(0, tpath)
                else:
                    tlist.insert(0, "..")
                break


        res = "/".join(tlist).replace("//", "/").replace("//", "/")
        return res

    def actionSelectFolder(self, path=None):
        """
        Selects a folder for a file watch dog
        :return:
        """
        if path is None:
            path =  QtWidgets.QFileDialog.getExistingDirectory(self.widget, "Select a folder for automatic file discovery",
                                                                   self.current_dir)

        if path is not None and len(path) > 0 and os.path.isdir(path):
            self.current_dir = path
            self.current_watch_folder = path
            self.watchdog_folder.startObserver(path)

            self.info("Using a folder ({}) for a watch dog processing".format(path))
            self._starter.signSetStatus("Using the folder ({}) and subfolders to watch files".format(path))