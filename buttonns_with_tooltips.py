# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
 
# Importing the necessary Qt classes.
 
from PyQt4 import QtGui
 
class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn1 = QtGui.QPushButton('Button1', self)
        btn2 = QtGui.QPushButton('Button2', self)
        btn1.setToolTip('This is  <b>Button 1</b>')
        btn1.resize(btn1.sizeHint())
        btn1.move(10, 10)
        
        btn2.setToolTip('This is  <b>Button 2</b>')
        btn2.resize(btn2.sizeHint())
        btn2.move(50, 50)   
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()