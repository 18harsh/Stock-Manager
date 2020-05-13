# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateProduct.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PIL import Image
import style
import os

con = sqlite3.connect("products.db")
cur = con.cursor()

class UpdateProduct(object):
    def setupUi(self, MainWindow,productid):
        self.productdetails(productid)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.updateproductlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.updateproductlabel.setFont(font)
        self.updateproductlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.updateproductlabel.setObjectName("updateproductlabel")
        self.verticalLayout.addWidget(self.updateproductlabel)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/{}".format(self.product_img)))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        # self.verticalLayout.setStyleSheet(style.producttopFrame())
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setObjectName("namelabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.namelabel)
        self.manufacturerlabel = QtWidgets.QLabel(self.centralwidget)
        self.manufacturerlabel.setObjectName("manufacturerlabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.manufacturerlabel)
        self.pricelabel = QtWidgets.QLabel(self.centralwidget)
        self.pricelabel.setObjectName("pricelabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pricelabel)
        self.quotalabel = QtWidgets.QLabel(self.centralwidget)
        self.quotalabel.setObjectName("quotalabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.quotalabel)
        self.statuslabel = QtWidgets.QLabel(self.centralwidget)
        self.statuslabel.setObjectName("statuslabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.statuslabel)
        self.nameentry = QtWidgets.QLineEdit(self.centralwidget)
        self.nameentry.setObjectName("nameentry")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameentry)
        self.manufacturerentry = QtWidgets.QLineEdit(self.centralwidget)
        self.manufacturerentry.setObjectName("manufacturerentry")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.manufacturerentry)
        self.priceentry = QtWidgets.QLineEdit(self.centralwidget)
        self.priceentry.setObjectName("priceentry")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.priceentry)
        self.quotaentry = QtWidgets.QLineEdit(self.centralwidget)
        self.quotaentry.setObjectName("quotaentry")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.quotaentry)
        self.uploadbutton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadbutton.setObjectName("uploadbutton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.uploadbutton)
        self.imagelabel = QtWidgets.QLabel(self.centralwidget)
        self.imagelabel.setObjectName("imagelabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.imagelabel)
        self.deletebutton = QtWidgets.QPushButton(self.centralwidget)
        self.deletebutton.setObjectName("deletebutton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.deletebutton)
        self.updatebutton = QtWidgets.QPushButton(self.centralwidget)
        self.updatebutton.setObjectName("updatebutton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.updatebutton)
        self.statusbutton = QtWidgets.QComboBox(self.centralwidget)
        self.statusbutton.setObjectName("statusbutton")
        self.statusbutton.addItem("")
        self.statusbutton.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.statusbutton)
        self.verticalLayout_2.addLayout(self.formLayout)
        # self.formLayout.setStyleSheet(style.productbottomFrame())
        MainWindow.setCentralWidget(self.centralwidget)

        self.uploadbutton.clicked.connect(lambda:(self.uploadImg(MainWindow)))
        self.deletebutton.clicked.connect(lambda:(self.deleteproduct(MainWindow)))
        self.updatebutton.clicked.connect(lambda:(self.updateproduct(MainWindow)))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.updateproductlabel.setText(_translate("MainWindow", "Update Product"))
        self.namelabel.setText(_translate("MainWindow", "Name:"))
        self.manufacturerlabel.setText(_translate("MainWindow", "Manufacturer:"))
        self.pricelabel.setText(_translate("MainWindow", "Price:"))
        self.quotalabel.setText(_translate("MainWindow", "Quota:"))
        self.statuslabel.setText(_translate("MainWindow", "Status:"))
        self.nameentry.setText(_translate("MainWindow", self.product_name))
        self.manufacturerentry.setText(_translate("MainWindow", self.product_manufacturer))
        self.priceentry.setText(_translate("MainWindow", str(self.product_price)))
        self.quotaentry.setText(_translate("MainWindow", str(self.product_quota)))
        self.defaultimg = self.product_img
        self.uploadbutton.setText(_translate("MainWindow", "Upload"))
        self.imagelabel.setText(_translate("MainWindow", "Image:"))
        self.deletebutton.setText(_translate("MainWindow", "Delete"))
        self.updatebutton.setText(_translate("MainWindow", "Update"))
        self.statusbutton.setItemText(0, _translate("MainWindow", "Available"))
        self.statusbutton.setItemText(1, _translate("MainWindow", "Unavailable"))
        index = self.statusbutton.findText(self.product_status,QtCore.Qt.MatchFixedString)
        self.statusbutton.setCurrentIndex(index)

    def uploadImg(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        size = (256,256)
        self.filename,ok = QFileDialog.getOpenFileName(MainWindow,"Upload Image","","Image Files(*.jpg *.png)")
        if ok:
            self.defaultimg = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save("img\\{0}".format(self.defaultimg))
            self.uploadbutton.setText(_translate("MainWindow", self.defaultimg))
        else:    
            self.defaultimg = self.product[5]
            self.uploadbutton.setText(_translate("MainWindow", "Upload"))    

    def productdetails(self,productid):
        query = ("SELECT * FROM products WHERE product_id=?")
        self.product = cur.execute(query,(productid,)).fetchone()
        self.product_id = self.product[0]
        self.product_name = self.product[1]
        self.product_manufacturer = self.product[2]
        self.product_price = self.product[3]
        self.product_quota = self.product[4]
        self.product_img = self.product[5]
        self.product_status = self.product[6]

    def deleteproduct(self,MainWindow):
        mbox = QMessageBox.warning(MainWindow,"Warning","Are you sure, you want to delete?",QMessageBox.Yes|QMessageBox.No)
        if mbox  == QMessageBox.Yes:
            try:    
                cur.execute("DELETE FROM products WHERE product_id=?",(self.product_id,))
                con.commit()
                QMessageBox.information(MainWindow,"Success","Product Deleted!")
                MainWindow.close()
            except:
                QMessageBox.critical(MainWindow,"Failed","Technical error")


    def updateproduct(self,MainWindow):
        name = self.nameentry.text()
        manufacturer = self.manufacturerentry.text()
        price = self.priceentry.text()
        quota = self.quotaentry.text()
        status = self.statusbutton.currentText()
        img = self.defaultimg
        id = self.product_id
        if (name and manufacturer and price and quota!=""):    
            try:
                query = "UPDATE products SET product_name=?,product_manufacturer=?,product_price=?,product_quota=?,product_img=?,product_availability=? WHERE product_id=?"
                cur.execute(query,(name,manufacturer,price,quota,img,status,id))
                con.commit()
                QMessageBox.information(MainWindow,"Success","Product Updated Successfully")
                MainWindow.close()
            except:  
                QMessageBox.critical(MainWindow,"Failed","Technical error")      
        else:
             QMessageBox.information(MainWindow,"Warning","Fill all field")