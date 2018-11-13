# -*- coding: utf-8 -*-
import sys
import subprocess
from PyQt4 import QtGui
      
class ToolsBar():
    def __init__(widget, self):
        #QtGui.Toolsar.__init__(self) 
        self.toolsBar = widget     
        self.setToolsBar() 

    def setToolsBar(self): 
        self.cut = QtGui.QAction( QtGui.QIcon('img/icons/icons8-eliminar-archivo-4.png'), 'Cut', self )# difference between both self ???
        self.toolsBar.addAction(self.cut)
        self.toolsBar.actionTriggered[QtGui.QAction].connect( self.toolPressed )
        self.copy = QtGui.QAction( QtGui.QIcon('img/icons/icons8-copiar-2.png'), 'Copy', self )
        self.toolsBar.addAction(self.copy)
        self.toolsBar.actionTriggered[QtGui.QAction].connect( self.toolPressed )
        self.paste = QtGui.QAction( QtGui.QIcon('img/icons/icons8-pegar.png'), 'Paste', self )
        self.toolsBar.addAction(self.paste)
        self.toolsBar.actionTriggered[QtGui.QAction].connect( self.toolPressed )
        self.closeFile = QtGui.QAction( QtGui.QIcon('img/icons/icons8-eliminar.png'), 'Close file', self )
        self.toolsBar.addAction(self.closeFile)
        self.toolsBar.actionTriggered[QtGui.QAction].connect( self.toolPressed )
    
    def toolPressed(self, tool):
        print "pressed tool button is",tool.text()	

    def layoutToolsBar(self):   
        self.setToolsBar()          
        grid = QtGui.QGridLayout() 
