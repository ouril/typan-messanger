# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'typan_msg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
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
        self.ok.setGeometry(QtCore.QRect(420, 450, 81, 31))
        self.ok.setObjectName("ok")
        self.Contacts = QtWidgets.QListView(self.centralwidget)
        self.Contacts.setGeometry(QtCore.QRect(20, 40, 121, 391))
        self.Contacts.setObjectName("Contacts")
        self.TextArea = QtWidgets.QListView(self.centralwidget)
        self.TextArea.setGeometry(QtCore.QRect(20, 450, 391, 71))
        self.TextArea.setObjectName("TextArea")
        self.messages = QtWidgets.QListView(self.centralwidget)
        self.messages.setGeometry(QtCore.QRect(200, 40, 281, 391))
        self.messages.setObjectName("messages")
        self.scoll_for_con = QtWidgets.QScrollBar(self.centralwidget)
        self.scoll_for_con.setGeometry(QtCore.QRect(140, 40, 16, 391))
        self.scoll_for_con.setOrientation(QtCore.Qt.Vertical)
        self.scoll_for_con.setObjectName("scoll_for_con")
        self.scroll_for_msg = QtWidgets.QScrollBar(self.centralwidget)
        self.scroll_for_msg.setGeometry(QtCore.QRect(476, 40, 16, 391))
        self.scroll_for_msg.setOrientation(QtCore.Qt.Vertical)
        self.scroll_for_msg.setObjectName("scroll_for_msg")
        self.Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel.setGeometry(QtCore.QRect(420, 490, 81, 31))
        self.Cancel.setObjectName("Cancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 25))
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

