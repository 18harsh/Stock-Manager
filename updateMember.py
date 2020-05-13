# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateMember.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QFileDialog,QMessageBox
con = sqlite3.connect("products.db")
cur = con.cursor()


class UpdateMember(object):
    def setupUi(self, MainWindow,memberId):
        self.memberdetails(memberId)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/members.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainlayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainlayout.setObjectName("mainlayout")
        self.topmainLayout = QtWidgets.QVBoxLayout()
        self.topmainLayout.setContentsMargins(-1, 20, -1, 0)
        self.topmainLayout.setObjectName("topmainLayout")
        self.updatememberlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(22)
        self.updatememberlabel.setFont(font)
        self.updatememberlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.updatememberlabel.setObjectName("updatememberlabel")
        self.topmainLayout.addWidget(self.updatememberlabel)
        self.imglabel = QtWidgets.QLabel(self.centralwidget)
        self.imglabel.setText("")
        self.imglabel.setPixmap(QtGui.QPixmap("icons/members.png"))
        self.imglabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imglabel.setObjectName("imglabel")
        self.topmainLayout.addWidget(self.imglabel)
        self.mainlayout.addLayout(self.topmainLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 0, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setObjectName("namelabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.namelabel)
        self.surnamelabel = QtWidgets.QLabel(self.centralwidget)
        self.surnamelabel.setObjectName("surnamelabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.surnamelabel)
        self.nameentry = QtWidgets.QLineEdit(self.centralwidget)
        self.nameentry.setObjectName("nameentry")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameentry)
        self.surnameentry = QtWidgets.QLineEdit(self.centralwidget)
        self.surnameentry.setObjectName("surnameentry")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surnameentry)
        self.phoneentry = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneentry.setObjectName("phoneentry")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.phoneentry)
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setObjectName("updateButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.updateButton)
        self.phonelabel = QtWidgets.QLabel(self.centralwidget)
        self.phonelabel.setObjectName("phonelabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.phonelabel)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.deleteButton)
        self.mainlayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.deleteButton.clicked.connect(lambda:(self.deletemember(MainWindow)))
        self.updateButton.clicked.connect(lambda:(self.updatemember(MainWindow)))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Update Member"))
        self.updatememberlabel.setText(_translate("MainWindow", "Update Member"))
        self.namelabel.setText(_translate("MainWindow", "Name:"))
        self.surnamelabel.setText(_translate("MainWindow", "Surname:"))
        self.nameentry.setText(_translate("MainWindow", self.member_name))
        self.surnameentry.setText(_translate("MainWindow", self.member_surname))
        self.phoneentry.setText(_translate("MainWindow", self.member_phone))
        self.updateButton.setText(_translate("MainWindow", "Update"))
        self.phonelabel.setText(_translate("MainWindow", "Phone Number:"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))

    def memberdetails(self,memberid):
        query = ("SELECT * FROM members WHERE member_id=?")
        self.member = cur.execute(query,(memberid,)).fetchone()
        self.member_id = self.member[0]
        self.member_name = self.member[1]
        self.member_surname = self.member[2]
        self.member_phone = self.member[3]

    def deletemember(self,MainWindow):
        mbox = QMessageBox.warning(MainWindow,"Warning","Are you sure, you want to delete?",QMessageBox.Yes|QMessageBox.No)
        if mbox  == QMessageBox.Yes:
            try:    
                cur.execute("DELETE FROM members WHERE member_id=?",(self.member_id,))
                con.commit()
                QMessageBox.information(MainWindow,"Success","Product Deleted!")
                MainWindow.close()
            except:
                QMessageBox.critical(MainWindow,"Failed","Technical error")

    def updatemember(self,MainWindow):
        name = self.nameentry.text()
        surname = self.surnameentry.text()
        phone = self.phoneentry.text()
        id = self.member_id
        
        if (name and surname and phone !=""):    
            try:
                query = "UPDATE members SET member_name=?,member_surname=?,member_phone=? WHERE member_id=?"
                cur.execute(query,(name,surname,phone,id))
                con.commit()
                QMessageBox.information(MainWindow,"Success","Product Updated Successfully")
                MainWindow.close()
            except:  
                QMessageBox.critical(MainWindow,"Failed","Technical error")      
        else:
             QMessageBox.information(MainWindow,"Warning","Fill all field")            
                    
            



