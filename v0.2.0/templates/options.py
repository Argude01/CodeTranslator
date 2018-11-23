# -*- coding: utf8 -*-
from PyQt4 import QtGui, QtCore
import sys

class optionsWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Options")
        self.setGeometry( 600, 400, 200, 200 )
        self.show()

        # Crear layout vertical
        vbox = QtGui.QVBoxLayout(self)
        gbox = QtGui.QGridLayout()
        hbox = QtGui.QHBoxLayout()

        # Creacion de los labels
        self.labelTitle = QtGui.QLabel("<h1>Lenguaje a traducir</h1>")
        self.originLanguage = QtGui.QLabel("De: ")
        self.targetLanguage = QtGui.QLabel("A: ")

        # Creacion de los botones (guardar y cancelActionar)
        self.saveAction = QtGui.QPushButton("Save")
        self.saveAction.clicked.connect(self.save)
        self.cancelAction = QtGui.QPushButton("cancel")
        self.cancelAction.clicked.connect(self.close)

        vbox.addWidget(self.labelTitle)

        # Creacion de los comboxes
        self.origin = QtGui.QComboBox()
        self.target = QtGui.QComboBox()
        self.ItemsCombox()
        self.origin.currentIndexChanged.connect(self.save)

        # Lista de items

        # Añadir los labels y los comboxes
        gbox.addWidget(self.originLanguage, 0,0)
        gbox.addWidget(self.origin, 0,1)
        gbox.addWidget(self.targetLanguage, 1,0)
        gbox.addWidget(self.target, 1,1)

        # Añadir los botones
        hbox.addWidget(self.saveAction)
        hbox.addWidget(self.cancelAction)
        
        # Aniadiendo los layouts
        vbox.addLayout(gbox)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def ItemsCombox(self):
        lista = ['',"JavaScript", "Python", "C++"]
        for item in lista:
            self.origin.addItem(item)
            self.target.addItem(item)
  
    def save(self):
        self.originLanguage.setText("De: ")
        self.targetLanguage.setText("A: ")
        self.originLanguage.setText(self.originLanguage.text() + self.origin.currentText())
        self.targetLanguage.setText(self.targetLanguage.text()+ self.target.currentText())



app = QtGui.QApplication(sys.argv)
window = optionsWindow()
window.show()

sys.exit(app.exec_())