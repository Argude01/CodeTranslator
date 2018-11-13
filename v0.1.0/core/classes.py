import sys
from PyQt4 import QtGui, QtCore

class windowGUI:
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.screen = QtGui.QDesktopWidget().screenGeometry()
        self.window = QtGui.QWidget()

    def showWindow(self):
        self.window.setWindowTitle('Code Translator')
        # resizing the window to W:90% x H:80% of the screen
        screenWidth = self.screen.width()
        screenHeigh = self.screen.height()
        self.window.resize( screenWidth*.9, screenHeigh*.8 ) 
        # moving the window to the center of the screen
        windowWidth = self.window.frameSize().width()
        windowHeigh = self.window.frameSize().height()
        self.window.move( screenWidth/2 - windowWidth/2, screenHeigh/2 - windowHeigh/2 )

        self.window.show()  
        sys.exit(self.app.exec_())   

