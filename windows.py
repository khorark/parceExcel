# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 188)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.file_name_le = QtWidgets.QLineEdit(self.centralwidget)
        self.file_name_le.setAutoFillBackground(False)
        self.file_name_le.setText("")
        self.file_name_le.setDragEnabled(True)
        self.file_name_le.setReadOnly(True)
        self.file_name_le.setObjectName("file_name_le")
        self.gridLayout.addWidget(self.file_name_le, 0, 0, 1, 2)
        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_btn.setObjectName("open_btn")
        self.gridLayout.addWidget(self.open_btn, 0, 2, 1, 1)
        self.progress_pg = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_pg.setProperty("value", 0)
        self.progress_pg.setObjectName("progress_pg")
        self.gridLayout.addWidget(self.progress_pg, 1, 0, 1, 1)
        self.start_bt = QtWidgets.QPushButton(self.centralwidget)
        self.start_bt.setObjectName("start_bt")
        self.gridLayout.addWidget(self.start_bt, 1, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.menu.addAction(self.action_open)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.menu_2.addAction(self.action_about)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "parceExel v.1.0"))
        self.file_name_le.setPlaceholderText(_translate("MainWindow", "Выберите файл"))
        self.open_btn.setText(_translate("MainWindow", "Открыть"))
        self.start_bt.setText(_translate("MainWindow", "Начать"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Справка"))
        self.action_open.setText(_translate("MainWindow", "Открыть..."))
        self.action_exit.setText(_translate("MainWindow", "Выход"))
        self.action_about.setText(_translate("MainWindow", "О программе"))

