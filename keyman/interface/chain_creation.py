# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chain_creation.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(215, 116)
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 20, 71, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox_2.setGeometry(QtCore.QRect(20, 70, 181, 32))
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 20, 78, 27))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

