from PyQt4 import QtGui #Importing PyQt4 module 
import sys #Necessary to be able to pass argv to QApplication
import os  #For listing directory files

import design #File holding MainWindow and all other design features of GUI
from arudino import *
class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self) #Define in design.py --> automatically sets up layout & widgets
        self.startButton.clicked.connect(self.start_folder)
        self.stopButton.clicked.connect(self.stop_folder)

    def start_folder(self):
        self.listWidget.clear()
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Start")

        if directory:
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)

    def stop_folder(self):
        self.listWidget.clear()
def main():
    app = QtGui.QApplication(sys.argv) #New instance of QApplication
    form = ExampleApp()                # Form is set to be ExampleApp
    form.show()                        # Show form
    app.exec_()                        # Execute App

if __name__ == '__main__':
    main()
