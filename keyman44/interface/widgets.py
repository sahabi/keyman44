from PyQt5.QtWidgets import QTreeWidgetItem
from pycoin.key.BIP32Node import BIP32Node

class KeyTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, key_type, level, key):
        self.key_type = key_type
        self.level = level
        self.key = key
        self.wif = key.wif(use_uncompressed=False)
        self.sec = key.sec_as_hex(use_uncompressed=False)
        self.address = key.address(use_uncompressed=False)
        entry = [self.key_type, self.level, self.wif, self.sec, self.address]
        QTreeWidgetItem.__init__(self, entry)

class PrivKeyTreeWidgetItem(KeyTreeWidgetItem):
    def __init__(self, key_type, level, key):
        KeyTreeWidgetItem.__init__(self, key_type, level, key)

class PubKeyTreeWidgetItem(KeyTreeWidgetItem):
    def __init__(self, key_type, level, key):
        KeyTreeWidgetItem.__init__(self, key_type, level, key)

class MasterKey(object):
    def __init__(self, name, seed):
        self.name = name
        self.seed = seed
        self.coins = {}

class Coin(object):
    def __init__(self, name, mk, network):
        self.name = name
        self.node = BIP32Node.from_master_secret(mk.seed,
                name).subkey(i=network, is_hardened=True, as_private=True)
        self.balance = 0
        self.accounts = {}

    def set_balance(self, amount):
        self.balance = amount

    def __repr__(self):
        return self.name

class Account(object):
    def __init__(self, name, coin, index):
        self.name = name
        self.balance = 0
        self.node = coin.node.subkey(i=index, is_hardened=True,
                as_private=True)
        self.external = self.node.subkey(i=0, as_private=False,
                is_hardened=False)
        self.internal = self.node.subkey(i=1, as_private=False,
                is_hardened=False)
        self.external_addr = []
        self.internal_addr = []

    def set_balance(self, amount):
        self.balance = amount

class ChangeAddress(object):
    def __init__(self, account, index):
        self.pubkey = account.internal.subkey(i=index, as_private=False,
                is_hardened=False)
        self.addr = self.pubkey.address(use_uncompressed=False)
        self.balance = 0

class ExternalAddress(object):
    def __init__(self, account, index):
        self.pubkey = account.external.subkey(i=index, as_private=False,
                is_hardened=False)
        self.addr = self.pubkey.address(use_uncompressed=False)
