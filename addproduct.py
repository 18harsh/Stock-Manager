# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addproduct.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox,QTableWidgetItem
import sqlite3
from PIL import Image
import os

con = sqlite3.connect("products.db")
cur = con.cursor()

defaultimg="store.png"

class AddProduct(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.topLayout = QtWidgets.QHBoxLayout()
        self.topLayout.setObjectName("topLayout")
        self.addproductimg = QtWidgets.QLabel(self.centralwidget)
        self.addproductimg.setText("")
        self.addproductimg.setPixmap(QtGui.QPixmap("icons/addproduct.png"))
        self.addproductimg.setObjectName("addproductimg")
        self.topLayout.addWidget(self.addproductimg)
        self.imgtexttitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.imgtexttitle.setFont(font)
        self.imgtexttitle.setObjectName("imgtexttitle")
        self.topLayout.addWidget(self.imgtexttitle)
        self.mainLayout.addLayout(self.topLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameentry = QtWidgets.QLineEdit(self.centralwidget)
        self.nameentry.setObjectName("nameentry")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameentry)
        self.manufacturerlabel = QtWidgets.QLabel(self.centralwidget)
        self.manufacturerlabel.setObjectName("manufacturerlabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.manufacturerlabel)
        self.manufacturerentry = QtWidgets.QLineEdit(self.centralwidget)
        self.manufacturerentry.setObjectName("manufacturerentry")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.manufacturerentry)
        self.priceentry = QtWidgets.QLineEdit(self.centralwidget)
        self.priceentry.setObjectName("priceentry")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.priceentry)
        self.quotaentry = QtWidgets.QLineEdit(self.centralwidget)
        self.quotaentry.setObjectName("quotaentry")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.quotaentry)
        self.pricelabel = QtWidgets.QLabel(self.centralwidget)
        self.pricelabel.setObjectName("pricelabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pricelabel)
        self.quotalabel = QtWidgets.QLabel(self.centralwidget)
        self.quotalabel.setObjectName("quotalabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.quotalabel)
        self.uploadlabel = QtWidgets.QLabel(self.centralwidget)
        self.uploadlabel.setObjectName("uploadlabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.uploadlabel)
        self.uploadButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadButton.setObjectName("uploadButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.uploadButton)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setObjectName("submitButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.submitButton)
        self._label = QtWidgets.QLabel(self.centralwidget)
        self._label.setText("")
        self._label.setObjectName("_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self._label)
        self.mainLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.uploadButton.clicked.connect(lambda:(self.uploadImg(MainWindow)))
        self.submitButton.clicked.connect(lambda:(self.funcaddproduct(MainWindow)))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Products"))
        self.imgtexttitle.setText(_translate("MainWindow", "Add Product"))
        self.nameLabel.setText(_translate("MainWindow", "Name:"))
        self.nameentry.setPlaceholderText(_translate("MainWindow", "Enter name of product"))
        self.manufacturerlabel.setText(_translate("MainWindow", "Manufacturer:"))
        self.manufacturerentry.setPlaceholderText(_translate("MainWindow", "Enter name of manufacturer"))
        self.priceentry.setPlaceholderText(_translate("MainWindow", "Enter price of product"))
        self.quotaentry.setPlaceholderText(_translate("MainWindow", "Enter Quota of product"))
        self.pricelabel.setText(_translate("MainWindow", "Price:"))
        self.quotalabel.setText(_translate("MainWindow", "Quota:"))
        self.uploadlabel.setText(_translate("MainWindow", "Upload:"))
        self.uploadButton.setText(_translate("MainWindow", "Browse"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
    
    def uploadImg(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        global defaultimg
        size = (256,256)
        self.filename,ok = QFileDialog.getOpenFileName(MainWindow,"Upload Image","","Image Files(*.jpg *.png)")
        if ok:
            defaultimg = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save("img\\{0}".format(defaultimg))
            self.uploadButton.setText(_translate("MainWindow", defaultimg))
        else:    
            defaultimg = "store.png"
            self.uploadButton.setText(_translate("MainWindow", "Browse"))

    def funcaddproduct(self,MainWindow):        
        global defaultimg
        _translate = QtCore.QCoreApplication.translate
        name = self.nameentry.text()
        manufacturer = self.manufacturerentry.text()
        price = self.priceentry.text()
        quota = self.quotaentry.text()
        if (name and manufacturer and price and quota!=""):
            try:
                query = "INSERT INTO 'products' (product_name,product_manufacturer,product_price,product_quota,product_img) VAlUES(?,?,?,?,?)"
                cur.execute(query,(name,manufacturer,price,quota,defaultimg))
                con.commit()
                QMessageBox.information(MainWindow,"Success","Product has been added")
                self.nameentry.setText("")
                self.manufacturerentry.setText("")
                self.priceentry.setText("")
                self.quotaentry.setText("")
                defaultimg = "store.png"
                self.uploadButton.setText(_translate("MainWindow", "Browse"))
            except:
                QMessageBox.critical(MainWindow,"Failed","Technical error")  
        else:
            QMessageBox.information(MainWindow,"Warning","Fill all field")        

  
