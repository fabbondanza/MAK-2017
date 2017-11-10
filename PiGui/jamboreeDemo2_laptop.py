from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot
import time
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import  FigureCanvasQTAgg as FigureCanvas
from math import factorial
from pylab import *
import os
import csv
import shutil
#from introScreen import *
from introScreen_v2 import *
from wellSelectScreen_v2 import *
from selectProtocolScreen_v2 import *
from absMenu import *
from absSpecMenu import *
from flrMenu_v2 import *
from flrSpecMenu import *
from measurementScreen import *
from calibrationScreen import *
from inputEmail import *
from arudinoPi_demos import *
from camera import *

###Includes for email sending ability of data
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

class KAMSpec(QtGui.QWidget):
    def __init__(self):
        super(KAMSpec, self).__init__()
        self.initUI()
        self.intro.startButton.clicked.connect(self.startWellSelect)
        self.intro.plateButton.clicked.connect(self.movePlateOut)
        self.intro.calibrateButton.clicked.connect(self.initializeCalibration)

        self.wellSelect.nextButton.clicked.connect(self.protocolSelectScreen)

        ### Connection Protocol Selection menu buttons to functions
        self.protocolSelect.absButton.clicked.connect(self.absSettings)
        # self.protocolSelect.absSpecButton.clicked.connect(self.absSpecSettings)
        self.protocolSelect.flrButton.clicked.connect(self.flrSettings)
        # self.protocolSelect.flrSpecButton.clicked.connect(self.flrSpecSettings)
        # self.protocolSelect.shakingButton.clicked.connect(self.shakeMenu)
        self.protocolSelect.addPlateButton.clicked.connect(self.addPlate)

        ### Connecting Absorbance Menu Settings buttons to functions
        self.absMenu.addProtocolButton.clicked.connect(lambda: self.addProtocol(1))
        # self.absSpecMenu.addProtocolButton.clicked.connect(lambda: self.addProtocol(2))
        self.flrMenu.addProtocolButton.clicked.connect(lambda: self.addProtocol(2))
        # self.flrSpecMenu.addProtocolButton.clicked.connect(lambda: self.addProtocol(4))
        self.absMenu.finishButton.clicked.connect(lambda: self.finishProtocolSelection(1))
        # self.absSpecMenu.finishButton.clicked.connect(lambda: self.finishProtocolSelection((2)))
        self.flrMenu.finishButton.clicked.connect(lambda: self.finishProtocolSelection(2))
        # self.flrSpecMenu.finishButton.clicked.connect(lambda:self.finishProtocolSelection(4))

        self.protocolDict = {}
        self.selectedWellsDict = {}
        self.protocolCount = [0]

    def initUI(self):

        self.intro = introScreen()
        self.wellSelect = wellSelectScreen()
        self.protocolSelect = selectProtocolScreen()
        self.absMenu = absMenu()
        # self.absSpecMenu = absSpecMenu()
        self.flrMenu = flrMenu()
        # self.flrSpecMenu = flrSpecMenu()
        self.machine = MotorMove()
        self.camera = LineCamera()
        self.measurementMenu = measurementScreen()
        self.calibrationMenu = calibrationScreen()
        self.plateCheck = True
        self.calibrationComplete = False
        self.slope = 0
        self.intercept = 0
        self.rowList = []

    def movePlateOut(self):
        # print 'plateOut'
        self.plateInsert = plateInsertionProtocol(self.machine)
        self.connect(self.plateInsert, QtCore.SIGNAL('finished()'), self.popOutMessage1)
        self.plateInsert.start()

    def popOutMessage1(self):
        result = QtGui.QMessageBox.question(QtGui.QWidget(), 'Plate Check', "Is a plate inserted?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                            QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            self.plateCheck = True
        else:
            self.plateCheck = False


    def startWellSelect(self):
        if self.plateCheck == True & self.calibrationComplete == True:
            self.intro.deleteLater()
            self.plateCount = 1
            self.protocolDict[self.plateCount] = []
            self.wellSelect.show()
        elif self.plateCheck == False:
            QtGui.QMessageBox.critical(QtGui.QWidget(), "Initialization Error", "Cannot start readings. No plate deteced. Please insert plate!")
        elif self.calibrationComplete == False:
            QtGui.QMessageBox.critical(QtGui.QWidget(), "Initialization Error", "Cannot start readings. Need to calibrate device first!")
        else:
            QtGui.QMessageBox.critical(QtGui.QWidget(), "Initialization Error", "Cannot start readings. Calibrate & Insert plate!")

    def protocolSelectScreen(self):
        self.wellSelect.hide()
        self.protocolSelect.show()
        self.selectedWellsDict[self.plateCount] = []
        for child in self.wellSelect.findChildren(QtGui.QLabel):
            if str(child.objectName()) in self.wellSelect.wellNames:
                name = str(child.objectName())
                row = name[0]
                column = int(name[1:len(name)])-1
                if self.wellSelect.selectionDict[row][column] == 'ON':
                    self.selectedWellsDict[self.plateCount].append(row+str(column))

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
        self.protocolCount[self.plateCount-1] += 1

        if type == 1:
            self.absMenu.hide()
            self.protocolDict[self.plateCount].append({type: {'Exposure Time': int(self.absMenu.exposureTimeSpinBox.value()), 'Wavelength': int(self.absMenu.wavelengthSpinBox.value())}})
            self.protocolSelect.show()
        elif type == 2:
            self.flrMenu.hide()
            self.protocolDict[self.plateCount].append({type: {'Exposure Time': int(self.flrMenu.exposureTimeSpinBox.value()), 'Excitation': str(self.flrMenu.excitationWavelengthComboBox.currentText())}})
            self.protocolSelect.show()

    def addPlate(self):
        self.plateCount += 1
        self.protocolCount.append(0)
        self.protocolDict[self.plateCount] = []
        self.protocolSelect.hide()
        self.wellSelect.clearWells()
        self.wellSelect.show()

    def finishProtocolSelection(self,type):
        self.protocolCount[self.plateCount-1] += 1
        if type == 1:
            self.absMenu.hide()
            self.protocolDict[self.plateCount].append({type: {'Exposure Time': int(self.absMenu.exposureTimeSpinBox.value()), 'Wavelength': int(self.absMenu.wavelengthSpinBox.value())}})
            self.measurementMenu.show()
            self.type = 1
        elif type == 2:
            self.flrMenu.hide()
            self.protocolDict[self.plateCount].append({type: {'Exposure Time': int(self.flrMenu.exposureTimeSpinBox.value()), 'Excitation': str(self.flrMenu.excitationWavelengthComboBox.currentText())}})
            self.measurementMenu.show()

        self.plate = 1
        self.measurementCheck = 0
        self.ypos = 0
        self.folderName =  time.strftime('%m_%d_%Y') + '_KAMSpec_Data_'+ time.strftime('%H_%M_%S')
        self.folder = 'Results\ ' + self.folderName
        os.makedirs(self.folder)
        for plate in range(1,self.plateCount+1):
            self.ypos += 2
            self.checkButton = QtGui.QCheckBox()
            self.checkButton.setText('Plate #'+str(plate))
            self.checkButton.setObjectName('Plate_'+str(plate))
            self.measurementMenu.gridLayout.addWidget(self.checkButton, self.ypos,1,1,4)
            for protocol in range(0,self.protocolCount[plate-1]):
                self.ypos += 1
                self.protocolCheckBox = QtGui.QCheckBox()
                self.protocolCheckBox.setObjectName('Plate_'+str(plate)+'_Protocol_'+str(protocol+1))
                if self.protocolDict[plate][protocol].keys()[0] == 1:
                    self.protocolCheckBox.setText('Absorbance')
                elif self.protocolDict[plate][protocol].keys()[0] == 2:
                    self.protocolCheckBox.setText('Flourescent Intensity')
                # elif self.protocolDict[plate][protocol].keys()[0] == 3:
                #     self.protocolCheckBox.setText('Flourescent Intensity')
                # elif self.protocolDict[plate][protocol].keys()[0] == 4:
                #     self.protocolCheckBox.setText('Flourescence Spectrum')
                self.measurementMenu.gridLayout.addWidget(self.protocolCheckBox, self.ypos,2, 1, 4)

        self.individualPlateRun(self.plate)

    def individualPlateRun(self, plate):
        self.csvFileName = self.folder+'\Plate_'+str(self.plate)+'_'+time.strftime('%d%m%Y')+'.csv'
        with open(self.csvFileName, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['KAM-Spec 2017'])
            spamwriter.writerow(['Date:', time.strftime('%m/%d/%Y')])
            spamwriter.writerow(['Time:', time.strftime('%H:%M:%S')])
            spamwriter.writerow([' '])
            spamwriter.writerow([' '])
            spamwriter.writerow([' '])
            spamwriter.writerow([' '])
            csvfile.close()
            self.protocol = 0
            self.lengthMeasurements = len(self.selectedWellsDict[self.plate])
            self.individualProtocolRun(self.plate,self.protocol, self.csvFileName)

    def individualProtocolRun(self, plate, protocol, csvFileName):
        if self.protocolDict[plate][protocol].keys()[0] == 1:
            self.type = 1
            self.lengthMeasurements = len(self.selectedWellsDict[plate])
            exposureTime = int(self.protocolDict[plate][protocol][1]['Exposure Time'])
            # print exposureTime
            wavelength = int(self.protocolDict[plate][protocol][1]['Wavelength'])
            self.abs_protocol = executeProtocol(1, self.selectedWellsDict, self.protocolDict, plate, protocol,
                                                csvFileName, self.camera, self.machine, self.measurementMenu,
                                                self.lengthMeasurements,self.slope,self.intercept)
            self.connect(self.abs_protocol, QtCore.SIGNAL("updateCurrentProtocol(QString)"), self.updateCurrentProtocol)
            self.connect(self.abs_protocol, QtCore.SIGNAL("statusPrint(QString)"), self.statusPrint)
            self.connect(self.abs_protocol, QtCore.SIGNAL("checkBox(QString)"), self.checkBox)
            self.connect(self.abs_protocol, QtCore.SIGNAL("cameraReady(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"), self.cameraStarter)
            self.abs_protocol.start()
        elif self.protocolDict[plate][protocol].keys()[0] == 2:
            self.type = 2
            self.lengthMeasurements = len(self.selectedWellsDict[plate])
            # exposureTime = int(self.protocolDict[plate][protocol][1]['Exposure Time'])
            # # print exposureTime
            # wavelength = int(self.protocolDict[plate][protocol][1]['Wavelength'])
            self.flr_protocol = executeProtocol(2, self.selectedWellsDict, self.protocolDict, plate, protocol,
                                                csvFileName, self.camera, self.machine, self.measurementMenu,
                                                self.lengthMeasurements,self.slope,self.intercept)
            self.connect(self.flr_protocol, QtCore.SIGNAL("updateCurrentProtocol(QString)"), self.updateCurrentProtocol)
            self.connect(self.flr_protocol, QtCore.SIGNAL("statusPrint(QString)"), self.statusPrint)
            self.connect(self.flr_protocol, QtCore.SIGNAL("checkBox(QString)"), self.checkBox)
            self.connect(self.flr_protocol, QtCore.SIGNAL("cameraReady(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"), self.cameraStarter)
            self.flr_protocol.start()


    def cameraStarter(self, exposureTime, wellList, waveOrled):
        self.exposureTime = exposureTime
        self.wellList = wellList
        self.wavelength = waveOrled
        self.excitationLED = waveOrled
        self.cameraStart = cameraInitialization(self.camera, exposureTime)
        self.connect(self.cameraStart, QtCore.SIGNAL("finished()"), self.cameraReady)
        self.cameraStart.start()

    def cameraReady(self):
        self.cameraStart.stop()

        if self.type == 1:
            self.updateCurrentProtocol('Plate '+ str(self.plate)+'- Absorbance...')
        elif self.type == 2:
            self.emit(QtCore.SIGNAL("updateCurrentProtocol(QString)"), 'Plate ' + str(self.plate) + '- Flourescent Intensity...')
        self.protocolStart = machineInitialization(self.machine,self.wellList, self.csvFileName, self.camera, self.measurementMenu)
        self.connect(self.protocolStart, QtCore.SIGNAL("runProtocol(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"), self.runProtocol)
        self.protocolStart.start()
        # print 'Camera Ready'

    def runProtocol(self, machine, toRead, dictionary, filename, camera, graph):
        # print 'runProtocol'
        self.protocolStart.stop()
        self.wellsToRead = toRead
        self.measureThread = measureProtocol(machine, toRead, dictionary, filename, camera, graph, self.type, self.slope, self.intercept, self.wavelength, self.excitationLED)
        self.connect(self.measureThread, QtCore.SIGNAL("addPlot(PyQt_PyObject,PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"), self.addPlot)
        self.measureThread.start()

    def addPlot(self, x,y,i, dictionary, toRead):
        # print 'addPlot'
        self.addCurve(x,y,i, self.protocol,dictionary, toRead)
        if i == self.lengthMeasurements-1:
            self.checkBox()
            self.statusPrint()


    def checkBox(self):
        for child in self.measurementMenu.findChildren(QtGui.QCheckBox):
            objName = str(child.objectName())
            splitName = objName.split('_')
            if len(splitName) > 2:
                # print splitName
                plateNumb = int(splitName[1])
                protocolNumb = int(splitName[3])
                if plateNumb == self.plate:
                    if protocolNumb == self.protocol+1:
                        child.toggle()

    def statusPrint(self):
        self.protocol += 1
        if self.protocol <= self.protocolCount[self.plate-1]-1:
            self.individualProtocolRun(self.plate, self.protocol, self.csvFileName)
        else:
            # print 'Done All Protocols for Plate #'+str(self.plate)
            for child in self.measurementMenu.findChildren(QtGui.QCheckBox):
                objName = str(child.objectName())
                splitName = objName.split('_')
                if len(splitName) == 2:
                    plateNumb = int(splitName[1])
                    if plateNumb == self.plate:
                        child.toggle()
            self.plate += 1
            if self.plate <= self.plateCount:
                self.individualPlateRun(self.plate)
            else:
                # print 'Done All Plates'
                plt.cla()
                self.reset()
                # self.emailSend = sendDataEmail(self.folderName, self.folder)
                # self.connect(self.emailSend, QtCore.SIGNAL('finished()'), self.reset)
                # self.emailSend.start()
    def stopwatch(self, seconds):
        start = time.time()
        time.clock()
        elapsed = 0
        while elapsed < seconds:
            elapsed = time.time() - start

    def initializeCalibration(self):
        self.intro.hide()
        self.calibrationMenu.show()
        self.calibrate_data = {}
        self.calibrateRun = measureCalibration(self.machine, self.camera)
        self.connect(self.calibrateRun, QtCore.SIGNAL("getMaxCalib(PyQt_PyObject)"), self.getMaxCalib)
        self.calibrateRun.start()

        plt.cla()
        self.axC = self.calibrationMenu.figure.add_subplot(111)
        self.axC.set_ylim(-10, 0xffff + 10)
        self.axC.set_xlim(0, 3648)
        self.curveCalib, = self.axC.plot([], [])
        self.read_frame()
        timerCalib = self.calibrationMenu.figure.canvas.new_timer(interval=250)
        timerCalib.add_callback(self.updateCalibrate)
        # self.ax.plot(x, y, label = str(self.selectedWellsDict[self.plate][i]))
        timerCalib.start()
        thisManager = get_current_fig_manager()
        thisManager.window.SetPosition((751, 361))
        plt.show()
        while self.calibrationComplete == False:
            print 'Calibrating'
        timerCalib.stop()


    def getMaxCalib(self, led):
        maxCalib = np.max(self.dataCalib)
        # print maxCalib
        smooth_data = self.savitzky_golay(self.dataCalib, 21, 2)
        self.calibrate_data[led] = list(np.where(smooth_data == np.max(smooth_data)))[0][0]
        if len(self.calibrate_data) == 3:
            self.calculateRegression()

    def calculateRegression(self):
        self.led_wavelengths = {
        'B': [468], 'Y': [585], 'R': [635]
        }

        self.regressionEquation = np.polyfit([self.calibrate_data['B'], self.calibrate_data['Y'], self.calibrate_data['R']],[self.led_wavelengths['B'], self.led_wavelengths['Y'], self.led_wavelengths['R']],1)
        # print self.regressionEquation
        self.slope = self.regressionEquation[0][0]
        self.intercept = self.regressionEquation[1][0]
        self.setCalibration()


    def setCalibration(self):
        self.calibrationComplete = True
        self.x = range(0, 3648)
        for j in self.x:
            self.x[j] = self.slope * j + self.intercept

        self.intro.show()
        self.calibrationMenu.deleteLater()

    def savitzky_golay(self, y, window_size, order, deriv=0, rate=1):
        try:
            window_size = np.abs(np.int(window_size))
            order = np.abs(np.int(order))
        except ValueError, msg:
            raise ValueError("window_size and order have to be of type int")
        if window_size % 2 != 1 or window_size < 1:
            raise TypeError("window_size size must be a positive odd number")
        if window_size < order + 2:
            raise TypeError("window_size is too small for the polynomials order")
        order_range = range(order + 1)
        half_window = (window_size - 1) // 2
        # precompute coefficients
        b = np.mat([[k ** i for i in order_range] for k in range(-half_window, half_window + 1)])
        m = np.linalg.pinv(b).A[deriv] * rate ** deriv * factorial(deriv)
        # pad the signal at the extremes with
        # values taken from the signal itself
        firstvals = y[0] - np.abs(y[1:half_window + 1][::-1] - y[0])
        lastvals = y[-1] + np.abs(y[-half_window - 1:-1][::-1] - y[-1])
        y = np.concatenate((firstvals, y, lastvals))
        return np.convolve(m[::-1], y, mode='valid')


    def read_frame2(self):
        for i in range(0,10):
            frame = self.camera.get_frame()
        return frame.image

    def read_frame(self):
        try:
            frame = self.camera.get_frame()
        except:
            return None
        if frame is not None:
            return frame.image  # - np.mean(frame.dark)
        else:
            return None



    def reset(self):
        self.wellSelect.hide()
        self.protocolSelect.hide()
        self.absMenu.hide()
        # self.absSpecMenu.hide()
        self.flrMenu.hide()
        # self.flrSpecMenu.hide()
        self.measurementMenu.hide()
        self.intro = introScreen()
        self.protocolDict = {}
        self.selectedWellsDict = {}
        self.protocolCount = [0]
        self.intro.startButton.clicked.connect(self.startWellSelect)
        self.intro.plateButton.clicked.connect(self.movePlateOut)
        self.intro.calibrateButton.clicked.connect(self.initializeCalibration)
        for child in self.measurementMenu.gridLayout.findChildren(QtGui.QCheckBox):
            self.measurementMenu.gridLayout.removeWidget(child)
        self.measurementMenu.figure.clear()

    def updateCurrentProtocol(self, protocolString):
        self.measurementMenu.measurementLabel.setText(protocolString)
        # self.abs_protocol.stop()

    def addCurve(self, x, y, i, protocol, dictionary, toRead):
        # print x
        # print y
        well = i+1
        self.dataDict = dictionary
        self.toReadNum = toRead
        if i == 0:
            plt.cla()
            self.measurementMenu.figure.clear()
            self.ax = self.measurementMenu.figure.add_subplot(111)
            self.ax.set_ylim(-10, 0xffff + 10)
            self.ax.set_xlim(np.min(self.x), np.max(self.x))
            self.curve, = self.ax.plot([], [])
            self.read_frame()
            timerMeasure = self.measurementMenu.figure.canvas.new_timer(interval=1000)
            timerMeasure.add_callback(self.update)
            # self.ax.plot(x, y, label = str(self.selectedWellsDict[self.plate][i]))
            timerMeasure.start()
            thisManager = get_current_fig_manager()
            thisManager.window.SetPosition((511, 361))
            plt.show()
            self.dataDict[self.toReadNum[i][0][0]][int(self.toReadNum[i][0][1:len(self.toReadNum[i][0])]) + 1] = self.data
            self.rowList.append(self.dataDict[self.toReadNum[i][0][0]][int(self.toReadNum[i][0][1:len(self.toReadNum[i][0])]) + 1])
        self.dataDict[self.toReadNum[i][0][0]][int(self.toReadNum[i][0][1:len(self.toReadNum[i][0])]) + 1] = self.data
        self.rowList.append(self.dataDict[self.toReadNum[i][0][0]][int(self.toReadNum[i][0][1:len(self.toReadNum[i][0])]) + 1])
        if well == self.lengthMeasurements:
            with open(self.csvFileName, 'ab') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerows(zip(*self.rowList))
                spamwriter.writerow(' ')
                spamwriter.writerow(' ')
                csvfile.close()
            # timerMeasure.stop()
            # self.reset()
        # self.measurementMenu.figure.savefig(self.folder+'\Plate'+str(self.plate)+'Protocol'+str(protocol)+'Well'+self.wellsToRead[i]+'.png')


    def update(self):
        self.data = self.read_frame()
        if self.data is None:
            return True
        else:
            x = self.x
            self.curve.set_data(x, self.data)
            self.measurementMenu.figure.canvas.draw()

    def updateCalibrate(self):
        if self.calibrationComplete == False:
            self.dataCalib = self.read_frame()
            if self.dataCalib is None:
                return True
            else:
                x = np.arange(len(self.dataCalib))
                self.curveCalib.set_data(x, self.dataCalib)
                self.calibrationMenu.figure.canvas.draw()

class cameraInitialization(QtCore.QThread):
    def __init__(self,camera, exposureTime):
        QtCore.QThread.__init__(self)
        self.camera = camera
        self.exposureTime = exposureTime

    def __del__(self):
        self.wait()

    def stop(self):
        self.terminate()

    def run(self):
        # print 'Initializing Camera'
        self.camera.set_exposure_time(self.exposureTime)
        # self.emit(QtCore.SIGNAL("finished()"), self.cameraReady)
        self.sleep(2)

class plateInsertionProtocol(QtCore.QThread):
    def __init__(self, machine):
        QtCore.QThread.__init__(self)
        self.machine = machine
        # print 'Moving plate/holder to slot'

    def __del__(self):
        self.wait()

    def run(self):
        self.machine._set_opening_position()
        time.sleep(2)


class machineInitialization(QtCore.QThread):
    signalList = QtCore.pyqtSignal(object, list, dict, str,  object, QtGui.QWidget)
    def __init__(self, machine, wellList, csvFileName, camera, graph):
        QtCore.QThread.__init__(self)
        self.machine = machine
        self.wellList = wellList
        self.csvFileName = csvFileName
        self.camera = camera
        self.measurementScreen = graph
        # print 'Initializing Machine'

        self.wellPositions = [
            [[5.5, 47], [11.5, 47], [18, 47], [24.5, 47], [31, 47], [37.5, 47], [44, 47], [50.5, 47], [57, 47],
             [63.5, 47], [70, 47], [76.5, 47]],
            [[5.5, 40], [11.5, 40], [18, 40], [24.5, 40], [31, 40], [37.5, 40], [44, 40], [50.5, 40], [57, 40],
             [63.5, 40], [70, 40], [76.5, 40]],
            [[5.5, 34], [11.5, 34], [18, 34], [24.5, 34], [31, 34], [37.5, 34], [44, 34], [50.5, 34], [57, 34],
             [63.5, 34], [70, 34], [76.5, 34]],
            [[5.5, 27], [11.5, 27], [18, 27], [24.5, 27], [31, 27], [37.5, 27], [44, 27], [50.5, 27], [57, 27],
             [63.5, 27], [70, 27], [76.5, 27]],
            [[5.5, 21], [11.5, 21], [18, 21], [24.5, 21], [31, 21], [37.5, 21], [44, 21], [50.5, 21], [57, 21],
             [63.5, 21], [70, 21], [76.5, 21]],
            [[5.5, 15], [11.5, 15], [18, 15], [24.5, 15], [31, 15], [37.5, 15], [44, 15], [50.5, 15], [57, 15],
             [63.5, 15], [70, 15], [76.5, 15]],
            [[5.5, 9], [11.5, 9], [18, 9], [24.5, 9], [31, 9], [37.5, 9], [44, 9], [50.5, 9], [57, 9], [63.5, 9],
             [70, 9], [76.5, 9]],
            [[5.5, 3], [11.5, 3], [18, 3], [24.5, 3], [31, 3], [37.5, 3], [44, 3], [50.5, 3], [57, 3], [63.5, 3],
             [70, 3], [76.5, 3]]]

    def __del__(self):
        self.wait()

    def stop(self):
        self.terminate()

    def run(self):
        self.machine._set_initial_position()
        self.toReadNum = []
        time.sleep(2)
        # print self.wellList
        for well in self.wellList:
            rowString = "ABCDEFGH"
            for l in range(0, len(rowString)):
                if well[0] == rowString[l]:
                    yindex = l
                else:
                    continue
            for n in range(0, 12):
                if int(well[1:len(well)]) == n:
                    xindex = n
            self.wellX = self.wellPositions[yindex][xindex][0]
            self.wellY = self.wellPositions[yindex][xindex][1]
            self.wellPosition = 'M' + str(self.wellX) + ',' + str(self.wellY)
            self.toReadNum.append([well, self.wellPosition])
        # print self.toReadNum
        self.dataDict = {}
        for i in range(0, len(self.toReadNum)):
             self.dataDict[self.toReadNum[i][0][0]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.emit(QtCore.SIGNAL('runProtocol(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)'), self.machine, self.toReadNum, self.dataDict, self.csvFileName, self.camera, self.measurementScreen)
       #self.signalList.emit(self.machine, self.toReadNum, self.dataDict, self.csvFileName, self.camera, self.measurementScreen)
        self.sleep(2)


class measureCalibration(QtCore.QThread):
    def __init__(self, machine, camera):
        QtCore.QThread.__init__(self)
        self.machine = machine
        self.camera = camera

    def __del__(self):
        self.wait()

    def stop(self):
        self.terminate()

    def run(self):
        self.machine._set_opening_position()
        while self.machine.motorStatus == 0:
            print "Moving"
        print 'Reached Initial Position'
        self.camera.set_work_mode(WorkMode.NORMAL)
        time.sleep(1)

        self.exposureTime = 250
        self.camera.set_exposure_time(self.exposureTime)
        self.machine._toggle_led('B')
        time.sleep(2)
        self.emit(QtCore.SIGNAL("getMaxCalib(PyQt_PyObject)"), 'B')
        self.machine._toggle_led('B')
        time.sleep(2)

        self.exposureTime = 2500
        self.camera.set_exposure_time(self.exposureTime)
        time.sleep(2)
        self.machine._toggle_led('Y')
        time.sleep(2)
        self.emit(QtCore.SIGNAL("getMaxCalib(PyQt_PyObject)"), 'Y')
        self.machine._toggle_led('Y')
        time.sleep(2)

        self.exposureTime = 8
        self.camera.set_exposure_time(self.exposureTime)
        time.sleep(2)
        self.machine._toggle_led('R')
        time.sleep(2)
        self.emit(QtCore.SIGNAL("getMaxCalib(PyQt_PyObject)"), 'R')
        self.machine._toggle_led('R')


    def stopwatch(self, seconds):
        start = time.time()
        time.clock()
        elapsed = 0
        while elapsed < seconds:
            elapsed = time.time() - start

class measureProtocol(QtCore.QThread):
    def __init__(self, machine, toRead, dictionary, csvFileName, camera, graph, type, slope, intercept, wavelength, led):
        QtCore.QThread.__init__(self)
        self.machine = machine
        self.toReadNum = toRead
        self.dataDict = dictionary
        self.csvFileName = csvFileName
        self.camera = camera
        self.measurementScreen = graph
        self.type = type
        self.slope = slope
        self.intercept = intercept
        self.wavelength = wavelength
        self.excitationLED = led

    def __del__(self):
        self.wait()

    def stop(self):
        self.terminate()

    def read_frame(self):
        try:
            frame = self.camera.get_frame()
        except:
            return None
        if frame is not None:
            return frame.image  # - np.mean(frame.dark)
        else:
            return None

    def run(self):
        # print 'Starting'

        # print self.type
        if self.type == 1:
            rowList = []
            for i in range(0,len(self.toReadNum)):
                self.machine._set_new_position(self.toReadNum[i][0],self.toReadNum[i][1])
                print "Moving"
                self.machine._toggle_led('W')
                time.sleep(2)
                absData = self.read_frame()
                if self.slope == 0:
                    x = range(1, len(absData) + 1)
                    self.wavelengthIndex = 1500
                else:
                    minList = []
                    x = range(1, len(absData) + 1)
                    for j in x:
                        x[j-1] = self.slope*j + self.intercept
                    # for k in range(0, len(x)):
                    #     minList.append(abs(x[k] - self.wavelength))
                    # for l in range(0, len(minList)):
                    #     if minList[l] == np.min(minList):
                    #         self.wavelengthIndex = l
                y = absData
                self.emit(QtCore.SIGNAL("addPlot(PyQt_PyObject,PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"), x, y, i, self.dataDict, self.toReadNum)
                self.machine._toggle_led('W')
                time.sleep(2)

        elif self.type == 2:
            if self.excitationLED == 'Blue':
                ledOn = 'b'
            elif self.excitationLED == 'Green':
                ledOn = 'g'
            elif self.excitationLED == 'Yellow':
                ledOn = 'y'
            rowList = []
            for i in range(0, len(self.toReadNum)):
                self.machine._set_new_position(self.toReadNum[i][0], self.toReadNum[i][1])
                print "Moving"
                self.machine._toggle_led(ledOn)
                time.sleep(2)
                absData = self.read_frame()
                if self.slope == 0:
                    x = range(1, len(absData) + 1)
                    self.wavelengthIndex = 1500
                else:
                    minList = []
                    x = range(1, len(absData) + 1)
                    for j in x:
                        x[j - 1] = self.slope * j + self.intercept
                    # for k in range(0, len(x)):
                    #     minList.append(abs(x[k] - self.wavelength))
                    # for l in range(0, len(minList)):
                    #     if minList[l] == np.min(minList):
                    #         self.wavelengthIndex = l
                y = absData
                self.emit(QtCore.SIGNAL(
                    "addPlot(PyQt_PyObject,PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"), x, y,
                          i, self.dataDict, self.toReadNum)
                self.machine._toggle_led(ledOn)
                time.sleep(2)
        self.sleep(2)


class executeProtocol(QtCore.QThread):
    def __init__(self, type, selectedWellsDict, protocolDict, plateNumb, protocolNumb, csvFileName, camera, machine, graph, length, slope, intercept):
        QtCore.QThread.__init__(self)
        self.type = type
        self.selectedWellsDict = selectedWellsDict
        self.protocolDict = protocolDict
        self.plate = plateNumb
        self.protocol = protocolNumb
        self.csvFileName = csvFileName
        self.camera = camera
        self.machine = machine
        self.measurementScreen = graph
        self.lengthMeasurements = length
        self.slope = slope
        self.intercept = intercept


    def __del__(self):
        self.wait()

    def stop(self):
        self.terminate()

    def run(self):
        self.running = True
        count = 0
        while self.running == True:
            count += 1
            if count == 1:
                if self.type == 1:
                    self.wellList = self.selectedWellsDict[self.plate]
                    self.exposureTime = int(self.protocolDict[self.plate][self.protocol][1]['Exposure Time'])
                    self.wavelength = int(self.protocolDict[self.plate][self.protocol][1]['Wavelength'])
                    self.absProtocol(self.wellList, self.exposureTime, self.wavelength, self.csvFileName)
                elif self.type == 2:
                    self.wellList =self.selectedWellsDict[self.plate]
                    self.exposureTime = int(self.protocolDict[self.plate][self.protocol][2]['Exposure Time'])
                    self.excitationLED = self.protocolDict[self.plate][self.protocol][2]['Excitation']
                    self.flrProtocol(self.wellList, self.exposureTime, self.excitationLED, self.csvFileName)
            else:
                continue



    def absProtocol(self, wellList, exposureTime, wavelength, csvFileName):
        with open(csvFileName, 'ab') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Absorbance'])
            spamwriter.writerow([' ']+['Exposure Time:'] + [str(exposureTime)+' ms'])
            spamwriter.writerow([' ']+['Wavelength:']+[str(wavelength)+' nm'])
            spamwriter.writerow(' ')
            csvfile.close()
        self.emit(QtCore.SIGNAL('cameraReady(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)'), exposureTime, self.wellList, self.wavelength)
        self.running = False

    def flrProtocol(self, wellList, exposureTime, led, csvFileName):
        with open(csvFileName, 'ab') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Fluorescence'])
            spamwriter.writerow([' ']+['Exposure Time:'] + [str(exposureTime)+' ms'])
            spamwriter.writerow([' ']+['LED:']+[led])
            spamwriter.writerow(' ')
            csvfile.close()
        self.emit(QtCore.SIGNAL('cameraReady(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)'), exposureTime, self.wellList, self.excitationLED)
        self.running = False

class sendDataEmail(QtCore.QThread):
    def __init__(self, folderName, folderDirectory):
        QtCore.QThread.__init__(self)
        self.folderName = folderName
        self.directory = folderDirectory

    def __del__(self):
        self.wait()

    def run(self):
        shutil.make_archive(self.directory, 'zip', self.directory)
        inputter = InputEmail()
        inputter.exec_()
        emailfrom = "kamspec2017l@gmail.com"
        emailto = str(inputter.text.text())
        fileToSend = self.directory + '.zip'
        username = "kamspec2017@gmail.com"
        password = "pennigem"

        msg = MIMEMultipart()
        msg["From"] = emailfrom
        msg["To"] = emailto
        msg["Subject"] = "[KAM-Spec] Data File Transfer, Date: " + time.strftime("%d:%m:%Y") +', Time: ' + time.strftime("%H:%M:%S")
        msg.preamble = "[KAM-Spec] Data File Transfer, Date: " + time.strftime("%d:%m:%Y") +', Time: ' + time.strftime("%H:%M:%S")

        ctype, encoding = mimetypes.guess_type(fileToSend)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"

        maintype, subtype = ctype.split("/", 1)

        if maintype == "text":
            fp = open(fileToSend)
            # Note: we should handle calculating the charset
            attachment = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "image":
            fp = open(fileToSend, "rb")
            attachment = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "audio":
            fp = open(fileToSend, "rb")
            attachment = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(fileToSend, "rb")
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
        msg.attach(attachment)

        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username, password)
        server.sendmail(emailfrom, emailto, msg.as_string())
        server.quit()

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = KAMSpec()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()