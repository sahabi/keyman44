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
import coin_selection
import account_creation
import chain_creation
import mk_page
from pycoin.key.BIP32Node import BIP32Node
from mnemonic import Mnemonic

#words = 'abandon ability able about above absent absorb abstract absurd abuse access accident account accuse achieve acid acoustic acquire across act action actor actress actual'

#node = BIP32Node.from_master_secret(Mnemonic.to_seed(words), 'BTC')


class App(object):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

        self.main_dialog = QtWidgets.QDialog()
        self.coin_select_dialog = QtWidgets.QDialog()
        self.acc_create_dialog = QtWidgets.QDialog()
        self.chain_create_dialog = QtWidgets.QDialog()
        self.mk_dialog = QtWidgets.QDialog()

        self.bip44_page = bip44_page.Ui_Dialog()
        self.bip44_page.setupUi(self.main_dialog)
        self.bip44_page.mk_add_btn.clicked.connect(self.add_mk)
        self.bip44_page.mk_rm_btn.clicked.connect(self.rm_mk)
        self.bip44_page.coin_add_btn.clicked.connect(self.add_coin)
        self.bip44_page.acc_add_btn.clicked.connect(self.add_acc)
        self.bip44_page.chn_add_btn.clicked.connect(self.add_chn)
        self.bip44_page.addr_add_btn.clicked.connect(self.add_addr)
        self.bip44_page.coin_rm_btn.clicked.connect(self.rm_coin)
        self.bip44_page.acc_rm_btn.clicked.connect(self.rm_acc)
        self.bip44_page.chn_rm_btn.clicked.connect(self.rm_chn)
        self.bip44_page.addr_rm_btn.clicked.connect(self.rm_addr)

        self.bip44_page.mk_list.clicked.connect(self.activate_mk)
        self.bip44_page.coin_list.clicked.connect(self.activate_coin)
        self.bip44_page.acc_list.clicked.connect(self.activate_acc)
        self.bip44_page.chain_list.clicked.connect(self.activate_chain)
        self.bip44_page.addr_list.clicked.connect(self.activate_addr)

        self.bip44_page.coin_add_btn.setDisabled(True)
        self.bip44_page.coin_rm_btn.setDisabled(True)
        self.bip44_page.acc_add_btn.setDisabled(True)
        self.bip44_page.acc_rm_btn.setDisabled(True)
        self.bip44_page.chn_add_btn.setDisabled(True)
        self.bip44_page.chn_rm_btn.setDisabled(True)
        self.bip44_page.addr_add_btn.setDisabled(True)
        self.bip44_page.addr_rm_btn.setDisabled(True)
        self.bip44_page.mk_add_btn.setDisabled(False)
        self.bip44_page.mk_rm_btn.setDisabled(True)

        self.mk_page = mk_page.Ui_Dialog()
        self.mk_page.setupUi(self.mk_dialog)

        self.currency_list = ['', 'BTC', 'BTC-testnet']
        self.coin_select_page = coin_selection.Ui_Dialog()
        self.coin_select_page.setupUi(self.coin_select_dialog)
        self.coin_select_page.comboBox.addItems(self.currency_list)

        self.acc_create_page = account_creation.Ui_Dialog()
        self.acc_create_page.setupUi(self.acc_create_dialog)

        self.chain_create_page = chain_creation.Ui_Dialog()
        self.chain_create_page.setupUi(self.chain_create_dialog)

        self.bip44_page.close_btn.clicked.connect(self.main_dialog.reject)
        self.main_dialog.show()

    def run(self):
        sys.exit(self.app.exec_())

    def add_mk(self):
        self.mk_dialog.exec_()
        #imk_name = self.

    def add_coin(self):
        self.coin_select_dialog.exec_()
        coin_name = self.coin_select_page.comboBox.currentText()
        if coin_name != '':
            self.bip44_page.coin_list.addItem(coin_name)
            self.coin_select_page.comboBox.removeItem(
                    self.coin_select_page.comboBox.currentIndex())


    def add_acc(self):
        self.acc_create_dialog.show()

    def add_chn(self):
        self.chain_create_dialog.show()

    def add_addr(self):
        pass

    def rm_mk(self):
        selection = self.bip44_page.mk_list.currentIndex()
        self.bip44_page.mk_rm_btn.setDisabled(True)
        self.bip44_page.mk_list.takeItem(selection.row())

    def rm_coin(self):
        selection = self.bip44_page.coin_list.currentIndex()
        self.coin_select_page.comboBox.addItem(self.bip44_page.coin_list.currentItem().text())
        self.bip44_page.coin_rm_btn.setDisabled(True)
        self.bip44_page.coin_list.takeItem(selection.row())

    def activate_mk(self):
        self.bip44_page.coin_add_btn.setDisabled(False)
        self.bip44_page.mk_rm_btn.setDisabled(False)

    def activate_coin(self):
        self.bip44_page.coin_rm_btn.setDisabled(False)
        self.bip44_page.acc_add_btn.setDisabled(False)

    def activate_acc(self):
        self.bip44_page.addr_rm_btn.setDisabled(False)
        self.bip44_page.chain_add_btn.setDisabled(False)

    def activate_chain(self):
        self.bip44_page.chain_rm_btn.setDisabled(False)
        self.bip44_page.addr_add_btn.setDisabled(False)

    def activate_addr(self):
        self.bip44_page.addr_rm_btn.setDisabled(False)

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
