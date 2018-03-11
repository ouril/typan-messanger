# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'typan_server.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(516, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(20, 500, 81, 31))
        self.ok.setObjectName("ok")
        self.clients = QtWidgets.QListView(self.centralwidget)
        self.clients.setGeometry(QtCore.QRect(40, 80, 431, 391))
        self.clients.setObjectName("clients")
        self.scroll_for_msg = QtWidgets.QScrollBar(self.centralwidget)
        self.scroll_for_msg.setGeometry(QtCore.QRect(470, 80, 16, 391))
        self.scroll_for_msg.setOrientation(QtCore.Qt.Vertical)
        self.scroll_for_msg.setObjectName("scroll_for_msg")
        self.Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel.setGeometry(QtCore.QRect(410, 500, 81, 31))
        self.Cancel.setObjectName("Cancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ok.setText(_translate("MainWindow", "OK"))
        self.Cancel.setText(_translate("MainWindow", "Cancel"))

