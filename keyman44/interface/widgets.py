from PyQt5.QtWidgets import QTreeWidgetItem
from pycoin.key.BIP32Node import BIP32Node

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
        self.n_accounts = 0

    def set_balance(self, amount):
        self.balance = amount

    def add(self, acc_name, acc):
        self.accounts[acc_name] = acc
        self.n_accounts = len(self.accounts.values())

    def remove(self, acc_name):
        del self.accounts[acc_name]
        self.n_accounts = len(self.accounts.values())

    def __repr__(self):
        return self.name

class Account(object):
    def __init__(self, name, coin):
        self.name = name
        self.balance = 0
        self.node = coin.node.subkey(i=coin.n_accounts, is_hardened=True,
                as_private=True)
        self.external = self.node.subkey(i=0, as_private=False,
                is_hardened=False)
        self.internal = self.node.subkey(i=1, as_private=False,
                is_hardened=False)
        self.external_addr = []
        self.internal_addr = []
        self.n_internal = 0
        self.n_external = 0

    def add(self, addr, external=True):
        if external:
            self.external_addr.append(addr)
        else:
            self.internal_addr.append(addr)
        self.n_internal = len(self.internal_addr)
        self.n_external = len(self.external_addr)

    def remove(self, addr, external=True):
        if external:
            self.external_addr.remove(addr)
        else:
            self.internal_addr.remove(addr)
        self.n_internal = len(self.internal_addr)
        self.n_external = len(self.external_addr)

    def set_balance(self, amount):
        self.balance = amount

class ChangeAddress(object):
    def __init__(self, account):
        self.pubkey = account.internal.subkey(i=account.n_internal, as_private=False,
                is_hardened=False)
        self.addr = self.pubkey.address(use_uncompressed=False)
        self.balance = 0

class ExternalAddress(object):
    def __init__(self, account):
        self.pubkey = account.external.subkey(i=account.n_external, as_private=False,
                is_hardened=False)
        self.addr = self.pubkey.address(use_uncompressed=False)
        self.balance = 0
