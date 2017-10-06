from PyQt4 import QtGui
from PyQt4 import QtCore

from introScreen import *
from wellSelectScreen_v2 import *
from selectProtocolScreen import *
from absMenu import *
from absSpecMenu import *
from flrMenu import *
from flrSpecMenu import *


class KAMSpec(QtGui.QWidget):
    def __init__(self):
        super(KAMSpec, self).__init__()
        self.initUI()
        self.intro.startButton.clicked.connect(self.startWellSelect)
        self.wellSelect.nextButton.clicked.connect(self.protocolSelectScreen)
        ### Connection Protocol Selection menu buttons to functions
        self.protocolSelect.absButton.clicked.connect(self.absSettings)
        self.protocolSelect.absSpecButton.clicked.connect(self.absSpecSettings)
        self.protocolSelect.flrButton.clicked.connect(self.flrSettings)
        self.protocolSelect.flrSpecButton.clicked.connect(self.flrSpecSettings)
        # self.protocolSelect.shakingButton.clicked.connect(self.shakeMenu)
        self.protocolSelect.addPlateButton.clicked.connect(self.addPlate)

        ### Connecting Absorbance Menu Settings buttons to functions
        self.absMenu.addProtocolButton.clicked.connect(lambda: self.addProtocol(1))
        self.absSpecMenu.addProtocolButton.clicked.connect(lambda: self.addProtocol(2))
        self.flrMenu.addProtocolButton.clicked.connect(lambda: self.addProtocol(3))
        self.flrSpecMenu.addProtocolButton.clicked.connect(lambda: self.addProtocol(4))
        #self.absMenu.finishButton.click.connect(self.finishProtocolSelection)


    def initUI(self):
        self.intro = introScreen()
        self.wellSelect = wellSelectScreen()
        self.protocolSelect = protocolSelectScreen()
        self.absMenu = absMenu()
        self.absSpecMenu = absSpecMenu()
        self.flrMenu = flrMenu()
        self.flrSpecMenu = flrSpecMenu()


    def startWellSelect(self):
        self.intro.deleteLater()
        self.plateCount = 1
        self.wellSelect.show()

    def protocolSelectScreen(self):
        self.wellSelect.hide()
        self.protocolSelect.show()

    def absSettings(self):
        self.protocolSelect.hide()
        self.absMenu.show()

    def absSpecSettings(self):
        self.protocolSelect.hide()
        self.absSpecMenu.show()

    def flrSettings(self):
        self.protocolSelect.hide()
        self.flrMenu.show()

    def flrSpecSettings(self):
        self.protocolSelect.hide()
        self.flrSpecMenu.show()

    def addProtocol(self, type):
        if type == 1:
            self.absMenu.hide()
            self.protocolSelect.show()
        elif type == 2:
            self.absSpecMenu.hide()
            self.protocolSelect.show()
        elif type == 3:
            self.flrMenu.hide()
            self.protocolSelect.show()
        elif type == 4:
            self.flrSpecMenu.hide()
            self.protocolSelect.show()
        elif type == 5:
            self.flrSpecMenu.hide()
            self.protocolSelect.show()

    def addPlate(self):
        self.plateCount += 1
        self.protocolSelect.hide()
        self.wellSelect.clearWells()
        self.wellSelect.show()




def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = KAMSpec()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()