from PyQt4 import QtGui
from PyQt4 import QtCore
import time
from introScreen import *
from wellSelectScreen_v2 import *
from selectProtocolScreen import *
from absMenu import *
from absSpecMenu import *
from flrMenu import *
from flrSpecMenu import *
from inputEmail import *
from arudino import *
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
        #self.absMenu.finishButton.click.connect(self.finishProtocolSelection)

        self.protocolDict = {}
        self.selectedWellsDict = {}
        self.protocolCount = 0

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
        self.protocolCount += 1
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
        self.protocolDict[self.plateCount] = []
        self.protocolSelect.hide()
        self.wellSelect.clearWells()
        self.wellSelect.show()

    def absorbanceProtocol(self, wellList, exposureTime, wavelength):
        self.camera.set_exposure_time(exposureTime)
        time.sleep(1)
        self.machine._set_initial_position()
        time.sleep(2)
        self.toReadNum = self.machine._convert_labels_to_numericals(wellList)
        print self.toReadNum
        for i in range(0,len(self.toReadNum)):
            self.machine._move_to_new_position(self.toReadNum[i])
            self.machine._toggle_led('W')
            absData = self.camera.get_frame()
            print absData[wavelength]
            self.machine._toggle_led('W')
            time.sleep(2)



    def sendDataEmail(self):
        inputter = InputEmail()
        inputter.exec_()
        emailfrom = "kamspec2017l@gmail.com"
        emailto = str(inputter.text.text())
        fileToSend = "hi.csv"
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