# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QTableWidgetItem,QAbstractItemView,QHeaderView
from PyQt5.QtGui import QFont
import sqlite3
from addproduct import *
from addmember import *
from updateProduct import *
from updateMember import *
from sellproduct import *
import style

con = sqlite3.connect("products.db")
cur = con.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/stock.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 1351, 651))
        self.tabs.setObjectName("tabs")
        self.tabs.blockSignals(True)
        self.tabs.currentChanged.connect(self.tabchanged)
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.mainLayout = QtWidgets.QHBoxLayout(self.tab1)
        self.mainLayout.setObjectName("mainLayout")
        self.leftmainLayout = QtWidgets.QVBoxLayout()
        self.leftmainLayout.setObjectName("leftmainLayout")
        self.producttable = QtWidgets.QTableWidget(self.tab1)
        self.producttable.setColumnCount(6)
        self.producttable.setObjectName("producttable")
        self.producttable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.producttable.setHorizontalHeaderItem(0, item)
        self.producttable.setColumnHidden(0,True)
        item = QtWidgets.QTableWidgetItem()
        self.producttable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.producttable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.producttable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.producttable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.producttable.setHorizontalHeaderItem(5, item)
        self.leftmainLayout.addWidget(self.producttable)
        self.mainLayout.addLayout(self.leftmainLayout,70)
        self.rightmainLayout = QtWidgets.QVBoxLayout()
        self.rightmainLayout.setObjectName("rightmainLayout")
        self.righttopmainLayout = QtWidgets.QHBoxLayout()
        self.righttopmainLayout.setObjectName("righttopmainLayout")
        self.topgroupBox = QtWidgets.QGroupBox(self.tab1)
        self.topgroupBox.setObjectName("topgroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.topgroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.righttoplayout = QtWidgets.QHBoxLayout()
        self.righttoplayout.setObjectName("righttoplayout")
        self.searchlabel = QtWidgets.QLabel(self.topgroupBox)
        self.searchlabel.setObjectName("searchlabel")
        self.righttoplayout.addWidget(self.searchlabel)
        self.searchedit = QtWidgets.QLineEdit(self.topgroupBox)
        self.searchedit.setObjectName("searchedit")
        self.righttoplayout.addWidget(self.searchedit)
        self.searchButton = QtWidgets.QPushButton(self.topgroupBox)
        self.searchButton.setObjectName("searchButton")
        self.righttoplayout.addWidget(self.searchButton)
        self.searchButton.setStyleSheet(style.searchButtonStyle())
        self.horizontalLayout_2.addLayout(self.righttoplayout)
        self.righttopmainLayout.addWidget(self.topgroupBox)
        self.rightmainLayout.addLayout(self.righttopmainLayout,20)
        self.topgroupBox.setStyleSheet(style.searchBoxStyle())
        self.rightmiddlemainLayout = QtWidgets.QHBoxLayout()
        self.rightmiddlemainLayout.setObjectName("rightmiddlemainLayout")
        self.middlegroupBox = QtWidgets.QGroupBox(self.tab1)
        self.middlegroupBox.setObjectName("middlegroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.middlegroupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rightmiddlelayout = QtWidgets.QHBoxLayout()
        self.rightmiddlelayout.setObjectName("rightmiddlelayout")
        self.allproductradioButton = QtWidgets.QRadioButton(self.middlegroupBox)
        self.allproductradioButton.setObjectName("allproductradioButton")
        self.rightmiddlelayout.addWidget(self.allproductradioButton)
        self.availaibleradioButton = QtWidgets.QRadioButton(self.middlegroupBox)
        self.availaibleradioButton.setObjectName("availaibleradioButton")
        self.rightmiddlelayout.addWidget(self.availaibleradioButton)
        self.unavailableradioButton = QtWidgets.QRadioButton(self.middlegroupBox)
        self.unavailableradioButton.setObjectName("unavailableradioButton")
        self.rightmiddlelayout.addWidget(self.unavailableradioButton)
        self.searchlist = QtWidgets.QPushButton(self.middlegroupBox)
        self.searchlist.setObjectName("searchlist")
        self.rightmiddlelayout.addWidget(self.searchlist)
        self.searchlist.setStyleSheet(style.listButtonStyle())
        self.horizontalLayout_3.addLayout(self.rightmiddlelayout)
        self.rightmiddlemainLayout.addWidget(self.middlegroupBox)
        self.rightmainLayout.addLayout(self.rightmiddlemainLayout,20)
        self.middlegroupBox.setStyleSheet(style.listBoxStyle())
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rightmainLayout.addLayout(self.horizontalLayout,60)
        self.mainLayout.addLayout(self.rightmainLayout,30)
        self.tabs.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.membermainLayout = QtWidgets.QHBoxLayout(self.tab2)
        self.membermainLayout.setObjectName("membermainLayout")
        self.membeleftmainLayout = QtWidgets.QHBoxLayout()
        self.membeleftmainLayout.setObjectName("membeleftmainLayout")
        self.membertable = QtWidgets.QTableWidget(self.tab2)
        self.membertable.setObjectName("membertable")
        self.membertable.setColumnCount(4)
        self.membertable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.membertable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.membertable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.membertable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.membertable.setHorizontalHeaderItem(3, item)
        self.membeleftmainLayout.addWidget(self.membertable)
        self.membermainLayout.addLayout(self.membeleftmainLayout,70)
        self.memberrightmainLayout = QtWidgets.QHBoxLayout()
        self.memberrightmainLayout.setObjectName("memberrightmainLayout")
        self.membergroupBox = QtWidgets.QGroupBox(self.tab2)
        self.membergroupBox.setObjectName("membergroupBox")
        self.memberrightgroupLayout = QtWidgets.QHBoxLayout(self.membergroupBox)
        self.memberrightgroupLayout.setObjectName("memberrightgroupLayout")
        self.memberightlayout = QtWidgets.QHBoxLayout()
        self.memberightlayout.setContentsMargins(10, 10, 10, 530)
        self.memberightlayout.setObjectName("memberightlayout")
        self.searchmemberlabel = QtWidgets.QLabel(self.membergroupBox)
        self.searchmemberlabel.setObjectName("searchmemberlabel")
        self.memberightlayout.addWidget(self.searchmemberlabel)
        self.searchmemberEdit = QtWidgets.QLineEdit(self.membergroupBox)
        self.searchmemberEdit.setObjectName("searchmemberEdit")
        self.memberightlayout.addWidget(self.searchmemberEdit)
        self.searchmemberButton = QtWidgets.QPushButton(self.membergroupBox)
        self.searchmemberButton.setObjectName("searchmemberButton")
        self.memberightlayout.addWidget(self.searchmemberButton)
        self.memberrightgroupLayout.addLayout(self.memberightlayout)
        self.memberrightmainLayout.addWidget(self.membergroupBox)
        self.membermainLayout.addLayout(self.memberrightmainLayout,30)
        self.tabs.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 357, 232))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.tproductslabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tproductslabel.setFont(font)
        self.tproductslabel.setObjectName("tproductslabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tproductslabel)
        self.totalproductlabel = QtWidgets.QLabel(self.groupBox)
        self.totalproductlabel.setObjectName("totalproductlabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.totalproductlabel)
        self.tmemberslabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tmemberslabel.setFont(font)
        self.tmemberslabel.setObjectName("tmemberslabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.tmemberslabel)
        self.totalmemberlabel = QtWidgets.QLabel(self.groupBox)
        self.totalmemberlabel.setObjectName("totalmemberlabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.totalmemberlabel)
        self.sproductlabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sproductlabel.setFont(font)
        self.sproductlabel.setObjectName("sproductlabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sproductlabel)
        self.soldproductlabel = QtWidgets.QLabel(self.groupBox)
        self.soldproductlabel.setObjectName("soldproductlabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.soldproductlabel)
        self.tamountlabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tamountlabel.setFont(font)
        self.tamountlabel.setObjectName("tamountlabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.tamountlabel)
        self.totalamountlabel = QtWidgets.QLabel(self.groupBox)
        self.totalamountlabel.setObjectName("totalamountlabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.totalamountlabel)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabs.addTab(self.tab3, "")
        self.tabs.blockSignals(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.AddProduct = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddProduct.setIcon(icon1)
        self.AddProduct.setObjectName("AddProduct")
        self.AddMember = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/addmember.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddMember.setIcon(icon2)
        self.AddMember.setObjectName("AddMember")
        self.SellProduct = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/sell.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SellProduct.setIcon(icon3)
        self.SellProduct.setObjectName("SellProduct")
        self.toolBar.addAction(self.AddProduct)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.AddMember)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.SellProduct)
        self.toolBar.addSeparator()
        self.producttable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.membertable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.displayProducts()
        self.producttable.doubleClicked.connect(self.selectedproduct)
        self.displaymembers()
        self.membertable.doubleClicked.connect(self.selectedmember)
        self.AddProduct.triggered.connect(self.functaddproduct)
        self.AddMember.triggered.connect(self.functaddmember)
        self.searchButton.clicked.connect(self.searchproducts)
        self.searchmemberButton.clicked.connect(self.searchmember)
        self.searchlist.clicked.connect(self.listsearchfunc)
        self.SellProduct.triggered.connect(self.funcsellproduct)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock Manager"))
        item = self.producttable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Id"))
        item = self.producttable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.producttable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Manufacturer"))
        item = self.producttable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.producttable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quota"))
        item = self.producttable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Availability"))
        self.producttable.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.producttable.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.topgroupBox.setTitle(_translate("MainWindow", "Search Box"))
        self.searchlabel.setText(_translate("MainWindow", "Search"))
        self.searchedit.setPlaceholderText(_translate("MainWindow", "Search For Products"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.middlegroupBox.setTitle(_translate("MainWindow", "List Box"))
        self.allproductradioButton.setText(_translate("MainWindow", "All Products"))
        self.allproductradioButton.setChecked(True)
        self.availaibleradioButton.setText(_translate("MainWindow", "Available"))
        self.unavailableradioButton.setText(_translate("MainWindow", "Unavailable"))
        self.searchlist.setText(_translate("MainWindow", "Search List"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab1), _translate("MainWindow", "Products"))
        item = self.membertable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Member ID"))
        item = self.membertable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Member Name"))
        item = self.membertable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Member Surname"))
        item = self.membertable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phone"))
        self.membertable.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.membertable.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.membergroupBox.setTitle(_translate("MainWindow", "Search For Members"))
        self.searchmemberlabel.setText(_translate("MainWindow", "Search Members"))
        self.searchmemberEdit.setPlaceholderText(_translate("MainWindow", "Search"))
        self.searchmemberButton.setText(_translate("MainWindow", "Search"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab2), _translate("MainWindow", "Members"))

        self.groupBox.setTitle(_translate("MainWindow", "Statistics"))
        self.tproductslabel.setText(_translate("MainWindow", "Total Products:"))
        self.tmemberslabel.setText(_translate("MainWindow", "Total Members:"))
        self.sproductlabel.setText(_translate("MainWindow", "Sold Products:"))
        self.tamountlabel.setText(_translate("MainWindow", "Total Amount:"))
        self.getstatistics()
        self.tabs.setTabText(self.tabs.indexOf(self.tab3), _translate("MainWindow", "Statistics"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.AddProduct.setText(_translate("MainWindow", "Add Product"))
        self.AddProduct.setToolTip(_translate("MainWindow", "Add Product"))
        self.AddMember.setText(_translate("MainWindow", "Add Member"))
        self.AddMember.setToolTip(_translate("MainWindow", "Add Member"))
        self.SellProduct.setText(_translate("MainWindow", "Sell Product"))
        self.SellProduct.setToolTip(_translate("MainWindow", "Sell Product"))

    def functaddproduct(self):
        self.productwindow = QtWidgets.QMainWindow()
        self.productUI = AddProduct()
        self.productUI.setupUi(self.productwindow)
        self.productwindow.show()
        self.displayProducts()

    def functaddmember(self):
        self.memberwindow = QtWidgets.QMainWindow()
        self.memberUI = AddMember()
        self.memberUI.setupUi(self.memberwindow)
        self.memberwindow.show()  
        self.displaymembers()

    def displayProducts(self):
        self.producttable.setFont(QFont("Times",12))
        for i in reversed(range(self.producttable.rowCount())):
            self.producttable.removeRow(i)

        query = cur.execute("SELECT product_id,product_name,product_manufacturer,product_price,product_quota,product_availability FROM products")
        for row_data in query:
            row_number = self.producttable.rowCount()
            self.producttable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.producttable.setItem(row_number,column_number,QTableWidgetItem(str(data)))          

    def displaymembers(self):
        self.membertable.setFont(QFont("Times",12))
        for i in reversed(range(self.membertable.rowCount())):
            self.membertable.removeRow(i)

        query = cur.execute("SELECT member_id,member_name,member_surname,member_phone FROM members")
        for row_data in query:
            row_number = self.membertable.rowCount()
            self.membertable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.membertable.setItem(row_number,column_number,QTableWidgetItem(str(data)))          

    def selectedproduct(self):
        global productId
        listProduct = []
        for i in range(0,6):
            listProduct.append(self.producttable.item(self.producttable.currentRow(),i).text())

        productId = listProduct[0] 
        self.updatewindow = QtWidgets.QMainWindow()
        self.updateUI = UpdateProduct()
        self.updateUI.setupUi(self.updatewindow,productId)
        self.updatewindow.show()
        self.displayProducts()

    def selectedmember(self):
        global memberId
        listMember = []
        for i in range(0,3):
            listMember.append(self.membertable.item(self.membertable.currentRow(),i).text())

        memberId = listMember[0] 
        self.updatememwindow = QtWidgets.QMainWindow()
        self.updatememUI = UpdateMember()
        self.updatememUI.setupUi(self.updatememwindow,memberId)
        self.updatememwindow.show()
        self.displaymembers()  

    def searchproducts(self):
        value = self.searchedit.text()
        if value == "":
             QMessageBox.information(MainWindow,"Warning","Fill all field")
        else:
            self.searchedit.setText("")
            query = ("SELECT product_id,product_name,product_manufacturer,product_price,product_quota,product_availability FROM products WHERE product_name LIKE ? or product_manufacturer LIKE ?")
            results = cur.execute(query,('%' + value + '%','%' + value +'%')).fetchall()
            if results == []:
                QMessageBox.information(MainWindow,"Search","No Result Found")
            else:
                self.producttable.setFont(QFont("Times",12))
                for i in reversed(range(self.producttable.rowCount())):
                    self.producttable.removeRow(i)
                for row_data in results:
                    row_number = self.producttable.rowCount()
                    self.producttable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.producttable.setItem(row_number,column_number,QTableWidgetItem(str(data)))          

    def searchmember(self):
        value = self.searchmemberEdit.text()
        if value == "":
             QMessageBox.information(MainWindow,"Warning","Fill all field")
        else:
            self.searchmemberEdit.setText("")
            query = ("SELECT member_id, member_name , member_surname, member_phone FROM members WHERE member_id LIKE ? or member_name LIKE ? or member_surname LIKE ? or member_phone LIKE ?")
            results = cur.execute(query,('%' + value + '%','%' + value +'%','%' + value +'%','%' + value +'%')).fetchall()
            if results == []:
                QMessageBox.information(MainWindow,"Search","No Result Found")
            else:
                self.membertable.setFont(QFont("Times",12))
                for i in reversed(range(self.membertable.rowCount())):
                    self.membertable.removeRow(i)
                for row_data in results:
                    row_number = self.membertable.rowCount()
                    self.membertable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.membertable.setItem(row_number,column_number,QTableWidgetItem(str(data)))           

    def listsearchfunc(self):
        if self.allproductradioButton.isChecked():
            self.displayProducts()
        elif self.availaibleradioButton.isChecked():
            query = ("SELECT product_id,product_name,product_manufacturer,product_price,product_quota,product_availability FROM products WHERE product_availability='Available'") 
            results = cur.execute(query).fetchall()
            if results == []:
                QMessageBox.information(MainWindow,"Search","No Result Found")
            else:
                self.producttable.setFont(QFont("Times",12))
                for i in reversed(range(self.producttable.rowCount())):
                    self.producttable.removeRow(i)
                for row_data in results:
                    row_number = self.producttable.rowCount()
                    self.producttable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.producttable.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        else:                 
            query = ("SELECT product_id,product_name,product_manufacturer,product_price,product_quota,product_availability FROM products WHERE product_availability='Unavailable'") 
            results = cur.execute(query).fetchall()
            if results == []:
                QMessageBox.information(MainWindow,"Search","No Result Found")
            else:
                self.producttable.setFont(QFont("Times",12))
                for i in reversed(range(self.producttable.rowCount())):
                    self.producttable.removeRow(i)
                for row_data in results:
                    row_number = self.producttable.rowCount()
                    self.producttable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.producttable.setItem(row_number,column_number,QTableWidgetItem(str(data))) 

    def funcsellproduct(self):
        self.sellproductwindow = QtWidgets.QMainWindow()
        self.sellproductUI = SellProduct()
        self.sellproductUI.setupUi(self.sellproductwindow)
        self.sellproductwindow.show()
                                   
    def getstatistics(self):
        _translate = QtCore.QCoreApplication.translate

        countproduct = cur.execute("SELECT count(product_id) FROM products").fetchall()                               
        countproduct = countproduct[0][0]

        countmember = cur.execute("SELECT count(member_id) FROM members").fetchall()                               
        countmember = countmember[0][0]

        soldproduct = cur.execute("SELECT SUM(selling_quantity) FROM sellings").fetchall()
        soldproduct = soldproduct[0][0]

        soldamount = cur.execute("SELECT SUM(selling_amount) FROM sellings").fetchall()
        soldamount = soldamount[0][0]

        self.totalproductlabel.setText(_translate("MainWindow", str(countproduct)))
        self.totalmemberlabel.setText(_translate("MainWindow", str(countmember)))
        self.soldproductlabel.setText(_translate("MainWindow", str(soldproduct)))
        self.totalamountlabel.setText(_translate("MainWindow", "₹ "+str(soldamount)))

    def tabchanged(self):
        self.getstatistics()
        self.displayProducts()
        self.displaymembers()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

