# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addmember.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox
import sqlite3

con = sqlite3.connect("products.db")
cur = con.cursor()

class AddMember(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/addmember.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.topmainLayout = QtWidgets.QVBoxLayout()
        self.topmainLayout.setContentsMargins(-1, 30, -1, 50)
        self.topmainLayout.setObjectName("topmainLayout")
        self.addmemberlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.addmemberlabel.setFont(font)
        self.addmemberlabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.addmemberlabel.setObjectName("addmemberlabel")
        self.topmainLayout.addWidget(self.addmemberlabel)
        self.addmemberImg = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.addmemberImg.setFont(font)
        self.addmemberImg.setText("")
        self.addmemberImg.setPixmap(QtGui.QPixmap("icons/addmember.png"))
        self.addmemberImg.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.addmemberImg.setObjectName("addmemberImg")
        self.topmainLayout.addWidget(self.addmemberImg)
        self.mainLayout.addLayout(self.topmainLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 20, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.membernameentry = QtWidgets.QLineEdit(self.centralwidget)
        self.membernameentry.setObjectName("membernameentry")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.membernameentry)
        self.membersurnameentry = QtWidgets.QLineEdit(self.centralwidget)
        self.membersurnameentry.setObjectName("membersurnameentry")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.membersurnameentry)
        self.memberphoneentry = QtWidgets.QLineEdit(self.centralwidget)
        self.memberphoneentry.setObjectName("memberphoneentry")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.memberphoneentry)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setObjectName("submitButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.submitButton)
        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setObjectName("namelabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.namelabel)
        self.surnamelabel = QtWidgets.QLabel(self.centralwidget)
        self.surnamelabel.setObjectName("surnamelabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.surnamelabel)
        self.phonelabel = QtWidgets.QLabel(self.centralwidget)
        self.phonelabel.setObjectName("phonelabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.phonelabel)
        self.emptylabel = QtWidgets.QLabel(self.centralwidget)
        self.emptylabel.setText("")
        self.emptylabel.setObjectName("emptylabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.emptylabel)
        self.mainLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.submitButton.clicked.connect(lambda:(self.addmember(MainWindow)))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Member"))
        self.addmemberlabel.setText(_translate("MainWindow", "Add Member"))
        self.membernameentry.setPlaceholderText(_translate("MainWindow", "Enter name of member"))
        self.membersurnameentry.setPlaceholderText(_translate("MainWindow", "Enter surname of member"))
        self.memberphoneentry.setPlaceholderText(_translate("MainWindow", "Enter phone number"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.namelabel.setText(_translate("MainWindow", "Name:"))
        self.surnamelabel.setText(_translate("MainWindow", "Surname:"))
        self.phonelabel.setText(_translate("MainWindow", "Phone Number:"))

    def addmember(self,MainWindow):
        name = self.membernameentry.text()
        surname = self.membersurnameentry.text()
        phone = self.memberphoneentry.text()
        if (name and surname and phone !=""):
            try:
                query = "INSERT INTO 'members' (member_name,member_surname,member_phone) VAlUES(?,?,?)"
                cur.execute(query,(name,surname,phone))
                con.commit()
                QMessageBox.information(MainWindow,"Success","Product has been added")
                self.membernameentry.setText("")
                self.membersurnameentry.setText("")
                self.memberphoneentry.setText("")
            except:
                QMessageBox.critical(MainWindow,"Failed","Technical error")  
        else:
            QMessageBox.information(MainWindow,"Warning","Fill all field")        






