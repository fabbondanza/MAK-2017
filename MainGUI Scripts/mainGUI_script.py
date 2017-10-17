from PyQt4 import QtGui
from PyQt4 import QtCore
import numpy as np
import os.path
from threading import Thread
from functools import partial
from absMenu import *
from absSpecMenu import *
from flrMenu import *
from flrSpecMenu import *
from shakeMenu import *
from wellplateMenu import *
from optionsMenu import *
from arudino import *
from camera import *
import win32com.client
import time
import matplotlib.pyplot as pl
import numpy as np
from math import factorial

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
        self.optionsWidg.runButton.clicked.connect(self.startMeasurement)
        self.optionsWidg.calibrateButton.clicked.connect(self.calibrate)

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
            self.widgetTypesAdded[int(str(parent.objectName()))].append([protocol.pos().y(),type])
        if type == 2:
            yposition = self.yPosDict[int(str(parent.objectName()))]
            protocol = absSpecMenu()
            protocol.setGeometry(5, yposition , 600, 130)
            protocol.closeButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.deleteProtocol(2,parent))
            protocol.setParent(parent)
            protocol.show()

            self.yPosDict[int(str(parent.objectName()))] += 130 #Update lowest y-position of last widget in scroll area where widget was just added
            self.widgetTypesAdded[int(str(parent.objectName()))].append([protocol.pos().y(),type])
        if type == 3:
            yposition = self.yPosDict[int(str(parent.objectName()))]
            protocol = flrMenu()
            protocol.setGeometry(5, yposition , 600, 125)
            protocol.closeButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.deleteProtocol(3,parent))
            protocol.setParent(parent)
            protocol.show()

            self.yPosDict[int(str(parent.objectName()))] += 125 #Update lowest y-position of last widget in scroll area where widget was just added
            self.widgetTypesAdded[int(str(parent.objectName()))].append([protocol.pos().y(),type])
        if type == 4:
            yposition = self.yPosDict[int(str(parent.objectName()))]
            protocol = flrSpecMenu()
            protocol.setGeometry(5, yposition , 600, 186)
            protocol.closeButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.deleteProtocol(4,parent))
            protocol.setParent(parent)
            protocol.show()

            self.yPosDict[int(str(parent.objectName()))] += 186 #Update lowest y-position of last widget in scroll area where widget was just added
            self.widgetTypesAdded[int(str(parent.objectName()))].append([protocol.pos().y(),type])
        if type == 5:
            yposition = self.yPosDict[int(str(parent.objectName()))]
            protocol = shakeMenu()
            protocol.setGeometry(5, yposition , 600, 99)
            protocol.closeButton.clicked.connect(protocol.deleteLater)
            protocol.destroyed.connect(lambda: self.deleteProtocol(5,parent))
            protocol.setParent(parent)
            protocol.show()

            self.yPosDict[int(str(parent.objectName()))] += 99 #Update lowest y-position of last widget in scroll area where widget was just added
            self.widgetTypesAdded[int(str(parent.objectName()))].append([protocol.pos().y(),type])

    def deleteProtocol(self,type,parent):
        widgetHeights = [100, 130, 125, 186, 99]
        deletedHeight = widgetHeights[type-1]
        widgetOptions = [absMenu, absSpecMenu, flrMenu, flrSpecMenu, shakeMenu]
        protocolsLeftYpositionsList = []
        formerProtocolList = []
        deletedProtocol = 0
        listOfParentArea = self.widgetTypesAdded[int(str(parent.objectName()))]
        sortedListofParentArea = sorted(listOfParentArea, key = lambda x: x[0])
        #print sortedListofParentArea
        for i in range(0, len(sortedListofParentArea)):
            formerProtocolList.append(sortedListofParentArea[i][0])

        for i in range(0,len(widgetOptions)):
            for child in parent.findChildren(widgetOptions[i]):
                protocolsLeftYpositionsList.append(child.pos().y())

        sortedRemainingProtocolyPositions = np.sort(protocolsLeftYpositionsList)
        print sortedRemainingProtocolyPositions
        for i in range(0,len(sortedRemainingProtocolyPositions)):
            if formerProtocolList[i] != sortedRemainingProtocolyPositions[i]:
                deletedProtocol = formerProtocolList[i]
                #print deletedProtocol
                break

        if deletedProtocol != 0:
            self.widgetTypesAdded[int(str(parent.objectName()))] = []
            for i in range(0, len(widgetOptions)):
                for child in parent.findChildren(widgetOptions[i]):
                    if child.pos().y() <= deletedProtocol:
                        self.widgetTypesAdded[int(str(parent.objectName()))].append([child.pos().y(),i+1])
                    elif child.pos().y() > deletedProtocol:
                        #print int(str(child.objectName()))
                        child.setGeometry(child.pos().x(),child.pos().y()-deletedHeight,child.geometry().width(),child.geometry().height())
                        self.widgetTypesAdded[int(str(parent.objectName()))].append([child.pos().y(),i+1])
                        #print int(str(child.objectName()))
        else:
            self.widgetTypesAdded[int(str(parent.objectName()))] = []
            for i in range(0, len(widgetOptions)):
                for child in parent.findChildren(widgetOptions[i]):
                    self.widgetTypesAdded[int(str(parent.objectName()))].append([child.pos().y(),i+1])
        self.yPosDict[int(str(parent.objectName()))] -= deletedHeight
        #print self.widgetTypesAdded

    def startMeasurement(self):
        self.toReadDict = {}
        self.dictOfProtocols = {}
        widgetOptions = [absMenu, absSpecMenu, flrMenu, flrSpecMenu, shakeMenu]
        for child in self.scrollAreaWidgetContents.findChildren(QtGui.QScrollArea):
            wellsToRead = []
            protocolNumber = int(str(child.objectName()))
            self.dictOfProtocols[protocolNumber] = {}

            for wellplate in child.findChildren(wellplateMenu):
                for radiobutton in wellplate.findChildren(QtGui.QRadioButton):
                    if radiobutton.isChecked() == True:
                        wellsToRead.append(str(radiobutton.objectName()))
            sortedWells = sorted(sorted(wellsToRead, key = lambda x:int(x[1:len(x)])), key = lambda x: x[0])
            self.toReadDict[protocolNumber] = sortedWells

            listofWidgets = self.widgetTypesAdded[protocolNumber]

            for i in range(0, len(listofWidgets)):
                if listofWidgets[i][1] == 1:
                    for widget in child.findChildren(absMenu):
                        if widget.pos().y() == listofWidgets[i][0]:
                            type = 'Absorbance'
                            expTime = widget.exposureTimeBox.value()
                            wavelength = widget.wavelengthBox.value()
                            self.dictOfProtocols[protocolNumber][i+1] = {
                                'Type': type,
                                'Exposure Time': expTime,
                                'Wavelength': wavelength
                            }
                elif listofWidgets[i][1] == 2:
                    for widget in child.findChildren(absSpecMenu):
                        if widget.pos().y() == listofWidgets[i][0]:
                            type = 'Absorbance Spectrum'
                            expTime = widget.exposureTimeBox.value()
                            start = widget.startWavelengthBox.value()
                            stop = widget.stopWavelengthBox.value()
                            self.dictOfProtocols[protocolNumber][i+1] = {
                                'Type': type,
                                'Exposure Time': expTime,
                                'Start Wavelength': start,
                                'Stop Wavelength': stop
                            }
                elif listofWidgets[i][1] == 3:
                    for widget in child.findChildren(flrMenu):
                        if widget.pos().y() == listofWidgets[i][0]:
                            type = 'Flourescent Intensity'
                            expTime = widget.exposureTimeBox.value()
                            excitation = str(widget.excitationBox.currentText())
                            emission = widget.emissionBox.value()
                            self.dictOfProtocols[protocolNumber][i+1] = {
                                'Type': type,
                                'Exposure Time': expTime,
                                'Emission': emission,
                                'Excitation': excitation
                            }
                elif listofWidgets[i][1] == 4:
                    for widget in child.findChildren(flrSpecMenu):
                        if widget.pos().y() == listofWidgets[i][0]:
                            type = 'Flourescence Spectrum'
                            expTime = widget.exposureTimeBox.value()
                            excitation = str(widget.excitationBox.currentText())
                            start = widget.startWavelengthBox.value()
                            stop = widget.stopWavelengthBox.value()
                            self.dictOfProtocols[protocolNumber][i+1] = {
                                'Type': type,
                                'Exposure Time': expTime,
                                'Start Wavelength': start,
                                'Stop Wavelength': stop,
                                'Excitation': excitation
                            }
                elif listofWidgets[i][1] == 5:
                    for widget in child.findChildren(shakeMenu):
                        if widget.pos().y() == listofWidgets[i][0]:
                            type = 'Shaking'
                            durTime = widget.durationBox.value()
                            self.dictOfProtocols[protocolNumber][i+1] = {
                                'Type': type,
                                'Duration': durTime
                            }
            #print self.dictOfProtocols
        self.openExcelSheet()


    def openExcelSheet(self):
        xl = win32com.client.gencache.EnsureDispatch("Excel.Application")
        xl.Visible = True
        Workbook = xl.Workbooks.Add()
        Sheets = Workbook.Sheets
        self.liveExportData(Sheets)

    def liveExportData(self,Sheets):
        time.sleep(1)
        Sheets(1).Cells(1, 1).Value = 'Kam-Spec 2017'
        Sheets(1).Cells(2,1).Value = 'Date: ' + time.strftime('%x')
        Sheets(1).Cells(2,3).Value = 'Time: ' + time.strftime('%X')
        currentRow = 2
        plateKeys = self.dictOfProtocols.keys()
        sortedPlateKeys = np.sort(plateKeys)
        time.sleep(1)
        self.machine = MotorMove()
        self.camera = LineCamera()
        for plate in plateKeys:
            wellList = self.toReadDict[plate]
            rowList = []
            colList = []
            for elmnt in wellList:
                if elmnt[0] not in rowList:
                    rowList.append(elmnt[0])
                if elmnt[1] not in colList:
                    colList.append(elmnt[1])
            protocolKeys = self.dictOfProtocols[plate].keys()
            plateDict = self.dictOfProtocols[plate]
            for key in protocolKeys:
                type = plateDict[key]['Type']
                if type == 'Absorbance':
                    currentRow += 2
                    expTime = plateDict[key]['Exposure Time']
                    wavelength = plateDict[key]['Wavelength']
                    Sheets(1).Cells(currentRow,1).Value = 'Measurement: '
                    Sheets(1).Cells(currentRow, 3).Value = type
                    Sheets(1).Cells(currentRow+1, 2).Value = 'Wavelength: '
                    Sheets(1).Cells(currentRow + 1, 4).Value = str(wavelength)+' nm'
                    Sheets(1).Cells(currentRow+2, 2).Value = 'Exposure Time: '
                    Sheets(1).Cells(currentRow + 2, 4).Value = str(expTime)+' ms'
                    currentRow += 5

                    for i in range(0,len(rowList)):
                        if i == 0:
                            for j in range(0,len(colList)):
                                Sheets(1).Cells(currentRow + i-1, 2+j).Value = colList[j]
                                Sheets(1).Cells(currentRow + i-1, 2+j).Interior.ColorIndex = 15
                        Sheets(1).Cells(currentRow+i, 1).Value = rowList[i]
                        Sheets(1).Cells(currentRow + i, 1).Interior.ColorIndex = 15

                    self.absorbanceProtocol(wellList)
                    currentRow += len(rowList)
                elif type == 'Absorbance Spectrum':
                    currentRow += 2
                    expTime = plateDict[key]['Exposure Time']
                    start = plateDict[key]['Start Wavelength']
                    stop = plateDict[key]['Stop Wavelength']
                    wavelengthRange = range(start,stop+1)
                    Sheets(1).Cells(currentRow,1).Value = 'Measurement: '
                    Sheets(1).Cells(currentRow, 3).Value = type
                    Sheets(1).Cells(currentRow+1, 2).Value = 'Start: '
                    Sheets(1).Cells(currentRow + 1, 4).Value = str(start)+' nm'
                    Sheets(1).Cells(currentRow+2, 2).Value = 'Stop: '
                    Sheets(1).Cells(currentRow + 2, 4).Value = str(stop)+' nm'
                    Sheets(1).Cells(currentRow+3, 2).Value = 'Exposure Time: '
                    Sheets(1).Cells(currentRow + 3, 4).Value = str(expTime)+' ms'
                    currentRow += 5

                    for i in range(0,len(wellList)):
                        if i == 0:
                            for j in range(0,len(wavelengthRange)):
                                Sheets(1).Cells(currentRow + i-1, 2+j).Value = wavelengthRange[j]
                                Sheets(1).Cells(currentRow + i-1, 2+j).Interior.ColorIndex = 15
                        Sheets(1).Cells(currentRow+i, 1).Value = wellList[i]
                        Sheets(1).Cells(currentRow + i, 1).Interior.ColorIndex = 15
                    currentRow += len(wellList)

                elif type == 'Flourescent Intensity':
                    currentRow += 2
                    expTime = plateDict[key]['Exposure Time']
                    excitation = plateDict[key]['Excitation']
                    emission = plateDict[key]['Emission']
                    Sheets(1).Cells(currentRow,1).Value = 'Measurement: '
                    Sheets(1).Cells(currentRow, 3).Value = type
                    Sheets(1).Cells(currentRow+1, 2).Value = 'Excitation: '
                    Sheets(1).Cells(currentRow + 1, 4).Value = str(excitation)+' nm'
                    Sheets(1).Cells(currentRow+2, 2).Value = 'Emission: '
                    Sheets(1).Cells(currentRow + 2, 4).Value = str(emission)+' nm'
                    Sheets(1).Cells(currentRow+3, 2).Value = 'Exposure Time: '
                    Sheets(1).Cells(currentRow + 3, 4).Value = str(expTime)+' ms'
                    currentRow += 5

                    for i in range(0,len(rowList)):
                        if i == 0:
                            for j in range(0,len(colList)):
                                Sheets(1).Cells(currentRow + i-1, 2+j).Value = colList[j]
                                Sheets(1).Cells(currentRow + i-1, 2+j).Interior.ColorIndex = 15
                        Sheets(1).Cells(currentRow+i, 1).Value = rowList[i]
                        Sheets(1).Cells(currentRow + i, 1).Interior.ColorIndex = 15
                    currentRow += len(rowList)

                elif type == 'Flourescence Spectrum':
                    currentRow += 2
                    expTime = plateDict[key]['Exposure Time']
                    start = plateDict[key]['Start Wavelength']
                    stop = plateDict[key]['Stop Wavelength']
                    excitation = plateDict[key]['Excitation']
                    wavelengthRange = range(start,stop+1)
                    Sheets(1).Cells(currentRow,1).Value = 'Measurement: '
                    Sheets(1).Cells(currentRow, 3).Value = type
                    Sheets(1).Cells(currentRow+1, 2).Value = 'Excitation: '
                    Sheets(1).Cells(currentRow + 1, 4).Value = str(excitation)
                    Sheets(1).Cells(currentRow+2, 2).Value = 'Start: '
                    Sheets(1).Cells(currentRow + 2, 4).Value = str(start)+' nm'
                    Sheets(1).Cells(currentRow+3, 2).Value = 'Stop: '
                    Sheets(1).Cells(currentRow + 3, 4).Value = str(stop)+' nm'
                    Sheets(1).Cells(currentRow+4, 2).Value = 'Exposure Time: '
                    Sheets(1).Cells(currentRow + 4, 4).Value = str(expTime)+' ms'
                    currentRow += 8

                    for i in range(0,len(wellList)):
                        if i == 0:
                            for j in range(0,len(wavelengthRange)):
                                Sheets(1).Cells(currentRow + i-1, 2+j).Value = wavelengthRange[j]
                                Sheets(1).Cells(currentRow + i-1, 2+j).Interior.ColorIndex = 15
                        Sheets(1).Cells(currentRow+i, 1).Value = wellList[i]
                        Sheets(1).Cells(currentRow + i, 1).Interior.ColorIndex = 15
                    currentRow += len(wellList)
                time.sleep(1)
        self.machine.ser.close()

    def absorbanceProtocol(self, wellList):
        self.machine._set_initial_position()
        time.sleep(2)
        #self.machine._set_led_in_position('W')
        #time.sleep(2)
        self.toReadNum = self.machine._convert_labels_to_numericals(wellList)
        print self.toReadNum
        for i in range(0,len(self.toReadNum)):
            self.machine._move_to_new_position(self.toReadNum[i])
            self.machine._toggle_led('B')
            time.sleep(2)
            self.machine._toggle_led('B')
            time.sleep(2)


    def calibrate(self):
        self.calibrate_data = {}
        self.camera = LineCamera()
        self.machine = MotorMove()
        print('Firmware version', self.camera.get_firmware_ver())
        print('Device version', self.camera.get_device_info())
        self.camera.set_work_mode(WorkMode.NORMAL)
        time.sleep(1)
        for i in range(0,4):
            leds = ['B','G','Y','R']
            self.exposureTime = 100
            self.camera.set_exposure_time(self.exposureTime)
            time.sleep(1)
            # self.machine._set_led_in_position(letter)
            # time.sleep(2)
            self.machine._toggle_led(leds[i])
            time.sleep(2)

            counter = 0
            while counter == 0:
                data = self.read_frame()
                time.sleep(.5)
                max = np.max(data)
                print 'Max: ' + str(max)
                if max > 50000:
                    if self.exposureTime > 5:
                        self.exposureTime = self.exposureTime - 5
                    elif self.exposureTime <= 5 and self.exposureTime > 1:
                        self.exposureTime = self.exposureTime - 1
                    elif self.exposureTime == 1:
                        self.exposureTime = self.exposureTime - 1/float(10)
                    elif self.exposureTime == 1/float(10):
                        print 'Low Reached'
                    print 'New ET: ' + str(float(self.exposureTime))
                    self.camera.set_exposure_time(self.exposureTime)
                    time.sleep(.5)
                elif max < 5000:
                    print 'Too Low'
                else:
                    counter = 1
                    print 'Done'

            smooth_data = self.savitzky_golay(data, 51, 2)
            self.calibrate_data[leds[i]] = list(np.where(smooth_data == np.max(smooth_data)))[0][0]
            self.machine._toggle_led(leds[i])
            # time.sleep(1)
            # self.machine.ser.write('Z')
            time.sleep(2)

        self.led_wavelengths = {
        'B': [468], 'G': [565], 'Y': [585], 'R': [635]
        }
        self.regressionEquation = np.polyfit([self.calibrate_data['B'],self.calibrate_data['G'], self.calibrate_data['Y'], self.calibrate_data['R']],[self.led_wavelengths['B'], self.led_wavelengths['G'], self.led_wavelengths['Y'], self.led_wavelengths['R']],1)
        print self.regressionEquation

    def savitzky_golay(self, y, window_size, order, deriv=0, rate=1):
        r"""Smooth (and optionally differentiate) data with a Savitzky-Golay filter.
        The Savitzky-Golay filter removes high frequency noise from data.
        It has the advantage of preserving the original shape and
        features of the signal better than other types of filtering
        approaches, such as moving averages techniques.
        Parameters
        ----------
        y : array_like, shape (N,)
            the values of the time history of the signal.
        window_size : int
            the length of the window. Must be an odd integer number.
        order : int
            the order of the polynomial used in the filtering.
            Must be less then `window_size` - 1.
        deriv: int
            the order of the derivative to compute (default = 0 means only smoothing)
        Returns
        -------
        ys : ndarray, shape (N)
            the smoothed signal (or it's n-th derivative).
        Notes
        -----
        The Savitzky-Golay is a type of low-pass filter, particularly
        suited for smoothing noisy data. The main idea behind this
        approach is to make for each point a least-square fit with a
        polynomial of high order over a odd-sized window centered at
        the point.
        Examples
        --------
        t = np.linspace(-4, 4, 500)
        y = np.exp( -t**2 ) + np.random.normal(0, 0.05, t.shape)
        ysg = savitzky_golay(y, window_size=31, order=4)
        import matplotlib.pyplot as plt
        plt.plot(t, y, label='Noisy signal')
        plt.plot(t, np.exp(-t**2), 'k', lw=1.5, label='Original signal')
        plt.plot(t, ysg, 'r', label='Filtered signal')
        plt.legend()
        plt.show()
        References
        ----------
        .. [1] A. Savitzky, M. J. E. Golay, Smoothing and Differentiation of
           Data by Simplified Least Squares Procedures. Analytical
           Chemistry, 1964, 36 (8), pp 1627-1639.
        .. [2] Numerical Recipes 3rd Edition: The Art of Scientific Computing
           W.H. Press, S.A. Teukolsky, W.T. Vetterling, B.P. Flannery
           Cambridge University Press ISBN-13: 9780521880688
        """
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


    def read_frame(self):
        for i in range(0,4):
            frame = self.camera.get_frame()
        return frame.image

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = KAMSpec()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()