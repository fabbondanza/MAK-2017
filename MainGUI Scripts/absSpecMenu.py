# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'absorbancespectrum_menu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class absSpecMenu(QtGui.QWidget):
    def __init__(self):
        super(absSpecMenu, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName(_fromUtf8("Absorbance Spec Menu"))
        self.resize(591, 126)
        self.label_7 = QtGui.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(50, 30, 21, 21))
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
        self.label_12 = QtGui.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(160, 50, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_12.setLineWidth(1)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_14 = QtGui.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(520, 50, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_14.setLineWidth(1)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_10 = QtGui.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(330, 30, 71, 21))
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
        self.label_6 = QtGui.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(40, 30, 531, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtGui.QFrame.Panel)
        self.label_6.setFrameShadow(QtGui.QFrame.Plain)
        self.label_6.setLineWidth(1)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.exposureTimeBox = QtGui.QSpinBox(self)
        self.exposureTimeBox.setGeometry(QtCore.QRect(410, 50, 101, 22))
        self.exposureTimeBox.setMinimum(1)
        self.exposureTimeBox.setMaximum(6500)
        self.exposureTimeBox.setObjectName(_fromUtf8("exposureTimeBox"))
        self.label_15 = QtGui.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(430, 70, 61, 21))
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
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(150, 30, 71, 21))
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
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 201, 21))
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
        self.label_9 = QtGui.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(380, 30, 71, 21))
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
        self.label_8 = QtGui.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(300, 30, 21, 21))
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
        self.startWavelengthBox = QtGui.QSpinBox(self)
        self.startWavelengthBox.setGeometry(QtCore.QRect(90, 50, 61, 22))
        self.startWavelengthBox.setMinimum(350)
        self.startWavelengthBox.setMaximum(700)
        self.startWavelengthBox.setObjectName(_fromUtf8("startWavelengthBox"))
        self.label_13 = QtGui.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(310, 50, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_13.setLineWidth(1)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(80, 30, 71, 21))
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
        self.label_11 = QtGui.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(60, 50, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_11.setLineWidth(1)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_16 = QtGui.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(60, 80, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_16.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_16.setLineWidth(1)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.stopWavelengthBox = QtGui.QSpinBox(self)
        self.stopWavelengthBox.setGeometry(QtCore.QRect(90, 80, 61, 22))
        self.stopWavelengthBox.setMinimum(350)
        self.stopWavelengthBox.setMaximum(700)
        self.stopWavelengthBox.setObjectName(_fromUtf8("stopWavelengthBox"))
        self.label_17 = QtGui.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(160, 80, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_17.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_17.setLineWidth(1)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.closeButton = QtGui.QPushButton(self)
        self.closeButton.setGeometry(QtCore.QRect(550, 10, 21, 20))
        self.closeButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Python_GUI/x-mark-4-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QtCore.QSize(12, 12))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.moveUpButton = QtGui.QPushButton(self)
        self.moveUpButton.setGeometry(QtCore.QRect(10, 50, 21, 20))
        self.moveUpButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../Python_GUI/MoveUpLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveUpButton.setIcon(icon1)
        self.moveUpButton.setObjectName(_fromUtf8("moveUpButton"))
        self.moveDownButton = QtGui.QPushButton(self)
        self.moveDownButton.setGeometry(QtCore.QRect(10, 70, 21, 20))
        self.moveDownButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../Python_GUI/MoveDownLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveDownButton.setIcon(icon2)
        self.moveDownButton.setObjectName(_fromUtf8("moveDownButton"))
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_12.raise_()
        self.label_14.raise_()
        self.label_10.raise_()
        self.exposureTimeBox.raise_()
        self.label_15.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.label_9.raise_()
        self.label_8.raise_()
        self.startWavelengthBox.raise_()
        self.label_13.raise_()
        self.label_4.raise_()
        self.label_11.raise_()
        self.label_16.raise_()
        self.stopWavelengthBox.raise_()
        self.label_17.raise_()
        self.closeButton.raise_()
        self.moveUpButton.raise_()
        self.moveDownButton.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Absorbance Spec Menu", "Absorbance Spec Menu", None))
        self.label_12.setText(_translate("Absorbance Spec Menu", "(nm)", None))
        self.label_14.setText(_translate("Absorbance Spec Menu", "(ms)", None))
        self.label_10.setText(_translate("Absorbance Spec Menu", "Reading", None))
        self.label_15.setText(_translate("Absorbance Spec Menu", " Max: 6500", None))
        self.label_2.setText(_translate("Absorbance Spec Menu", "Absorbance Spectrum", None))
        self.label_13.setText(_translate("Absorbance Spec Menu", "Exposure Time:", None))
        self.label_4.setText(_translate("Absorbance Spec Menu", "Wavelength", None))
        self.label_11.setText(_translate("Absorbance Spec Menu", "Start:", None))
        self.label_16.setText(_translate("Absorbance Spec Menu", "Stop:", None))
        self.label_17.setText(_translate("Absorbance Spec Menu", "(nm)", None))

