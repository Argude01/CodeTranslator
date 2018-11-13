import sys
from core.classes import windowGUI

class translatorGUI(windowGUI):
    def __init__(self):
        self.window = windowGUI()
        self.window.showWindow()
       
app = translatorGUI()
      

