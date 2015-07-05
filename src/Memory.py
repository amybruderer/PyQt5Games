#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Jul 5, 2015

@author: Amy Bruderer

Create a game of memory in PyQt5
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())
