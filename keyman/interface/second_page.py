# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_page.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_second(object):
    def setupUi(self, second):
        second.setObjectName("second")
        second.resize(887, 567)
        second.setBaseSize(QtCore.QSize(0, 0))
        second.setSizeGripEnabled(False)
        self.close_button = QtWidgets.QDialogButtonBox(second)
        self.close_button.setGeometry(QtCore.QRect(470, 520, 381, 32))
        self.close_button.setOrientation(QtCore.Qt.Horizontal)
        self.close_button.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.close_button.setObjectName("close_button")
        self.gen_pubsubkey_button = QtWidgets.QPushButton(second)
        self.gen_pubsubkey_button.setGeometry(QtCore.QRect(230, 380, 181, 23))
        self.gen_pubsubkey_button.setMouseTracking(True)
        self.gen_pubsubkey_button.setObjectName("gen_pubsubkey_button")
        self.gen_privsubkey = QtWidgets.QPushButton(second)
        self.gen_privsubkey.setGeometry(QtCore.QRect(40, 380, 171, 23))
        self.gen_privsubkey.setMouseTracking(True)
        self.gen_privsubkey.setObjectName("gen_privsubkey")
        self.treeWidget = QtWidgets.QTreeWidget(second)
        self.treeWidget.setGeometry(QtCore.QRect(50, 20, 791, 341))
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.treeWidget.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.gen_pubsubkey_button_2 = QtWidgets.QPushButton(second)
        self.gen_pubsubkey_button_2.setGeometry(QtCore.QRect(430, 380, 121, 23))
        self.gen_pubsubkey_button_2.setMouseTracking(True)
        self.gen_pubsubkey_button_2.setObjectName("gen_pubsubkey_button_2")
        self.gen_pubsubkey_button_3 = QtWidgets.QPushButton(second)
        self.gen_pubsubkey_button_3.setGeometry(QtCore.QRect(580, 380, 91, 23))
        self.gen_pubsubkey_button_3.setMouseTracking(True)
        self.gen_pubsubkey_button_3.setObjectName("gen_pubsubkey_button_3")

        self.retranslateUi(second)
        self.close_button.accepted.connect(second.accept)
        self.close_button.rejected.connect(second.reject)
        QtCore.QMetaObject.connectSlotsByName(second)

    def retranslateUi(self, second):
        _translate = QtCore.QCoreApplication.translate
        second.setWindowTitle(_translate("second", "Keyman"))
        self.gen_pubsubkey_button.setText(_translate("second", "Generate PubSubKey"))
        self.gen_privsubkey.setText(_translate("second", "Generate PrivSubKey"))
        self.treeWidget.headerItem().setText(0, _translate("second", "Tree"))
        self.treeWidget.headerItem().setText(1, _translate("second", "Public Key"))
        self.treeWidget.headerItem().setText(2, _translate("second", "Private Key"))
        self.treeWidget.headerItem().setText(3, _translate("second", "Address"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("second", "Seed"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("second", "Master Key"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("second", "Level 1 Key 0"))
        self.treeWidget.topLevelItem(0).child(0).child(0).child(0).setText(0, _translate("second", "Level 2 Key 0"))
        self.treeWidget.topLevelItem(0).child(0).child(1).setText(0, _translate("second", "Level 1 Key 1"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.gen_pubsubkey_button_2.setText(_translate("second", "Create Child"))
        self.gen_pubsubkey_button_3.setText(_translate("second", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    second = QtWidgets.QDialog()
    ui = Ui_second()
    ui.setupUi(second)
    second.show()
    sys.exit(app.exec_())

