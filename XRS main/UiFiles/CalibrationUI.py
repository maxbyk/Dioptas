# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calibration.ui'
#
# Created: Sun May 11 08:38:22 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_XrsCalibrationWidget(object):
    def setupUi(self, XrsCalibrationWidget):
        XrsCalibrationWidget.setObjectName(_fromUtf8("XrsCalibrationWidget"))
        XrsCalibrationWidget.resize(1027, 688)
        XrsCalibrationWidget.setMinimumSize(QtCore.QSize(5, 5))
        XrsCalibrationWidget.setStyleSheet(_fromUtf8(""))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(XrsCalibrationWidget)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.splitter = QtGui.QSplitter(XrsCalibrationWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tab_widget = QtGui.QTabWidget(self.widget)
        self.tab_widget.setObjectName(_fromUtf8("tab_widget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.img_pg_layout = GraphicsLayoutWidget(self.tab)
        self.img_pg_layout.setMinimumSize(QtCore.QSize(5, 5))
        self.img_pg_layout.setFrameShape(QtGui.QFrame.NoFrame)
        self.img_pg_layout.setFrameShadow(QtGui.QFrame.Plain)
        self.img_pg_layout.setObjectName(_fromUtf8("img_pg_layout"))
        self.horizontalLayout_2.addWidget(self.img_pg_layout)
        self.tab_widget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cake_pg_layout = GraphicsLayoutWidget(self.tab_2)
        self.cake_pg_layout.setObjectName(_fromUtf8("cake_pg_layout"))
        self.horizontalLayout_3.addWidget(self.cake_pg_layout)
        self.tab_widget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.spectrum_pg_layout = GraphicsLayoutWidget(self.tab_3)
        self.spectrum_pg_layout.setMinimumSize(QtCore.QSize(5, 5))
        self.spectrum_pg_layout.setSizeIncrement(QtCore.QSize(5, 5))
        self.spectrum_pg_layout.setBaseSize(QtCore.QSize(5, 5))
        self.spectrum_pg_layout.setObjectName(_fromUtf8("spectrum_pg_layout"))
        self.horizontalLayout_7.addWidget(self.spectrum_pg_layout)
        self.tab_widget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tab_widget)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.integrate_btn = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.integrate_btn.sizePolicy().hasHeightForWidth())
        self.integrate_btn.setSizePolicy(sizePolicy)
        self.integrate_btn.setMinimumSize(QtCore.QSize(300, 0))
        self.integrate_btn.setObjectName(_fromUtf8("integrate_btn"))
        self.horizontalLayout_4.addWidget(self.integrate_btn)
        spacerItem = QtGui.QSpacerItem(168, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pos_lbl = QtGui.QLabel(self.widget)
        self.pos_lbl.setObjectName(_fromUtf8("pos_lbl"))
        self.horizontalLayout_4.addWidget(self.pos_lbl)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.load_file_btn = QtGui.QPushButton(self.layoutWidget)
        self.load_file_btn.setMaximumSize(QtCore.QSize(1677215, 16777215))
        self.load_file_btn.setObjectName(_fromUtf8("load_file_btn"))
        self.verticalLayout_4.addWidget(self.load_file_btn)
        self.filename_lbl = QtGui.QLabel(self.layoutWidget)
        self.filename_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.filename_lbl.setObjectName(_fromUtf8("filename_lbl"))
        self.verticalLayout_4.addWidget(self.filename_lbl)
        self.ToolBox = QtGui.QToolBox(self.layoutWidget)
        self.ToolBox.setObjectName(_fromUtf8("ToolBox"))
        self.toolBoxPage1 = QtGui.QWidget()
        self.toolBoxPage1.setGeometry(QtCore.QRect(0, 0, 339, 438))
        self.toolBoxPage1.setObjectName(_fromUtf8("toolBoxPage1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.toolBoxPage1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.toolBoxPage1)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sv_distance_txt = QtGui.QLineEdit(self.toolBoxPage1)
        self.sv_distance_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sv_distance_txt.setObjectName(_fromUtf8("sv_distance_txt"))
        self.gridLayout.addWidget(self.sv_distance_txt, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.toolBoxPage1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.toolBoxPage1)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.sv_wavelength_txt = QtGui.QLineEdit(self.toolBoxPage1)
        self.sv_wavelength_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sv_wavelength_txt.setObjectName(_fromUtf8("sv_wavelength_txt"))
        self.gridLayout.addWidget(self.sv_wavelength_txt, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.toolBoxPage1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.toolBoxPage1)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.sv_pixel_width_txt = QtGui.QLineEdit(self.toolBoxPage1)
        self.sv_pixel_width_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sv_pixel_width_txt.setObjectName(_fromUtf8("sv_pixel_width_txt"))
        self.gridLayout.addWidget(self.sv_pixel_width_txt, 2, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.toolBoxPage1)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.toolBoxPage1)
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.sv_pixel_height_txt = QtGui.QLineEdit(self.toolBoxPage1)
        self.sv_pixel_height_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sv_pixel_height_txt.setObjectName(_fromUtf8("sv_pixel_height_txt"))
        self.gridLayout.addWidget(self.sv_pixel_height_txt, 3, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.toolBoxPage1)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.toolBoxPage1)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.calibrant_cb = QtGui.QComboBox(self.toolBoxPage1)
        self.calibrant_cb.setEditable(False)
        self.calibrant_cb.setFrame(True)
        self.calibrant_cb.setObjectName(_fromUtf8("calibrant_cb"))
        self.gridLayout.addWidget(self.calibrant_cb, 4, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.rotate_p90_btn = QtGui.QPushButton(self.toolBoxPage1)
        self.rotate_p90_btn.setObjectName(_fromUtf8("rotate_p90_btn"))
        self.gridLayout_4.addWidget(self.rotate_p90_btn, 0, 0, 1, 1)
        self.rotate_m90_btn = QtGui.QPushButton(self.toolBoxPage1)
        self.rotate_m90_btn.setObjectName(_fromUtf8("rotate_m90_btn"))
        self.gridLayout_4.addWidget(self.rotate_m90_btn, 0, 1, 1, 1)
        self.invert_horizontal_btn = QtGui.QPushButton(self.toolBoxPage1)
        self.invert_horizontal_btn.setObjectName(_fromUtf8("invert_horizontal_btn"))
        self.gridLayout_4.addWidget(self.invert_horizontal_btn, 1, 0, 1, 1)
        self.invert_vertical_btn = QtGui.QPushButton(self.toolBoxPage1)
        self.invert_vertical_btn.setObjectName(_fromUtf8("invert_vertical_btn"))
        self.gridLayout_4.addWidget(self.invert_vertical_btn, 1, 1, 1, 1)
        self.reset_transformations_btn = QtGui.QPushButton(self.toolBoxPage1)
        self.reset_transformations_btn.setObjectName(_fromUtf8("reset_transformations_btn"))
        self.gridLayout_4.addWidget(self.reset_transformations_btn, 2, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_4)
        spacerItem1 = QtGui.QSpacerItem(20, 178, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.ToolBox.addItem(self.toolBoxPage1, _fromUtf8(""))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 339, 438))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label_10 = QtGui.QLabel(self.page)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_5.addWidget(self.label_10)
        self.peak_num_sb = QtGui.QSpinBox(self.page)
        self.peak_num_sb.setMinimum(1)
        self.peak_num_sb.setObjectName(_fromUtf8("peak_num_sb"))
        self.horizontalLayout_5.addWidget(self.peak_num_sb)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.automatic_peak_num_inc_cb = QtGui.QCheckBox(self.page)
        self.automatic_peak_num_inc_cb.setChecked(True)
        self.automatic_peak_num_inc_cb.setObjectName(_fromUtf8("automatic_peak_num_inc_cb"))
        self.horizontalLayout_6.addWidget(self.automatic_peak_num_inc_cb)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.clear_peaks_btn = QtGui.QPushButton(self.page)
        self.clear_peaks_btn.setObjectName(_fromUtf8("clear_peaks_btn"))
        self.verticalLayout_6.addWidget(self.clear_peaks_btn)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.ToolBox.addItem(self.page, _fromUtf8(""))
        self.pyFAI = QtGui.QWidget()
        self.pyFAI.setGeometry(QtCore.QRect(0, 0, 339, 438))
        self.pyFAI.setObjectName(_fromUtf8("pyFAI"))
        self.gridLayout_3 = QtGui.QGridLayout(self.pyFAI)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_21 = QtGui.QLabel(self.pyFAI)
        self.label_21.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_3.addWidget(self.label_21, 0, 0, 1, 1)
        self.pf_distance_txt = QtGui.QLineEdit(self.pyFAI)
        self.pf_distance_txt.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pf_distance_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pf_distance_txt.setObjectName(_fromUtf8("pf_distance_txt"))
        self.gridLayout_3.addWidget(self.pf_distance_txt, 0, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.pyFAI)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_3.addWidget(self.label_20, 0, 2, 1, 1)
        self.pf_distance_cb = QtGui.QCheckBox(self.pyFAI)
        self.pf_distance_cb.setText(_fromUtf8(""))
        self.pf_distance_cb.setChecked(True)
        self.pf_distance_cb.setObjectName(_fromUtf8("pf_distance_cb"))
        self.gridLayout_3.addWidget(self.pf_distance_cb, 0, 3, 1, 1)
        self.label_22 = QtGui.QLabel(self.pyFAI)
        self.label_22.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_3.addWidget(self.label_22, 1, 0, 1, 1)
        self.pf_wavelength_txt = QtGui.QLineEdit(self.pyFAI)
        self.pf_wavelength_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pf_wavelength_txt.setObjectName(_fromUtf8("pf_wavelength_txt"))
        self.gridLayout_3.addWidget(self.pf_wavelength_txt, 1, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.pyFAI)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_3.addWidget(self.label_19, 1, 2, 1, 1)
        self.pf_wavelength_cb = QtGui.QCheckBox(self.pyFAI)
        self.pf_wavelength_cb.setText(_fromUtf8(""))
        self.pf_wavelength_cb.setObjectName(_fromUtf8("pf_wavelength_cb"))
        self.gridLayout_3.addWidget(self.pf_wavelength_cb, 1, 3, 1, 1)
        self.label_27 = QtGui.QLabel(self.pyFAI)
        self.label_27.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_3.addWidget(self.label_27, 2, 0, 1, 1)
        self.pf_poni1_txt = QtGui.QLineEdit(self.pyFAI)
        self.pf_poni1_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pf_poni1_txt.setObjectName(_fromUtf8("pf_poni1_txt"))
        self.gridLayout_3.addWidget(self.pf_poni1_txt, 2, 1, 1, 1)
        self.label_29 = QtGui.QLabel(self.pyFAI)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_3.addWidget(self.label_29, 2, 2, 1, 1)
        self.pf_poni2_txt = QtGui.QLineEdit(self.pyFAI)
        self.pf_poni2_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pf_poni2_txt.setObjectName(_fromUtf8("pf_poni2_txt"))
        self.gridLayout_3.addWidget(self.pf_poni2_txt, 3, 1, 1, 1)
        self.label_30 = QtGui.QLabel(self.pyFAI)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_3.addWidget(self.label_30, 3, 2, 1, 1)
        self.label_28 = QtGui.QLabel(self.pyFAI)
        self.label_28.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_3.addWidget(self.label_28, 4, 0, 1, 1)
        self.pf_rotation1_txt = QtGui.QLineEdit(self.pyFAI)
        self.pf_rotation1_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pf_rotation1_txt.setObjectName(_fromUtf8("pf_rotation1_txt"))
        self.gridLayout_3.addWidget(self.pf_rotation1_txt, 4, 1, 1, 1)
        self.label_31 = QtGui.QLabel(self.pyFAI)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_3.addWidget(self.label_31, 4, 2, 1, 1)
        self.pf_rotation2_txt = QtGui.QLineEdit(self.pyFAI)
        self.pf_rotation2_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pf_rotation2_txt.setObjectName(_fromUtf8("pf_rotation2_txt"))
        self.gridLayout_3.addWidget(self.pf_rotation2_txt, 5, 1, 1, 1)
        self.label_32 = QtGui.QLabel(self.pyFAI)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_3.addWidget(self.label_32, 5, 2, 1, 1)
        self.pf_rotation3_txt = QtGui.QLineEdit(self.pyFAI)
        self.pf_rotation3_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pf_rotation3_txt.setObjectName(_fromUtf8("pf_rotation3_txt"))
        self.gridLayout_3.addWidget(self.pf_rotation3_txt, 6, 1, 1, 1)
        self.label_33 = QtGui.QLabel(self.pyFAI)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_3.addWidget(self.label_33, 6, 2, 1, 1)
        self.label_46 = QtGui.QLabel(self.pyFAI)
        self.label_46.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.gridLayout_3.addWidget(self.label_46, 7, 0, 1, 1)
        self.pf_pixel_width_txt = QtGui.QLineEdit(self.pyFAI)
        self.pf_pixel_width_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pf_pixel_width_txt.setObjectName(_fromUtf8("pf_pixel_width_txt"))
        self.gridLayout_3.addWidget(self.pf_pixel_width_txt, 7, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.pyFAI)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 7, 2, 1, 1)
        self.label_47 = QtGui.QLabel(self.pyFAI)
        self.label_47.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.gridLayout_3.addWidget(self.label_47, 8, 0, 1, 1)
        self.pf_pixel_height_txt = QtGui.QLineEdit(self.pyFAI)
        self.pf_pixel_height_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pf_pixel_height_txt.setObjectName(_fromUtf8("pf_pixel_height_txt"))
        self.gridLayout_3.addWidget(self.pf_pixel_height_txt, 8, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.pyFAI)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 8, 2, 1, 1)
        self.pf_update_btn = QtGui.QPushButton(self.pyFAI)
        self.pf_update_btn.setObjectName(_fromUtf8("pf_update_btn"))
        self.gridLayout_3.addWidget(self.pf_update_btn, 9, 0, 1, 4)
        spacerItem5 = QtGui.QSpacerItem(20, 94, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 10, 1, 1, 1)
        self.ToolBox.addItem(self.pyFAI, _fromUtf8(""))
        self.toolBoxPage3 = QtGui.QWidget()
        self.toolBoxPage3.setGeometry(QtCore.QRect(0, 0, 339, 438))
        self.toolBoxPage3.setObjectName(_fromUtf8("toolBoxPage3"))
        self.gridLayout_7 = QtGui.QGridLayout(self.toolBoxPage3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_37 = QtGui.QLabel(self.toolBoxPage3)
        self.label_37.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout_7.addWidget(self.label_37, 0, 0, 1, 1)
        self.f2_distance_txt = QtGui.QLineEdit(self.toolBoxPage3)
        self.f2_distance_txt.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.f2_distance_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.f2_distance_txt.setObjectName(_fromUtf8("f2_distance_txt"))
        self.gridLayout_7.addWidget(self.f2_distance_txt, 0, 1, 1, 1)
        self.label_36 = QtGui.QLabel(self.toolBoxPage3)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout_7.addWidget(self.label_36, 0, 3, 1, 1)
        self.f2_distance_cb = QtGui.QCheckBox(self.toolBoxPage3)
        self.f2_distance_cb.setText(_fromUtf8(""))
        self.f2_distance_cb.setChecked(True)
        self.f2_distance_cb.setObjectName(_fromUtf8("f2_distance_cb"))
        self.gridLayout_7.addWidget(self.f2_distance_cb, 0, 4, 1, 1)
        self.label_34 = QtGui.QLabel(self.toolBoxPage3)
        self.label_34.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_7.addWidget(self.label_34, 1, 0, 1, 1)
        self.f2_wavelength_txt = QtGui.QLineEdit(self.toolBoxPage3)
        self.f2_wavelength_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.f2_wavelength_txt.setObjectName(_fromUtf8("f2_wavelength_txt"))
        self.gridLayout_7.addWidget(self.f2_wavelength_txt, 1, 1, 1, 1)
        self.label_38 = QtGui.QLabel(self.toolBoxPage3)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_7.addWidget(self.label_38, 1, 3, 1, 1)
        self.f2_wavelength_cb = QtGui.QCheckBox(self.toolBoxPage3)
        self.f2_wavelength_cb.setText(_fromUtf8(""))
        self.f2_wavelength_cb.setObjectName(_fromUtf8("f2_wavelength_cb"))
        self.gridLayout_7.addWidget(self.f2_wavelength_cb, 1, 4, 1, 1)
        self.label_39 = QtGui.QLabel(self.toolBoxPage3)
        self.label_39.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.gridLayout_7.addWidget(self.label_39, 2, 0, 1, 1)
        self.f2_center_x_txt = QtGui.QLineEdit(self.toolBoxPage3)
        self.f2_center_x_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.f2_center_x_txt.setObjectName(_fromUtf8("f2_center_x_txt"))
        self.gridLayout_7.addWidget(self.f2_center_x_txt, 2, 1, 1, 1)
        self.label_35 = QtGui.QLabel(self.toolBoxPage3)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout_7.addWidget(self.label_35, 2, 3, 1, 1)
        self.label_41 = QtGui.QLabel(self.toolBoxPage3)
        self.label_41.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_7.addWidget(self.label_41, 3, 0, 1, 1)
        self.f2_center_y_txt = QtGui.QLineEdit(self.toolBoxPage3)
        self.f2_center_y_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.f2_center_y_txt.setObjectName(_fromUtf8("f2_center_y_txt"))
        self.gridLayout_7.addWidget(self.f2_center_y_txt, 3, 1, 1, 1)
        self.label_40 = QtGui.QLabel(self.toolBoxPage3)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.gridLayout_7.addWidget(self.label_40, 3, 3, 1, 1)
        self.label_45 = QtGui.QLabel(self.toolBoxPage3)
        self.label_45.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.gridLayout_7.addWidget(self.label_45, 4, 0, 1, 1)
        self.f2_rotation_txt = QtGui.QLineEdit(self.toolBoxPage3)
        self.f2_rotation_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.f2_rotation_txt.setObjectName(_fromUtf8("f2_rotation_txt"))
        self.gridLayout_7.addWidget(self.f2_rotation_txt, 4, 1, 1, 1)
        self.label_44 = QtGui.QLabel(self.toolBoxPage3)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.gridLayout_7.addWidget(self.label_44, 4, 3, 1, 1)
        self.label_42 = QtGui.QLabel(self.toolBoxPage3)
        self.label_42.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_7.addWidget(self.label_42, 5, 0, 1, 1)
        self.f2_tilt_txt = QtGui.QLineEdit(self.toolBoxPage3)
        self.f2_tilt_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.f2_tilt_txt.setObjectName(_fromUtf8("f2_tilt_txt"))
        self.gridLayout_7.addWidget(self.f2_tilt_txt, 5, 1, 1, 1)
        self.label_43 = QtGui.QLabel(self.toolBoxPage3)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_7.addWidget(self.label_43, 5, 3, 1, 1)
        self.label_78 = QtGui.QLabel(self.toolBoxPage3)
        self.label_78.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_78.setObjectName(_fromUtf8("label_78"))
        self.gridLayout_7.addWidget(self.label_78, 6, 0, 1, 1)
        self.f2_pixel_width_txt = QtGui.QLineEdit(self.toolBoxPage3)
        self.f2_pixel_width_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.f2_pixel_width_txt.setObjectName(_fromUtf8("f2_pixel_width_txt"))
        self.gridLayout_7.addWidget(self.f2_pixel_width_txt, 6, 1, 1, 1)
        self.label_77 = QtGui.QLabel(self.toolBoxPage3)
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.gridLayout_7.addWidget(self.label_77, 6, 3, 1, 1)
        self.label_75 = QtGui.QLabel(self.toolBoxPage3)
        self.label_75.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_75.setObjectName(_fromUtf8("label_75"))
        self.gridLayout_7.addWidget(self.label_75, 7, 0, 1, 1)
        self.f2_pixel_height_txt = QtGui.QLineEdit(self.toolBoxPage3)
        self.f2_pixel_height_txt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.f2_pixel_height_txt.setObjectName(_fromUtf8("f2_pixel_height_txt"))
        self.gridLayout_7.addWidget(self.f2_pixel_height_txt, 7, 1, 1, 1)
        self.label_76 = QtGui.QLabel(self.toolBoxPage3)
        self.label_76.setObjectName(_fromUtf8("label_76"))
        self.gridLayout_7.addWidget(self.label_76, 7, 3, 1, 1)
        self.f2_update_btn = QtGui.QPushButton(self.toolBoxPage3)
        self.f2_update_btn.setObjectName(_fromUtf8("f2_update_btn"))
        self.gridLayout_7.addWidget(self.f2_update_btn, 8, 0, 1, 5)
        spacerItem6 = QtGui.QSpacerItem(20, 147, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem6, 9, 2, 1, 1)
        self.ToolBox.addItem(self.toolBoxPage3, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.ToolBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.load_calibration_btn = QtGui.QPushButton(self.layoutWidget)
        self.load_calibration_btn.setObjectName(_fromUtf8("load_calibration_btn"))
        self.horizontalLayout.addWidget(self.load_calibration_btn)
        self.save_calibration_btn = QtGui.QPushButton(self.layoutWidget)
        self.save_calibration_btn.setObjectName(_fromUtf8("save_calibration_btn"))
        self.horizontalLayout.addWidget(self.save_calibration_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_8.addWidget(self.splitter)

        self.retranslateUi(XrsCalibrationWidget)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QObject.connect(self.f2_distance_cb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pf_distance_cb.toggle)
        QtCore.QObject.connect(self.pf_distance_cb, QtCore.SIGNAL(_fromUtf8("clicked()")), self.f2_distance_cb.toggle)
        QtCore.QObject.connect(self.f2_wavelength_cb, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.pf_wavelength_cb.toggle)
        QtCore.QObject.connect(self.pf_wavelength_cb, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.f2_wavelength_cb.toggle)
        QtCore.QMetaObject.connectSlotsByName(XrsCalibrationWidget)
        XrsCalibrationWidget.setTabOrder(self.sv_distance_txt, self.sv_wavelength_txt)
        XrsCalibrationWidget.setTabOrder(self.sv_wavelength_txt, self.sv_pixel_width_txt)
        XrsCalibrationWidget.setTabOrder(self.sv_pixel_width_txt, self.sv_pixel_height_txt)
        XrsCalibrationWidget.setTabOrder(self.sv_pixel_height_txt, self.calibrant_cb)
        XrsCalibrationWidget.setTabOrder(self.calibrant_cb, self.rotate_p90_btn)
        XrsCalibrationWidget.setTabOrder(self.rotate_p90_btn, self.rotate_m90_btn)
        XrsCalibrationWidget.setTabOrder(self.rotate_m90_btn, self.invert_horizontal_btn)
        XrsCalibrationWidget.setTabOrder(self.invert_horizontal_btn, self.invert_vertical_btn)
        XrsCalibrationWidget.setTabOrder(self.invert_vertical_btn, self.pf_distance_txt)
        XrsCalibrationWidget.setTabOrder(self.pf_distance_txt, self.pf_distance_cb)
        XrsCalibrationWidget.setTabOrder(self.pf_distance_cb, self.pf_wavelength_txt)
        XrsCalibrationWidget.setTabOrder(self.pf_wavelength_txt, self.pf_wavelength_cb)
        XrsCalibrationWidget.setTabOrder(self.pf_wavelength_cb, self.pf_poni1_txt)
        XrsCalibrationWidget.setTabOrder(self.pf_poni1_txt, self.pf_poni2_txt)
        XrsCalibrationWidget.setTabOrder(self.pf_poni2_txt, self.pf_rotation1_txt)
        XrsCalibrationWidget.setTabOrder(self.pf_rotation1_txt, self.pf_rotation2_txt)
        XrsCalibrationWidget.setTabOrder(self.pf_rotation2_txt, self.pf_rotation3_txt)
        XrsCalibrationWidget.setTabOrder(self.pf_rotation3_txt, self.f2_distance_txt)
        XrsCalibrationWidget.setTabOrder(self.f2_distance_txt, self.f2_distance_cb)
        XrsCalibrationWidget.setTabOrder(self.f2_distance_cb, self.f2_wavelength_txt)
        XrsCalibrationWidget.setTabOrder(self.f2_wavelength_txt, self.f2_wavelength_cb)
        XrsCalibrationWidget.setTabOrder(self.f2_wavelength_cb, self.f2_center_x_txt)
        XrsCalibrationWidget.setTabOrder(self.f2_center_x_txt, self.f2_center_y_txt)
        XrsCalibrationWidget.setTabOrder(self.f2_center_y_txt, self.f2_tilt_txt)
        XrsCalibrationWidget.setTabOrder(self.f2_tilt_txt, self.f2_rotation_txt)
        XrsCalibrationWidget.setTabOrder(self.f2_rotation_txt, self.load_calibration_btn)
        XrsCalibrationWidget.setTabOrder(self.load_calibration_btn, self.save_calibration_btn)

    def retranslateUi(self, XrsCalibrationWidget):
        XrsCalibrationWidget.setWindowTitle(_translate("XrsCalibrationWidget", "XRS Calibration", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), _translate("XrsCalibrationWidget", "Image", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2),
                                   _translate("XrsCalibrationWidget", "Cake", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_3),
                                   _translate("XrsCalibrationWidget", "Spectrum", None))
        self.integrate_btn.setText(_translate("XrsCalibrationWidget", "Calibrate", None))
        self.pos_lbl.setText(_translate("XrsCalibrationWidget", "Position", None))
        self.load_file_btn.setText(_translate("XrsCalibrationWidget", "Load File", None))
        self.filename_lbl.setText(_translate("XrsCalibrationWidget", "Filename", None))
        self.label.setText(_translate("XrsCalibrationWidget", "Distance:", None))
        self.sv_distance_txt.setText(_translate("XrsCalibrationWidget", "400", None))
        self.label_6.setText(_translate("XrsCalibrationWidget", "mm", None))
        self.label_2.setText(_translate("XrsCalibrationWidget", "Wavelength:", None))
        self.sv_wavelength_txt.setText(_translate("XrsCalibrationWidget", "0.4133", None))
        self.label_7.setText(_translate("XrsCalibrationWidget", "Å", None))
        self.label_3.setText(_translate("XrsCalibrationWidget", "Pixelwidth:", None))
        self.sv_pixel_width_txt.setText(_translate("XrsCalibrationWidget", "200", None))
        self.label_8.setText(_translate("XrsCalibrationWidget", "μm", None))
        self.label_4.setText(_translate("XrsCalibrationWidget", "Pixelheight:", None))
        self.sv_pixel_height_txt.setText(_translate("XrsCalibrationWidget", "200", None))
        self.label_9.setText(_translate("XrsCalibrationWidget", "μm", None))
        self.label_5.setText(_translate("XrsCalibrationWidget", "Calibrant:", None))
        self.rotate_p90_btn.setText(_translate("XrsCalibrationWidget", "Rotate +90°", None))
        self.rotate_m90_btn.setText(_translate("XrsCalibrationWidget", "Rotate -90°", None))
        self.invert_horizontal_btn.setText(_translate("XrsCalibrationWidget", "Flip horizontal", None))
        self.invert_vertical_btn.setText(_translate("XrsCalibrationWidget", "Flip vertical", None))
        self.reset_transformations_btn.setText(_translate("XrsCalibrationWidget", "Reset Transformations", None))
        self.ToolBox.setItemText(self.ToolBox.indexOf(self.toolBoxPage1),
                                 _translate("XrsCalibrationWidget", "Start Values", None))
        self.label_10.setText(_translate("XrsCalibrationWidget", "Current peaknumber:", None))
        self.automatic_peak_num_inc_cb.setText(_translate("XrsCalibrationWidget", "automatic", None))
        self.clear_peaks_btn.setText(_translate("XrsCalibrationWidget", "Clear All Peaks", None))
        self.ToolBox.setItemText(self.ToolBox.indexOf(self.page),
                                 _translate("XrsCalibrationWidget", "Peakpicker", None))
        self.label_21.setText(_translate("XrsCalibrationWidget", "Distance:", None))
        self.label_20.setText(_translate("XrsCalibrationWidget", "mm", None))
        self.label_22.setText(_translate("XrsCalibrationWidget", "Wavelength:", None))
        self.label_19.setText(_translate("XrsCalibrationWidget", "Å", None))
        self.label_27.setText(_translate("XrsCalibrationWidget", "PONI:", None))
        self.label_29.setText(_translate("XrsCalibrationWidget", "m", None))
        self.label_30.setText(_translate("XrsCalibrationWidget", "m", None))
        self.label_28.setText(_translate("XrsCalibrationWidget", "Rotations:", None))
        self.label_31.setText(_translate("XrsCalibrationWidget", "rad", None))
        self.label_32.setText(_translate("XrsCalibrationWidget", "rad", None))
        self.label_33.setText(_translate("XrsCalibrationWidget", "rad", None))
        self.label_46.setText(_translate("XrsCalibrationWidget", "Pixelwidth:", None))
        self.label_11.setText(_translate("XrsCalibrationWidget", "μm", None))
        self.label_47.setText(_translate("XrsCalibrationWidget", "Pixelheight:", None))
        self.label_12.setText(_translate("XrsCalibrationWidget", "μm", None))
        self.pf_update_btn.setText(_translate("XrsCalibrationWidget", "Update", None))
        self.ToolBox.setItemText(self.ToolBox.indexOf(self.pyFAI),
                                 _translate("XrsCalibrationWidget", "pyFAI Calibration", None))
        self.label_37.setText(_translate("XrsCalibrationWidget", "Distance:", None))
        self.label_36.setText(_translate("XrsCalibrationWidget", "mm", None))
        self.label_34.setText(_translate("XrsCalibrationWidget", "Wavelength:", None))
        self.label_38.setText(_translate("XrsCalibrationWidget", "Å", None))
        self.label_39.setText(_translate("XrsCalibrationWidget", "Center X:", None))
        self.label_35.setText(_translate("XrsCalibrationWidget", "px", None))
        self.label_41.setText(_translate("XrsCalibrationWidget", "Center Y:", None))
        self.label_40.setText(_translate("XrsCalibrationWidget", "px", None))
        self.label_45.setText(_translate("XrsCalibrationWidget", "Rotation:", None))
        self.label_44.setText(_translate("XrsCalibrationWidget", "deg", None))
        self.label_42.setText(_translate("XrsCalibrationWidget", "Tilt:", None))
        self.label_43.setText(_translate("XrsCalibrationWidget", "deg", None))
        self.label_78.setText(_translate("XrsCalibrationWidget", "Pixelwidth:", None))
        self.label_77.setText(_translate("XrsCalibrationWidget", "μm", None))
        self.label_75.setText(_translate("XrsCalibrationWidget", "Pixelheight:", None))
        self.label_76.setText(_translate("XrsCalibrationWidget", "μm", None))
        self.f2_update_btn.setText(_translate("XrsCalibrationWidget", "Update", None))
        self.ToolBox.setItemText(self.ToolBox.indexOf(self.toolBoxPage3),
                                 _translate("XrsCalibrationWidget", "Fit2D Calibration", None))
        self.load_calibration_btn.setText(_translate("XrsCalibrationWidget", "Load Calibration", None))
        self.save_calibration_btn.setText(_translate("XrsCalibrationWidget", "Save Calibration", None))


from pyqtgraph import GraphicsLayoutWidget
