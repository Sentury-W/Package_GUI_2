# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menubar_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 786)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(5, 11, 261, 671))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableView_2 = QtWidgets.QTableView(self.tab_2)
        self.tableView_2.setGeometry(QtCore.QRect(5, 11, 261, 671))
        self.tableView_2.setObjectName("tableView_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(11, 14, 611, 271))
        self.label_2.setStyleSheet("border:1px solid;")
        self.label_2.setObjectName("label_2")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(11, 14, 611, 271))
        self.label.setStyleSheet("border:1px solid;")
        self.label.setObjectName("label")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget_2)
        spacerItem2 = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.tabWidget_3 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setGeometry(QtCore.QRect(11, 14, 611, 271))
        self.label_3.setStyleSheet("border:1px solid;")
        self.label_3.setObjectName("label_3")
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_4 = QtWidgets.QLabel(self.tab_6)
        self.label_4.setGeometry(QtCore.QRect(11, 14, 611, 271))
        self.label_4.setStyleSheet("border:1px solid;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.tabWidget_3.addTab(self.tab_6, "")
        self.verticalLayout.addWidget(self.tabWidget_3)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 10)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(3, 7)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1073, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuInput_Data_2 = QtWidgets.QMenu(self.menu)
        self.menuInput_Data_2.setObjectName("menuInput_Data_2")
        self.menuCHINA = QtWidgets.QMenu(self.menuInput_Data_2)
        self.menuCHINA.setObjectName("menuCHINA")
        self.menuRUSSIA = QtWidgets.QMenu(self.menuInput_Data_2)
        self.menuRUSSIA.setObjectName("menuRUSSIA")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_6.setObjectName("menu_6")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action3sigma = QtWidgets.QAction(MainWindow)
        self.action3sigma.setObjectName("action3sigma")
        self.actionJY_error = QtWidgets.QAction(MainWindow)
        self.actionJY_error.setObjectName("actionJY_error")
        self.actionbox_plot = QtWidgets.QAction(MainWindow)
        self.actionbox_plot.setObjectName("actionbox_plot")
        self.actioniso_for = QtWidgets.QAction(MainWindow)
        self.actioniso_for.setObjectName("actioniso_for")
        self.actionCNN = QtWidgets.QAction(MainWindow)
        self.actionCNN.setObjectName("actionCNN")
        self.actionInsert = QtWidgets.QAction(MainWindow)
        self.actionInsert.setObjectName("actionInsert")
        self.actionLSTM = QtWidgets.QAction(MainWindow)
        self.actionLSTM.setObjectName("actionLSTM")
        self.actionReatored_Data = QtWidgets.QAction(MainWindow)
        self.actionReatored_Data.setObjectName("actionReatored_Data")
        self.action1D_data = QtWidgets.QAction(MainWindow)
        self.action1D_data.setObjectName("action1D_data")
        self.action2D_Figure = QtWidgets.QAction(MainWindow)
        self.action2D_Figure.setObjectName("action2D_Figure")
        self.actionFeb = QtWidgets.QAction(MainWindow)
        self.actionFeb.setObjectName("actionFeb")
        self.actionMar = QtWidgets.QAction(MainWindow)
        self.actionMar.setObjectName("actionMar")
        self.actionApr = QtWidgets.QAction(MainWindow)
        self.actionApr.setObjectName("actionApr")
        self.actionMay = QtWidgets.QAction(MainWindow)
        self.actionMay.setObjectName("actionMay")
        self.actionJune = QtWidgets.QAction(MainWindow)
        self.actionJune.setObjectName("actionJune")
        self.actionJuly = QtWidgets.QAction(MainWindow)
        self.actionJuly.setObjectName("actionJuly")
        self.actionAug = QtWidgets.QAction(MainWindow)
        self.actionAug.setObjectName("actionAug")
        self.actionep = QtWidgets.QAction(MainWindow)
        self.actionep.setObjectName("actionep")
        self.actionOct = QtWidgets.QAction(MainWindow)
        self.actionOct.setObjectName("actionOct")
        self.actionNov = QtWidgets.QAction(MainWindow)
        self.actionNov.setObjectName("actionNov")
        self.actionDec = QtWidgets.QAction(MainWindow)
        self.actionDec.setObjectName("actionDec")
        self.actionCHINA = QtWidgets.QAction(MainWindow)
        self.actionCHINA.setObjectName("actionCHINA")
        self.actionRUSS = QtWidgets.QAction(MainWindow)
        self.actionRUSS.setObjectName("actionRUSS")
        self.actionSLS03 = QtWidgets.QAction(MainWindow)
        self.actionSLS03.setObjectName("actionSLS03")
        self.actionOriginal_Data_2 = QtWidgets.QAction(MainWindow)
        self.actionOriginal_Data_2.setObjectName("actionOriginal_Data_2")
        self.actionSLS01_3 = QtWidgets.QAction(MainWindow)
        self.actionSLS01_3.setObjectName("actionSLS01_3")
        self.actionSLS02 = QtWidgets.QAction(MainWindow)
        self.actionSLS02.setObjectName("actionSLS02")
        self.actionSLS03_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS03_2.setObjectName("actionSLS03_2")
        self.actionSLS04 = QtWidgets.QAction(MainWindow)
        self.actionSLS04.setObjectName("actionSLS04")
        self.actionSLS05 = QtWidgets.QAction(MainWindow)
        self.actionSLS05.setObjectName("actionSLS05")
        self.actionSLS06 = QtWidgets.QAction(MainWindow)
        self.actionSLS06.setObjectName("actionSLS06")
        self.actionSLS07 = QtWidgets.QAction(MainWindow)
        self.actionSLS07.setObjectName("actionSLS07")
        self.actionSLS08 = QtWidgets.QAction(MainWindow)
        self.actionSLS08.setObjectName("actionSLS08")
        self.actionSLS09 = QtWidgets.QAction(MainWindow)
        self.actionSLS09.setObjectName("actionSLS09")
        self.actionSLS10 = QtWidgets.QAction(MainWindow)
        self.actionSLS10.setObjectName("actionSLS10")
        self.actionSLS11 = QtWidgets.QAction(MainWindow)
        self.actionSLS11.setObjectName("actionSLS11")
        self.actionSLS12 = QtWidgets.QAction(MainWindow)
        self.actionSLS12.setObjectName("actionSLS12")
        self.actionSLS13 = QtWidgets.QAction(MainWindow)
        self.actionSLS13.setObjectName("actionSLS13")
        self.actionSLS14 = QtWidgets.QAction(MainWindow)
        self.actionSLS14.setObjectName("actionSLS14")
        self.actionSLS15 = QtWidgets.QAction(MainWindow)
        self.actionSLS15.setObjectName("actionSLS15")
        self.actionSLS16 = QtWidgets.QAction(MainWindow)
        self.actionSLS16.setObjectName("actionSLS16")
        self.actionSLS17 = QtWidgets.QAction(MainWindow)
        self.actionSLS17.setObjectName("actionSLS17")
        self.actionSLS18 = QtWidgets.QAction(MainWindow)
        self.actionSLS18.setObjectName("actionSLS18")
        self.actionSLS19 = QtWidgets.QAction(MainWindow)
        self.actionSLS19.setObjectName("actionSLS19")
        self.actionSLS20 = QtWidgets.QAction(MainWindow)
        self.actionSLS20.setObjectName("actionSLS20")
        self.actionSLS21 = QtWidgets.QAction(MainWindow)
        self.actionSLS21.setObjectName("actionSLS21")
        self.actionSLS22 = QtWidgets.QAction(MainWindow)
        self.actionSLS22.setObjectName("actionSLS22")
        self.actionSLS23 = QtWidgets.QAction(MainWindow)
        self.actionSLS23.setObjectName("actionSLS23")
        self.actionSLS24 = QtWidgets.QAction(MainWindow)
        self.actionSLS24.setObjectName("actionSLS24")
        self.actionSLX01 = QtWidgets.QAction(MainWindow)
        self.actionSLX01.setObjectName("actionSLX01")
        self.actionSLX02 = QtWidgets.QAction(MainWindow)
        self.actionSLX02.setObjectName("actionSLX02")
        self.actionSLX03 = QtWidgets.QAction(MainWindow)
        self.actionSLX03.setObjectName("actionSLX03")
        self.actionSLX04 = QtWidgets.QAction(MainWindow)
        self.actionSLX04.setObjectName("actionSLX04")
        self.actionSLX05 = QtWidgets.QAction(MainWindow)
        self.actionSLX05.setObjectName("actionSLX05")
        self.actionSLX06 = QtWidgets.QAction(MainWindow)
        self.actionSLX06.setObjectName("actionSLX06")
        self.actionSLX07 = QtWidgets.QAction(MainWindow)
        self.actionSLX07.setObjectName("actionSLX07")
        self.actionSLX08 = QtWidgets.QAction(MainWindow)
        self.actionSLX08.setObjectName("actionSLX08")
        self.actionSLX09 = QtWidgets.QAction(MainWindow)
        self.actionSLX09.setObjectName("actionSLX09")
        self.actionSLX10 = QtWidgets.QAction(MainWindow)
        self.actionSLX10.setObjectName("actionSLX10")
        self.actionSLX11 = QtWidgets.QAction(MainWindow)
        self.actionSLX11.setObjectName("actionSLX11")
        self.actionSLX12 = QtWidgets.QAction(MainWindow)
        self.actionSLX12.setObjectName("actionSLX12")
        self.actionSLX13 = QtWidgets.QAction(MainWindow)
        self.actionSLX13.setObjectName("actionSLX13")
        self.actionSLX14 = QtWidgets.QAction(MainWindow)
        self.actionSLX14.setObjectName("actionSLX14")
        self.actionSLX15 = QtWidgets.QAction(MainWindow)
        self.actionSLX15.setObjectName("actionSLX15")
        self.actionSLX16 = QtWidgets.QAction(MainWindow)
        self.actionSLX16.setObjectName("actionSLX16")
        self.actionSLX17 = QtWidgets.QAction(MainWindow)
        self.actionSLX17.setObjectName("actionSLX17")
        self.actionSLX18 = QtWidgets.QAction(MainWindow)
        self.actionSLX18.setObjectName("actionSLX18")
        self.actionSLX19 = QtWidgets.QAction(MainWindow)
        self.actionSLX19.setObjectName("actionSLX19")
        self.actionSLX20 = QtWidgets.QAction(MainWindow)
        self.actionSLX20.setObjectName("actionSLX20")
        self.actionSLX21 = QtWidgets.QAction(MainWindow)
        self.actionSLX21.setObjectName("actionSLX21")
        self.actionSLX22 = QtWidgets.QAction(MainWindow)
        self.actionSLX22.setObjectName("actionSLX22")
        self.actionSLX23 = QtWidgets.QAction(MainWindow)
        self.actionSLX23.setObjectName("actionSLX23")
        self.actionSXL24 = QtWidgets.QAction(MainWindow)
        self.actionSXL24.setObjectName("actionSXL24")
        self.actionSLS01 = QtWidgets.QAction(MainWindow)
        self.actionSLS01.setObjectName("actionSLS01")
        self.actionLoad_Data = QtWidgets.QAction(MainWindow)
        self.actionLoad_Data.setObjectName("actionLoad_Data")
        self.actionSLS01_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS01_2.setCheckable(False)
        self.actionSLS01_2.setObjectName("actionSLS01_2")
        self.actionSLS02_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS02_2.setObjectName("actionSLS02_2")
        self.actionSLS03_3 = QtWidgets.QAction(MainWindow)
        self.actionSLS03_3.setObjectName("actionSLS03_3")
        self.actionSLS04_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS04_2.setObjectName("actionSLS04_2")
        self.actionSLS05_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS05_2.setObjectName("actionSLS05_2")
        self.actionSLS06_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS06_2.setObjectName("actionSLS06_2")
        self.actionSLS07_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS07_2.setObjectName("actionSLS07_2")
        self.actionSLS08_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS08_2.setObjectName("actionSLS08_2")
        self.actionSLS09_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS09_2.setObjectName("actionSLS09_2")
        self.actionSLS10_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS10_2.setObjectName("actionSLS10_2")
        self.actionSLS11_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS11_2.setObjectName("actionSLS11_2")
        self.actionSLS12_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS12_2.setObjectName("actionSLS12_2")
        self.actionSLS13_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS13_2.setObjectName("actionSLS13_2")
        self.actionSLS14_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS14_2.setObjectName("actionSLS14_2")
        self.actionSLS15_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS15_2.setObjectName("actionSLS15_2")
        self.actionSLS16_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS16_2.setObjectName("actionSLS16_2")
        self.actionSLS17_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS17_2.setObjectName("actionSLS17_2")
        self.actionSLS18_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS18_2.setObjectName("actionSLS18_2")
        self.actionSLS19_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS19_2.setObjectName("actionSLS19_2")
        self.actionSLS20_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS20_2.setObjectName("actionSLS20_2")
        self.actionSLS21_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS21_2.setObjectName("actionSLS21_2")
        self.actionSLS22_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS22_2.setObjectName("actionSLS22_2")
        self.actionSLS23_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS23_2.setObjectName("actionSLS23_2")
        self.actionSLS24_2 = QtWidgets.QAction(MainWindow)
        self.actionSLS24_2.setObjectName("actionSLS24_2")
        self.actionSLX01_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX01_2.setObjectName("actionSLX01_2")
        self.actionSLX02_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX02_2.setObjectName("actionSLX02_2")
        self.actionSLX03_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX03_2.setObjectName("actionSLX03_2")
        self.actionSLX04_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX04_2.setObjectName("actionSLX04_2")
        self.actionSLX05_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX05_2.setObjectName("actionSLX05_2")
        self.actionSLX06_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX06_2.setObjectName("actionSLX06_2")
        self.actionSLX07_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX07_2.setObjectName("actionSLX07_2")
        self.actionSLX08_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX08_2.setObjectName("actionSLX08_2")
        self.actionSLX09_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX09_2.setObjectName("actionSLX09_2")
        self.actionSLX10_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX10_2.setObjectName("actionSLX10_2")
        self.actionSLX11_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX11_2.setObjectName("actionSLX11_2")
        self.actionSLX12_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX12_2.setObjectName("actionSLX12_2")
        self.actionSLX13_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX13_2.setObjectName("actionSLX13_2")
        self.actionSLX14_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX14_2.setObjectName("actionSLX14_2")
        self.actionSLX15_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX15_2.setObjectName("actionSLX15_2")
        self.actionSLX16_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX16_2.setObjectName("actionSLX16_2")
        self.actionSLX17_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX17_2.setObjectName("actionSLX17_2")
        self.actionSLX18_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX18_2.setObjectName("actionSLX18_2")
        self.actionSLX19_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX19_2.setObjectName("actionSLX19_2")
        self.actionSLX20_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX20_2.setObjectName("actionSLX20_2")
        self.actionSLX21_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX21_2.setObjectName("actionSLX21_2")
        self.actionSLX22_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX22_2.setObjectName("actionSLX22_2")
        self.actionSLX23_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX23_2.setObjectName("actionSLX23_2")
        self.actionSLX24_2 = QtWidgets.QAction(MainWindow)
        self.actionSLX24_2.setObjectName("actionSLX24_2")
        self.actionk_means = QtWidgets.QAction(MainWindow)
        self.actionk_means.setObjectName("actionk_means")
        self.actionSVM = QtWidgets.QAction(MainWindow)
        self.actionSVM.setObjectName("actionSVM")
        self.actionDetected_Data = QtWidgets.QAction(MainWindow)
        self.actionDetected_Data.setObjectName("actionDetected_Data")
        self.menuCHINA.addAction(self.actionSLS01_2)
        self.menuCHINA.addAction(self.actionSLS02_2)
        self.menuCHINA.addAction(self.actionSLS03_3)
        self.menuCHINA.addAction(self.actionSLS04_2)
        self.menuCHINA.addAction(self.actionSLS05_2)
        self.menuCHINA.addAction(self.actionSLS06_2)
        self.menuCHINA.addAction(self.actionSLS07_2)
        self.menuCHINA.addAction(self.actionSLS08_2)
        self.menuCHINA.addAction(self.actionSLS09_2)
        self.menuCHINA.addAction(self.actionSLS10_2)
        self.menuCHINA.addAction(self.actionSLS11_2)
        self.menuCHINA.addAction(self.actionSLS12_2)
        self.menuCHINA.addAction(self.actionSLS13_2)
        self.menuCHINA.addAction(self.actionSLS14_2)
        self.menuCHINA.addAction(self.actionSLS15_2)
        self.menuCHINA.addAction(self.actionSLS16_2)
        self.menuCHINA.addAction(self.actionSLS17_2)
        self.menuCHINA.addAction(self.actionSLS18_2)
        self.menuCHINA.addAction(self.actionSLS19_2)
        self.menuCHINA.addAction(self.actionSLS20_2)
        self.menuCHINA.addAction(self.actionSLS21_2)
        self.menuCHINA.addAction(self.actionSLS22_2)
        self.menuCHINA.addAction(self.actionSLS23_2)
        self.menuCHINA.addAction(self.actionSLS24_2)
        self.menuRUSSIA.addAction(self.actionSLX01_2)
        self.menuRUSSIA.addAction(self.actionSLX02_2)
        self.menuRUSSIA.addAction(self.actionSLX03_2)
        self.menuRUSSIA.addAction(self.actionSLX04_2)
        self.menuRUSSIA.addAction(self.actionSLX05_2)
        self.menuRUSSIA.addAction(self.actionSLX06_2)
        self.menuRUSSIA.addAction(self.actionSLX07_2)
        self.menuRUSSIA.addAction(self.actionSLX08_2)
        self.menuRUSSIA.addAction(self.actionSLX09_2)
        self.menuRUSSIA.addAction(self.actionSLX10_2)
        self.menuRUSSIA.addAction(self.actionSLX11_2)
        self.menuRUSSIA.addAction(self.actionSLX12_2)
        self.menuRUSSIA.addAction(self.actionSLX13_2)
        self.menuRUSSIA.addAction(self.actionSLX14_2)
        self.menuRUSSIA.addAction(self.actionSLX15_2)
        self.menuRUSSIA.addAction(self.actionSLX16_2)
        self.menuRUSSIA.addAction(self.actionSLX17_2)
        self.menuRUSSIA.addAction(self.actionSLX18_2)
        self.menuRUSSIA.addAction(self.actionSLX19_2)
        self.menuRUSSIA.addAction(self.actionSLX20_2)
        self.menuRUSSIA.addAction(self.actionSLX21_2)
        self.menuRUSSIA.addAction(self.actionSLX22_2)
        self.menuRUSSIA.addAction(self.actionSLX23_2)
        self.menuRUSSIA.addAction(self.actionSLX24_2)
        self.menuInput_Data_2.addAction(self.menuCHINA.menuAction())
        self.menuInput_Data_2.addAction(self.menuRUSSIA.menuAction())
        self.menu.addAction(self.actionLoad_Data)
        self.menu.addSeparator()
        self.menu.addAction(self.menuInput_Data_2.menuAction())
        self.menu_2.addAction(self.actionJY_error)
        self.menu_2.addAction(self.action3sigma)
        self.menu_2.addAction(self.actionbox_plot)
        self.menu_2.addAction(self.actioniso_for)
        self.menu_2.addAction(self.actionk_means)
        self.menu_2.addAction(self.actionSVM)
        self.menu_3.addAction(self.actionCNN)
        self.menu_4.addAction(self.actionInsert)
        self.menu_4.addAction(self.actionLSTM)
        self.menu_5.addAction(self.actionOriginal_Data_2)
        self.menu_5.addAction(self.actionDetected_Data)
        self.menu_5.addAction(self.actionReatored_Data)
        self.menu_6.addAction(self.action1D_data)
        self.menu_6.addAction(self.action2D_Figure)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "原始数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "恢复数据"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "原数据图像"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "异常检测结果"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "插值恢复"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "LSTM"))
        self.menu.setTitle(_translate("MainWindow", "功能"))
        self.menuInput_Data_2.setTitle(_translate("MainWindow", "载入数据"))
        self.menuCHINA.setTitle(_translate("MainWindow", "CHINA"))
        self.menuRUSSIA.setTitle(_translate("MainWindow", "RUSSIA"))
        self.menu_2.setTitle(_translate("MainWindow", "异常检测"))
        self.menu_3.setTitle(_translate("MainWindow", "异常分类"))
        self.menu_4.setTitle(_translate("MainWindow", "异常恢复"))
        self.menu_5.setTitle(_translate("MainWindow", "数据显示"))
        self.menu_6.setTitle(_translate("MainWindow", "数据保存"))
        self.action3sigma.setText(_translate("MainWindow", "3-sigma"))
        self.actionJY_error.setText(_translate("MainWindow", "JY_error"))
        self.actionbox_plot.setText(_translate("MainWindow", "box_plot"))
        self.actioniso_for.setText(_translate("MainWindow", "iostation_forest"))
        self.actionCNN.setText(_translate("MainWindow", "CNN"))
        self.actionInsert.setText(_translate("MainWindow", "Insert"))
        self.actionLSTM.setText(_translate("MainWindow", "LSTM"))
        self.actionReatored_Data.setText(_translate("MainWindow", "Restored Data"))
        self.action1D_data.setText(_translate("MainWindow", "1D_data"))
        self.action2D_Figure.setText(_translate("MainWindow", "2D_Figure"))
        self.actionFeb.setText(_translate("MainWindow", "Feb"))
        self.actionMar.setText(_translate("MainWindow", "Mar"))
        self.actionApr.setText(_translate("MainWindow", "Apr"))
        self.actionMay.setText(_translate("MainWindow", "May"))
        self.actionJune.setText(_translate("MainWindow", "June"))
        self.actionJuly.setText(_translate("MainWindow", "July"))
        self.actionAug.setText(_translate("MainWindow", "Aug"))
        self.actionep.setText(_translate("MainWindow", "Sep"))
        self.actionOct.setText(_translate("MainWindow", "Oct"))
        self.actionNov.setText(_translate("MainWindow", "Nov"))
        self.actionDec.setText(_translate("MainWindow", "Dec"))
        self.actionCHINA.setText(_translate("MainWindow", "CHINA"))
        self.actionRUSS.setText(_translate("MainWindow", "RUSS"))
        self.actionSLS03.setText(_translate("MainWindow", "SLS03"))
        self.actionOriginal_Data_2.setText(_translate("MainWindow", "Original Data"))
        self.actionSLS01_3.setText(_translate("MainWindow", "SLS01"))
        self.actionSLS02.setText(_translate("MainWindow", "SLS02"))
        self.actionSLS03_2.setText(_translate("MainWindow", "SLS03"))
        self.actionSLS04.setText(_translate("MainWindow", "SLS04"))
        self.actionSLS05.setText(_translate("MainWindow", "SLS05"))
        self.actionSLS06.setText(_translate("MainWindow", "SLS06"))
        self.actionSLS07.setText(_translate("MainWindow", "SLS07"))
        self.actionSLS08.setText(_translate("MainWindow", "SLS08"))
        self.actionSLS09.setText(_translate("MainWindow", "SLS09"))
        self.actionSLS10.setText(_translate("MainWindow", "SLS10"))
        self.actionSLS11.setText(_translate("MainWindow", "SLS11"))
        self.actionSLS12.setText(_translate("MainWindow", "SLS12"))
        self.actionSLS13.setText(_translate("MainWindow", "SLS13"))
        self.actionSLS14.setText(_translate("MainWindow", "SLS14"))
        self.actionSLS15.setText(_translate("MainWindow", "SLS15"))
        self.actionSLS16.setText(_translate("MainWindow", "SLS16"))
        self.actionSLS17.setText(_translate("MainWindow", "SLS17"))
        self.actionSLS18.setText(_translate("MainWindow", "SLS18"))
        self.actionSLS19.setText(_translate("MainWindow", "SLS19"))
        self.actionSLS20.setText(_translate("MainWindow", "SLS20"))
        self.actionSLS21.setText(_translate("MainWindow", "SLS21"))
        self.actionSLS22.setText(_translate("MainWindow", "SLS22"))
        self.actionSLS23.setText(_translate("MainWindow", "SLS23"))
        self.actionSLS24.setText(_translate("MainWindow", "SLS24"))
        self.actionSLX01.setText(_translate("MainWindow", "SLX01"))
        self.actionSLX02.setText(_translate("MainWindow", "SLX02"))
        self.actionSLX03.setText(_translate("MainWindow", "SLX03"))
        self.actionSLX04.setText(_translate("MainWindow", "SLX04"))
        self.actionSLX05.setText(_translate("MainWindow", "SLX05"))
        self.actionSLX06.setText(_translate("MainWindow", "SLX06"))
        self.actionSLX07.setText(_translate("MainWindow", "SLX07"))
        self.actionSLX08.setText(_translate("MainWindow", "SLX08"))
        self.actionSLX09.setText(_translate("MainWindow", "SLX09"))
        self.actionSLX10.setText(_translate("MainWindow", "SLX10"))
        self.actionSLX11.setText(_translate("MainWindow", "SLX11"))
        self.actionSLX12.setText(_translate("MainWindow", "SLX12"))
        self.actionSLX13.setText(_translate("MainWindow", "SLX13"))
        self.actionSLX14.setText(_translate("MainWindow", "SLX14"))
        self.actionSLX15.setText(_translate("MainWindow", "SLX15"))
        self.actionSLX16.setText(_translate("MainWindow", "SLX16"))
        self.actionSLX17.setText(_translate("MainWindow", "SLX17"))
        self.actionSLX18.setText(_translate("MainWindow", "SLX18"))
        self.actionSLX19.setText(_translate("MainWindow", "SLX19"))
        self.actionSLX20.setText(_translate("MainWindow", "SLX20"))
        self.actionSLX21.setText(_translate("MainWindow", "SLX21"))
        self.actionSLX22.setText(_translate("MainWindow", "SLX22"))
        self.actionSLX23.setText(_translate("MainWindow", "SLX23"))
        self.actionSXL24.setText(_translate("MainWindow", "SXL24"))
        self.actionSLS01.setText(_translate("MainWindow", "SLS01"))
        self.actionLoad_Data.setText(_translate("MainWindow", "选择数据"))
        self.actionSLS01_2.setText(_translate("MainWindow", "SLS01"))
        self.actionSLS02_2.setText(_translate("MainWindow", "SLS02"))
        self.actionSLS03_3.setText(_translate("MainWindow", "SLS03"))
        self.actionSLS04_2.setText(_translate("MainWindow", "SLS04"))
        self.actionSLS05_2.setText(_translate("MainWindow", "SLS05"))
        self.actionSLS06_2.setText(_translate("MainWindow", "SLS06"))
        self.actionSLS07_2.setText(_translate("MainWindow", "SLS07"))
        self.actionSLS08_2.setText(_translate("MainWindow", "SLS08"))
        self.actionSLS09_2.setText(_translate("MainWindow", "SLS09"))
        self.actionSLS10_2.setText(_translate("MainWindow", "SLS10"))
        self.actionSLS11_2.setText(_translate("MainWindow", "SLS11"))
        self.actionSLS12_2.setText(_translate("MainWindow", "SLS12"))
        self.actionSLS13_2.setText(_translate("MainWindow", "SLS13"))
        self.actionSLS14_2.setText(_translate("MainWindow", "SLS14"))
        self.actionSLS15_2.setText(_translate("MainWindow", "SLS15"))
        self.actionSLS16_2.setText(_translate("MainWindow", "SLS16"))
        self.actionSLS17_2.setText(_translate("MainWindow", "SLS17"))
        self.actionSLS18_2.setText(_translate("MainWindow", "SLS18"))
        self.actionSLS19_2.setText(_translate("MainWindow", "SLS19"))
        self.actionSLS20_2.setText(_translate("MainWindow", "SLS20"))
        self.actionSLS21_2.setText(_translate("MainWindow", "SLS21"))
        self.actionSLS22_2.setText(_translate("MainWindow", "SLS22"))
        self.actionSLS23_2.setText(_translate("MainWindow", "SLS23"))
        self.actionSLS24_2.setText(_translate("MainWindow", "SLS24"))
        self.actionSLX01_2.setText(_translate("MainWindow", "SLX01"))
        self.actionSLX02_2.setText(_translate("MainWindow", "SLX02"))
        self.actionSLX03_2.setText(_translate("MainWindow", "SLX03"))
        self.actionSLX04_2.setText(_translate("MainWindow", "SLX04"))
        self.actionSLX05_2.setText(_translate("MainWindow", "SLX05"))
        self.actionSLX06_2.setText(_translate("MainWindow", "SLX06"))
        self.actionSLX07_2.setText(_translate("MainWindow", "SLX07"))
        self.actionSLX08_2.setText(_translate("MainWindow", "SLX08"))
        self.actionSLX09_2.setText(_translate("MainWindow", "SLX09"))
        self.actionSLX10_2.setText(_translate("MainWindow", "SLX10"))
        self.actionSLX11_2.setText(_translate("MainWindow", "SLX11"))
        self.actionSLX12_2.setText(_translate("MainWindow", "SLX12"))
        self.actionSLX13_2.setText(_translate("MainWindow", "SLX13"))
        self.actionSLX14_2.setText(_translate("MainWindow", "SLX14"))
        self.actionSLX15_2.setText(_translate("MainWindow", "SLX15"))
        self.actionSLX16_2.setText(_translate("MainWindow", "SLX16"))
        self.actionSLX17_2.setText(_translate("MainWindow", "SLX17"))
        self.actionSLX18_2.setText(_translate("MainWindow", "SLX18"))
        self.actionSLX19_2.setText(_translate("MainWindow", "SLX19"))
        self.actionSLX20_2.setText(_translate("MainWindow", "SLX20"))
        self.actionSLX21_2.setText(_translate("MainWindow", "SLX21"))
        self.actionSLX22_2.setText(_translate("MainWindow", "SLX22"))
        self.actionSLX23_2.setText(_translate("MainWindow", "SLX23"))
        self.actionSLX24_2.setText(_translate("MainWindow", "SLX24"))
        self.actionk_means.setText(_translate("MainWindow", "k_means"))
        self.actionSVM.setText(_translate("MainWindow", "SVM"))
        self.actionDetected_Data.setText(_translate("MainWindow", "Detected Data"))
