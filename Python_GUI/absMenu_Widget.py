# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'absorbance_menu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from protocol_functionality_test import *

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

class absMenu_Widget(QtGui.QWidget):
    def __init__(self):
        super(absMenu_Widget, self).__init__()
        self.initUI()
    def initUI(self):
        self.setObjectName(_fromUtf8("Absorbance Menu"))
        self.resize(547, 85)
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_2.setLineWidth(1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_6 = QtGui.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 531, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtGui.QFrame.Panel)
        self.label_6.setFrameShadow(QtGui.QFrame.Plain)
        self.label_6.setLineWidth(1)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_4.setLineWidth(1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(120, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtGui.QFrame.HLine)
        self.label_5.setFrameShadow(QtGui.QFrame.Plain)
        self.label_5.setLineWidth(2)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 21, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtGui.QFrame.HLine)
        self.label_7.setFrameShadow(QtGui.QFrame.Plain)
        self.label_7.setLineWidth(2)
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(270, 20, 21, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtGui.QFrame.HLine)
        self.label_8.setFrameShadow(QtGui.QFrame.Plain)
        self.label_8.setLineWidth(2)
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(350, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtGui.QFrame.HLine)
        self.label_9.setFrameShadow(QtGui.QFrame.Plain)
        self.label_9.setLineWidth(2)
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(300, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_10.setLineWidth(1)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.spinBox = QtGui.QSpinBox(self)
        self.spinBox.setGeometry(QtCore.QRect(120, 40, 61, 22))
        self.spinBox.setMinimum(350)
        self.spinBox.setMaximum(700)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_11 = QtGui.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(30, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_11.setLineWidth(1)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(190, 40, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_12.setLineWidth(1)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(280, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_13.setLineWidth(1)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.spinBox_2 = QtGui.QSpinBox(self)
        self.spinBox_2.setGeometry(QtCore.QRect(380, 40, 101, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(6500)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.label_14 = QtGui.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(490, 40, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_14.setLineWidth(1)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(400, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_15.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_15.setLineWidth(1)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.absButton = QtGui.QPushButton(self)
        self.absButton.setGeometry(QtCore.QRect(510, 0, 31, 20))
        self.absButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("x-mark-4-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.absButton.setIcon(icon)
        self.absButton.setObjectName(_fromUtf8("absButton"))
        self.label_6.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.spinBox.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.spinBox_2.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.absButton.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Absorbance Menu", "Absorbance Menu", None))
        self.label_2.setText(_translate("Absorbance Menu", "Absorbance", None))
        self.label_4.setText(_translate("Absorbance Menu", "Wavelength", None))
        self.label_10.setText(_translate("Absorbance Menu", "Reading", None))
        self.label_11.setText(_translate("Absorbance Menu", "Measurement:", None))
        self.label_12.setText(_translate("Absorbance Menu", "(nm)", None))
        self.label_13.setText(_translate("Absorbance Menu", "Exposure Time:", None))
        self.label_14.setText(_translate("Absorbance Menu", "(ms)", None))
        self.label_15.setText(_translate("Absorbance Menu", " Max: 6500", None))



