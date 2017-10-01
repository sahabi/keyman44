# -*- coding: utf-8 -*-

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
from .widgets import PubKeyTreeWidgetItem, PrivKeyTreeWidgetItem

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
        master_node = BIP32Node(self.netcode, self.chain_code,
                secret_exponent=int(self.secret_exponent,16))
        master_pub_node = master_node.public_copy()
        privkey_tree_item = PrivKeyTreeWidgetItem(key_type='Private Key',
                level='m', key=master_node, wif='this is wif')
        pubkey_tree_item = PubKeyTreeWidgetItem(key_type='Public Key',
                level='M', key=master_pub_node, sec='this is sec', address='this is address')

        self.privkeychain.append(privkey_tree_item)
        self.pubkeychain.append(pubkey_tree_item)
        self.ui.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.treeWidget.customContextMenuRequested.connect(self.show_context_menu)
        self.ui.treeWidget.addTopLevelItems([privkey_tree_item, pubkey_tree_item])
        self.second.show()

    def show_context_menu(self, pos):
        menu = QtWidgets.QMenu()
        if self.pubkeychain.isSelected():
            menu.addAction("Create PubKey", self.derive_pub_from_pub)
        elif self.privkeychain.isSelected():
            menu.addAction("Create PubKey", self.derive_pub_from_priv)
            menu.addAction("Create PrivKey", self.derive_priv)
        action = menu.exec_(self.ui.treeWidget.mapToGlobal(pos))

    def derive_pub_from_priv(self, index=1):
        parent_level = self.privkeychain.get_selected_level()
        parent_key = self.privkeychain.get_selected_key().key
        self._derive_pub(parent_key, parent_level, self.privkeychain)

    def derive_pub_from_pub(self, index=1):
        parent_level = self.pubkeychain.get_selected_level()
        parent_key = self.pubkeychain.get_selected_key().key
        self._derive_pub(parent_key, parent_level, self.pubkeychain)

    def _derive_pub(self, parent_key, parent_level, keychain, index=1):
        child_key_type = 'Public Key'
        child_key = parent_key.public_copy()
        if parent_level[0] not in ['N', 'M']:
            child_key_label = 'N({})'.format(parent_level) + '/{}'.format(index)
        else:
            child_key_label = parent_level + '/{}'.format(index)
        child_tree_item = PubKeyTreeWidgetItem(child_key_type, child_key,
                child_key_label, sec=child_key.sec(use_uncompressed=False))
        self.pubkeychain.append(child_tree_item)
        keychain.get_selected_key().addChild(child_tree_item)

    def derive_priv(self, index=1):
        parent_level = self.privkeychain.get_selected_level()
        parent_key = self.privkeychain.get_selected_key().key
        child_key_type = 'Private Key'
        child_key = parent_key.subkey(as_private=True)
        child_tree_item = PrivKeyTreeWidgetItem(child_key_type, child_key,
                parent_level + '/{}'.format(index))
        self.privkeychain.append(child_tree_item)
        self.privkeychain.get_selected_key().addChild(child_tree_item)

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
