from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot
import time
import csv
from introScreen import *
from wellSelectScreen_v2 import *
from selectProtocolScreen import *
from absMenu import *
from absSpecMenu import *
from flrMenu import *
from flrSpecMenu import *
from measurementScreen import *
from inputEmail import *
from arudinoPi import *
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
        #self.intro.startButton.clicked.connect(self.sendDataEmail)
        self.intro.startButton.clicked.connect(self.startWellSelect)
        self.wellSelect.nextButton.clicked.connect(self.protocolSelectScreen)

        ### Connection Protocol Selection menu buttons to functions
        self.protocolSelect.absButton.clicked.connect(self.absSettings)
        self.protocolSelect.absSpecButton.clicked.connect(self.absSpecSettings)
        self.protocolSelect.flrButton.clicked.connect(self.flrSettings)
        self.protocolSelect.flrSpecButton.clicked.connect(self.flrSpecSettings)
        # self.protocolSelect.shakingButton.clicked.connect(self.shakeMenu)
        self.protocolSelect.addPlateButton.clicked.connect(self.addPlate)

        ### Connecting Absorbance Menu Settings buttons to functions
        self.absMenu.addProtocolButton.clicked.connect(lambda: self.addProtocol(1))
        self.absSpecMenu.addProtocolButton.clicked.connect(lambda: self.addProtocol(2))
        self.flrMenu.addProtocolButton.clicked.connect(lambda: self.addProtocol(3))
        self.flrSpecMenu.addProtocolButton.clicked.connect(lambda: self.addProtocol(4))
        self.absMenu.finishButton.clicked.connect(lambda: self.finishProtocolSelection(1))
        self.absSpecMenu.finishButton.clicked.connect(lambda: self.finishProtocolSelection((2)))
        self.flrMenu.finishButton.clicked.connect(lambda: self.finishProtocolSelection(3))
        self.flrSpecMenu.finishButton.clicked.connect(lambda:self.finishProtocolSelection(4))

        self.protocolDict = {}
        self.selectedWellsDict = {}
        self.protocolCount = [0]

    def initUI(self):
        self.intro = introScreen()
        self.wellSelect = wellSelectScreen()
        self.protocolSelect = protocolSelectScreen()
        self.absMenu = absMenu()
        self.absSpecMenu = absSpecMenu()
        self.flrMenu = flrMenu()
        self.flrSpecMenu = flrSpecMenu()
        self.machine = MotorMove()
        self.camera = LineCamera()
        self.measurementMenu = measurementScreen()


    def startWellSelect(self):
        self.intro.deleteLater()
        self.plateCount = 1
        self.protocolDict[self.plateCount] = []
        self.wellSelect.show()

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
            self.absSpecMenu.hide()
            self.protocolDict[self.plateCount].append({type: {'Exposure Time': int(self.absSpecMenu.exposureTimeSpinBox.value()), 'Start Wavelength': int(self.absSpecMenu.startWavelengthSpinBox.value()), 'Stop Wavelength': int(self.absSpecMenu.stopWavelengthSpinBox.value()) }})
            self.protocolSelect.show()
        elif type == 3:
            self.flrMenu.hide()
            self.protocolDict[self.plateCount].append({type: {'Exposure Time': int(self.flrMenu.exposureTimeSpinBox.value()), 'Excitation': str(self.flrMenu.excitationWavelengthComboBox.currentText()), 'Emission': int(self.flrMenu.emissionWavelengthSpinBox.value())}})
            self.protocolSelect.show()
        elif type == 4:
            self.flrSpecMenu.hide()
            self.protocolDict[self.plateCount].append({type: {'Exposure Time': int(self.flrSpecMenu.exposureTimeSpinBox.value()), 'Excitation': str(self.flrSpecMenu.excitationWavelengthComboBox.currentText()), 'Start Wavelength': int(self.flrSpecMenu.startWavelengthSpinBox.value()), 'Stop Wavelength': int(self.flrSpecMenu.stopWavelengthSpinBox.value())}})
            self.protocolSelect.show()
        elif type == 5:
            self.flrSpecMenu.hide()
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
        elif type == 2:
            self.absSpecMenu.hide()
            self.protocolDict[self.plateCount].append({type: {'Exposure Time': int(self.absSpecMenu.exposureTimeSpinBox.value()), 'Start Wavelength': int(self.absSpecMenu.startWavelengthSpinBox.value()), 'Stop Wavelength': int(self.absSpecMenu.stopWavelengthSpinBox.value()) }})
            self.measurementMenu.show()

        elif type == 3:
            self.flrMenu.hide()
            self.protocolDict[self.plateCount].append({type: {'Exposure Time': int(self.flrMenu.exposureTimeSpinBox.value()), 'Excitation': str(self.flrMenu.excitationWavelengthComboBox.currentText()), 'Emission': int(self.flrMenu.emissionWavelengthSpinBox.value())}})
            self.measurementMenu.show()

        elif type == 4:
            self.flrSpecMenu.hide()
            self.protocolDict[self.plateCount].append({type: {'Exposure Time': int(self.flrSpecMenu.exposureTimeSpinBox.value()), 'Excitation': str(self.flrSpecMenu.excitationWavelengthComboBox.currentText()), 'Start Wavelength': int(self.flrSpecMenu.startWavelengthSpinBox.value()), 'Stop Wavelength': int(self.flrSpecMenu.stopWavelengthSpinBox.value())}})
            self.measurementMenu.show()

        elif type == 5:
            self.flrSpecMenu.hide()
            self.measurementMenu.show()

        self.plate = 1
        self.ypos = 0
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
                self.measurementMenu.gridLayout.addWidget(self.protocolCheckBox,self.ypos,2, 1, 4)



        self.individualPlateRun(self.plate)

    def individualPlateRun(self, plate):
        self.csvFileName = 'Plate_'+str(self.plate)+'_'+time.strftime('%d%m%Y')+'.csv'
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
            # for protocol in range(0, len(self.protocolDict[plate])):
            #     if self.protocolDict[plate][protocol].keys()[0] == 1:
            #         self.lengthMeasurements = len(self.selectedWellsDict[plate])
            #         exposureTime = int(self.protocolDict[plate][protocol][1]['Exposure Time'])
            #         wavelength = int(self.protocolDict[plate][protocol][1]['Wavelength'])
            #         self.abs_protocol = executeProtocol(1,self.selectedWellsDict, self.protocolDict, plate, protocol,csvFileName, self.camera, self.machine, self.measurementMenu, self.lengthMeasurements)
            #         self.connect(self.abs_protocol, QtCore.SIGNAL("updateCurrentProtocol(QString)"), self.updateCurrentProtocol)
            #         self.connect(self.abs_protocol, QtCore.SIGNAL("addCurve(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"), self.addCurve)
            #         self.connect(self.abs_protocol, QtCore.SIGNAL("finished()"), self.statusPrint)
            #         self.abs_protocol.start()

                        #self.absProtocol(wellList, exposureTime, wavelength,csvFileName)
        #     #self.sendDataEmail(csvFileName)

    def individualProtocolRun(self, plate, protocol, csvFileName):
        if self.protocolDict[plate][protocol].keys()[0] == 1:
            self.lengthMeasurements = len(self.selectedWellsDict[plate])
            exposureTime = int(self.protocolDict[plate][protocol][1]['Exposure Time'])
            print exposureTime
            wavelength = int(self.protocolDict[plate][protocol][1]['Wavelength'])
            self.abs_protocol = executeProtocol(1, self.selectedWellsDict, self.protocolDict, plate, protocol,
                                                csvFileName, self.camera, self.machine, self.measurementMenu,
                                                self.lengthMeasurements)
            self.connect(self.abs_protocol, QtCore.SIGNAL("updateCurrentProtocol(QString)"), self.updateCurrentProtocol)
            self.connect(self.abs_protocol, QtCore.SIGNAL("addCurve(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"),
                         self.addCurve)
            self.connect(self.abs_protocol, QtCore.SIGNAL("statusPrint(QString)"), self.statusPrint)
            self.connect(self.abs_protocol, QtCore.SIGNAL("checkBox(QString)"), self.checkBox)
            self.abs_protocol.start()

    def checkBox(self, string):
        print 'Checked'
        for child in self.measurementMenu.findChildren(QtGui.QCheckBox):
            objName = str(child.objectName())
            splitName = objName.split('_')
            if len(splitName) > 2:
                print splitName
                plateNumb = int(splitName[1])
                protocolNumb = int(splitName[3])
                if plateNumb == self.plate:
                    if protocolNumb == self.protocol+1:
                        child.toggle()

    def statusPrint(self, string):
        print string
        self.protocol += 1
        if self.protocol <= self.protocolCount[self.plate-1]-1:
            self.individualProtocolRun(self.plate, self.protocol, self.csvFileName)
        else:
            'Done All Protocols for Plate #'+str(self.plate)
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
                print 'Done All Plates'

    def updateCurrentProtocol(self, protocolString):
        self.measurementMenu.measurementLabel.setText(protocolString)

    def addCurve(self, x, y, i, protocol):
        print x
        print y
        well = i+1
        if i == 0:
            plt.cla()
            self.ax = self.measurementMenu.figure.add_subplot(111)
            self.ax.plot(x, y, label = str(self.selectedWellsDict[self.plate][i]))
        else:
            self.ax.plot(x, y, label = str(self.selectedWellsDict[self.plate][i]))
        self.ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=5, mode="expand", borderaxespad=0.)
        self.measurementMenu.canvas.draw()
        if well == self.lengthMeasurements:
            self.measurementMenu.figure.savefig('C:\Users\LokoKoko\MAK-2017\PiGui\Plate'+str(self.plate)+'Protocol'+str(protocol)+'.png')



class cameraInitialization(QtCore.QThread):
    def __init__(self,camera, exposureTime):
        QtCore.QThread.__init__(self)
        self.camera = camera
        self.exposureTime = exposureTime


    def __del__(self):
        self.wait()

    def run(self):
        print 'Initializing Camera'
        self.camera.set_exposure_time(self.exposureTime)
        # self.emit(QtCore.SIGNAL("finished()"), self.cameraReady)
        self.sleep(2)

class machineInitialization(QtCore.QThread):
    signalList = QtCore.pyqtSignal(object, list, dict, str,  object, QtGui.QWidget)
    def __init__(self, machine, wellList, csvFileName, camera, graph):
        QtCore.QThread.__init__(self)
        self.machine = machine
        self.wellList = wellList
        self.csvFileName = csvFileName
        self.camera = camera
        self.measurementScreen = graph
        print 'Initializing Machine'

    def __del__(self):
        self.wait()

    def run(self):
        self.machine._set_initial_position()
        time.sleep(2)
        self.toReadNum = self.machine._convert_labels_to_numericals(self.wellList)
        print self.toReadNum
        self.dataDict = {}
        for i in range(0, len(self.toReadNum)):
             self.dataDict[int(self.toReadNum[i][0])] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.emit(QtCore.SIGNAL('runProtocol(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)'), self.machine, self.toReadNum, self.dataDict, self.csvFileName, self.camera, self.measurementScreen)
       #self.signalList.emit(self.machine, self.toReadNum, self.dataDict, self.csvFileName, self.camera, self.measurementScreen)
        self.sleep(2)
class measureProtocol(QtCore.QThread):
    plotSignal = QtCore.pyqtSignal(list,np.ndarray,int, object)

    def __init__(self, machine, toRead, dictionary, csvFileName, camera, graph):
        QtCore.QThread.__init__(self)
        self.machine = machine
        self.toReadNum = toRead
        self.dataDict = dictionary
        self.csvFileName = csvFileName
        self.camera = camera
        self.measurementScreen = graph

    def __del__(self):
        self.wait()

    def run(self):
        for i in range(0,len(self.toReadNum)):
            self.machine._move_to_new_position(self.toReadNum[i])
            self.machine._toggle_led('W')
            time.sleep(2)
            absData = self.camera.get_frame()
            x = range(1,len(absData[1])+1)
            y = absData[1]
            self.emit(QtCore.SIGNAL("addPlot(PyQt_PyObject,PyQt_PyObject, PyQt_PyObject)"), x, y, i)
            self.dataDict[int(self.toReadNum[i][0])][int(self.toReadNum[i][2:len(self.toReadNum[i])+1])] = absData[1][1]
            self.machine._toggle_led('W')
            time.sleep(2)

            self.columnList = []
            for key in sorted(self.dataDict.keys()):
                for column in range(0,len(self.dataDict[key])):
                    if self.dataDict[key][column] != 0:
                        if column not in self.columnList:
                            self.columnList.append(column)
            sortedColumnList = sorted(self.columnList)
            csvColumnList = [' '] + sortedColumnList
        with open(self.csvFileName, 'ab') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(csvColumnList)
            for key in sorted(self.dataDict.keys()):
                row = []
                letters = ['A','B','C','D','E','F','G','H']

                for column in sortedColumnList:
                    if self.dataDict[key][column] != 0:
                        row.append(self.dataDict[key][column])
                    else:
                        row.append(' ')
                row = [letters[key-1]] + row
                spamwriter.writerow(row)
            spamwriter.writerow(' ')
            spamwriter.writerow(' ')
            csvfile.close()
        self.sleep(2)



class executeProtocol(QtCore.QThread):
    def __init__(self, type, selectedWellsDict, protocolDict, plateNumb, protocolNumb, csvFileName, camera, machine, graph, length):
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

    def __del__(self):
        self.wait()

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

        self.cameraStart = cameraInitialization(self.camera, exposureTime)
        self.connect(self.cameraStart, QtCore.SIGNAL("finished()"), self.cameraReady)
        self.cameraStart.start()
        # self.sleep(2)
        # self.camera.set_exposure_time(exposureTime)
        # time.sleep(1)
        # self.machine._set_initial_position()
        # time.sleep(2)
        # self.toReadNum = self.machine._convert_labels_to_numericals(wellList)
        # print self.toReadNum
        # self.dataDict = {}
        # for i in range(0, len(self.toReadNum)):
        #     self.dataDict[int(self.toReadNum[i][0])] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # print self.dataDict
    def cameraReady(self):
        self.emit(QtCore.SIGNAL("updateCurrentProtocol(QString)"), 'Plate '+ str(self.plate)+'- Absorbance...')
        self.protocolStart = machineInitialization(self.machine,self.wellList, self.csvFileName, self.camera, self.measurementScreen)
        self.connect(self.protocolStart, QtCore.SIGNAL("runProtocol(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"), self.runProtocol)
        self.protocolStart.start()
        print 'Camera Ready'

    def runProtocol(self, machine, toRead, dictionary, filename, camera, graph):
        print 'runProtocol'
        self.wellsToRead = toRead
        self.measureThread = measureProtocol(machine, toRead, dictionary, filename, camera, graph)
        self.connect(self.measureThread, QtCore.SIGNAL("addPlot(PyQt_PyObject,PyQt_PyObject, PyQt_PyObject)"), self.addPlot)
        self.measureThread.start()

    def addPlot(self, x,y,i):
        print 'addPlot'
        self.emit(QtCore.SIGNAL("addCurve(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)"),x,y,i, self.protocol)
        if i == self.lengthMeasurements-1:
            self.emit(QtCore.SIGNAL("checkBox(QString)"), "Check")
            self.emit(QtCore.SIGNAL("statusPrint(QString)"), "Done Protocol")


    # @pyqtSlot(dict)
    # def runProtocol(self, machine, toRead, dictionary, filename, camera, graph):
    #     measureThread = measureProtocol(machine, toRead, dictionary, filename, camera, graph)
    #     measureThread.plotSignal.connect(self.addPlot)
    #     measureThread.start()




    # for i in range(0,len(self.toReadNum)):
    #     self.machine._move_to_new_position(self.toReadNum[i])
    #     self.machine._toggle_led('W')
    #     time.sleep(2)
    #     absData = self.camera.get_frame()
    #     self.dataDict[int(self.toReadNum[i][0])][int(self.toReadNum[i][2:len(self.toReadNum[i])+1])] = absData[1][1]
    #     self.machine._toggle_led('W')
    #     time.sleep(2)
    #
    #     self.columnList = []
    #     for key in sorted(self.dataDict.keys()):
    #         for column in range(0,len(self.dataDict[key])):
    #             if self.dataDict[key][column] != 0:
    #                 if column not in self.columnList:
    #                     self.columnList.append(column)
    #     sortedColumnList = sorted(self.columnList)
    #     csvColumnList = [' '] + sortedColumnList
    # with open(csvFileName, 'ab') as csvfile:
    #     spamwriter = csv.writer(csvfile, delimiter=',',
    #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     spamwriter.writerow(csvColumnList)
    #     for key in sorted(self.dataDict.keys()):
    #         row = []
    #         letters = ['A','B','C','D','E','F','G','H']
    #
    #         for column in sortedColumnList:
    #             if self.dataDict[key][column] != 0:
    #                 row.append(self.dataDict[key][column])
    #             else:
    #                 row.append(' ')
    #         row = [letters[key-1]] + row
    #         spamwriter.writerow(row)
    #     spamwriter.writerow(' ')
    #     spamwriter.writerow(' ')
    #     csvfile.close()

    def sendDataEmail(self,filename):
        inputter = InputEmail()
        inputter.exec_()
        emailfrom = "kamspec2017l@gmail.com"
        emailto = str(inputter.text.text())
        fileToSend = filename
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