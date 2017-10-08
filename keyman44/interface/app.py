# -*- coding: utf-8 -*-
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from pycoin.cmds.ku import get_entropy
from pycoin.networks.default import get_current_netcode
import sys
from PyQt5.QtWidgets import QTreeWidgetItem
from .widgets import MasterKey, Coin, Account, ExternalAddress
import bip44_page
import send_page
import rcv_page
import coin_selection
import account_creation
import mk_page
from mnemonic import Mnemonic

#words = 'abandon ability able about above absent absorb abstract absurd abuse access accident account accuse achieve acid acoustic acquire across act action actor actress actual'

#node = BIP32Node.from_master_secret(Mnemonic.to_seed(words), 'BTC')


class App(object):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.mk_record = {}
        self.init_bip44_page()
        self.init_mk_page()
        self.init_coin_page()
        self.init_acc_page()
        self.init_send_page()
        self.init_rcv_page()
        self.bip44_dialog.show()

    def init_bip44_page(self):
        self.bip44_dialog = QtWidgets.QDialog()
        self.bip44_page = bip44_page.Ui_Dialog()
        self.bip44_page.setupUi(self.bip44_dialog)
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
        self.bip44_page.close_btn.clicked.connect(self.bip44_dialog.reject)
        self.init_bip44_wallet_context()
        self.init_bip44_buttons()

    def init_bip44_wallet_context(self):
        self.bip44_page.coin_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        coin_wallet_context_menu = partial(self.wallet_context_menu,
                widget=self.bip44_page.coin_list)
        self.bip44_page.coin_list.customContextMenuRequested.connect(coin_wallet_context_menu)
        acc_wallet_context_menu = partial(self.wallet_context_menu,
                widget=self.bip44_page.acc_list)
        self.bip44_page.acc_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.bip44_page.acc_list.customContextMenuRequested.connect(acc_wallet_context_menu)
        addr_wallet_context_menu = partial(self.wallet_context_menu,
                widget=self.bip44_page.addr_list)
        self.bip44_page.addr_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.bip44_page.addr_list.customContextMenuRequested.connect(addr_wallet_context_menu)
        self.popMenu = QtWidgets.QMenu(self.bip44_dialog)
        send = QtWidgets.QAction('Send', self.bip44_dialog)
        send.triggered.connect(self.show_send)
        rcv = QtWidgets.QAction('Receive', self.bip44_dialog)
        rcv.triggered.connect(self.show_rcv)
        history = QtWidgets.QAction('History', self.bip44_dialog)
        history.triggered.connect(self.show_history)
        self.popMenu.addAction(send)
        self.popMenu.addAction(rcv)
        self.popMenu.addAction(history)

    def wallet_context_menu(self, point, widget):
        # show context menu
        self.popMenu.exec_(widget.mapToGlobal(point))

    def test(self):
        print('im triggered')

    def show_send(self):
        self.send_dialog.exec_()

    def show_rcv(self):
        self.rcv_dialog.exec_()

    def show_history(self):
        pass

    def init_bip44_buttons(self):
        self.bip44_page.coin_add_btn.setDisabled(True)
        self.bip44_page.coin_rm_btn.setDisabled(True)
        self.bip44_page.acc_add_btn.setDisabled(True)
        self.bip44_page.acc_rm_btn.setDisabled(True)
        self.bip44_page.addr_add_btn.setDisabled(True)
        self.bip44_page.addr_rm_btn.setDisabled(True)
        self.bip44_page.mk_add_btn.setDisabled(False)
        self.bip44_page.mk_rm_btn.setDisabled(True)

    def init_mk_page(self):
        self.mk_dialog = QtWidgets.QDialog()
        self.mk_page = mk_page.Ui_Dialog()
        self.mk_page.setupUi(self.mk_dialog)
        self.mk_page.gen_mnem.clicked.connect(self.gen_mnem)

    def init_coin_page(self):
        self.coin_dialog = QtWidgets.QDialog()
        self.coin_page = coin_selection.Ui_Dialog()
        self.coin_page.setupUi(self.coin_dialog)
        self.currency_list = ['', 'BTC', 'XTN']
        self.coin_page.comboBox.addItems(self.currency_list)

    def init_acc_page(self):
        self.acc_dialog = QtWidgets.QDialog()
        self.acc_page = account_creation.Ui_Dialog()
        self.acc_page.setupUi(self.acc_dialog)

    def init_send_page(self):
        self.send_dialog = QtWidgets.QDialog()
        self.send_page = send_page.Ui_Dialog()
        self.send_page.setupUi(self.send_dialog)


    def init_rcv_page(self):
        self.rcv_dialog = QtWidgets.QDialog()
        self.rcv_page = rcv_page.Ui_Dialog()
        self.rcv_page.setupUi(self.rcv_dialog)

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

    def add_coin(self, purpose=44):
        self.coin_page.comboBox.clear()
        current_list = set([self.bip44_page.coin_list.item(i).text() for i in
                range(self.bip44_page.coin_list.count())])
        remaining_coins = set(self.currency_list) - set(current_list)
        print current_list, remaining_coins
        self.coin_page.comboBox.addItems(list(remaining_coins))
        self.coin_dialog.exec_()
        mk_name = self.bip44_page.mk_list.selectedItems()[0].text()
        coin_name = self.coin_page.comboBox.currentText()
        if coin_name == 'BTC':
            network = 0
        elif coin_name == 'XTN':
            network = 1
        else:
            return
        coin = Coin(name=coin_name, mk=self.mk_record[mk_name], network=network)
        self.mk_record[mk_name].coins[coin.name] = coin
        if coin != '':
            self.bip44_page.coin_list.addItem(coin.name)
            self.coin_page.comboBox.removeItem(
                    self.coin_page.comboBox.currentIndex())

    def add_acc(self):
        self.acc_dialog.exec_()
        acc_name = self.acc_page.acc_name.toPlainText()
        coin_name = self.bip44_page.coin_list.selectedItems()[0].text()
        mk_name = self.bip44_page.mk_list.selectedItems()[0].text()
        coin = self.mk_record[mk_name].coins[coin_name]
        account = Account(name=acc_name, coin=coin)
        coin.add(acc_name, account)
        self.bip44_page.acc_list.addItem(account.name)

    def add_addr(self):
        acc_name = self.bip44_page.acc_list.selectedItems()[0].text()
        coin_name = self.bip44_page.coin_list.selectedItems()[0].text()
        mk_name = self.bip44_page.mk_list.selectedItems()[0].text()
        account = self.mk_record[mk_name].coins[coin_name].accounts[acc_name]
        addr = ExternalAddress(account=account)
        account.add(addr)
        self.bip44_page.addr_list.addItem(addr.addr)

    def rm_mk(self):
        selection = self.bip44_page.mk_list.currentIndex()
        self.bip44_page.mk_rm_btn.setDisabled(True)
        self.bip44_page.mk_list.takeItem(selection.row())

    def rm_coin(self):
        selection = self.bip44_page.coin_list.currentIndex()
        self.coin_page.comboBox.addItem(self.bip44_page.coin_list.currentItem().text())
        self.bip44_page.coin_rm_btn.setDisabled(True)
        self.bip44_page.coin_list.takeItem(selection.row())

    def rm_acc(self):
        pass

    def rm_addr(self):
        pass

    def activate_mk(self):
        mk_name = self.bip44_page.mk_list.selectedItems()[0].text()
        self.bip44_page.coin_add_btn.setDisabled(False)
        self.bip44_page.mk_rm_btn.setDisabled(False)
        coins = self.mk_record[mk_name].coins.keys()
        self.bip44_page.coin_list.clear()
        self.bip44_page.acc_list.clear()
        self.bip44_page.addr_list.clear()
        self.bip44_page.coin_list.addItems(coins)

    def activate_coin(self):
        mk_name = self.bip44_page.mk_list.selectedItems()[0].text()
        coin_name = self.bip44_page.coin_list.selectedItems()[0].text()
        self.bip44_page.coin_rm_btn.setDisabled(False)
        self.bip44_page.acc_add_btn.setDisabled(False)
        accounts = self.mk_record[mk_name].coins[coin_name].accounts.keys()
        self.bip44_page.acc_list.clear()
        self.bip44_page.addr_list.clear()
        self.bip44_page.acc_list.addItems(accounts)

    def activate_acc(self):
        mk_name = self.bip44_page.mk_list.selectedItems()[0].text()
        coin_name = self.bip44_page.coin_list.selectedItems()[0].text()
        acc_name = self.bip44_page.acc_list.selectedItems()[0].text()
        self.bip44_page.acc_rm_btn.setDisabled(False)
        self.bip44_page.addr_add_btn.setDisabled(False)
        addresses =\
        self.mk_record[mk_name].coins[coin_name].accounts[acc_name].external_addr
        self.bip44_page.addr_list.clear()
        self.bip44_page.addr_list.addItems([addr.addr for addr in addresses])

        self.bip44_page.addr_add_btn.setDisabled(False)

    def activate_addr(self):
        self.bip44_page.addr_rm_btn.setDisabled(False)

    def gen_seed(self):
        self.chain_code, self.secret_exponent = get_chain_secret_pair()
        self.ui.secret_exponent.setText(self.secret_exponent)
        self.ui.chain_code.setText(self.chain_code)

    def gen_mnem(self):
        mnem = Mnemonic('english')
        words = mnem.generate()
        self.mk_page.mnem.setText(words)

    def detect_text(self, text):
        if len(text) > 0:
            self.ui.next_button.setEnabled(True)
        else:
            self.ui.next_button.setEnabled(False)

app = App()
app.run()
