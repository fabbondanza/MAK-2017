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
from click_drag_test_working import *

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.protList = {}
        self._buttons = -1
        self.widgetCount = 1
        self.last_protocol = 0
        self.y_position = 0
        self.initUI()
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
        self.setGeometry(50,50,775,550)
        self.grid = QtGui.QGridLayout()
        self.setLayout(self.grid)
        self.protocolWidget = protocolMenu_Widget()
        self.shakeWidget = shakeMenu_Widget()
        self.grid.addWidget(self.protocolWidget, 1, 0, 35, 3)

        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 545, 2500))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.grid.addWidget(self.scrollArea, 2, 25, 50, 10)


        #### Menu Bar ####
        self.myQMenuBar = QtGui.QMenuBar() #Creating Menubar
        fileTab = self.myQMenuBar.addMenu('File') #Initializing the File Tab
        openAction = QtGui.QAction('Open Script', self)
        openAction.triggered.connect(self.openProtocol)
        saveAction = QtGui.QAction('Save Script', self)
        saveAction.triggered.connect(self.saveProtocol)
        saveAsAction = QtGui.QAction('Save As...', self)
        fileTab.addAction(openAction)
        fileTab.addAction(saveAction)
        fileTab.addAction(saveAsAction)

        measurementTab = self.myQMenuBar.addMenu('Measurement') #Initializing the Measurement Tab
        plateOutAction = QtGui.QAction('Move Plate Out', self)
        plateInAction = QtGui.QAction('Move Plate In', self)
        calibrateAction = QtGui.QAction('Calibration', self)
        dataExportAction = QtGui.QAction('Data Export Settings', self)
        measurementTab.addAction(plateOutAction)
        measurementTab.addAction(plateInAction)
        measurementTab.addAction(calibrateAction)
        measurementTab.addAction(dataExportAction)
        #######################################################
        self.grid.addWidget(self.myQMenuBar,0,0,2,3)
        self.show()

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self, protocolString):
        self._buttons  += 1
        if protocolString == 'Abs':
            protocol = absMenu_Widget()
            protocol.setObjectName(str(self._buttons))
            protocol.stopButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.checked(1))
            #protocol.stopButton.clicked.connect(lambda: self.closeProtocol())
            #protocol.stopButton.clicked.connect(lambda: self.closeProtocol(1, protocol.pos()))#lambda: self.closeProtocol(1, protocol.pos()))
            protocol.setParent(self.scrollAreaWidgetContents)
            protocol.setGeometry(0,self.y_position+5, 547, 85)
            protocol.show()
            self.y_position += 90
        elif protocolString == 'AbsSpec':
            protocol = absSpecMenu_Widget()
            protocol.setObjectName(str(self._buttons))
            protocol.stopButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.checked(2))
            #protocol.stopButton.clicked.connect(lambda: self.closeProtocol(2, protocol.pos()))
            protocol.setParent(self.scrollAreaWidgetContents)
            protocol.setGeometry(0, self.y_position+5, 555, 109)
            protocol.show()
            self.y_position += 114
        elif protocolString == 'Flr':
            protocol = flrMenu_Widget()
            protocol.setObjectName(str(self._buttons))
            protocol.stopButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.checked(3))
            #protocol.stopButton.clicked.connect(lambda: self.closeProtocol(3,protocol.pos()))
            protocol.setParent(self.scrollAreaWidgetContents)
            protocol.setGeometry(0, self.y_position+5, 552, 119)
            protocol.show()
            self.y_position += 124
        elif protocolString == 'FlrSpec':
            protocol = flrSpecMenu_Widget()
            protocol.setObjectName(str(self._buttons))
            protocol.stopButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.checked(4))
            #protocol.stopButton.clicked.connect(lambda: self.closeProtocol(4,protocol.pos()))
            protocol.setParent(self.scrollAreaWidgetContents)
            protocol.setGeometry(0, self.y_position+5, 559, 182)
            protocol.show()
            self.y_position += 187

        elif protocolString == 'Shake':
            protocol = shakeMenu_Widget()
            protocol.setObjectName(str(self._buttons))
            print protocol.objectName()
            protocol.stopButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.checked(5))
            #protocol.stopButton.clicked.connect(lambda: self.closeProtocol(5,protocol.pos()))
            protocol.setParent(self.scrollAreaWidgetContents)
            protocol.setGeometry(0, self.y_position+5, 576, 95)
            protocol.show()
            self.y_position += 100

    def checked(self,widgetType):
        list = [absMenu_Widget, absSpecMenu_Widget, flrMenu_Widget, flrSpecMenu_Widget, shakeMenu_Widget]
        listHeight = [90, 114, 124, 187, 100]
        self.updateY = listHeight[widgetType-1]
        y_dict = {}
        numberCheck = range(0,25)
        for type in range(1,6):
            for child in self.scrollAreaWidgetContents.findChildren(list[type-1]):
                y_dict[int(child.objectName())] = child.pos().y()
        print y_dict.keys()
        for element in range(0,len(y_dict.keys())):
            if y_dict.keys()[element] != numberCheck[element]:
                self.missingSpace = numberCheck[element]
                print 'Missing ' + str(self.missingSpace)
                break
        for type in range(1, 6):
            for child in self.scrollAreaWidgetContents.findChildren(list[type - 1]):
                x = child.pos().x()
                y = child.pos().y()
                w = child.geometry().width()
                h = child.geometry().height()
                name = int(child.objectName())
                if name > self.missingSpace:
                    child.setGeometry(x, y - self.updateY, w, h)
                    child.setObjectName(str(int(child.objectName())-1))
        self._buttons -= 1
        self.y_position -= self.updateY
    # def closeProtocol(self):
    #
    # # def closeProtocol(self,type, pos):
    #     #y_position = pos.y()
    #     self.updateY = 90
    #
    #     self.y_position -= self.updateY
    #     listWidg = [absMenu_Widget, absSpecMenu_Widget, flrMenu_Widget, flrSpecMenu_Widget, shakeMenu_Widget]
    #     listHeight = [85, 100]
    #     # for child in self.scrollAreaWidgetContents.findChildren(list[type-1]):
    #     #     if child.pos().y() > y_position:
    #     #         self.updateY = child.geometry().height()+5
    #     #         if self.y_position > 0:
    #     #             self.y_position -= self.updateY
    #     for selection in listWidg:
    #         for child in self.scrollAreaWidgetContents.findChildren(selection):
    #             x = child.pos().x()
    #             y = child.pos().y()
    #             w = child.geometry().width()
    #             h = child.geometry().height()
    #             if y-self.updateY >= 0:
    #                 child.setGeometry(x,y-self.updateY,w,h)

    def saveProtocol(self):
        date = time.strftime('%m.%d.%Y-%H%M%S')
        save_path = 'C:\Users\LokoKoko\MAK-2017\Python_GUI\Protocols'
        completeName = os.path.join(save_path,"Protocol_"+date+".txt")
        file = open(completeName, 'w')
        file.write("Protocol - " + date+'\n')
        file.write(''+'\n')
        file.write('Final Y: ' + str(self.y_position) + '\n')
        file.write('' + '\n')
        list = [absMenu_Widget, absSpecMenu_Widget, flrMenu_Widget, flrSpecMenu_Widget, shakeMenu_Widget]
        for type in range(1, 6):
            for child in self.scrollAreaWidgetContents.findChildren(list[type-1]):
                file.write('Type: '+ str(type)+'\n')
                file.write('ObjectName: '+ child.objectName()+'\n')
                file.write('X: ' + str(child.pos().x())+'\n')
                file.write('Y: ' + str(child.pos().y())+'\n')
                file.write('W: ' + str(child.geometry().width())+'\n')
                file.write('H: ' + str(child.geometry().height())+'\n')
                if type == 1:
                    file.write('Wavelength: ' + str(child.wavelength.value())+'\n')
                    file.write('Exposure Time: ' + str(child.exposureTime.value())+'\n')
                elif type == 2:
                    file.write('Start Wavelength: ' + str(child.startWave.value())+'\n')
                    file.write('Stop Wavelength: ' + str(child.stopWave.value())+'\n')
                    file.write('Exposure Time: ' + str(child.exposureTime.value())+'\n')
                elif type == 3:
                    file.write('Excitation Wavelength: ' + str(child.excitationWave.currentText())+'\n')
                    file.write('Emission Wavelength: ' + str(child.emissionWave.value())+'\n')
                    file.write('Exposure Time: ' + str(child.exposureTime.value())+'\n')
                elif type == 4:
                    file.write('Excitation Wavelength: ' + str(child.excitationWave.currentText())+'\n')
                    file.write('Start Wavelength: ' + str(child.startWave.value())+'\n')
                    file.write('Stop Wavelength: ' + str(child.stopWave.value())+'\n')
                    file.write('Exposure Time: ' + str(child.exposureTime.value())+'\n')
                elif type == 5:
                    file.write('Duration: ' + str(child.duration.value())+'\n')
                file.write(''+'\n')
        file.close()

    def openProtocol(self):
        #Open menu
        dlg = QtGui.QFileDialog()
        dlg.setFileMode(QtGui.QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")
        self.filename = QStringList()
        if dlg.exec_():
            self.filename = dlg.selectedFiles()
            for child in self.scrollAreaWidgetContents.findChildren(QtGui.QWidget):
                child.hide()

        file = open(self.filename[0],'r')
        f = file.read().split('Type: ')
        self.y_position = int(f[0].split('Final Y: ')[1])
        self._buttons = -1
        for selection in range(1,len(f)):
            widg = f[selection].split('\n')
            type = int(widg[0])
            objName = str(widg[1].split('ObjectName: ')[1])
            print objName
            X = int(widg[2].split('X: ')[1])
            Y = int(widg[3].split('Y: ')[1])
            W = int(widg[4].split('W: ')[1])
            H = int(widg[5].split('H: ')[1])
            self._buttons += 1
            if type == 1:
                wavelength = int(widg[6].split('Wavelength: ')[1])
                exposureTime = int(widg[7].split('Exposure Time: ')[1])
                addWidgAbs = absMenu_Widget()
                addWidgAbs.setObjectName(objName)
                addWidgAbs.stopButton.clicked.connect(addWidgAbs.deleteLater)
                addWidgAbs.destroyed.connect(lambda: self.checked(1))
                #addWidgAbs.stopButton.clicked.connect(lambda: self.closeProtocol(1, addWidgAbs.pos()))
                addWidgAbs.setParent(self.scrollAreaWidgetContents)
                addWidgAbs.setGeometry(X, Y, W, H)
                addWidgAbs.wavelength.setValue(wavelength)
                addWidgAbs.exposureTime.setValue(exposureTime)
                addWidgAbs.show()
            elif type == 2:
                startWave = int(widg[6].split('Start Wavelength: ')[1])
                stopWave = int(widg[7].split('Stop Wavelength: ')[1])
                exposureTime = int(widg[8].split('Exposure Time: ')[1])
                addWidgAbsSpec = absSpecMenu_Widget()
                addWidgAbsSpec.setObjectName(objName)
                addWidgAbsSpec.stopButton.clicked.connect(addWidgAbsSpec.deleteLater)
                addWidgAbsSpec.destroyed.connect(lambda: self.checked(2))
                #addWidgAbsSpec.stopButton.clicked.connect(lambda: self.closeProtocol(2, addWidgAbsSpec.pos()))
                addWidgAbsSpec.setParent(self.scrollAreaWidgetContents)
                addWidgAbsSpec.setGeometry(X, Y, W, H)
                addWidgAbsSpec.startWave.setValue(startWave)
                addWidgAbsSpec.stopWave.setValue(stopWave)
                addWidgAbsSpec.exposureTime.setValue(exposureTime)
                addWidgAbsSpec.show()
            elif type == 3:
                excitationWave = widg[6].split('Excitation Wavelength: ')[1]
                emissionWave = int(widg[7].split('Emission Wavelength: ')[1])
                exposureTime = int(widg[8].split('Exposure Time: ')[1])
                addWidgFlr = flrMenu_Widget()
                addWidgFlr.setObjectName(objName)
                addWidgFlr.stopButton.clicked.connect(addWidgFlr.deleteLater)
                addWidgFlr.destroyed.connect(lambda: self.checked(3))
                #addWidgFlr.stopButton.clicked.connect(lambda: self.closeProtocol(3, addWidgFlr.pos()))
                addWidgFlr.setParent(self.scrollAreaWidgetContents)
                addWidgFlr.setGeometry(X, Y, W, H)
                index = addWidgFlr.excitationWave.findText(excitationWave, QtCore.Qt.MatchFixedString)
                addWidgFlr.excitationWave.setCurrentIndex(index)
                addWidgFlr.emissionWave.setValue(emissionWave)
                addWidgFlr.exposureTime.setValue(exposureTime)
                addWidgFlr.show()
            elif type == 4:
                excitationWave = widg[6].split('Excitation Wavelength: ')[1]
                startWave = int(widg[7].split('Start Wavelength: ')[1])
                stopWave = int(widg[8].split('Stop Wavelength: ')[1])
                exposureTime = int(widg[9].split('Exposure Time: ')[1])
                addWidgFlrSpec = flrSpecMenu_Widget()
                addWidgFlrSpec.setObjectName(objName)
                addWidgFlrSpec.stopButton.clicked.connect(addWidgFlrSpec.deleteLater)
                addWidgFlrSpec.destroyed.connect(lambda: self.checked(4))
                #addWidgFlrSpec.stopButton.clicked.connect(lambda: self.closeProtocol(4, addWidgFlrSpec.pos()))
                addWidgFlrSpec.setParent(self.scrollAreaWidgetContents)
                addWidgFlrSpec.setGeometry(X, Y, W, H)
                index = addWidgFlrSpec.excitationWave.findText(excitationWave, QtCore.Qt.MatchFixedString)
                addWidgFlrSpec.excitationWave.setCurrentIndex(index)
                addWidgFlrSpec.startWave.setValue(startWave)
                addWidgFlrSpec.stopWave.setValue(stopWave)
                addWidgFlrSpec.exposureTime.setValue(exposureTime)
                addWidgFlrSpec.show()
            elif type == 5:
                duration = int(widg[6].split('Duration: ')[1])
                addWidgShake = shakeMenu_Widget()
                addWidgShake.setObjectName(objName)
                addWidgShake.stopButton.clicked.connect(addWidgShake.deleteLater)
                addWidgShake.destroyed.connect(lambda: self.checked(5))
                #addWidgShake.stopButton.clicked.connect(lambda: self.closeProtocol(5, addWidgShake.pos()))
                addWidgShake.setParent(self.scrollAreaWidgetContents)
                addWidgShake.setGeometry(X, Y, W, H)
                addWidgShake.duration.setValue(duration)
                addWidgShake.show()
            print self.y_position

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = Example()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
