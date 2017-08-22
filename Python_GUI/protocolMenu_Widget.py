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

class protocolMenu_Widget(QtGui.QWidget):
    def __init__(self):
        super(protocolMenu_Widget, self).__init__()
        self.initUI()
    def initUI(self):
        self.setObjectName(_fromUtf8("Protocol Menu"))
        self.resize(161, 312)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 10, 101, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.splitter = QtGui.QSplitter(self)
        self.splitter.setGeometry(QtCore.QRect(10, 70, 131, 221))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.shakeButton = QtGui.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.shakeButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("shakeLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shakeButton.setIcon(icon)
        self.shakeButton.setIconSize(QtCore.QSize(40, 40))
        self.shakeButton.setObjectName(_fromUtf8("shakeButton"))
        self.absButton = QtGui.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.absButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("absorbanceLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.absButton.setIcon(icon1)
        self.absButton.setIconSize(QtCore.QSize(40, 40))
        self.absButton.setObjectName(_fromUtf8("absButton"))
        self.absSpecButton = QtGui.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.absSpecButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("absSpectrumLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.absSpecButton.setIcon(icon2)
        self.absSpecButton.setIconSize(QtCore.QSize(40, 40))
        self.absSpecButton.setObjectName(_fromUtf8("absSpecButton"))
        self.flrButton = QtGui.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.flrButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("flourescenceLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flrButton.setIcon(icon3)
        self.flrButton.setIconSize(QtCore.QSize(40, 40))
        self.flrButton.setObjectName(_fromUtf8("flrButton"))
        self.flrSpecButton = QtGui.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.flrSpecButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("flrSpectrumLogo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flrSpecButton.setIcon(icon4)
        self.flrSpecButton.setIconSize(QtCore.QSize(40, 40))
        self.flrSpecButton.setObjectName(_fromUtf8("flrSpecButton"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("Protocol Menu", "Protocol Menu", None))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">Protocol <br/>Options</p></body></html>", None))
        self.shakeButton.setText(_translate("Protocol Menu", "Shaking", None))
        self.absButton.setText(_translate("Protocol Menu", "Absorbance", None))
        self.absSpecButton.setText(_translate("Protocol Menu", "Absorbance \n"
"  Spectrum", None))
        self.flrButton.setText(_translate("Protocol Menu", "Flourescent \n"
"  Intensity", None))
        self.flrSpecButton.setText(_translate("Protocol Menu", "Flourescence\n"
"   Spectrum", None))




# def main():
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     app.setStyle("Cleanlooks")
#     ex = Example_1()
#     ex.show()
#     sys.exit(app.exec_())
# if __name__ == '__main__':
#     main()
