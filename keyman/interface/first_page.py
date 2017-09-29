# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_page.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pycoin.key.BIP32Node import BIP32Node
from pycoin.cmds.ku import get_entropy
from pycoin.networks.default import get_current_netcode

class Ui_first(object):
    def setupUi(self, first):
        first.setObjectName("first")
        first.resize(411, 247)

        self.close_button = QtWidgets.QDialogButtonBox(first)
        self.close_button.setGeometry(QtCore.QRect(10, 210, 381, 32))
        self.close_button.setOrientation(QtCore.Qt.Horizontal)
        self.close_button.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.close_button.setObjectName("close_button")
        self.seed = QtWidgets.QLineEdit(first)
        self.seed.setGeometry(QtCore.QRect(40, 80, 331, 21))
        self.seed.setObjectName("seed")
        self.gen_seed_button = QtWidgets.QPushButton(first)
        self.gen_seed_button.setGeometry(QtCore.QRect(100, 110, 101, 23))
        self.gen_seed_button.setMouseTracking(True)
        self.gen_seed_button.setObjectName("gen_seed_button")
        self.next_button = QtWidgets.QPushButton(first)
        self.next_button.setEnabled(False)
        self.next_button.setGeometry(QtCore.QRect(230, 110, 101, 23))
        self.next_button.setObjectName("next_button")

        self.retranslateUi(first)
        self.close_button.accepted.connect(first.accept)
        self.close_button.rejected.connect(first.reject)
        QtCore.QMetaObject.connectSlotsByName(first)
        self.gen_seed_button.clicked.connect(self.gen_seed)
        self.seed.textChanged.connect(self.detect_text)
        self.next_button.clicked.connect(self.next)
        first.show()

    def retranslateUi(self, first):
        _translate = QtCore.QCoreApplication.translate
        first.setWindowTitle(_translate("first", "Welcome"))
        self.gen_seed_button.setText(_translate("first", "Generate Seed "))
        self.next_button.setText(_translate("first", "Next"))

    def next(self):
        print first.done(0)

    def gen_seed(self):
        master_secret = BIP32Node.from_master_secret(get_entropy(),
                netcode=get_current_netcode())
        self.seed.setText(master_secret)

    def detect_text(self, text):
        if len(text) > 0:
            self.next_button.setEnabled(True)
        else:
            self.next_button.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    first = QtWidgets.QDialog()
    second = QtWidgets.QDialog()
    ui = Ui_first()
    ui.setupUi(first)
    #first.show()
    sys.exit(app.exec_())

