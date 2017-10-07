# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mk_page.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(615, 227)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(420, 180, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.mnem = QtWidgets.QTextEdit(Dialog)
        self.mnem.setGeometry(QtCore.QRect(40, 40, 441, 71))
        self.mnem.setObjectName("mnem")
        self.gen_mnem = QtWidgets.QPushButton(Dialog)
        self.gen_mnem.setGeometry(QtCore.QRect(490, 60, 98, 27))
        self.gen_mnem.setObjectName("gen_mnem")
        self.passphrase = QtWidgets.QTextEdit(Dialog)
        self.passphrase.setGeometry(QtCore.QRect(330, 130, 211, 31))
        self.passphrase.setObjectName("passphrase")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 91, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(240, 140, 91, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.mk_name = QtWidgets.QTextEdit(Dialog)
        self.mk_name.setGeometry(QtCore.QRect(80, 130, 131, 31))
        self.mk_name.setObjectName("mk_name")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 140, 91, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.gen_mnem.setText(_translate("Dialog", "Generate "))
        self.label_5.setText(_translate("Dialog", "Mnemonics"))
        self.label_6.setText(_translate("Dialog", "Passphrase"))
        self.label_7.setText(_translate("Dialog", "Name"))

