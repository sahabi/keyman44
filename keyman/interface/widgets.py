from PyQt5.QtWidgets import QTreeWidgetItem

class KeyTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, key_type, level, key, wif='-', sec='-', address='-'):
        self.key_type = key_type
        self.level = level
        self.key = key
        self.wif = wif
        self.sec = sec
        self.address = address
        entry = [self.key_type, self.level, self.wif, self.sec, self.address]
        QTreeWidgetItem.__init__(self, entry)

class PrivKeyTreeWidgetItem(KeyTreeWidgetItem):
    def __init__(self, key_type, level, key, wif, sec='-', address='-'):
        KeyTreeWidgetItem.__init__(self, key_type, level, key, wif, sec,
                address)

class PubKeyTreeWidgetItem(KeyTreeWidgetItem):
    def __init__(self, key_type, level, key, sec, address, wif='-'):
        KeyTreeWidgetItem.__init__(self, key_type, level, key, wif, sec,
                address)

