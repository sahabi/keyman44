# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_page.ui'
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
        self.master_key = QtWidgets.QLineEdit(first)
        self.master_key.setGeometry(QtCore.QRect(40, 80, 331, 21))
        self.master_key.setObjectName("master_key")
        self.gen_key_button = QtWidgets.QPushButton(first)
        self.gen_key_button.setGeometry(QtCore.QRect(100, 110, 101, 23))
        self.gen_key_button.setMouseTracking(True)
        self.gen_key_button.setObjectName("gen_key_button")
        self.next_button = QtWidgets.QPushButton(first)
        self.next_button.setEnabled(False)
        self.next_button.setGeometry(QtCore.QRect(230, 110, 101, 23))
        self.next_button.setObjectName("next_button")

        self.retranslateUi(first)
        self.close_button.accepted.connect(first.accept)
        self.close_button.rejected.connect(first.reject)
        QtCore.QMetaObject.connectSlotsByName(first)

    def retranslateUi(self, first):
        _translate = QtCore.QCoreApplication.translate
        first.setWindowTitle(_translate("first", "Welcome"))
        self.gen_key_button.setText(_translate("first", "Generate Key"))
        self.next_button.setText(_translate("first", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    first = QtWidgets.QDialog()
    ui = Ui_first()
    ui.setupUi(first)
    first.show()
    sys.exit(app.exec_())

