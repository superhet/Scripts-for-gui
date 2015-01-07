# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 16:38:44 2015

@author: Alois_W
"""


import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        self.statusBar().showMessage('hallo, das ist ein Statuszeile')
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')    
        self.show()


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()