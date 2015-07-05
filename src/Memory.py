#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Jul 5, 2015

@author: Amy Bruderer

Create a game of memory in PyQt5
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    btn_red = QPushButton('', w)
    btn_red.resize(50, 50)
    btn_red.move(50, 50)
    btn_red.setStyleSheet('background-color: red')

    btn_green = QPushButton('', w)
    btn_green.resize(50, 50)
    btn_green.move(100, 50)
    btn_green.setStyleSheet('background-color: green')

    btn_blue = QPushButton('', w)
    btn_blue.resize(50, 50)
    btn_blue.move(50, 100)
    btn_blue.setStyleSheet('background-color: blue')

    btn_yellow = QPushButton('', w)
    btn_yellow.resize(50, 50)
    btn_yellow.move(100, 100)
    btn_yellow.setStyleSheet('background-color: yellow')

    w.resize(200, 200)
    w.move(300, 300)
    w.setWindowTitle('Memory')
    w.show()

    sys.exit(app.exec_())
