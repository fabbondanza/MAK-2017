# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shaking_menu.ui'
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

class shakeMenu_Widget(QtGui.QWidget):
    def __init__(self):
        super(shakeMenu_Widget, self).__init__()
        self.initUI()

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == QtCore.Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

        super(shakeMenu_Widget, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos

        super(shakeMenu_Widget, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(shakeMenu_Widget, self).mouseReleaseEvent(event)

    def initUI(self):
        self.setObjectName(_fromUtf8("Shake Menu"))
        self.resize(576, 95)
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 201, 21))
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
        self.label_5 = QtGui.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(130, 20, 71, 21))
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
        self.label_11 = QtGui.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(30, 40, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_11.setLineWidth(1)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 81, 21))
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
        self.duration = QtGui.QSpinBox(self)
        self.duration.setGeometry(QtCore.QRect(90, 40, 391, 22))
        self.duration.setAlignment(QtCore.Qt.AlignCenter)
        self.duration.setMinimum(1)
        self.duration.setMaximum(60)
        self.duration.setObjectName(_fromUtf8("duration"))
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
        self.label_15.setGeometry(QtCore.QRect(250, 60, 61, 21))
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
        self.stopButton = QtGui.QPushButton(self)
        self.stopButton.setGeometry(QtCore.QRect(510, 0, 31, 20))
        self.stopButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("x-mark-4-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.label_6.raise_()
        self.label_2.raise_()
        self.label_7.raise_()
        self.label_5.raise_()
        self.label_11.raise_()
        self.label_4.raise_()
        self.duration.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.stopButton.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Shake Menu", "Shake Menu", None))
        self.label_2.setText(_translate("Shake Menu", "Shaking", None))
        self.label_11.setText(_translate("Shake Menu", "Duration: ", None))
        self.label_4.setText(_translate("Shake Menu", "Time Settings", None))
        self.label_14.setText(_translate("Shake Menu", "(s)", None))
        self.label_15.setText(_translate("Shake Menu", " Max: 60", None))


