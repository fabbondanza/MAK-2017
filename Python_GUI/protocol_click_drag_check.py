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
from shakeMenu_Widget_CD import *
from protocolMenu_Widget import *
from wellPlate_Widg_CD import *
from class_click_and_drag_test import *


###### CLICK AND DRAGE WORKS OF WIDGETS - Initial Functionality
###### Widget pops up and is draggable with MIDDLE MOUSE BUTTON
###### Wells can be selected ON with LEFT MOUSE BUTTON CLICK AND DRAG
###### Wells can be selected OFF with RIGHT  MOUSE BUTTON CLICK AND DRAG

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
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
        self.grid.addWidget(self.protocolWidget, 1, 0, 35, 10)
        self.position_y = 1
        self.show()

    def on_pushButton_clicked(self, string):
        if string == 'Plate':
            protocol = WellPlate()
            self.grid.addWidget(protocol,self.position_y,35,15,45)
            self.position_y += 45


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
