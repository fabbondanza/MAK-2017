# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'flrMenu_v2.ui'
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

class flrMenu(QtGui.QWidget):
    def __init__(self):
        super(flrMenu, self).__init__()
        self.initUI()
        self.exposureTimeScrollBar.valueChanged.connect(self.exposureTimeSpinBox.setValue)

    def initUI(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(794, 430)
        self.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.line = QtGui.QFrame(self)
        self.line.setGeometry(QtCore.QRect(10, 60, 651, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 751, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.exposureTimeSpinBox = QtGui.QSpinBox(self)
        self.exposureTimeSpinBox.setGeometry(QtCore.QRect(320, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(20)
        self.exposureTimeSpinBox.setFont(font)
        self.exposureTimeSpinBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.exposureTimeSpinBox.setMinimum(1)
        self.exposureTimeSpinBox.setMaximum(6500)
        self.exposureTimeSpinBox.setObjectName(_fromUtf8("exposureTimeSpinBox"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 391, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(450, 100, 71, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 571, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(390, 170, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.finishButton = QtGui.QPushButton(self)
        self.finishButton.setGeometry(QtCore.QRect(600, 330, 181, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.finishButton.setFont(font)
        self.finishButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 57, 43);"))
        self.finishButton.setObjectName(_fromUtf8("finishButton"))
        self.addProtocolButton = QtGui.QPushButton(self)
        self.addProtocolButton.setGeometry(QtCore.QRect(410, 330, 181, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.addProtocolButton.setFont(font)
        self.addProtocolButton.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 127);"))
        self.addProtocolButton.setObjectName(_fromUtf8("addProtocolButton"))
        self.excitationWavelengthComboBox = QtGui.QComboBox(self)
        self.excitationWavelengthComboBox.setGeometry(QtCore.QRect(270, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(20)
        self.excitationWavelengthComboBox.setFont(font)
        self.excitationWavelengthComboBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(170, 255, 255);"))
        self.excitationWavelengthComboBox.setObjectName(_fromUtf8("excitationWavelengthComboBox"))
        self.excitationWavelengthComboBox.addItem(_fromUtf8(""))
        self.excitationWavelengthComboBox.addItem(_fromUtf8(""))
        self.excitationWavelengthComboBox.addItem(_fromUtf8(""))
        self.exposureTimeScrollBar = QtGui.QScrollBar(self)
        self.exposureTimeScrollBar.setGeometry(QtCore.QRect(560, 110, 191, 31))
        self.exposureTimeScrollBar.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 127);"))
        self.exposureTimeScrollBar.setMinimum(1)
        self.exposureTimeScrollBar.setMaximum(6500)
        self.exposureTimeScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.exposureTimeScrollBar.setObjectName(_fromUtf8("exposureTimeScrollBar"))
        self.line.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.finishButton.raise_()
        self.addProtocolButton.raise_()
        self.exposureTimeSpinBox.raise_()
        self.excitationWavelengthComboBox.raise_()
        self.exposureTimeScrollBar.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "self", None))
        self.label.setText(_translate("self", "Flourescent Intensity Settings ", None))
        self.label_2.setText(_translate("self", "Exposure Time:", None))
        self.label_3.setText(_translate("self", "(ms)", None))
        self.label_4.setText(_translate("self", "Excitation:", None))
        self.label_5.setText(_translate("self", "(nm)", None))
        self.finishButton.setText(_translate("self", "Finish", None))
        self.addProtocolButton.setText(_translate("self", "Add Protocol", None))
        self.excitationWavelengthComboBox.setItemText(0, _translate("self", "Blue", None))
        self.excitationWavelengthComboBox.setItemText(1, _translate("self", "Green", None))
        self.excitationWavelengthComboBox.setItemText(2, _translate("self", "Yellow", None))

