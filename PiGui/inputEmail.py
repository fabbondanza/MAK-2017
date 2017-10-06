from PyQt4 import QtGui
from PyQt4 import QtCore

class InputEmail(QtGui.QDialog):
    '''
    this is for when you need to get some user input text
    '''

    def __init__(self, parent=None, title='Data Transfer Information', label='Enter Email', text=''):
        QtGui.QWidget.__init__(self, parent)

        # --Layout Stuff---------------------------#
        mainLayout = QtGui.QVBoxLayout()

        layout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel()
        self.label.setText(label)
        layout.addWidget(self.label)

        self.text = QtGui.QLineEdit(text)
        layout.addWidget(self.text)

        mainLayout.addLayout(layout)

        # --The Button------------------------------#
        layout = QtGui.QHBoxLayout()
        button = QtGui.QPushButton("ACCEPT")  # string or icon
        self.connect(button, QtCore.SIGNAL("clicked()"), self.close)
        layout.addWidget(button)

        mainLayout.addLayout(layout)
        self.setLayout(mainLayout)

        self.resize(400, 60)
        self.setWindowTitle('KAM-Spec 2017')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('KAM-Spec Logo LtoH.svg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)