from PyQt4 import QtGui, QtCore
import numpy as np


class WellPlate(QtGui.QWidget):
    def __init__(self):
        super(WellPlate, self).__init__()
        self.initUI()

    def initUI(self):

        self.grid = QtGui.QGridLayout()
        self.vboxLayout = QtGui.QVBoxLayout()
        self.vboxLayout2 = QtGui.QVBoxLayout()
        self.hboxLayout = QtGui.QHBoxLayout()
        self.setLayout(self.vboxLayout)
        letters = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        numbers = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        positions = [(i, j) for i in range(9) for j in range(13)]

        for position in positions:
            if position[0] == 0:
                if position[1] == 0:
                    label = QtGui.QLabel('')
                    self.grid.addWidget(label, *position)
                else:
                    label = QtGui.QLabel(str(position[1]))
                    label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                    self.grid.addWidget(label, *position)
            elif position[1] == 0:
                if position[0] == 0:
                    label = QtGui.QLabel('')
                    self.grid.addWidget(label, *position)
                else:
                    label = QtGui.QLabel(letters[position[0]])
                    self.grid.addWidget(label, *position)
            else:
                button = QtGui.QRadioButton('')
                button.setObjectName(letters[position[0]] + numbers[position[1]])
                self.grid.addWidget(button, *position)
                button.setAutoExclusive(False)

        self.rubberband = QtGui.QRubberBand(
            QtGui.QRubberBand.Rectangle, self)

        self.setMouseTracking(True)

        self.clearAll = QtGui.QPushButton('Clear All Wells')
        self.deletePlate = QtGui.QPushButton('Delete Plate')
        self.plateLabel = QtGui.QLineEdit()
        self.plateLabel.setPlaceholderText('Enter Plate Protocol Label')

        self.hboxLayout.addLayout(self.grid)
        self.vboxLayout2.addWidget(self.plateLabel)
        self.vboxLayout2.addWidget(self.clearAll)
        self.vboxLayout2.addWidget(self.deletePlate)
        self.hboxLayout.addLayout(self.vboxLayout2)
        self.vboxLayout.addLayout(self.hboxLayout)
        self.vboxLayout.addWidget(QHLine())


    def mousePressEvent(self, event):
        self.origin = event.pos()
        self.rubberband.setGeometry(
            QtCore.QRect(self.origin, QtCore.QSize()))
        self.rubberband.show()
        QtGui.QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        if self.rubberband.isVisible():
            self.rubberband.setGeometry(
                QtCore.QRect(self.origin, event.pos()).normalized())
        QtGui.QWidget.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        if self.rubberband.isVisible():
            self.rubberband.hide()
            selected = []
            rect = self.rubberband.geometry()
            for child in self.findChildren(QtGui.QRadioButton):
                if rect.intersects(child.geometry()):
                    child.toggle()

        QtGui.QWidget.mouseReleaseEvent(self, event)

class QHLine(QtGui.QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QtGui.QFrame.HLine)
        self.setFrameShadow(QtGui.QFrame.Sunken)
