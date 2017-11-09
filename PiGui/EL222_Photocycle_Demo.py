from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot
import time
from datetime import datetime, timedelta
import numpy as np
from wellSelectScreen_v2 import *
from arudinoPi_demos import *
from mightex import *
import csv
from threading import Timer,Thread,Event

wellPositions = [[[5.5, 47],[11.5,47],[18,47],[24.5,47],[31,47],[37.5,47],[44,47],[50.5,47],[57,47],[63.5,47],[70,47],[76.5,47]],
                 [[5.5,40],[11.5,40],[18,40],[24.5,40],[31,40],[37.5,40],[44,40],[50.5,40],[57,40],[63.5,40],[70,40],[76.5,40]],
                 [[5.5,34],[11.5,34],[18,34],[24.5,34],[31,34],[37.5,34],[44,34],[50.5,34],[57,34],[63.5,34],[70,34],[76.5,34]],
                 [[5.5,27],[11.5,27],[18,27],[24.5,27],[31,27],[37.5,27],[44,27],[50.5,27],[57,27],[63.5,27],[70,27],[76.5,27]],
                 [[5.5,21],[11.5,21],[18,21],[24.5,21],[31,21],[37.5,21],[44,21],[50.5,21],[57,21],[63.5,21],[70,21],[76.5,21]],
                 [[5.5,15],[11.5,15],[18,15],[24.5,15],[31,15],[37.5,15],[44,15],[50.5,15],[57,15],[63.5,15],[70,15],[76.5,15]],
                 [[5.5,9],[11.5,9],[18,9],[24.5,9],[31,9],[37.5,9],[44,9],[50.5,9],[57,9],[63.5,9],[70,9],[76.5,9]],
                 [[5.5,3],[11.5,3],[18,3],[24.5,3],[31,3],[37.5,3],[44,3],[50.5,3],[57,3],[63.5,3],[70,3],[76.5,3]]]
class QSDemo(QtGui.QWidget):
    def __init__(self):
        super(QSDemo, self).__init__()
        self.initUI()
        self.wellSelect.nextButton.clicked.connect(self.recognizeWellsSelected)

    def initUI(self):
        self.wellSelect = wellSelectScreen()
        self.wellSelect.show()
        self.camera = LineCamera()
        self.camera.set_work_mode(WorkMode.NORMAL)
        self.exposureTime = 20150
        self.camera.set_exposure_time(self.exposureTime)
        self.machine = MotorMove()
        self.count = 0

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
        self.absorbanceMeasurement()

    def absorbanceMeasurement(self):
        with open('testCSV.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['KAM-Spec 2017'])
            spamwriter.writerow(['Date:', time.strftime('%m/%d/%Y')])
            spamwriter.writerow(['Time:', time.strftime('%H:%M:%S')])
            spamwriter.writerow([' '])
            spamwriter.writerow([' '])
            spamwriter.writerow([' '])
            spamwriter.writerow([' '])
            spamwriter.writerow(['EL222'])
        csvfile.close()
        time.sleep(1)
        self.machine._set_initial_position()
        while self.machine.motorStatus == 0:
            print "Moving"
        print 'Reached Initial Position'
        self.rowList = []
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
            print 'Measuring'
            time.sleep(1+self.exposureTime*.1/1000)
            row = [well]
            data = []
            data = self.read_frame()
            while data == []:
                print "Waiting"
            for i in data:
                row.append(i)
            self.rowList.append(row)
            self.machine._toggle_led('W')
            time.sleep(1)
        self.stopwatch(5)
        self.perturbSample()

    def perturbSample(self):
        self.machine._toggle_led('b')
        time.sleep(1)
        self.stopwatch(5)
        self.machine._toggle_led('b')
        time.sleep(1)
        self.measureLight()

    def stopwatch(self, seconds):
        start = time.time()
        time.clock()
        elapsed = 0
        while elapsed < seconds:
            elapsed = time.time() - start
            print elapsed

    def read_frame(self):
        try:
            frame = self.camera.get_frame()
        except:
            return None
        if frame is not None:
            return frame.image  # - np.mean(frame.dark)
        else:
            return None

    def measureLight(self):
        self.count += 1
        self.machine._toggle_led('Y')
        self.stopwatch(1+self.exposureTime*.1/1000)
        data = self.read_frame()
        row = []
        if data is None:
            return True
        else:
            for i in data:
                row.append(i)
        with open('EL222_test_functionality.csv', 'ab') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(row)
            print 'Added'
        csvfile.close()
        self.machine._toggle_led('Y')
        time.sleep(1)
        if self.count < 5:
            self.measureLight()

# def photoCycleMeasure():
#     t = Timer(.1, measureLight)
#     t.start()
    # for m in range(0,5):
    #     self.machine._toggle_led('W')
    #     time.sleep(1)
    #     t = perpetualTimer(.1, self.update2)
    #     t.start()
    #     time.sleep(.1)
    #     t.cancel()
    #     self.machine._toggle_led('W')

    #     time.sleep(1+self.exposureTime*.1/1000)
    #     row = [m]
    #     data = self.read_frame()
    #     while data == []:
    #         print "Waiting"
    #     for i in data:
    #         row.append(i)
    #     self.rowList.append(row)
    #     self.machine._toggle_led('W')
    #     time.sleep(1)
    #     self.stopwatch(5)
    # self.rowList = sorted(self.rowList)
    # with open('EL222_test_functionality.csv', 'ab') as csvfile:
    #     spamwriter = csv.writer(csvfile, delimiter=',',
    #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     spamwriter.writerows(zip(*self.rowList))
    # csvfile.close()


class perpetualTimer():
   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
       self.handle_function()

   def cancel(self):
      self.thread.cancel()

# def measureLight():
    # if self.count == .1:
    #     print 'ON'
    #     print 'IMAGE'
    #     print 'OFF'
        # self.machine._toggle_led('W')
        # data = self.read_frame()
        # self.machine._toggle_led('W')
        # row = []
        # if data is None:
        #     return True
        # else:
        #     for i in data:
        #         row.append(i)
        # with open('EL222_test_functionality.csv', 'ab') as csvfile:
        #     spamwriter = csv.writer(csvfile, delimiter=',',
        #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #     spamwriter.writerow(row)
        #     print 'Added'
        # csvfile.close()
    # elif self.count % 5 == 0:
    #     print 'ON'
    #     print 'IMAGE'
    #     print 'OFF'
        # self.machine._toggle_led('W')
        # time.sleep(.5)
        # data = self.read_frame()
        # self.machine._toggle_led('W')
        # time.sleep(.5)
        # row = []
        # if data is None:
        #     return True
        # else:
        #     for i in data:
        #         row.append(i)
        # with open('EL222_test_functionality.csv', 'ab') as csvfile:
        #     spamwriter = csv.writer(csvfile, delimiter=',',
        #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #     spamwriter.writerow(row)
        #     print 'Added'
        # csvfile.close()
    # if self.count == 5:
    #     print 'DONE'
    #     self.t.cancel()

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    ex = QSDemo()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()