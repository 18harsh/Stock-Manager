# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sellproduct.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QTableWidgetItem,QAbstractItemView,QHeaderView
import sqlite3
from productsold import *

con = sqlite3.connect("products.db")
cur = con.cursor()


class SellProduct(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/sell.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.topmainLayout = QtWidgets.QVBoxLayout()
        self.topmainLayout.setObjectName("topmainLayout")
        self.sellproductlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sellproductlabel.setFont(font)
        self.sellproductlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sellproductlabel.setObjectName("sellproductlabel")
        self.topmainLayout.addWidget(self.sellproductlabel)
        self.sellimg = QtWidgets.QLabel(self.centralwidget)
        self.sellimg.setText("")
        self.sellimg.setPixmap(QtGui.QPixmap("icons/shop.png"))
        self.sellimg.setAlignment(QtCore.Qt.AlignCenter)
        self.sellimg.setObjectName("sellimg")
        self.topmainLayout.addWidget(self.sellimg)
        self.mainLayout.addLayout(self.topmainLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 50, -1, 0)
        self.formLayout.setObjectName("formLayout")
        self.productlabel = QtWidgets.QLabel(self.centralwidget)
        self.productlabel.setObjectName("productlabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.productlabel)
        self.memberlabel = QtWidgets.QLabel(self.centralwidget)
        self.memberlabel.setObjectName("memberlabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.memberlabel)
        self.membercombo = QtWidgets.QComboBox(self.centralwidget)
        self.membercombo.setObjectName("membercombo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.membercombo)
        self.quantitylabel = QtWidgets.QLabel(self.centralwidget)
        self.quantitylabel.setObjectName("quantitylabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.quantitylabel)
        self.quantitycombo = QtWidgets.QComboBox(self.centralwidget)
        self.quantitycombo.setObjectName("quantitycombo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.quantitycombo)
        self._label = QtWidgets.QLabel(self.centralwidget)
        self._label.setText("")
        self._label.setObjectName("_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self._label)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setObjectName("submitButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.submitButton)
        self.productcombo = QtWidgets.QComboBox(self.centralwidget)
        self.productcombo.setObjectName("productcombo")
        self.productcombo.currentIndexChanged.connect(self.changeComboValue)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.productcombo)
        self.mainLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.submitButton.clicked.connect(lambda:(self.submit(MainWindow)))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sell Product"))
        self.sellproductlabel.setText(_translate("MainWindow", "Sell Products"))
        self.productlabel.setText(_translate("MainWindow", "Product:"))
        self.memberlabel.setText(_translate("MainWindow", "Member:"))
        self.quantitylabel.setText(_translate("MainWindow", "Quantity:"))
        self.submitButton.setText(_translate("MainWindow", "Sumbit"))

        query1 = ("SELECT * FROM products WHERE product_availability = ?")
        products = cur.execute(query1,('Available',)).fetchall()

        query2 = ("SELECT member_id, member_name FROM members")
        members = cur.execute(query2).fetchall()

        quantity = products[0][4]
        for product in products:
            self.productcombo.addItem(product[1],product[0])
        for member in members:
            self.membercombo.addItem(member[1],member[0])
 
        for i in range(1,quantity+1):
            self.quantitycombo.addItem(str(i))

    def changeComboValue(self):
        self.quantitycombo.clear()
        product_id = self.productcombo.currentData()
        query = ("SELECT product_quota FROM products WHERE product_id=?")
        quota = cur.execute(query,(product_id,)).fetchone()      
        for i in range(1,quota[0]+1):
            self.quantitycombo.addItem(str(i))

    def submit(self,MainWindow):
        productName = self.productcombo.currentText()
        productId = self.productcombo.currentData()

        memberName = self.membercombo.currentText()
        memberId = self.membercombo.currentData()

        quantity = int(self.quantitycombo.currentText())

        confirmlist = [productName,productId,memberName,memberId,quantity]
        
        MainWindow.close()
        self.productsoldwindow = QtWidgets.QMainWindow()
        self.productsoldUI = ProductSold()
        self.productsoldUI.setupUi(self.productsoldwindow,confirmlist)
        self.productsoldwindow.show()



