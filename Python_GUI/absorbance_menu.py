from PyQt4 import QtGui, QtCore
import numpy as np

#Started 8.21.17
#Author: Karol Szymula
#Purpose: iGEM2017 Penn Team
#Description:
#       Widget for the menu GUI. Contains all settings for a regular absorbance measurement at specific wavelength.
#       Wavelength of measurement is input by user. Exposure time is also capable of being selected by user.

class AbsorbanceMenu(QtGui.QWidget):
    def __init__(self):
        super(AbsorbanceMenu, self).__init__()
        self.initUI()

    def initUI(self):
        # Sets horizantel layout for the absorbance setting menu
        self.setGeometry(350, 350, 500,100 ) #Sets six of widget (X placement, Y placement, Width, Height)

        self.mainBox = QtGui.QVBoxLayout()
        self.setLayout(self.mainBox)

        #### Title Box ####
        self.titleBox = QtGui.QGridLayout()
        self.boxTitle = QtGui.QLabel('Absorbance')
        self.boxTitle.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.titleBox.addWidget(QHLine(), 0, 0, 1, 5)
        self.titleBox.addWidget(self.boxTitle,0, 5, 1, 1)
        self.titleBox.addWidget(QHLine(),0, 6, 1, 59)
        self.titleBox.addWidget(QVLine(),0,1,25,1)
        self.titleBox.addWidget(QVLine(), 0, 63, 25, 1)
        self.titleBox.addWidget(QHLine(), 23, 0, 1,65)
        #####################

        #### Wavelength Setting Box #####
        self.wavelengthSettingBox = QtGui.QGridLayout()
        self.boxTitle = QtGui.QLabel('Wavelength')
        self.boxTitle.setStyleSheet("font-size: 12px; font-weight: 100; font-style: italic")
        self.wavelengthSettingBox.addWidget(QHLine(), 0, 0, 1, 1)
        self.wavelengthSettingBox.addWidget(self.boxTitle, 0, 1, 1, 1)
        self.wavelengthSettingBox.addWidget(QHLine(), 0, 2, 1, 18)
        #####################

        #### Reading Setting Box ####
        self.readingSettingBox = QtGui.QVBoxLayout()
        #####################






        self.mainBox.addLayout(self.titleBox)
        self.titleBox.addLayout(self.wavelengthSettingBox,1,2,20,20)
        #self.mainBox.addLayout(self.readingSettingBox)

        self.setWindowTitle('MAK-Spec 2017')
        self.show()
class QHLine(QtGui.QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QtGui.QFrame.HLine)
        self.setFrameShadow(QtGui.QFrame.Sunken)


class QVLine(QtGui.QFrame):
    def __init__(self):
        super(QVLine, self).__init__()
        self.setFrameShape(QtGui.QFrame.VLine)
        self.setFrameShadow(QtGui.QFrame.Sunken)

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Cleanlooks")
    ex = AbsorbanceMenu()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
