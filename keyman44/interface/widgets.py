from PyQt5.QtWidgets import QTreeWidgetItem

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

