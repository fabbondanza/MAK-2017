from PyQt4 import QtGui
from PyQt4 import QtCore

from introScreen import *

class KAMSpec(QtGui.QWidget):
    def __init__(self):
        super(KAMSpec, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('KAM-Spec 2017')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('KAM-Spec Logo LtoH.svg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setGeometry(2, 2, 800, 480)
        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)
        self.intro = Ui_Form()
        self.vbox.addWidget(self.intro)
        self.show()

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = KAMSpec()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()