from PyQt4 import QtGui, QtCore
import sys

class VentanaOpcion(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Opciones")

        # Crear layout vertical
        vbox = QtGui.QVBoxLayout(self)
        gbox = QtGui.QGridLayout()
        hbox = QtGui.QHBoxLayout()

        # Creacion de los labels
        self.labelTitle = QtGui.QLabel("<h1>Lenguaje a traducir</h1>")
        self.labelOrigen = QtGui.QLabel("De: ")
        self.labelDestino = QtGui.QLabel("A: ")

        # Creacion de los botones (guardar y cancelar)
        self.btn_guardar = QtGui.QPushButton("Guardar")
        self.btn_cancelar = QtGui.QPushButton("Cancelar")

        vbox.addWidget(self.labelTitle)

        # Creacion de los comboxes
        self.cbox_origen = QtGui.QComboBox()
        self.cbox_destino = QtGui.QComboBox()

        # Lista de items
        self.ItemsCombox()

        # Añadir los labels y los comboxes
        gbox.addWidget(self.labelOrigen, 0,0)
        gbox.addWidget(self.cbox_origen, 0,1)
        gbox.addWidget(self.labelDestino, 1,0)
        gbox.addWidget(self.cbox_destino, 1,1)

        # Añadir los botones
        hbox.addWidget(self.btn_guardar)
        hbox.addWidget(self.btn_cancelar)
        
        # Añadiendo los layouts
        vbox.addLayout(gbox)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.Conexiones()
    
    def ItemsCombox(self):
        lista = ["JavaScript", "Python", "C++"]
        for item in lista:
            self.cbox_origen.addItem(item)
            self.cbox_destino.addItem(item)
    
    def Conexiones(self):
        # Conexion salir = cancelar
        self.btn_cancelar.clicked.connect(self.close)



app = QtGui.QApplication(sys.argv)
window = VentanaOpcion()
window.show()

sys.exit(app.exec_())