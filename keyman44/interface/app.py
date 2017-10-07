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
from .widgets import MasterKey, Coin, Account, ExternalAddress
import bip44_page
import send_page
import rcv_page
import coin_selection
import account_creation
import mk_page
from pycoin.key.BIP32Node import BIP32Node
from mnemonic import Mnemonic

#words = 'abandon ability able about above absent absorb abstract absurd abuse access accident account accuse achieve acid acoustic acquire across act action actor actress actual'

#node = BIP32Node.from_master_secret(Mnemonic.to_seed(words), 'BTC')


class App(object):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

        self.mk_record = {}
        self.coin_record = {}
        self.account_record = {}
        self.account_counter = 0
        self.ext_addr_record = []
        self.ext_addr_counter = 0

        self.main_dialog = QtWidgets.QDialog()
        self.coin_select_dialog = QtWidgets.QDialog()
        self.acc_create_dialog = QtWidgets.QDialog()
        self.mk_dialog = QtWidgets.QDialog()

        self.bip44_page = bip44_page.Ui_Dialog()
        self.bip44_page.setupUi(self.main_dialog)
        self.bip44_page.mk_add_btn.clicked.connect(self.add_mk)
        self.bip44_page.mk_rm_btn.clicked.connect(self.rm_mk)
        self.bip44_page.coin_add_btn.clicked.connect(self.add_coin)
        self.bip44_page.acc_add_btn.clicked.connect(self.add_acc)
        self.bip44_page.addr_add_btn.clicked.connect(self.add_addr)
        self.bip44_page.coin_rm_btn.clicked.connect(self.rm_coin)
        self.bip44_page.acc_rm_btn.clicked.connect(self.rm_acc)
        self.bip44_page.addr_rm_btn.clicked.connect(self.rm_addr)

        self.bip44_page.mk_list.clicked.connect(self.activate_mk)
        self.bip44_page.coin_list.clicked.connect(self.activate_coin)
        self.bip44_page.acc_list.clicked.connect(self.activate_acc)
        self.bip44_page.addr_list.clicked.connect(self.activate_addr)

        self.bip44_page.coin_add_btn.setDisabled(True)
        self.bip44_page.coin_rm_btn.setDisabled(True)
        self.bip44_page.acc_add_btn.setDisabled(True)
        self.bip44_page.acc_rm_btn.setDisabled(True)
        self.bip44_page.addr_add_btn.setDisabled(True)
        self.bip44_page.addr_rm_btn.setDisabled(True)
        self.bip44_page.mk_add_btn.setDisabled(False)
        self.bip44_page.mk_rm_btn.setDisabled(True)

        self.mk_page = mk_page.Ui_Dialog()
        self.mk_page.setupUi(self.mk_dialog)
        self.mk_page.gen_mnem.clicked.connect(self.gen_mnem)

        self.currency_list = ['', 'BTC', 'BTC-testnet']
        self.coin_select_page = coin_selection.Ui_Dialog()
        self.coin_select_page.setupUi(self.coin_select_dialog)
        self.coin_select_page.comboBox.addItems(self.currency_list)

        self.acc_create_page = account_creation.Ui_Dialog()
        self.acc_create_page.setupUi(self.acc_create_dialog)

        self.bip44_page.close_btn.clicked.connect(self.main_dialog.reject)
        self.main_dialog.show()

    def run(self):
        sys.exit(self.app.exec_())

    def add_mk(self):
        self.mk_dialog.exec_()
        mk_name = self.mk_page.mk_name.toPlainText()
        seed = Mnemonic.to_seed(self.mk_page.mnem.toPlainText())
        passphrase = self.mk_page.passphrase.toPlainText()
        mk = MasterKey(name=mk_name, seed=seed)
        self.mk_record[mk.name] = mk
        self.bip44_page.mk_list.addItem(mk.name)
        #imk_name = self.

    def add_coin(self, purpose=44):
        self.coin_select_dialog.exec_()
        mk_name = self.bip44_page.mk_list.selectedItems()[0].text()
        coin_name = self.coin_select_page.comboBox.currentText()
        if coin_name == 'BTC':
            network = 0
        elif coin_name == 'BTC-testnet':
            network = 1
        else:
            return
        coin = Coin(name=coin_name, mk=self.mk_record[mk_name], network=network)
        self.coin_record[coin.name] = coin
        self.mk_record[mk_name].coins[coin.name] = coin
        if coin != '':
            self.bip44_page.coin_list.addItem(coin.name)
            self.coin_select_page.comboBox.removeItem(
                    self.coin_select_page.comboBox.currentIndex())

    def gen_mnem(self):
        mnem = Mnemonic('english')
        words = mnem.generate()
        self.mk_page.mnem.setText(words)

    def add_acc(self):
        self.acc_create_dialog.exec_()
        acc_name = self.acc_create_page.acc_name.toPlainText()
        coin_name = self.bip44_page.coin_list.selectedItems()[0].text()
        coin = self.coin_record[coin_name]
        account = Account(name=acc_name, coin=coin, index=self.account_counter)
        self.account_record[account.name] = account
        self.coin_record[coin_name].accounts[acc_name] = account
        self.account_counter = len(self.account_record.values())
        self.bip44_page.acc_list.addItem(account.name)

    def add_addr(self):
        acc_name = self.bip44_page.acc_list.selectedItems()[0].text()
        account = self.account_record[acc_name]
        addr = ExternalAddress(account=account, index=self.ext_addr_counter)
        self.ext_addr_record.append(addr)
        self.account_record[acc_name].external_addr.append(addr)
        self.ext_addr_counter = len(self.ext_addr_record)
        self.bip44_page.addr_list.addItem(addr.addr)

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
        self.bip44_page.addr_add_btn.setDisabled(False)

    def activate_addr(self):
        self.bip44_page.addr_rm_btn.setDisabled(False)

    def rm_acc(self):
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
