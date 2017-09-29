# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstgui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_first(object):
    def setupUi(self, first):
        first.setObjectName("first")
        first.resize(411, 247)
        self.close_button = QtWidgets.QDialogButtonBox(first)
        self.close_button.setGeometry(QtCore.QRect(10, 210, 381, 32))
        self.close_button.setOrientation(QtCore.Qt.Horizontal)
        self.close_button.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.close_button.setObjectName("close_button")
        self.secret_exponent = QtWidgets.QLineEdit(first)
        self.secret_exponent.setGeometry(QtCore.QRect(40, 50, 331, 21))
        self.secret_exponent.setObjectName("secret_exponent")
        self.gen_key_button = QtWidgets.QPushButton(first)
        self.gen_key_button.setGeometry(QtCore.QRect(80, 150, 101, 23))
        self.gen_key_button.setMouseTracking(True)
        self.gen_key_button.setObjectName("gen_key_button")
        self.next_button = QtWidgets.QPushButton(first)
        self.next_button.setEnabled(False)
        self.next_button.setGeometry(QtCore.QRect(220, 150, 101, 23))
        self.next_button.setObjectName("next_button")
        self.chain_code = QtWidgets.QLineEdit(first)
        self.chain_code.setGeometry(QtCore.QRect(40, 110, 331, 21))
        self.chain_code.setObjectName("chain_code")
        self.label = QtWidgets.QLabel(first)
        self.label.setGeometry(QtCore.QRect(160, 20, 141, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(first)
        self.label_2.setGeometry(QtCore.QRect(150, 80, 141, 17))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(first)
        self.close_button.accepted.connect(first.accept)
        self.close_button.rejected.connect(first.reject)
        QtCore.QMetaObject.connectSlotsByName(first)

    def retranslateUi(self, first):
        _translate = QtCore.QCoreApplication.translate
        first.setWindowTitle(_translate("first", "Welcome"))
        self.gen_key_button.setText(_translate("first", "Generate Key"))
        self.next_button.setText(_translate("first", "Next"))
        self.label.setText(_translate("first", "Secret Exponent"))
        self.label_2.setText(_translate("first", "Chain Code"))

