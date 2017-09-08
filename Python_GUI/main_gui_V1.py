from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
import time
import os.path

from functools import partial
from absMenu_Widget import *
from absSpecMenu_Widget import *
from flrMenu_Widget import *
from flrSpecMenu_Widget import *
from shakeMenu_Widget import *
from protocolMenu_Widget import *
from wellPlate_Widg import *

class KAMSpec(QtGui.QWidget):
    def __init__(self):
        super(KAMSpec, self).__init__()
        self.missingPlate = []
        self.plateYPositions = []
        self.missingSpace = []
        self.plate_count = 0
        self.protList = {}
        self._buttons = -1
        self.widgetCount = 1
        self.last_protocol = 0
        self.y_position = 0
        self.initUI()
        self.protocolWidget.wellButton.clicked.connect(lambda: self.on_pushButton_clicked('Plate'))
        self.protocolWidget.shakeButton.clicked.connect(lambda: self.on_pushButton_clicked('Shake'))
        self.protocolWidget.absButton.clicked.connect(lambda: self.on_pushButton_clicked('Abs'))
        self.protocolWidget.absSpecButton.clicked.connect(lambda: self.on_pushButton_clicked('AbsSpec'))
        self.protocolWidget.flrButton.clicked.connect(lambda: self.on_pushButton_clicked('Flr'))
        self.protocolWidget.flrSpecButton.clicked.connect(lambda: self.on_pushButton_clicked('FlrSpec'))

    def initUI(self):
        self.setWindowTitle('KAM-Spec 2017')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('KAM-Spec Logo.svg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setGeometry(50, 50, 850, 550)
        self.grid = QtGui.QGridLayout()
        self.setLayout(self.grid)
        self.protocolWidget = protocolMenu_Widget()
        self.shakeWidget = shakeMenu_Widget()
        self.grid.addWidget(self.protocolWidget, 1, 0, 35, 3)

        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 700, 2500))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.grid.addWidget(self.scrollArea, 2, 25, 50, 10)

        # #### Menu Bar ####
        # self.myQMenuBar = QtGui.QMenuBar()  # Creating Menubar
        # fileTab = self.myQMenuBar.addMenu('File')  # Initializing the File Tab
        # openAction = QtGui.QAction('Open Script', self)
        # openAction.triggered.connect(self.openProtocol)
        # saveAction = QtGui.QAction('Save Script', self)
        # saveAction.triggered.connect(self.saveProtocol)
        # saveAsAction = QtGui.QAction('Save As...', self)
        # fileTab.addAction(openAction)
        # fileTab.addAction(saveAction)
        # fileTab.addAction(saveAsAction)
        #
        # measurementTab = self.myQMenuBar.addMenu('Measurement')  # Initializing the Measurement Tab
        # plateOutAction = QtGui.QAction('Move Plate Out', self)
        # plateInAction = QtGui.QAction('Move Plate In', self)
        # calibrateAction = QtGui.QAction('Calibration', self)
        # dataExportAction = QtGui.QAction('Data Export Settings', self)
        # measurementTab.addAction(plateOutAction)
        # measurementTab.addAction(plateInAction)
        # measurementTab.addAction(calibrateAction)
        # measurementTab.addAction(dataExportAction)
        # #######################################################
        # self.grid.addWidget(self.myQMenuBar, 0, 0, 2, 3)
        self.show()


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = KAMSpec()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()