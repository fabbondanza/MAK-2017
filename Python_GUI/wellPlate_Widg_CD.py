from PyQt4 import QtGui, QtCore
from protocolMenu_Widget import *
import numpy as np


class WellPlate(QtGui.QWidget):
    def __init__(self):
        super(WellPlate, self).__init__()
        self.initUI()

    def initUI(self):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        self.protocolWidg = protocolMenu_Widget()
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
        self.clicked = 0

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.origin = event.pos()
            self.rubberband.setGeometry(
                QtCore.QRect(self.origin, QtCore.QSize()))
            self.clicked = 1
        elif event.button() == QtCore.Qt.RightButton:
            self.origin = event.pos()
            self.rubberband.setGeometry(
                QtCore.QRect(self.origin, QtCore.QSize()))
            self.clicked = 2
            #self.rubberband.show()
        elif event.button() == QtCore.Qt.MiddleButton:
            self.clicked = 0
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()
        QtGui.QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        if self.clicked == 1:
            self.rubberband.setGeometry(
                QtCore.QRect(self.origin, event.pos()).normalized())

            rectDim = self.rubberband.geometry()
            rectPos = self.rubberband.pos()
            print rectDim.width(), rectDim.height()
            print rectPos.x(), rectPos.y()
            for child in self.findChildren(QtGui.QRadioButton):
                if rectDim.intersects(child.geometry()):
                    child.setChecked(True)
            QtGui.QWidget.mouseMoveEvent(self, event)

        elif self.clicked == 2:
            self.rubberband.setGeometry(
                QtCore.QRect(self.origin, event.pos()).normalized())

            rectDim = self.rubberband.geometry()
            for child in self.findChildren(QtGui.QRadioButton):
                if rectDim.intersects(child.geometry()):
                    child.setChecked(False)
            QtGui.QWidget.mouseMoveEvent(self, event)

        elif event.buttons() == QtCore.Qt.MiddleButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())

            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            print newPos, currPos, self.pos()
            for child in self.parent().findChildren(protocolMenu_Widget):
                if self.geometry().intersects(child.geometry()):
                    self.move(newPos + QtCore.QPoint(10,0))
                    self.origin = newPos + QtCore.QPoint(10,0)
                    self.__mouseMovePos = globalPos
                else:
                    self.move(newPos)
                    self.origin = newPos
                    self.__mouseMovePos = globalPos
            for child in self.parent().findChildren(WellPlate):
                if self.geometry().intersects(child.geometry()):
                    self.setGeometry(self.pos().x(), self.pos().y() + self.geometry().height(), self.geometry().width(),
                                     self.geometry().height())
                    child.setGeometry(self.pos().x(),child.pos().y()-self.geometry().height(), child.geometry().width(),child.geometry().height())
                    if child.pos().y() < 0:
                        child.setGeometry(self.pos().x(), 15, child.geometry().width(), child.geometry().height())
                    self.move(newPos)
                    self.origin = newPos
                    self.__mouseMovePos = globalPos
                else:
                    self.move(newPos)
                    self.origin = newPos
                    self.__mouseMovePos = globalPos

    def mouseReleaseEvent(self, event):
        if self.clicked == 1:
            self.clicked = 0
            self.rubberband.hide()
            selected = []
        elif self.clicked == 2:
            self.clicked = 0

        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return
        super(WellPlate, self).mouseReleaseEvent(event)

class QHLine(QtGui.QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QtGui.QFrame.HLine)
        self.setFrameShadow(QtGui.QFrame.Sunken)
