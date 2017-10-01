# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_page.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from pycoin.key.BIP32Node import BIP32Node
from pycoin.cmds.ku import get_entropy
from pycoin.networks.default import get_current_netcode
from first_page import Ui_first
from ..encoding.encoding import get_chain_secret_pair
import sys
from second_page import Ui_second
from PyQt5.QtWidgets import QTreeWidgetItem
from pycoin.key.BIP32Node import BIP32Node
from .keychain import KeyChain
from .widgets import KeyTreeWidgetItem
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
        self.netcode = get_current_netcode()
        self.privkeychain = KeyChain()
        self.pubkeychain = KeyChain()

    def run(self):
        sys.exit(self.app.exec_())

    def retranslateUi(self, first):
        _translate = QtCore.QCoreApplication.translate
        self.first.setWindowTitle(_translate("first", "Welcome"))
        self.gen_seed_button.setText(_translate("first", "Generate Seed "))
        self.next_button.setText(_translate("first", "Next"))

    def next(self):
        self.first.done(0)
        self.start_second()

    def start_second(self):
        self.ui = Ui_second()
        self.ui.setupUi(self.second)
        self.master_node = BIP32Node(self.netcode, self.chain_code,
                secret_exponent=int(self.secret_exponent,16))
        self.privkey_tree_item = KeyTreeWidgetItem('Private Key','M')
        self.privkeychain.append(self.privkey_tree_item)
        self.ui.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.treeWidget.customContextMenuRequested.connect(self.show_menu)
        self.ui.treeWidget.addTopLevelItems([self.privkey_tree_item])
        self.second.show()

    def show_menu(self, pos):
        menu = QtWidgets.QMenu()
        if self.privkeychain.isSelected():
            menu.addAction("Create PubKey", self.create_pub_from_priv)
            menu.addAction("Create PrivKey", self.create_priv)
        elif self.pubkeychain.isSelected():
            menu.addAction("Create PubKey", self.create_pub_from_pub)
        action = menu.exec_(self.ui.treeWidget.mapToGlobal(pos))

    def create_pub_from_priv(self):
        level = self.privkeychain.get_selected_level()
        print(level)

    def create_priv(self):
        level = self.privkey_keychain.which()

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
