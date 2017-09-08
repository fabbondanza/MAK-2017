from PyQt4 import QtGui
from PyQt4 import QtCore
import numpy as np
import time
import os.path

from functools import partial
from absMenu import *
from absSpecMenu import *
from flrMenu import *
from flrSpecMenu import *
from shakeMenu import *
from wellplateMenu import *
from optionsMenu import *


class KAMSpec(QtGui.QWidget):
    def __init__(self):
        super(KAMSpec, self).__init__()
        self.initUI()
        ###### Setting initial values of necessary variables
        self.plate_number = 0
        self.yPosDict = {}
        self.widgetTypesAdded = {}

        ##### Setting button functionality
        self.optionsWidg.addPlateButton.clicked.connect(self.addPlate)


    def initUI(self):
        self.setWindowTitle('KAM-Spec 2017')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('KAM-Spec Logo LtoH.svg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setGeometry(400, 100, 1125, 850)
        self.grid = QtGui.QGridLayout()
        self.setLayout(self.grid)
        self.optionsWidg = optionsMenu()
        self.grid.addWidget(self.optionsWidg, 1, 0, 35, 3)

        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 900, 2500))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.grid.addWidget(self.scrollArea, 2, 25, 50, 10)
        self.show()

    def addPlate(self):
        self.plate_number += 1 #Update the number of plates on screen
        wellPlateScroll = QtGui.QScrollArea(self) #Create new scroll area for the new plate
        wellPlateScroll.setObjectName(str(self.plate_number)) #Set its object name to the plate number
        wellPlateScroll.setGeometry(0,self.plate_number*510 -500,810,500) #Set it's dimensions and proper position below other plates
        wellPlateScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) #Turn of the horizontal scroll bar for the new plate scroll area
        wellPlateScroll.setWidgetResizable(False)
        wellPlateProtocols = QtGui.QWidget(wellPlateScroll) #Set the area where protocols can be added
        wellPlateProtocols.setObjectName(str(self.plate_number))
        wellPlateProtocols.setGeometry(QtCore.QRect(0, 0, 900, 2500))
        wellPlateScroll.setWidget(wellPlateProtocols)
        wellPlateScroll.setParent(self.scrollAreaWidgetContents)
        wellPlateScroll.destroyed.connect(self.deletePlate) #Set connection to event, when well plate gets deleted.

        #Add new well plate widget menu to the new scroll area
        newPlate = wellplateMenu()
        newPlate.setParent(wellPlateProtocols)
        #Set Button functionality in well plate menu
        newPlate.closeButton.clicked.connect(wellPlateScroll.deleteLater) #X button, which closes out entire well plate with all its protocols
        newPlate.absButton.clicked.connect(lambda: self.addProtocol(1,newPlate.parent()))
        newPlate.absSpecButton.clicked.connect(lambda: self.addProtocol(2, newPlate.parent()))
        newPlate.flrButton.clicked.connect(lambda: self.addProtocol(3, newPlate.parent()))
        newPlate.flrSpecButton.clicked.connect(lambda: self.addProtocol(4,newPlate.parent()))
        newPlate.shakeButton.clicked.connect(lambda: self.addProtocol(5,newPlate.parent()))

        #Check if the addition of the new well plate requires an increases in the height of the scroll area.
        # If the bottom of the new well plate scroll area is larger than the height of the main scroll area window, the height of the main scroll area will be increased.
        if wellPlateScroll.pos().y()+500 > self.scrollAreaWidgetContents.geometry().height():
            self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0,0,900,self.scrollAreaWidgetContents.geometry().height()+1000))

        self.yPosDict[int(str(wellPlateProtocols.objectName()))] = 310 #This adds a key to the dictionary of y-positions, with 1 key representing lowest y-position taken by a widget per-scroll area
        self.widgetTypesAdded[int(str(wellPlateProtocols.objectName()))] = []

        wellPlateScroll.show()
        newPlate.show()

    def deletePlate(self):
        platesLeftList = []
        deletedPlate = 0
        formerPlatesList = range(1,self.plate_number+1)
        #print formerPlatesList
        for child in self.scrollAreaWidgetContents.findChildren(QtGui.QScrollArea):
            platesLeftList.append(int(str(child.objectName())))

        #print platesLeftList

        for i in range(0,len(platesLeftList)):
            if formerPlatesList[i] != platesLeftList[i]:
                deletedPlate = formerPlatesList[i]
                #print deletedPlate
        if deletedPlate != 0:
            for child in self.scrollAreaWidgetContents.findChildren(QtGui.QScrollArea):
                if int(str(child.objectName()))> deletedPlate:
                    #print int(str(child.objectName()))
                    child.setObjectName(str(int(str(child.objectName()))-1))
                    child.setGeometry(0,int(str(child.objectName()))*510 -500,810,500)
                    #print int(str(child.objectName()))
        self.plate_number -= 1


    def addProtocol(self,type, parent):
        if type == 1:
            yposition = self.yPosDict[int(str(parent.objectName()))]
            protocol = absMenu()
            protocol.setGeometry(5, yposition , 600, 100)
            protocol.closeButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.deleteProtocol(1,parent))
            protocol.setParent(parent)
            protocol.show()

            self.yPosDict[int(str(parent.objectName()))] += 100 #Update lowest y-position of last widget in scroll area where widget was just added
            self.widgetTypesAdded[int(str(parent.objectName()))].append([type, protocol.pos().y()])
        if type == 2:
            yposition = self.yPosDict[int(str(parent.objectName()))]
            protocol = absSpecMenu()
            protocol.setGeometry(5, yposition , 600, 130)
            protocol.closeButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.deleteProtocol(2,parent))
            protocol.setParent(parent)
            protocol.show()

            self.yPosDict[int(str(parent.objectName()))] += 130 #Update lowest y-position of last widget in scroll area where widget was just added
            self.widgetTypesAdded[int(str(parent.objectName()))].append([type, protocol.pos().y()])
        if type == 3:
            yposition = self.yPosDict[int(str(parent.objectName()))]
            protocol = flrMenu()
            protocol.setGeometry(5, yposition , 600, 125)
            protocol.closeButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.deleteProtocol(3,parent))
            protocol.setParent(parent)
            protocol.show()

            self.yPosDict[int(str(parent.objectName()))] += 125 #Update lowest y-position of last widget in scroll area where widget was just added
            self.widgetTypesAdded[int(str(parent.objectName()))].append([type, protocol.pos().y()])
        if type == 4:
            yposition = self.yPosDict[int(str(parent.objectName()))]
            protocol = flrSpecMenu()
            protocol.setGeometry(5, yposition , 600, 186)
            protocol.closeButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.deleteProtocol(4,parent))
            protocol.setParent(parent)
            protocol.show()

            self.yPosDict[int(str(parent.objectName()))] += 186 #Update lowest y-position of last widget in scroll area where widget was just added
            self.widgetTypesAdded[int(str(parent.objectName()))].append([type, protocol.pos().y()])
        if type == 5:
            yposition = self.yPosDict[int(str(parent.objectName()))]
            protocol = shakeMenu()
            protocol.setGeometry(5, yposition , 600, 99)
            protocol.closeButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.deleteProtocol(5,parent))
            protocol.setParent(parent)
            protocol.show()

            self.yPosDict[int(str(parent.objectName()))] += 99 #Update lowest y-position of last widget in scroll area where widget was just added
            self.widgetTypesAdded[int(str(parent.objectName()))].append([type, protocol.pos().y()])

    def deleteProtocol(self,type,parent):
        widgetHeights = [100, 130, 125, 186, 99]
        deletedHeight = widgetHeights[type-1]
        widgetOptions = [absMenu, absSpecMenu, flrMenu, flrSpecMenu, shakeMenu]
        protocolsLeftYpositionsList = []
        formerProtocolList = []
        deletedProtocol = 0
        listOfParentArea = self.widgetTypesAdded[int(str(parent.objectName()))]
        for i in range(0, len(listOfParentArea)):
            formerProtocolList.append(listOfParentArea[i][1])


        for i in range(0,len(widgetOptions)):
            for child in parent.findChildren(widgetOptions[i]):
                protocolsLeftYpositionsList.append(child.pos().y())

        sortedRemainingProtocolyPositions = np.sort(protocolsLeftYpositionsList)

        for i in range(0,len(sortedRemainingProtocolyPositions)):
            if formerProtocolList[i] != sortedRemainingProtocolyPositions[i]:
                deletedProtocol = formerProtocolList[i]

        if deletedProtocol != 0:
            for i in range(0, len(widgetOptions)):
                for child in parent.findChildren(widgetOptions[i]):
                    if child.pos().y() > deletedProtocol:
                        #print int(str(child.objectName()))
                        child.setGeometry(child.pos().x(),child.pos().y()-deletedHeight,child.geometry().width(),child.geometry().height())
                        #print int(str(child.objectName()))
        self.yPosDict[int(str(parent.objectName()))] -= deletedHeight
def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = KAMSpec()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()