# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/asdfg60842/Desktop/Project/PYTHON/TexasHoldem/ui/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 556)
        MainWindow.setMinimumSize(QtCore.QSize(240, 320))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 340, 161, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(58, 134, 255);\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(58, 134, 255);\n"
"    background-color: white;\n"
"    border: 2px solid rgb(58, 134, 255);\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: white;\n"
"    background-color: rgb(58, 134, 255);\n"
"    border-radius: 25px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 80, 311, 181))
        self.label.setStyleSheet("QLabel\n"
"{\n"
"        color: #fcedd8;\n"
"           font-family: \'Phosphate\', cursive;\n"
"}")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Game Start!"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:64pt;\">Texas </span></p><p align=\"center\"><span style=\" font-size:64pt;\">Hold\'em</span></p></body></html>"))
