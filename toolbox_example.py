# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 17:12:40 2015

@author: Alois_W
"""

import sys


from PyQt4 import QtGui


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        exitAction = QtGui.QAction(QtGui.QIcon.fromTheme('exit.xpm'), 'Exit', self)
        #exitAction = QtGui.QAction(QtGui.QIcon.fromTheme('exit'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')    
        self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()