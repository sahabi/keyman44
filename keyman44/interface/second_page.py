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
        self.close_button.setGeometry(QtCore.QRect(760, 521, 91, 31))
        self.close_button.setOrientation(QtCore.Qt.Horizontal)
        self.close_button.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.close_button.setObjectName("close_button")
        self.treeWidget = QtWidgets.QTreeWidget(second)
        self.treeWidget.setGeometry(QtCore.QRect(50, 20, 791, 341))
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.treeWidget.headerItem().setFont(0, font)
        self.pushButton = QtWidgets.QPushButton(second)
        self.pushButton.setGeometry(QtCore.QRect(30, 520, 91, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(second)
        self.close_button.accepted.connect(second.accept)
        self.close_button.rejected.connect(second.reject)
        QtCore.QMetaObject.connectSlotsByName(second)

    def retranslateUi(self, second):
        _translate = QtCore.QCoreApplication.translate
        second.setWindowTitle(_translate("second", "Keyman"))
        self.treeWidget.headerItem().setText(0, _translate("second", "Keys"))
        self.treeWidget.headerItem().setText(1, _translate("second", "Level"))
        self.treeWidget.headerItem().setText(2, _translate("second", "WIF-compressed"))
        self.treeWidget.headerItem().setText(3, _translate("second", "SEC-compressed"))
        self.treeWidget.headerItem().setText(4, _translate("second", "Address"))
        self.pushButton.setText(_translate("second", "Export"))

