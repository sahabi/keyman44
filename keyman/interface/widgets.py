from PyQt5.QtWidgets import QTreeWidgetItem

class KeyTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, key_type, level):
        self.key_type = key_type
        self.level = level
        entry = [self.key_type, self.level]
        QTreeWidgetItem.__init__(self, entry)
