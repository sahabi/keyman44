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
        self.bip44_page.coin_add_btn.clicked.connect(self.add_coin)
        self.bip44_page.acc_add_btn.clicked.connect(self.add_acc)
        self.bip44_page.chn_add_btn.clicked.connect(self.add_chn)
        self.bip44_page.addr_add_btn.clicked.connect(self.add_addr)
        self.bip44_page.coin_rm_btn.clicked.connect(self.rm_coin)
        self.bip44_page.acc_rm_btn.clicked.connect(self.rm_acc)
        self.bip44_page.chn_rm_btn.clicked.connect(self.rm_chn)
        self.bip44_page.addr_rm_btn.clicked.connect(self.rm_addr)

    def run(self):
        sys.exit(self.app.exec_())

    def add_coin(self):
        self.netcode = get_current_netcode()

    def add_acc(self):
        pass

    def add_chn(self):
        pass

    def add_addr(self):
        pass

    def rm_coin(self):
        pass

    def rm_acc(self):
        pass

    def rm_chn(self):
        pass

    def rm_addr(self):
        pass

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
