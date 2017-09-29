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
from first_page import Ui_first
from ..encoding.encoding import get_chain_secret_pair
import sys
from second_page import Ui_second

class App(object):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.first = QtWidgets.QDialog()
        self.second = QtWidgets.QDialog()
        self.ui = Ui_first()
        self.ui.setupUi(self.first)
        self.ui.gen_key_button.clicked.connect(self.gen_seed)
        self.ui.secret_exponent.textChanged.connect(self.detect_text)
        self.ui.next_button.clicked.connect(self.next)
        self.first.show()
    def run(self):
        sys.exit(self.app.exec_())

    def retranslateUi(self, first):
        _translate = QtCore.QCoreApplication.translate
        self.first.setWindowTitle(_translate("first", "Welcome"))
        self.gen_seed_button.setText(_translate("first", "Generate Seed "))
        self.next_button.setText(_translate("first", "Next"))

    def next(self):
        self.first.done(0)
        self.ui = Ui_second()
        self.ui.setupUi(self.second)
        self.second.show()
        #sys.exit(self.app.exec_())

    def gen_seed(self):
        self.chain_code, self.secret_exponent = get_chain_secret_pair()
        self.ui.secret_exponent.setText(self.secret_exponent)
        self.ui.chain_code.setText(self.chain_code)

    def detect_text(self, text):
        if len(text) > 0:
            self.ui.next_button.setEnabled(True)
        else:
            self.ui.next_button.setEnabled(False)

app = App()
app.run()
