# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_Client.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newClient(object):
    def setupUi(self, newClient):
        newClient.setObjectName("newClient")
        newClient.resize(379, 139)
        newClient.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.FirstName = QtWidgets.QPlainTextEdit(newClient)
        self.FirstName.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.FirstName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FirstName.setObjectName("FirstName")
        self.LastName = QtWidgets.QPlainTextEdit(newClient)
        self.LastName.setGeometry(QtCore.QRect(140, 30, 91, 31))
        self.LastName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LastName.setObjectName("LastName")
        self.PhoneNumber = QtWidgets.QPlainTextEdit(newClient)
        self.PhoneNumber.setGeometry(QtCore.QRect(250, 30, 104, 31))
        self.PhoneNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PhoneNumber.setObjectName("PhoneNumber")
        self.Confirm = QtWidgets.QPushButton(newClient)
        self.Confirm.setGeometry(QtCore.QRect(140, 80, 75, 23))
        self.Confirm.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.Confirm.setObjectName("Confirm")

        self.retranslateUi(newClient)
        QtCore.QMetaObject.connectSlotsByName(newClient)

    def retranslateUi(self, newClient):
        _translate = QtCore.QCoreApplication.translate
        newClient.setWindowTitle(_translate("newClient", "Dialog"))
        self.FirstName.setPlainText(_translate("newClient", "First Name"))
        self.LastName.setPlainText(_translate("newClient", "Last Name"))
        self.PhoneNumber.setPlainText(_translate("newClient", "Phone Number"))
        self.Confirm.setText(_translate("newClient", "Confirm"))

