# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productsold.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

con = sqlite3.connect("products.db")
cur = con.cursor()


class ProductSold(object):
    def setupUi(self, MainWindow,confirmlist):
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
        font = QtGui.QFont()
        font.setPointSize(14)
        self.productlabel.setFont(font)
        self.productlabel.setObjectName("productlabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.productlabel)
        self.memberlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.memberlabel.setFont(font)
        self.memberlabel.setObjectName("memberlabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.memberlabel)
        self.amountlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.amountlabel.setFont(font)
        self.amountlabel.setObjectName("amountlabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.amountlabel)
        self._label = QtWidgets.QLabel(self.centralwidget)
        self._label.setText("")
        self._label.setObjectName("_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self._label)
        self.prodlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.prodlabel.setFont(font)
        self.prodlabel.setObjectName("prodlabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.prodlabel)
        self.memlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.memlabel.setFont(font)
        self.memlabel.setObjectName("memlabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.memlabel)
        self.amtlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.amtlabel.setFont(font)
        self.amtlabel.setObjectName("amtlabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.amtlabel)
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.confirmButton.setFont(font)
        self.confirmButton.setStyleSheet("background-color:green")
        self.confirmButton.setObjectName("confirmButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.confirmButton)
        self._label_2 = QtWidgets.QLabel(self.centralwidget)
        self._label_2.setText("")
        self._label_2.setObjectName("_label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self._label_2)
        self.mainLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.confirmButton.clicked.connect(lambda:(self.confirm(MainWindow,confirmlist)))

        self.retranslateUi(MainWindow,confirmlist)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow,confirmlist):
        global total
        _translate = QtCore.QCoreApplication.translate

        query = ("SELECT product_price FROM products WHERE product_id=?")
        price = cur.execute(query,(confirmlist[1],)).fetchone()  
        total = price[0]* int(confirmlist[4])

        MainWindow.setWindowTitle(_translate("MainWindow", "Product Sold"))
        self.sellproductlabel.setText(_translate("MainWindow", "Product Sold"))
        self.productlabel.setText(_translate("MainWindow", "Product:"))
        self.memberlabel.setText(_translate("MainWindow", "Member:"))
        self.amountlabel.setText(_translate("MainWindow", "Amount:"))
        self.prodlabel.setText(_translate("MainWindow", confirmlist[0]))
        self.memlabel.setText(_translate("MainWindow", confirmlist[2]))
        self.amtlabel.setText(_translate("MainWindow", str(price[0]) +" x "+str(confirmlist[4])+" = "+str(total)))
        self.confirmButton.setText(_translate("MainWindow", "Confirm"))


    def confirm(self,MainWindow,confirmlist):
        global total
        try:
            sellQuery = ("INSERT INTO 'sellings' (selling_product_id,selling_member_id,selling_quantity,selling_amount) VALUES (?,?,?,?)")
            cur.execute(sellQuery,(confirmlist[1],confirmlist[3],confirmlist[4],total))
            con.commit()
            quotaquery = ("SELECT product_quota FROM products WHERE product_id=?")
            quota = cur.execute(quotaquery,(confirmlist[1],)).fetchone()      

            if quota[0] == confirmlist[4]:
                query = "UPDATE products SET product_quota=?,product_availability=? WHERE product_id=?"
                cur.execute(query,(0,"Unavailable",confirmlist[1]))
                con.commit()
                QMessageBox.information(MainWindow,"Success","Product has been sold!")
            elif quota[0] > confirmlist[4]:
                query = "UPDATE products SET product_quota=? WHERE product_id=?"
                cur.execute(query,((quota[0]-confirmlist[4]),confirmlist[1]))
                con.commit()
                QMessageBox.information(MainWindow,"Success","Product has been sold!")
            else:    
                QMessageBox.critical(MainWindow,"Failed","low inventory quantity") 

            MainWindow.close()
        except:
            QMessageBox.critical(MainWindow,"Failed","Technical error")  
            



