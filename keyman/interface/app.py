# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from pycoin.key.BIP32Node import BIP32Node
from pycoin.cmds.ku import get_entropy
from pycoin.networks.default import get_current_netcode
from ..encoding.encoding import get_chain_secret_pair
import sys
from PyQt5.QtWidgets import QTreeWidgetItem
from pycoin.key.BIP32Node import BIP32Node
from .keychain import KeyChain
from .widgets import PubKeyTreeWidgetItem, PrivKeyTreeWidgetItem
import bip44_page
import send_page
import rcv_page

class App(object):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv) 
        self.main_dialog = QtWidgets.QDialog()
        self.bip44_page = bip44_page.Ui_Dialog()
        self.bip44_page.setupUi(self.main_dialog)
        self.main_dialog.show()
        self.netcode = get_current_netcode()

    def run(self):
        sys.exit(self.app.exec_())

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
