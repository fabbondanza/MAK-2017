# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
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

class protocolSelectScreen(QtGui.QWidget):
    def __init__(self):
        super(protocolSelectScreen, self).__init__()
        self.initUI()
        #self.show()

    def initUI(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(794, 430)
        self.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.absButton = QtGui.QPushButton(self)
        self.absButton.setGeometry(QtCore.QRect(20, 30, 351, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.absButton.setFont(font)
        self.absButton.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 127);"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("absorbanceLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.absButton.setIcon(icon)
        self.absButton.setIconSize(QtCore.QSize(50, 50))
        self.absButton.setObjectName(_fromUtf8("absButton"))
        self.absSpecButton = QtGui.QPushButton(self)
        self.absSpecButton.setGeometry(QtCore.QRect(390, 30, 351, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.absSpecButton.setFont(font)
        self.absSpecButton.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 127);"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("absSpectrumLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.absSpecButton.setIcon(icon1)
        self.absSpecButton.setIconSize(QtCore.QSize(50, 50))
        self.absSpecButton.setObjectName(_fromUtf8("absSpecButton"))
        self.flrButton = QtGui.QPushButton(self)
        self.flrButton.setGeometry(QtCore.QRect(20, 150, 351, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.flrButton.setFont(font)
        self.flrButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 255);"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("flourescenceLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flrButton.setIcon(icon2)
        self.flrButton.setIconSize(QtCore.QSize(50, 50))
        self.flrButton.setObjectName(_fromUtf8("flrButton"))
        self.flrSpecButton = QtGui.QPushButton(self)
        self.flrSpecButton.setGeometry(QtCore.QRect(390, 150, 351, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.flrSpecButton.setFont(font)
        self.flrSpecButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 255);"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("flrSpectrumLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flrSpecButton.setIcon(icon3)
        self.flrSpecButton.setIconSize(QtCore.QSize(50, 50))
        self.flrSpecButton.setObjectName(_fromUtf8("flrSpecButton"))
        self.addPlateButton = QtGui.QPushButton(self)
        self.addPlateButton.setGeometry(QtCore.QRect(390, 270, 351, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.addPlateButton.setFont(font)
        self.addPlateButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("AddPlateLogo2.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addPlateButton.setIcon(icon4)
        self.addPlateButton.setIconSize(QtCore.QSize(70, 70))
        self.addPlateButton.setObjectName(_fromUtf8("addPlateButton"))
        self.shakingButton = QtGui.QPushButton(self)
        self.shakingButton.setGeometry(QtCore.QRect(20, 270, 351, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.shakingButton.setFont(font)
        self.shakingButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("shakeLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shakingButton.setIcon(icon5)
        self.shakingButton.setIconSize(QtCore.QSize(65, 65))
        self.shakingButton.setObjectName(_fromUtf8("shakingButton"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle('KAM-Spec 2017')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('KAM-Spec Logo LtoH.svg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.absButton.setText(_translate("self", "Absorbance", None))
        self.absSpecButton.setText(_translate("self", "Absorbance \n"
"  Spectrum", None))
        self.flrButton.setText(_translate("self", "Flourescent \n"
"  Intensity", None))
        self.flrSpecButton.setText(_translate("self", "Flourescence \n"
"  Spectrum", None))
        self.addPlateButton.setText(_translate("self", "      Add \n"
" New Plate", None))
        self.shakingButton.setText(_translate("self", "Shaking", None))

