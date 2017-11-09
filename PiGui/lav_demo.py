#### The following demo code is used to demonstrate the device performing a LOV-DOMAIN spectra time dynamic expreiment.
## In the demo, LOV-DOMAIN is exposed to white light and exposure time is manually set until all values are below
## 60,000 pixel values. The spectral data of LOV-DOMAIN is then imaged for 2 minutes under white light. Following this,
## the white light is turned off, a blue light is turned on from the bottom (angle 36.23 deg) and the LOV is exposed
## to it for 30 seconds. After 30 seconds the blue led is turned off, the white led is turned on once again and spectral
## data is measured for 3 minutes with same exact exposure settings.

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot
import time
import numpy as np
from wellSelectScreen_v2 import *
from arudinoPi_demos import *
from mightex import *
import csv


wellPositions = [[[5.5, 47],[11.5,47],[18,47],[24.5,47],[31,47],[37.5,47],[44,47],[50.5,47],[57,47],[63.5,47],[70,47],[76.5,47]],
                 [[5.5,40],[11.5,40],[18,40],[24.5,40],[31,40],[37.5,40],[44,40],[50.5,40],[57,40],[63.5,40],[70,40],[76.5,40]],
                 [[5.5,34],[11.5,34],[18,34],[24.5,34],[31,34],[37.5,34],[44,34],[50.5,34],[57,34],[63.5,34],[70,34],[76.5,34]],
                 [[5.5,27],[11.5,27],[18,27],[24.5,27],[31,27],[37.5,27],[44,27],[50.5,27],[57,27],[63.5,27],[70,27],[76.5,27]],
                 [[5.5,21],[11.5,21],[18,21],[24.5,21],[31,21],[37.5,21],[44,21],[50.5,21],[57,21],[63.5,21],[70,21],[76.5,21]],
                 [[5.5,15],[11.5,15],[18,15],[24.5,15],[31,15],[37.5,15],[44,15],[50.5,15],[57,15],[63.5,15],[70,15],[76.5,15]],
                 [[5.5,9],[11.5,9],[18,9],[24.5,9],[31,9],[37.5,9],[44,9],[50.5,9],[57,9],[63.5,9],[70,9],[76.5,9]],
                 [[5.5,3],[11.5,3],[18,3],[24.5,3],[31,3],[37.5,3],[44,3],[50.5,3],[57,3],[63.5,3],[70,3],[76.5,3]]]

class LOV_Demo(QtGui.QWidget):
    def __init__(self):
        super(LOV_Demo, self).__init__()
        self.initUI()
        self.wellSelect.nextButton.clicked.connect(self.recognizeWellsSelected)

    def initUI(self):
        self.wellSelect = wellSelectScreen()
        self.wellSelect.show()
        self.camera = LineCamera()
        self.camera.set_work_mode(WorkMode.NORMAL)
        self.camera.set_exposure_time(10)
        self.machine = MotorMove()

    def recognizeWellsSelected(self):
        self.wellSelect.destroy()
        self.selectedWellsList = []
        for child in self.wellSelect.findChildren(QtGui.QLabel):
            if str(child.objectName()) in self.wellSelect.wellNames:
                name = str(child.objectName())
                row = name[0]
                column = int(name[1:len(name)])-1
                if self.wellSelect.selectionDict[row][column] == 'ON':
                    self.selectedWellsList.append(row+str(column+1))
        self.blankSelect()

    def blankSelect(self):
        self.wellSelect = wellSelectScreen()
        self.wellSelect.nextButton.clicked.connect(self.recognizeBlank)
        self.wellSelect.show()
        self.wellSelect.label_118.setText('Select')
        self.wellSelect.label_119.setText(' a Blank')

    def recognizeBlank(self):
        for child in self.wellSelect.findChildren(QtGui.QLabel):
            if str(child.objectName()) in self.wellSelect.wellNames:
                name = str(child.objectName())
                row = name[0]
                column = int(name[1:len(name)])-1
                if self.wellSelect.selectionDict[row][column] == 'ON':
                    self.blankWell = row+str(column+1)
        self.moveToBlankWell()

    def moveToBlankWell(self):
        rowString = "ABCDEFGH"
        for l in range(0,len(rowString)):
            if self.blankWell[0] == rowString[l]:
                yindex = l
            else:
                continue
        for n in range(0,12):
            if int(self.blankWell[1:len(self.blankWell)])-1 == n:
                xindex = n
        self.blankPositionX= wellPositions[yindex][xindex][0]
        self.blankPositionY = wellPositions[yindex][xindex][1]
        self.blankPosition = 'M'+str(self.blankPositionX)+','+str(self.blankPositionY)
        self.machine._set_blank_position(self.blankWell,self.blankPosition)
        while self.machine.motorStatus == 0:
            print "Moving"
        time.sleep(1)
        self.maximizeBlankExposure()

    def maximizeBlankExposure(self):
        self.rowList = []
        self.machine._toggle_led('W')
        time.sleep(3)
        counter = 0
        self.exposureTime = 20500  # 2050us
        while counter == 0 :
            data = []
            data = self.read_frame()
        #     max = np.max(data[1])
        #     print 'Max: ' + str(max)
        #     if max > 55000:
        #         exposureTime = self.exposureTime - 100
        #         self.camera.set_exposure_time(exposureTime)
        #         time.sleep(.5)
        #     elif max < 5000:
        #         exposureTime = self.exposureTime + 5000
        #         self.camera.set_exposure_time(self.exposureTime)
        #         time.sleep(.5)
        #     else:
        #         self.blankData = data[1]
        #         counter = 1
        #         print 'Done'
        # self.absorbanceExpTime = self.exposureTime
        # self.camera.set_exposure_time(self.absorbanceExpTime)
        # self.machine._toggle_led('W')
        # time.sleep(1)
        # self.absorbanceMeasurement()

    def absorbanceMeasurement(self):
        with open('testCSV', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['KAM-Spec 2017'])
            spamwriter.writerow(['Date:', time.strftime('%m/%d/%Y')])
            spamwriter.writerow(['Time:', time.strftime('%H:%M:%S')])
            spamwriter.writerow([' '])
            spamwriter.writerow([' '])
            spamwriter.writerow([' '])
            spamwriter.writerow([' '])
            spamwriter.writerow(['ABSORBANCE'])
        csvfile.close()

        self.camera.set_exposure_time(self.absorbanceExpTime)
        rowList = [["A Blank"]]
        for i in self.blankData:
            rowList[0].append(i)
        for well in self.selectedWellsList:
            rowString = "ABCDEFGH"
            for l in range(0, len(rowString)):
                if well[0] == rowString[l]:
                    yindex = l
                else:
                    continue
            for n in range(0, 12):
                if int(well[1:len(well)]) - 1 == n:
                    xindex = n
            self.wellX = wellPositions[yindex][xindex][0]
            self.wellY = wellPositions[yindex][xindex][1]
            self.wellPosition = 'M' + str(self.wellX) + ',' + str(self.wellY)

            self.machine._set_new_position(well, self.wellPosition)
            while self.machine.motorStatus == 0:
                print "Moving"
            self.machine._toggle_led('W')
            time.sleep(1)
            data = self.camera.get_frame()
            while data == []:
                print "Waiting"

            row = [well]
            for i in data[1]:
                row.append(i)
            rowList.append(row)
            self.machine._toggle_led('W')
            time.sleep(1)
        rowList = sorted(rowList)
        with open('testCSV', 'ab') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerows(zip(*rowList))
        csvfile.close()
        print "Finished Data Export"

    def read_frame(self):
        for i in range(0,30):
            frame = self.camera.get_frame()
        if frame is not None:
            return frame.image
        else:
            self.lowerExposureTime()

    def lowerExposureTime(self):
        self.exposureTime = self.exposureTime - 1000

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = LOV_Demo()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()