# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 16:41:34 2015

@author: Alois_W
"""

import sys
from PyQt4 import QtGui

class Mainwindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(Mainwindow, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        #First item of Menubar
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        #Item for statusbar
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        #Second item of Menubar
        firstAction = QtGui.QAction('&First Entry', self)
        firstAction.setStatusTip('Something useful')
        
        #Third item of Menubar
        secondAction = QtGui.QAction('&First Entry', self)
        secondAction.setStatusTip('Something really useful')
        
        self.statusBar()

        menubar = self.menuBar()
        
        #Items of Menubar
        fileMenu = menubar.addMenu('&File')
        item1 = menubar.addMenu('&Item1')
        item2 = menubar.addMenu('&Item2')
        
        #Append to elements to Menubar
        fileMenu.addAction(exitAction)
        item1.addAction(firstAction)
        item2.addAction(secondAction)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')    
        self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Mainwindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()  