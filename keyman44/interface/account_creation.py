# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/account_creation.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(220, 104)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 60, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.acc_name = QtWidgets.QTextEdit(Dialog)
        self.acc_name.setGeometry(QtCore.QRect(30, 20, 71, 31))
        self.acc_name.setObjectName("acc_name")
        self.acc_n = QtWidgets.QTextEdit(Dialog)
        self.acc_n.setGeometry(QtCore.QRect(120, 20, 71, 31))
        self.acc_n.setObjectName("acc_n")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

