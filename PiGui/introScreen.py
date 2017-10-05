# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'introScreen.ui'
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

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.initUI()
        self.show()
    def initUI(self):
        self.setObjectName(_fromUtf8("Form"))
        self.resize(794, 480)
        self.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 165);"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(600, 100, 71, 71))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../Python_GUI/igem_logo.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(560, 40, 151, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.logoImg = QtGui.QLabel(self)
        self.logoImg.setGeometry(QtCore.QRect(20, 10, 731, 441))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.logoImg.setPalette(palette)
        self.logoImg.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 165);"))
        self.logoImg.setText(_fromUtf8(""))
        self.logoImg.setPixmap(QtGui.QPixmap(_fromUtf8("../Python_GUI/KAM-Spec Logo LtoH.svg")))
        self.logoImg.setObjectName(_fromUtf8("logoImg"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(570, 180, 151, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(48)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.startButton = QtGui.QPushButton(self)
        self.startButton.setEnabled(True)
        self.startButton.setGeometry(QtCore.QRect(450, 300, 331, 151))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.startButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 127);"))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.logoImg.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.startButton.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "PENN", None))
        self.label_3.setText(_translate("Form", "2017", None))
        self.startButton.setText(_translate("Form", "START", None))

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = Ui_Form()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()