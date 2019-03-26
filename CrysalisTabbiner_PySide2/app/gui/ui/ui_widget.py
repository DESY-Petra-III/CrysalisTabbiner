# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_widget.ui',
# licensing of 'ui_widget.ui' applies.
#
# Created: Mon Mar 25 18:34:06 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from app.imports.common import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 516)
        Form.setStyleSheet("QWidget {\n"
"background-color: #fff;\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"font-size: 16px;\n"
"border: 1px solid #ccc;\n"
"}\n"
"\n"
"QLabel {\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QToolButton {\n"
"background-color: #ccc;\n"
"border: 2px solid #333;\n"
"color: #333;\n"
"\n"
"width: 40px;\n"
"height: 30px;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QToolButton:enabled {\n"
"background-color: #fff;\n"
"border: 2px solid #0d0;\n"
"color: #000;\n"
"}\n"
"\n"
"QToolButton:hover:enabled {\n"
"background-color: #0D0;\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #ccc;\n"
"border: 2px solid #333;\n"
"color: #333;\n"
"width: 40px;\n"
"height: 30px;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"background-color: #fff;\n"
"border: 2px solid #C00;\n"
"color: #000;\n"
"}\n"
"\n"
"QPushButton:hover:enabled {\n"
"background-color: #f00;\n"
"color: #fff;\n"
"}\n"
"\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid black;\n"
"    border-bottom: 0px;\n"
"    border-right: 0px;\n"
"    border-left: 0px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    padding-top:2ex;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top center */\n"
"    padding: 0px 20px;\n"
"    color: #39D;\n"
"}\n"
"\n"
"QSpinBox {\n"
"padding-top: 5px;\n"
"padding-bottom: 5px;\n"
"padding-left: 1ex;\n"
"border: 1px solid #ccc;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(-1, -1, 10, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gp_output = QtWidgets.QGroupBox(Form)
        self.gp_output.setObjectName("gp_output")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gp_output)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_process = QtWidgets.QPushButton(self.gp_output)
        self.btn_process.setMinimumSize(QtCore.QSize(80, 0))
        self.btn_process.setObjectName("btn_process")
        self.gridLayout_3.addWidget(self.btn_process, 0, 4, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.gp_output)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 20))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 5)
        self.widget_3 = QtWidgets.QWidget(self.gp_output)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setMinimumSize(QtCore.QSize(140, 0))
        self.label_8.setStyleSheet("QLabel {\n"
"color: #999;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.sb_group = QtWidgets.QSpinBox(self.widget_3)
        self.sb_group.setMinimumSize(QtCore.QSize(100, 0))
        self.sb_group.setStyleSheet("")
        self.sb_group.setMinimum(1)
        self.sb_group.setMaximum(12)
        self.sb_group.setProperty("value", 5)
        self.sb_group.setObjectName("sb_group")
        self.gridLayout_4.addWidget(self.sb_group, 0, 2, 1, 1)
        self.sb_radius = QtWidgets.QSpinBox(self.widget_3)
        self.sb_radius.setMinimum(0)
        self.sb_radius.setMaximum(25)
        self.sb_radius.setObjectName("sb_radius")
        self.gridLayout_4.addWidget(self.sb_radius, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.widget_3, 2, 0, 1, 5)
        self.btn_openfo = QtWidgets.QToolButton(self.gp_output)
        self.btn_openfo.setObjectName("btn_openfo")
        self.gridLayout_3.addWidget(self.btn_openfo, 0, 2, 1, 1)
        self.le_fileoutput = QtWidgets.QLineEdit(self.gp_output)
        self.le_fileoutput.setEnabled(False)
        self.le_fileoutput.setMinimumSize(QtCore.QSize(100, 40))
        self.le_fileoutput.setStyleSheet("")
        self.le_fileoutput.setObjectName("le_fileoutput")
        self.gridLayout_3.addWidget(self.le_fileoutput, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gp_output)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.btn_same = QtWidgets.QPushButton(self.gp_output)
        self.btn_same.setObjectName("btn_same")
        self.gridLayout_3.addWidget(self.btn_same, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.gp_output, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 12))
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 0, 0, 1, 1)
        self.gb_input = QtWidgets.QGroupBox(Form)
        self.gb_input.setMinimumSize(QtCore.QSize(0, 80))
        self.gb_input.setMaximumSize(QtCore.QSize(16777215, 80))
        self.gb_input.setObjectName("gb_input")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gb_input)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.gb_input)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.le_fileinput = QtWidgets.QLineEdit(self.gb_input)
        self.le_fileinput.setEnabled(False)
        self.le_fileinput.setMinimumSize(QtCore.QSize(100, 40))
        self.le_fileinput.setObjectName("le_fileinput")
        self.gridLayout_2.addWidget(self.le_fileinput, 0, 1, 1, 1)
        self.btn_openfi = QtWidgets.QToolButton(self.gb_input)
        self.btn_openfi.setObjectName("btn_openfi")
        self.gridLayout_2.addWidget(self.btn_openfi, 0, 2, 1, 1)
        self.btn_reopen = QtWidgets.QToolButton(self.gb_input)
        self.btn_reopen.setMinimumSize(QtCore.QSize(80, 0))
        self.btn_reopen.setObjectName("btn_reopen")
        self.gridLayout_2.addWidget(self.btn_reopen, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.gb_input, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(0, 80))
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lbl_version = QtWidgets.QLabel(self.widget)
        self.lbl_version.setText("")
        self.lbl_version.setObjectName("lbl_version")
        self.gridLayout_5.addWidget(self.lbl_version, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 1, 1, 1)
        self.lbl_numpoints = QtWidgets.QLabel(self.widget)
        self.lbl_numpoints.setText("")
        self.lbl_numpoints.setObjectName("lbl_numpoints")
        self.gridLayout_5.addWidget(self.lbl_numpoints, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 1, 3, 1, 1)
        self.sb_binning = QtWidgets.QSpinBox(self.widget)
        self.sb_binning.setMinimum(1)
        self.sb_binning.setMaximum(20)
        self.sb_binning.setObjectName("sb_binning")
        self.gridLayout_5.addWidget(self.sb_binning, 0, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.widget, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn_openfi, QtCore.SIGNAL("clicked()"), Form.actionSelectInputFile)
        QtCore.QObject.connect(self.btn_reopen, QtCore.SIGNAL("clicked()"), Form.actionUpdateFile)
        QtCore.QObject.connect(self.btn_openfo, QtCore.SIGNAL("clicked()"), Form.actionSelectOutputFile)
        QtCore.QObject.connect(self.btn_process, QtCore.SIGNAL("clicked()"), Form.actionProcessFile)
        QtCore.QObject.connect(self.btn_same, QtCore.SIGNAL("clicked()"), Form.actionMakeSamePath)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.le_fileinput, self.btn_openfi)
        Form.setTabOrder(self.btn_openfi, self.btn_reopen)
        Form.setTabOrder(self.btn_reopen, self.sb_binning)
        Form.setTabOrder(self.sb_binning, self.le_fileoutput)
        Form.setTabOrder(self.le_fileoutput, self.btn_openfo)
        Form.setTabOrder(self.btn_openfo, self.btn_same)
        Form.setTabOrder(self.btn_same, self.btn_process)
        Form.setTabOrder(self.btn_process, self.sb_group)
        Form.setTabOrder(self.sb_group, self.sb_radius)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.gp_output.setTitle(QtWidgets.QApplication.translate("Form", "Output", None, -1))
        self.btn_process.setToolTip(QtWidgets.QApplication.translate("Form", "Process the data and saves. Filters the points having the same pixel position or position inside the radius", None, -1))
        self.btn_process.setText(QtWidgets.QApplication.translate("Form", "Process", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Form", "Final Group", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Form", "Options:", None, -1))
        self.sb_group.setToolTip(QtWidgets.QApplication.translate("Form", "All points which have same pixel position, or position within the radius will be saved with a final group", None, -1))
        self.sb_radius.setToolTip(QtWidgets.QApplication.translate("Form", "Radius within which points lying close to the diamonds will be filtered", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Form", "Radius", None, -1))
        self.btn_openfo.setToolTip(QtWidgets.QApplication.translate("Form", "Select output file (.tabbin)", None, -1))
        self.btn_openfo.setText(QtWidgets.QApplication.translate("Form", "...", None, -1))
        self.le_fileoutput.setToolTip(QtWidgets.QApplication.translate("Form", "Crysalis output filename (.tabbin)", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Filename:", None, -1))
        self.btn_same.setToolTip(QtWidgets.QApplication.translate("Form", "Makes the output file the same as the input file", None, -1))
        self.btn_same.setText(QtWidgets.QApplication.translate("Form", "Same", None, -1))
        self.gb_input.setTitle(QtWidgets.QApplication.translate("Form", "Input", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Filename:", None, -1))
        self.btn_openfi.setToolTip(QtWidgets.QApplication.translate("Form", "Open .tabbin file for processing", None, -1))
        self.btn_openfi.setText(QtWidgets.QApplication.translate("Form", "...", None, -1))
        self.btn_reopen.setToolTip(QtWidgets.QApplication.translate("Form", "Update or reload the selected .tabbin file", None, -1))
        self.btn_reopen.setText(QtWidgets.QApplication.translate("Form", "refresh", None, -1))
        self.lbl_version.setToolTip(QtWidgets.QApplication.translate("Form", "Version of the .tabbin file", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Num. points:", None, -1))
        self.lbl_numpoints.setToolTip(QtWidgets.QApplication.translate("Form", "Number of points inside the .tabbin file", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "Version:", None, -1))
        self.sb_binning.setToolTip(QtWidgets.QApplication.translate("Form", "Binning option for pixel merging (file opening only)", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Binning:", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

