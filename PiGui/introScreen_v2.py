# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'introScreen_v2.ui'
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

class introScreen(QtGui.QWidget):
    def __init__(self):
        super(introScreen, self).__init__()
        self.initUI()


    def initUI(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(794, 430)
        self.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(580, 80, 71, 71))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../Python_GUI/igem_logo.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(540, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rockwell"))
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(560, 160, 141, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rockwell"))
        font.setPointSize(48)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.startButton = QtGui.QPushButton(self)
        self.startButton.setEnabled(True)
        self.startButton.setGeometry(QtCore.QRect(450, 360, 331, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.startButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 127);"))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.calibrateButton = QtGui.QPushButton(self)
        self.calibrateButton.setEnabled(True)
        self.calibrateButton.setGeometry(QtCore.QRect(510, 300, 211, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.calibrateButton.setFont(font)
        self.calibrateButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.calibrateButton.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("CalibrateLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calibrateButton.setIcon(icon)
        self.calibrateButton.setIconSize(QtCore.QSize(60, 60))
        self.calibrateButton.setObjectName(_fromUtf8("calibrateButton"))
        self.plateButton = QtGui.QPushButton(self)
        self.plateButton.setEnabled(True)
        self.plateButton.setGeometry(QtCore.QRect(510, 240, 211, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.plateButton.setFont(font)
        self.plateButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.plateButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 127);\n"
"background-color: rgb(170, 170, 255);"))
        self.plateButton.setObjectName(_fromUtf8("plateButton"))
        self.label_4 = QtGui.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 411, 361))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("kamSpecLogo.svg")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()

    def retranslateUi(self):
        self.setWindowTitle('KAM-Spec 2017')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('kamSpecLogo.svg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.label_2.setText(_translate("self", "PENN", None))
        self.label_3.setText(_translate("self", "2017", None))
        self.startButton.setText(_translate("self", "START", None))
        self.calibrateButton.setText(_translate("self", "Calibrate", None))
        self.plateButton.setText(_translate("self", "Plate In/Out", None))

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = introScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()