class KeyChain(object):
    def __init__(self, key_list=None):
        if key_list is None:
            self.key_list = []
        else:
            self.key_list = key_list
       # self.label = label

    def isSelected(self):
        for key in self.key_list:
            if key.isSelected():
                return True
        return False

    def which(self):
        for i, key in enumerate(self.key_list):
            if key.isSelected():
                return i
        return None

    def append(self, key):
        self.key_list.append(key)

    def get_selected_level(self):
        for key in self.key_list:
            if key.isSelected():
                return key.level

    def get_selected_key(self):
        return self.key_list[self.which()]

#    def derive_pubkey(self):

