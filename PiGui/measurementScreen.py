# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'measurementScreen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt4agg import  FigureCanvasQTAgg as FigureCanvas



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


class measurementScreen(QtGui.QWidget):
    def __init__(self):
        super(measurementScreen, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(800, 430)
        self.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.measurementLabel = QtGui.QLabel(self)
        self.measurementLabel.setGeometry(QtCore.QRect(200, 10, 571, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(22)
        self.measurementLabel.setFont(font)
        self.measurementLabel.setObjectName(_fromUtf8("measurementLabel"))
        self.line = QtGui.QFrame(self)
        self.line.setGeometry(QtCore.QRect(10, 40, 751, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(260, 60, 16, 361))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 47, 13))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayoutWidget = QtGui.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 90, 251, 331))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(280, 60, 511, 361))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayoutWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.figure = plt.figure(figsize=(1,1))
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout_2.addWidget(self.canvas, 1,0,10,10)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle('KAM-Spec 2017')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('KAM-Spec Logo LtoH.svg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.label.setText(_translate("self", "In Progress:", None))
        self.measurementLabel.setText(_translate("self", "Initialization...", None))
        self.label_3.setText(_translate("self", "To Do:", None))

