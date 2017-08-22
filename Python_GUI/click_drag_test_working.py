from PyQt4 import QtGui, QtCore
import numpy as np

class WellPlate(QtGui.QWidget):
    def __init__(self):
        super(WellPlate, self).__init__()
        self.initUI()

    def initUI(self):

        self.grid = QtGui.QGridLayout()
        self.setLayout(self.grid)
        letters = ['','A','B','C','D','E','F','G','H']
        numbers = ['','1','2','3','4','5','6','7','8','9','10','11','12']
        positions = [(i,j) for i in range(9) for j in range(13)]

        for position in positions:
            if position[0] == 0:
                if position[1] == 0:
                   label = QtGui.QLabel('')
                   self.grid.addWidget(label, *position)
                else:
                   label = QtGui.QLabel(str(position[1]))
                   label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
                   self.grid.addWidget(label, *position)
            elif position[1] == 0:
               if position[0] == 0:
                   label = QtGui.QLabel('')
                   self.grid.addWidget(label, *position)
               else:
                   label = QtGui.QLabel(letters[position[0]])
                   self.grid.addWidget(label, *position)
            else:
                button = QtGui.QRadioButton('')
                button.setObjectName(letters[position[0]]+numbers[position[1]])
                self.grid.addWidget(button, *position)
                button.setAutoExclusive(False)
                
        self.rubberband = QtGui.QRubberBand(
            QtGui.QRubberBand.Rectangle, self)

        self.setMouseTracking(True)


        self.hbox_measurementType = QtGui.QHBoxLayout()
        self.hbox_measurementType.addWidget(QtGui.QCheckBox('Absorbance'))
        self.hbox_measurementType.addWidget(QtGui.QCheckBox('Fluorescence'))
        
    def mousePressEvent(self, event):
        self.origin = event.pos()
        self.rubberband.setGeometry(
            QtCore.QRect(self.origin, QtCore.QSize()))
        self.rubberband.show()
        QtGui.QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        if self.rubberband.isVisible():
            self.rubberband.setGeometry(
                QtCore.QRect(self.origin, event.pos()).normalized())
        QtGui.QWidget.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        if self.rubberband.isVisible():
            self.rubberband.hide()
            selected = []
            rect = self.rubberband.geometry()
            for child in self.findChildren(QtGui.QRadioButton):
                if rect.intersects(child.geometry()):
                    child.toggle()

        QtGui.QWidget.mouseReleaseEvent(self, event)

class MeasurementSettings(QtGui.QWidget):
    def __init__(self):
        super(MeasurementSettings, self).__init__()
        self.initUI()

    def initUI(self):
        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)
        self.measurementType = QtGui.QHBoxLayout()
        self.absCheck = QtGui.QCheckBox('Absorbance')
        self.flrCheck = QtGui.QCheckBox('Fluorescence')
        self.measurementType.addWidget(self.absCheck)

        self.measurementType.addWidget(self.flrCheck)
        self.vbox.addLayout(self.measurementType)
        self.hbox_1 = QtGui.QHBoxLayout()

        self.vbox.addLayout(self.hbox_1)
        
        self.vbox_1_1 = QtGui.QVBoxLayout()
        
        self.vbox_1_2 = QtGui.QVBoxLayout()
        self.vbox_1_3 = QtGui.QVBoxLayout()
        self.hbox_1.addLayout(self.vbox_1_1)
        self.hbox_1.addLayout(self.vbox_1_3)
        self.hbox_1.addLayout(self.vbox_1_2)

        self.absExposureTimeLabel = QtGui.QLabel('Exposure Time:')
        self.flrExposureTimeLabel = QtGui.QLabel('Exposure Time:')
        self.absExposureTimeLabel.setFrameStyle(1)
        self.vbox_1_1.addWidget(self.absExposureTimeLabel)
        self.vbox_1_2.addWidget(self.flrExposureTimeLabel)
        self.absExposureTimeLabel.hide()
        self.flrExposureTimeLabel.hide()
        

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
        self.measureButton.clicked.connect(self.checkWells)
        self.clearButton.clicked.connect(self.clearWells)
        #self.sett.absCheck.stateChanged.connect(self.abs_state_change)
        #self.sett.flrCheck.stateChanged.connect(self.flr_state_change)

    def initUI(self):
        self.well = WellPlate()
        #self.sett = MeasurementSettings()
        self.measureButton = QtGui.QPushButton('Measure')
        self.clearButton = QtGui.QPushButton('Clear Selection')

        hbox_total = QtGui.QHBoxLayout()
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.well)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.measureButton)
        vbox.addLayout(hbox)
        vbox.addWidget(self.clearButton)
        hbox_total.addLayout(vbox)

        hbox_1 = QtGui.QHBoxLayout()
        #hbox_1.addWidget(self.sett)
        vbox_1 = QtGui.QVBoxLayout()
        vbox_1.addLayout(hbox_1)
        vbox_1.addStretch()
        hbox_total.addLayout(vbox_1)
        

        
        self.setLayout(hbox_total)
        self.setGeometry(350,350, 700, 250)
        self.setWindowTitle('MAK-Spec 2017')
        self.show()

    def checkWells(self):
        rows = ['A','B','C','D','E','F','G','H']
        cols = np.arange(1,13)
        toRead = []
        radios = self.well.findChildren(QtGui.QRadioButton)
        for button in radios:
            if button.isChecked():
                toRead.append(str(button.objectName()))
        if toRead == []:
            self.noWellSelected()

    def clearWells(self):
        radios = self.well.findChildren(QtGui.QRadioButton)
        for button in radios:
            if button.isChecked():
                button.setChecked(False)

    def noWellSelected(self):
       msg = QtGui.QMessageBox()
       msg.setIcon(QtGui.QMessageBox.Warning)
       msg.setText("No wells selected for measurement")
       msg.setWindowTitle("Measurement Error")
       msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
       retval = msg.exec_()

    # def abs_state_change(self):
    #     button = self.sett.absCheck
    #     settings = self.sett.absExposureTimeLabel
    #     if button.isChecked():
    #         settings.show()
    #     else:
    #         settings.hide()

    # def flr_state_change(self):
    #     button = self.sett.flrCheck
    #     settings = self.sett.flrExposureTimeLabel
    #     if button.isChecked():
    #         settings.show()
    #     else:
    #         settings.hide()
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Cleanlooks")
    ex = Example()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
