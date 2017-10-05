from PyQt4 import QtGui
from PyQt4 import QtCore

from introScreen import *
from wellSelectScreen_v2 import *

class KAMSpec(QtGui.QWidget):
    def __init__(self):
        super(KAMSpec, self).__init__()
        self.initUI()
        self.intro.startButton.clicked.connect(self.startWellSelect)
        self.wellSelect.nextButton.clicked.connect(self.protocolSelectScreen)

    def initUI(self):
        self.intro = introScreen()
        self.wellSelect = wellSelectScreen()

    def startWellSelect(self):
        self.intro.hide()
        self.wellSelect.show()

    def protocolSelectScreen(self):
        self.wellSelect.hide()


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = KAMSpec()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()