# -*- coding: utf-8 -*-
import sys
import re
import subprocess
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

        self.colorHintAction = QtGui.QAction( 'Color Hint', self )
        self.colorHintAction.triggered.connect( self.colorHint )
        self.colorHintAction.setStatusTip( self.trUtf8('Color Hint option menu selected: coloring this file!') )

        self.validateLexiconAction = QtGui.QAction( 'Call Lexicon', self )
        self.validateLexiconAction.triggered.connect( self.validateLexicon )
        self.validateLexiconAction.setStatusTip( self.trUtf8('Validate option menu selected: validating lexicon in this file...') )


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
        self.menuValidate = self.menu.addMenu('&Validate')
        self.menuValidate.addAction( self.validateLexiconAction )
        # Submenu
        self.menuTraductor = self.menu.addMenu('&Traductor')
        self.menuTraductor.addAction( self.colorHintAction )

    # Tool Bar
        self.toolbar = QtGui.QToolBar()
        self.addToolBar( QtCore.Qt.LeftToolBarArea, self.toolbar )
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
        self.editor.setStyleSheet('QTextEdit {color:black}')
        self.editor.setFontItalic(False)    
        # Text Editor Cursor
        self.cursor = self.editor.textCursor()

    # Status Bar
        self.setStatusBar( QtGui.QStatusBar() )

    # Conections
    def open(self):
        self.filename = QtGui.QFileDialog.getOpenFileName( self, 'Open File', '.', '(*.*)' )
        
        if self.filename:
            with open( self.filename, 'r') as self.file:
                self.editor.setText( self.file.read() )

    def save(self):
        if not self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName( self, 'Save file' )
            with open(self.filename, 'w') as self.file:
                self.file.write( self.editor.toPlainText() )
        else:
            with open(self.filename, 'w') as self.file:
                self.file.write( self.editor.toPlainText() )

    def saveAs(self):
        if self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName( self, 'Save As...', self.filename )
            with open(self.filename, 'a+') as self.file:
                self.file.write( self.editor.toPlainText() )

    def close(self):
        if self.filename:
            self.file.close()
            self.editor.setText('')

    def exit(self):
        pass
    
    def validateLexicon(self):
        subprocess.call(['sh', 'intermediate.sh', 'python', 'lexicon.py', self.filename, 'lexicon.tmp'])
        self.builtContainerFileAndPatterns()

    def builtContainerFileAndPatterns(self):
        tokens_tmp = [ token.rstrip('\n') for token in open('lexicon.tmp') ]
        self.tokens = []
        self.containerPatterns = []
        self.containerFile = []
        description_items = ''
        value_items = ''
        i=0
        for token in tokens_tmp: 
            #print token
            token = token.split(',')            #return ["('RESWORD'"," 'function')"]
            #print token
            token[0] = token[0].strip("(")      #  token["'RESWORD'"," 'fuction')"]    
            #print token[0]        
            token[1] = token[1].strip(")")      #  token["'RESWORD'"," 'fuction'"]
            #print token[1]
            token[0] = token[0].strip("'")      #  token["RESOWRD"," 'function'"] 
            #print token[0]
            token[1] = token[1].strip(" ")      #  token["RESOWRD","'function"]
            token[1] = token[1].strip("'")      #  token["RESOWRD","function"]
            #print token[1]
            #print token
            #print"-"*50
            self.tokens.append(token)           # [" DESCRIPTION "," VALUE "]
            value_items += str(token[1])        # " VALUE "    
            description_items += str(token[0])  # " DESCRIPTION "

            if token[0] == '\\n' or token[0] == 'None':           
                self.containerFile.insert(i,value_items)
                self.containerPatterns.insert(i,description_items)  # didn't work with append ¿WHY?
                value_items = ''
                description_items = ''
                i+=1
    
        print '\nContainer File'
        print '-'*80
        for s in self.containerFile: print str(self.containerFile.index(s)) +'-> '+ s
        print '\nContainer Patterns'
        print '-'*80
        for d in self.containerPatterns: print str(self.containerPatterns.index(d)) +'-> '+ d      
        print '\n'*2

    def getListKeywords(self):
        self.listKeywords = []
        for token in self.tokens:
            if token[0]!=' ' and token[0]!='\\n' and token[0]!= 'None':
                if not token[0] in self.listKeywords:             
                    self.listKeywords.append( str(token[0]) )
        return self.listKeywords
    
    def getFormatsColorHint(self):
        # grouping characters
        groupingCharactersFormat = QtGui.QTextCharFormat()
        groupingCharactersFormat.setFontWeight( QtGui.QFont.Bold )
        groupingCharactersFormat.setFontItalic( True )
        # reserved words : function 
        reswordFunctionFormat = QtGui.QTextCharFormat()
        reswordFunctionFormat.setFontCapitalization( QtGui.QFont.AllLowercase )
        reswordFunctionFormat.setForeground( QtGui.QColor( QtCore.Qt.green ) )
        # reserved words : if 
        reswordIfFormat = QtGui.QTextCharFormat()
        reswordIfFormat.setFontCapitalization( QtGui.QFont.AllLowercase )
        reswordIfFormat.setForeground( QtGui.QColor( QtCore.Qt.red ) )
        # reserved words : return
        reswordReturnFormat = QtGui.QTextCharFormat()
        reswordReturnFormat.setFontCapitalization( QtGui.QFont.AllLowercase )
        reswordReturnFormat.setForeground( QtGui.QColor( QtCore.Qt.red ) )
        # reserved words : true / false
        reswordBooleanFormat = QtGui.QTextCharFormat()
        reswordBooleanFormat.setFontCapitalization( QtGui.QFont.AllLowercase )
        reswordBooleanFormat.setForeground( QtGui.QColor( QtCore.Qt.magenta ) )
        # User IDentificator
        UIDFormat = QtGui.QTextCharFormat()
        UIDFormat.setFontWeight( QtGui.QFont.DemiBold )
        UIDFormat.setFontUnderline( True )
        UIDFormat.setForeground( QtGui.QColor( QtCore.Qt.cyan ) )

        self.dictFormats = { 'groupingCharacters': groupingCharactersFormat,
                             'reswordFunction': reswordFunctionFormat,
                             'reswordIf': reswordIfFormat,
                             'reswordReturn': reswordReturnFormat,
                             'reswordBoolean': reswordBooleanFormat,
                             'UID': UIDFormat }

        return self.dictFormats

    def setGroupCharTokenFormat(self, pattern, textFormat):        
        regex = QtCore.QRegExp(pattern)
        pos = 0
        index = regex.indexIn(self.editor.toPlainText(), pos)
        while index != -1:
            self.cursor.setPosition(index)
            self.cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
            print self.cursor.selectedText()
            self.cursor.mergeCharFormat(textFormat)
            pos = index + regex.matchedLength()
            index = regex.indexIn(self.editor.toPlainText(), pos)
    
    def colorHint(self):
        listKeywords = self.getListKeywords()
        print listKeywords
        dictFormats = self.getFormatsColorHint()
        for key in listKeywords:
            if key=='(' or key==')' or key=='[' or key==']' or key=='{' or key=='}':
                self.setGroupCharTokenFormat(key, dictFormats['groupingCharacters'])

            if key=='function':
                self.setGroupCharTokenFormat(key, dictFormats['reswordFunction'])

            if key=='return':
                self.setGroupCharTokenFormat(key, dictFormats['reswordReturn'])
            
            if key=='if':
                self.setGroupCharTokenFormat(key, dictFormats['reswordIf'])

            if key=='false' or key=='true':
                self.setGroupCharTokenFormat(key, dictFormats['reswordBoolean'])  

            if key=='UID':
                self.setGroupCharTokenFormat(key, dictFormats['UID'])
            
    '''
    def getTexteSelected(self):
        self.cursor = self.editor.textCursor()
        self.cursor.setPosition(start)
        self.cursos.setPosition(end, QtGui.QTextCursor.KeepAnchor)
        self.cursor.movePosition( QtGui.QTextCursor.StartOfLine )

    def colorHint(self):
        self.toUpperTokens()    
        
        for token in self.tokens:
            if token[0] == 'RESWORD':
                word = token[1]
                print '\n' + '='*100
                print 'TOKEN[word]: ' + word             
                #for line in self.containerFile:
                    # line.find(word)
                    start = 0
                    end = 0  
                    if line.find(word) > -1:                    
                        start = position
                        end = position + len(word)
                        print '_'*100
                        print 'current line: ' + line
                        print '-'*100
                        self.cursor.setPosition( start )
                        self.cursor.setPosition( end, QtGui.QTextCursor.KeepAnchor )
                        self.editor.setTextCursor( self.cursor )
                        if self.cursor.hasSelection():
                            self.cursor.insertText(self.cursor.selectedText().toUpper())
                        #currentSelection = self.cursor.selectedText()
                        #editorSelection = self.editor.document().find( currentSelection )
                        #editorSelectionFormat = editorSelection.charFormat()
                        #editorSelection.setFontItalic(True)
                        #editorSelectionFormat.setTextColor( QtGui.QColor( QtCore.Qt.black ) )
                        #self.editor.setText( currentSelection )

                        #self.cursor.selectedText().setTextColor( QtGui.QColor( QtCore.Qt.black ) )
                        print 'cursor position: ' + str(self.cursor.position())
                        print 'location word: ' + str(start) + ':' + str(end) + ' - ' + line[start:end]
                        print '-'*100   
                        line = line[end:len(line)]                  
                        print 'updated line: ' + line

                         
            if token[0] == '(' or token[0] == ')' or token[0] == '{' or token[0] == '}' or token[0] == '[' or token[0] == ']':
                word = token[1]
                print 'word: ' + word             
                for line in self.containerFile:
                    position = 0
                    start = 0
                    end = 0  
                    while position > -1:
                        position = line.find(word)
                        start = position
                        end = position + len(word)
                        print '-'*30
                        print line
                        print str(start) + ':' + str(end) + ' - ' + line[start:end]
                        line = line[end:len(line)]
                        print line
                        print '-'*30  
                        self.cursor.setPosition(position, self.cursor.anchor())
                        self.cursor.selectedText().setFontItalic(True)
        '''
                    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    traductor = Traductor()
    traductor.show()
    sys.exit(app.exec_())