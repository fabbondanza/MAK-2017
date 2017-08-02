from PyQt4 import QtGui #Importing PyQt4 module 
import sys #Necessary to be able to pass argv to QApplication
import os  #For listing directory files
import numpy as np

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import gui_v1_design #File holding MainWindow and all other design features of GUI 
from arudino import * 
class ExampleApp(QtGui.QMainWindow, gui_v1_design.Ui_MainWindow):
    
    
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self) #Define in design.py --> automatically sets up layout & widgets
        self.pushButton.clicked.connect(self.checkWells)


    def checkWells(self):
        rows = ['A','B','C','D','E','F','G','H']
        cols = np.arange(1,13)
        toRead = []
        radios = self.groupbox.findChildren(QtGui.QRadioButton)
        for button in radios:
            if button.isChecked():
                toRead.append(str(button.objectName()).split('_')[1])
        print toRead
        m = MotorMove()
        m._set_initial_position()
        m._get_current_position()
        toReadNum = m._convert_labels_to_numericals(toRead)
        m._move_to_new_position(toReadNum)
        m.arduino.close()

def main():
    m = MotorMove()
    m.arduino.close()
    app = QtGui.QApplication(sys.argv) #New instance of QApplication
    app.setStyle("PLastique")
    form = ExampleApp()                # Form is set to be ExampleApp
    form.show()                        # Show form
    app.exec_()                        # Execute App
if __name__ == '__main__':
    main()
