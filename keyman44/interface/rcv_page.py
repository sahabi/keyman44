# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/rcv_page.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 260, 98, 27))
        self.pushButton.setObjectName("pushButton")
        self.qr_label = QtWidgets.QLabel(Dialog)
        self.qr_label.setGeometry(QtCore.QRect(55, 70, 311, 161))
        self.qr_label.setAlignment(QtCore.Qt.AlignCenter)
        self.qr_label.setObjectName("qr_label")
        self.address_label = QtWidgets.QLabel(Dialog)
        self.address_label.setGeometry(QtCore.QRect(20, 10, 371, 17))
        self.address_label.setObjectName("address_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Close"))
        self.qr_label.setText(_translate("Dialog", "QR CODE"))
        self.address_label.setText(_translate("Dialog", "Address"))

