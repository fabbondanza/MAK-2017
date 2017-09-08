# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'replacement_options_menu.ui'
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

class optionsMenu(QtGui.QWidget):
    def __init__(self):
        super(optionsMenu, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName(_fromUtf8("Options Menu"))
        self.resize(226, 458)
        self.kamLogo = QtGui.QLabel(self)
        self.kamLogo.setGeometry(QtCore.QRect(10, -10, 241, 231))
        self.kamLogo.setText(_fromUtf8(""))
        self.kamLogo.setPixmap(QtGui.QPixmap(_fromUtf8("../Python_GUI/KAM-Spec Logo LtoH.svg")))
        self.kamLogo.setScaledContents(True)
        self.kamLogo.setObjectName(_fromUtf8("kamLogo"))
        self.line = QtGui.QFrame(self)
        self.line.setGeometry(QtCore.QRect(10, 170, 201, 20))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(10, 370, 201, 20))
        self.line_2.setFrameShadow(QtGui.QFrame.Plain)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.runButton = QtGui.QPushButton(self)
        self.runButton.setGeometry(QtCore.QRect(10, 400, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.runButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Python_GUI/RunLogo2.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runButton.setIcon(icon)
        self.runButton.setIconSize(QtCore.QSize(45, 45))
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 200, 160, 185))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addPlateButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addPlateButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../Python_GUI/AddPlateLogo2.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addPlateButton.setIcon(icon1)
        self.addPlateButton.setIconSize(QtCore.QSize(50, 50))
        self.addPlateButton.setObjectName(_fromUtf8("addPlateButton"))
        self.verticalLayout.addWidget(self.addPlateButton)
        self.calibrateButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calibrateButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../Python_GUI/CalibrateLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calibrateButton.setIcon(icon2)
        self.calibrateButton.setIconSize(QtCore.QSize(50, 50))
        self.calibrateButton.setObjectName(_fromUtf8("calibrateButton"))
        self.verticalLayout.addWidget(self.calibrateButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plateOutButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plateOutButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../Python_GUI/red-down-arrow-hi.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plateOutButton.setIcon(icon3)
        self.plateOutButton.setIconSize(QtCore.QSize(15, 15))
        self.plateOutButton.setObjectName(_fromUtf8("plateOutButton"))
        self.horizontalLayout.addWidget(self.plateOutButton)
        self.plateInButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plateInButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../Python_GUI/green-up-arrow.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plateInButton.setIcon(icon4)
        self.plateInButton.setIconSize(QtCore.QSize(15, 15))
        self.plateInButton.setObjectName(_fromUtf8("plateInButton"))
        self.horizontalLayout.addWidget(self.plateInButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Options Menu", "Options Menu", None))
        self.runButton.setText(_translate("Options Menu", "Run Protocol", None))
        self.addPlateButton.setText(_translate("Options Menu", "Add Plate", None))
        self.calibrateButton.setText(_translate("Options Menu", "Calibrate", None))
        self.plateOutButton.setText(_translate("Options Menu", "Plate\n"
" Out", None))
        self.plateInButton.setText(_translate("Options Menu", "Plate\n"
" In", None))

