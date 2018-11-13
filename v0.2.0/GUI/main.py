# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore

class Traductor( QtGui.QMainWindow ):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setWindowTitle('Code Translator')
        self.setWindowIcon( QtGui.QIcon('icons/icons8-google-code.png') )
        # resizing the QMainWindow to W:90% x H:80% of the screen
        self.screen = QtGui.QDesktopWidget().screenGeometry()
        screenWidth = self.screen.width()
        screenHeigh = self.screen.height()
        self.setMinimumSize( screenWidth*.9, screenHeigh*.8 ) 
        
        self.filename = ""
       
    # Actions    
        self.openFileAction = QtGui.QAction( QtGui.QIcon( 'icons/icons8-ver-archivo.png' ), 'Open file', self )
        self.openFileAction.setShortcut( 'Ctrl+O' )
        self.openFileAction.triggered.connect( self.open )
        self.openFileAction.setStatusTip( self.trUtf8('Open file option menu selected: opening file!') )

        self.saveFileAction = QtGui.QAction( QtGui.QIcon( 'icons/icons8-guardar-2.png' ), 'Save file', self )
        self.saveFileAction.setShortcut( 'Ctrl+S' )
        self.saveFileAction.triggered.connect( self.save )
        self.saveFileAction.setStatusTip( self.trUtf8('Save file option menu selected: saving file!') )

        self.saveAsFileAction = QtGui.QAction( QtGui.QIcon( 'icons/icons8-guardar-como-2.png' ), 'Save As... ', self )
        self.saveAsFileAction.setShortcut( 'Ctrl+Shift+S' )
        self.saveAsFileAction.triggered.connect( self.saveAs )
        self.saveAsFileAction.setStatusTip( self.trUtf8('Save as file option menu selected: renaming file!') )

        self.closeFileAction = QtGui.QAction( QtGui.QIcon( 'icons/icons8-eliminar-archivo-4.png' ), 'Close file', self )
        self.closeFileAction.setShortcut( 'Ctrl+W' )
        self.closeFileAction.triggered.connect( self.close )
        self.closeFileAction.setStatusTip( self.trUtf8('Close file option menu selected: closing file!') )

        self.exitAction = QtGui.QAction( QtGui.QIcon( 'icons/icons8-exportar.png' ), 'Exit', self )
        self.exitAction.setShortcut( 'Ctrl+Q' )
        self.exitAction.triggered.connect( self.exit )
        self.exitAction.setStatusTip( self.trUtf8('Quit option menu selected: quiting application!') )

    # Menu
        self.menu = self.menuBar()
        # Submenu
        self.menuFile = self.menu.addMenu('&File')
        self.menuFile.addAction( self.openFileAction )  
        self.menuFile.addAction( self.saveFileAction )  
        self.menuFile.addAction( self.saveAsFileAction )  
        self.menuFile.addAction( self.closeFileAction )  
        self.menuFile.addSeparator()
        self.menuFile.addAction( self.exitAction )  
        # Submenu
        self.menuFile = self.menu.addMenu('&Translate')

    # Tool Bar
        self.toolbar = QtGui.QToolBar()
        self.addToolBar( QtCore.Qt.RightToolBarArea, self.toolbar )
        # Options
        self.toolbar.addAction( self.openFileAction )
        self.toolbar.addAction( self.saveFileAction )  
        self.toolbar.addAction( self.saveAsFileAction )  
        self.toolbar.addAction( self.closeFileAction )  
        self.toolbar.addSeparator()
        self.toolbar.addAction( self.exitAction )   
 
    # Text Editor
        self.editor = QtGui.QTextEdit()
        self.setCentralWidget( self.editor )
        self.editor.setDocumentTitle( self.filename )
        
    # Status Bar
        self.setStatusBar( QtGui.QStatusBar() )

    # Conections
    def open(self):
        self.filename = QtGui.QFileDialog.getOpenFileName( self, 'Open File', '.', '(*.txt)' )
        
        if self.filename:
            with open( self.filename, 'r') as self.file:
                self.editor.setText( self.file.read() )

    def save(self):
        if not self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName( self, 'Save file' )
            with open( self.filename, 'w') as self.file:
                self.file.write( self.editor.toPlainText() )
        else:
            with open( self.filename, 'w') as self.file:
                self.file.write( self.editor.toPlainText() )

    def saveAs(self):
        if self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName( self, 'Save As...', self.filename )
            with open( self.filename, 'a+') as self.file:
                self.file.write( self.editor.toPlainText() )

    def close(self):
        if self.filename:
            self.file.close()
            self.editor.setText('')

    def exit(self):
        pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    traductor = Traductor()
    traductor.show()
    sys.exit(app.exec_())