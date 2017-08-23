from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np

from absMenu_Widget import *
from absSpecMenu_Widget import *
from flrMenu_Widget import *
from flrSpecMenu_Widget import *
from shakeMenu_Widget import *
from protocolMenu_Widget import *
from click_drag_test_working import *

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self._buttons = -1
        self.last_protocol = 0
        self.y_position = 0
        self.initUI()
        self.protocolWidget.shakeButton.clicked.connect(lambda: self.on_pushButton_clicked('Shake'))
        self.protocolWidget.absButton.clicked.connect(lambda: self.on_pushButton_clicked('Abs'))
        self.protocolWidget.absSpecButton.clicked.connect(lambda: self.on_pushButton_clicked('AbsSpec'))
        self.protocolWidget.flrButton.clicked.connect(lambda: self.on_pushButton_clicked('Flr'))
        self.protocolWidget.flrSpecButton.clicked.connect(lambda: self.on_pushButton_clicked('FlrSpec'))

    def initUI(self):
        self.setGeometry(50,50,775,550)
        self.grid = QtGui.QGridLayout()
        self.setLayout(self.grid)
        self.protocolWidget = protocolMenu_Widget()
        self.shakeWidget = shakeMenu_Widget()
        self.grid.addWidget(self.protocolWidget, 0, 0, 35, 3)

        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 545, 2500))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.grid.addWidget(self.scrollArea, 2, 25, 50, 10)
        self.blank = []
        self.show()

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self, protocolString):
        self._buttons  += 1
        protocol_heights = [0,90, 114, 124, 187, 100]
        print protocolString
        if protocolString == 'Abs':
            protocol = absMenu_Widget()
            protocol.stopButton.clicked.connect(lambda: self.closeProtocol(1,protocol.pos()))
            protocol.setParent(self.scrollAreaWidgetContents)
            protocol.setGeometry(0,self.y_position+5, 547, 85)
            protocol.show()
            self.y_position += 90
            #self.last_protocol = 1
        elif protocolString == 'AbsSpec':
            protocol = absSpecMenu_Widget()
            protocol.stopButton.clicked.connect(lambda: self.closeProtocol(2,protocol.pos()))
            protocol.setParent(self.scrollAreaWidgetContents)
            protocol.setGeometry(0, self.y_position+5, 555, 109)
            protocol.show()
            self.y_position += 114
            #self.last_protocol = 2
        elif protocolString == 'Flr':
            protocol = flrMenu_Widget()
            protocol.stopButton.clicked.connect(lambda: self.closeProtocol(3,protocol.pos()))
            protocol.setParent(self.scrollAreaWidgetContents)
            protocol.setGeometry(0, self.y_position+5, 552, 119)
            protocol.show()
            self.y_position += 124
            #self.last_protocol = 3
        elif protocolString == 'FlrSpec':
            protocol = flrSpecMenu_Widget()
            protocol.stopButton.clicked.connect(lambda: self.closeProtocol(4,protocol.pos()))
            protocol.setParent(self.scrollAreaWidgetContents)
            protocol.setGeometry(0, self.y_position+5, 559, 182)
            protocol.show()
            self.y_position += 187
            #self.last_protocol = 4
        elif protocolString == 'Shake':
            protocol = shakeMenu_Widget()
            protocol.stopButton.clicked.connect(lambda: self.closeProtocol(5,protocol.pos()))
            protocol.setParent(self.scrollAreaWidgetContents)
            protocol.setGeometry(0, self.y_position+5, 576, 95)
            protocol.show()
            self.y_position += 100
            #self.last_protocol = 5


    def closeProtocol(self,type, pos):
        y_position = pos.y()
        list = [absMenu_Widget, absSpecMenu_Widget, flrMenu_Widget, flrSpecMenu_Widget, shakeMenu_Widget]

        for child in self.scrollAreaWidgetContents.findChildren(list[type-1]):
            if child.pos().y() == y_position:
                self.updateY = child.geometry().height()
                child.hide()
                self.y_position -= self.updateY
                for selection in list:
                    for child in self.scrollAreaWidgetContents.findChildren(selection):
                        x = child.pos().x()
                        y = child.pos().y()
                        w = child.geometry().width()
                        h = child.geometry().height()
                        if y > y_position:
                            child.setGeometry(x,y-self.updateY,w,h)




def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = Example()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
