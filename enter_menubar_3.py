import menubar_3
import pandas as pd
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox, QDialog, QStatusBar, QHeaderView
from PyQt5.QtGui import QBrush, QColor, QPainter
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from sensor_id_list import SENSOR_ID_LIST
from NEW_detect_data import ds_load
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import shutil
from error_detect import JY_error, box_plot, iostation_forest, k_means, svm_, three_sigma, detect_st_threshold

global SLdata_list
global SLMdate_list
global index_list
global file_name
global file_path
global dl
global path
path = "./file/"
SLdata_list = []
SLMdate_list = []
global ID
ID = 999

METHOD = ['JY', '3-sigma', 'box_plot', 'isolation_forest', 'k_means', 'svm']

class Window(menubar_3.Ui_MainWindow, QMainWindow):
    status = []
    global method
    global error_index_list
    def __init__(self):
        super(menubar_3.Ui_MainWindow, self).__init__()
        # 创建界面
        self.setupUi(self)
        #实例化状态栏
        self.statusBar=QStatusBar()
        #设置状态栏，类似布局设置
        self.setStatusBar(self.statusBar)

        # save.triggered.connect(self.process)
        # self.actionSLS01.triggered.connect(self.input_1)
        # self.actionOriginal_Data_2.triggered.connect(self.ori_image)
        self.actionLoad_Data.triggered.connect(self.load_data)
        # 索力选择(未完成 余下工作复制粘贴即可)
        self.actionSLS01_2.triggered.connect(self.SLS01)
        self.actionSLS02_2.triggered.connect(self.SLS02)
        self.actionSLS03_2.triggered.connect(self.SLS03)
        self.actionSLS04_2.triggered.connect(self.SLS04)
        self.actionSLS05_2.triggered.connect(self.SLS05)
        self.actionSLS06_2.triggered.connect(self.SLS06)
        # self.actionSLS07_2.triggered.connect(self.SLS07)
        # self.actionSLS08_2.triggered.connect(self.SLS08)
        # self.actionSLS09_2.triggered.connect(self.SLS09)
        # self.actionSLS10_2.triggered.connect(self.SLS10)
        # self.actionSLS11_2.triggered.connect(self.SLS11)
        # self.actionSLS12_2.triggered.connect(self.SLS12)
        # self.actionSLS13_2.triggered.connect(self.SLS13)
        # self.actionSLS14_2.triggered.connect(self.SLS14)
        # self.actionSLS15_2.triggered.connect(self.SLS15)
        # self.actionSLS16_2.triggered.connect(self.SLS16)
        # self.actionSLS17_2.triggered.connect(self.SLS17)
        # self.actionSLS18_2.triggered.connect(self.SLS18)
        # self.actionSLS19_2.triggered.connect(self.SLS19)
        # self.actionSLS20_2.triggered.connect(self.SLS20)
        # self.actionSLS21_2.triggered.connect(self.SLS21)
        # self.actionSLS22_2.triggered.connect(self.SLS22)
        # self.actionSLS23_2.triggered.connect(self.SLS23)
        # self.actionSLS24_2.triggered.connect(self.SLS24)
        # 异常检测6种方法嵌入
        self.actionJY_error.triggered.connect(self.JY)
        self.action3sigma.triggered.connect(self.three_sigma)
        self.actionbox_plot.triggered.connect(self.BOX)
        self.actioniso_for.triggered.connect(self.ISO_FOREST)
        self.actionk_means.triggered.connect(self.K_MEANS)
        self.actionSVM.triggered.connect(self.SVM)

        # 数据可视化
        self.actionOriginal_Data_2.triggered.connect(self.ORI_FIG)
        self.actionDetected_Data.triggered.connect(self.DECT_FIG)

    def load_data(self):
        global file_name
        global SLdata_list
        global SLMdate_list
        global dl
        global file_path
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "选择载入的数据文件", ".", "*.csv")
        dl = ds_load(file_path)
        dl.sort_by_time_order()

        self.statusBar.showMessage('已选择数据文件', 10000)
        # self.statusBar.addWidget()

    def SLS01(self):
        global SLdata_list
        global SLMdate_list
        global status
        status = np.zeros(6)
        global dl
        global ID
        ID = 0
        if file_path:
            sensor_id = SENSOR_ID_LIST[ID]
            index_list = dl.get_SLdata_index(sensor_id)  # 查找传感器数据的索引
            SLdata_list = dl.get_data_st_index(index_list, 11)  # 根据索引值得到数据
            SLMdate_list = dl.get_data_st_index(index_list, 1)
            # 设置数据层次结构，4行4列
            self.model = QStandardItemModel(len(SLdata_list), 2)
            # 设置水平方向四个头标签文本内容
            self.model.setHorizontalHeaderLabels(['日期', '数据'])

            # 添加数据
            for row in range(len(SLdata_list)):
                for column in range(2):
                    if column == 0:
                        item = QStandardItem(SLMdate_list[row])
                        item.setEditable(False)
                        self.model.setItem(row, column, item)
                    elif column == 1:
                        item = QStandardItem(str(SLdata_list[row]))
                        item.setEditable(False)
                        self.model.setItem(row, column, item)
            # QTableView 绑定 数据
            self.tableView.setModel(self.model)
            # 水平方向标签拓展剩下的窗口部分，填满表格
            self.tableView.horizontalHeader().setStretchLastSection(True)
            # # 表格宽度高度随内容改变
            # self.tableWidget.resizeColumnToContents(len(SLdata_list))
            # self.tableWidget.resizeRowToContents(2)
            # 水平方向，表格大小拓展到适当的尺寸
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            self.statusBar.showMessage('请先选择要载入的数据文件', 10000)
        self.statusBar.showMessage('已载入' + str(SENSOR_ID_LIST[ID]) + '数据', 10000)

    def SLS02(self):
        global SLdata_list
        global SLMdate_list
        global index_list
        global status
        status = np.zeros(6)
        global dl
        global ID
        ID = 1
        if file_path:
            sensor_id = SENSOR_ID_LIST[ID]
            index_list = dl.get_SLdata_index(sensor_id)  # 查找传感器数据的索引
            SLdata_list = dl.get_data_st_index(index_list, 11)  # 根据索引值得到数据
            SLMdate_list = dl.get_data_st_index(index_list, 1)
            self.textBrowser_2.clear()
            self.textBrowser_2.append("<font color='black'>" + '   DATE        data(SLS02)   ' + "<font>")
            NUM = len(SLdata_list)
            for num in range(0, NUM):
                self.textBrowser_2.append(
                    "<font color='black'>" + str(SLMdate_list[num]) + '   ' + str(SLdata_list[num]) + "<font>")

    def SLS03(self):
        global SLdata_list
        global SLMdate_list
        global index_list
        global status
        status = np.zeros(6)
        global dl
        global ID
        ID = 2
        if file_path:
            sensor_id = SENSOR_ID_LIST[ID]
            index_list = dl.get_SLdata_index(sensor_id)  # 查找传感器数据的索引
            SLdata_list = dl.get_data_st_index(index_list, 11)  # 根据索引值得到数据
            SLMdate_list = dl.get_data_st_index(index_list, 1)
            self.textBrowser_2.clear()
            self.textBrowser_2.append("<font color='black'>" + '   DATE        data(SLS03)   ' + "<font>")
            NUM = len(SLdata_list)
            for num in range(0, NUM):
                self.textBrowser_2.append(
                    "<font color='black'>" + str(SLMdate_list[num]) + '   ' + str(SLdata_list[num]) + "<font>")

    def SLS04(self):
        global SLdata_list
        global SLMdate_list
        global index_list
        global status
        status = np.zeros(6)
        global dl
        global ID
        ID = 3
        if file_path:
            sensor_id = SENSOR_ID_LIST[ID]
            index_list = dl.get_SLdata_index(sensor_id)  # 查找传感器数据的索引
            SLdata_list = dl.get_data_st_index(index_list, 11)  # 根据索引值得到数据
            SLMdate_list = dl.get_data_st_index(index_list, 1)
            self.textBrowser_2.clear()
            self.textBrowser_2.append("<font color='black'>" + '   DATE        data(SLS04)   ' + "<font>")
            NUM = len(SLdata_list)
            for num in range(0, NUM):
                self.textBrowser_2.append(
                    "<font color='black'>" + str(SLMdate_list[num]) + '     ' + str(SLdata_list[num]) + "<font>")

    def SLS05(self):
        global SLdata_list
        global SLMdate_list
        global index_list
        global status
        status = np.zeros(6)
        global dl
        global ID
        ID = 4
        if file_path:
            sensor_id = SENSOR_ID_LIST[ID]
            index_list = dl.get_SLdata_index(sensor_id)  # 查找传感器数据的索引
            SLdata_list = dl.get_data_st_index(index_list, 11)  # 根据索引值得到数据
            SLMdate_list = dl.get_data_st_index(index_list, 1)
            self.textBrowser_2.clear()
            self.textBrowser_2.append("<font color='black'>" + '   DATE        data(SLS05)   ' + "<font>")
            NUM = len(SLdata_list)
            for num in range(0, NUM):
                self.textBrowser_2.append(
                    "<font color='black'>" + str(SLMdate_list[num]) + '   ' + str(SLdata_list[num]) + "<font>")

    def SLS06(self):
        global SLdata_list
        global SLMdate_list
        global index_list
        global status
        status = np.zeros(6)
        global dl
        global ID
        ID = 5
        if file_path:
            sensor_id = SENSOR_ID_LIST[ID]
            index_list = dl.get_SLdata_index(sensor_id)  # 查找传感器数据的索引
            SLdata_list = dl.get_data_st_index(index_list, 11)  # 根据索引值得到数据
            SLMdate_list = dl.get_data_st_index(index_list, 1)
            self.textBrowser_2.clear()
            self.textBrowser_2.append("<font color='black'>" + '   DATE        data(SLS06)   ' + "<font>")
            NUM = len(SLdata_list)
            for num in range(0, NUM):
                self.textBrowser_2.append(
                    "<font color='black'>" + str(SLMdate_list[num]) + '   ' + str(SLdata_list[num]) + "<font>")

    def JY(self):
        global ID
        global error_index_list
        global method
        method = 0
        global status
        status[0] = 1
        LIM_file = "./file/2022_suoli_lim.csv"
        data = pd.read_csv(LIM_file)
        MIN_data = data['MINDATA'].tolist()
        MAX_data = data['MAXDATA'].tolist()
        BASE_data = data['BASE'].tolist()
        # error_index_list = detect_st_threshold(SLdata_list, SENSOR_ID_LIST[ID])
        error_index_list = JY_error(SLdata_list, MAXDATA=MAX_data[ID], MINDATA=MIN_data[ID])
        if file_path:
            # 设置数据层次结构，4行4列
            self.model = QStandardItemModel(len(SLdata_list), 2)
            # 设置水平方向四个头标签文本内容
            self.model.setHorizontalHeaderLabels(['日期', '数据'])
            # 添加数据
            for row in range(len(SLdata_list)):
                for column in range(2):
                    if column == 0:
                        item = QStandardItem(SLMdate_list[row])
                        item.setEditable(False)
                        if row in error_index_list:
                            item.setBackground(QColor('yellow'))
                        else:
                            pass
                        self.model.setItem(row, column, item)
                    elif column == 1:
                        item = QStandardItem(str(SLdata_list[row]))
                        item.setEditable(False)
                        if row in error_index_list:
                            item.setBackground(QColor('yellow'))
                        else:
                            pass
                        self.model.setItem(row, column, item)
            # QTableView 绑定 数据
            self.tableView.setModel(self.model)
            # 水平方向标签拓展剩下的窗口部分，填满表格
            self.tableView.horizontalHeader().setStretchLastSection(True)
            # # 表格宽度高度随内容改变
            # self.tableWidget.resizeColumnToContents(len(SLdata_list))
            # self.tableWidget.resizeRowToContents(2)
            # 水平方向，表格大小拓展到适当的尺寸
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            self.statusBar.showMessage('请先选择要载入的数据文件', 10000)
        self.statusBar.showMessage(str(SENSOR_ID_LIST[int(ID)]) + '数据 经验阈值方法检测完成', 10000)
        # self.textBrowser_2.clear()
        # self.textBrowser_2.append('   DATE        data(JY)   ')
        # for index in range(0, len(SLMdate_list)):
        #     if index in error_index_list:
        #         self.textBrowser_2.append("<font color='red'>" + str(SLMdate_list[index]) + '   ' + str(SLdata_list[index]) + "<font>")
        #     else:
        #         self.textBrowser_2.append("<font color='black'>" + str(SLMdate_list[index]) + '   ' + str(SLdata_list[index]) + "<font>")

    def three_sigma(self):
        global error_index_list
        global ID
        global method
        method = 1
        global status
        status[1] = 1
        if file_path:
            ts = three_sigma()
            error_index_list = ts.three_sigma1_(SLdata_list, np.mean(SLdata_list), np.std(SLdata_list))
            # 设置数据层次结构，4行4列
            self.model = QStandardItemModel(len(SLdata_list), 2)
            # 设置水平方向四个头标签文本内容
            self.model.setHorizontalHeaderLabels(['日期', '数据'])
            # 添加数据
            for row in range(len(SLdata_list)):
                for column in range(2):
                    if column == 0:
                        item = QStandardItem(SLMdate_list[row])
                        item.setEditable(False)
                        if row in error_index_list:
                            item.setBackground(QColor('yellow'))
                        else:
                            pass
                        self.model.setItem(row, column, item)
                    elif column == 1:
                        item = QStandardItem(str(SLdata_list[row]))
                        item.setEditable(False)
                        if row in error_index_list:
                            item.setBackground(QColor('yellow'))
                        else:
                            pass
                        self.model.setItem(row, column, item)
            # QTableView 绑定 数据
            self.tableView.setModel(self.model)
            # 水平方向标签拓展剩下的窗口部分，填满表格
            self.tableView.horizontalHeader().setStretchLastSection(True)
            # # 表格宽度高度随内容改变
            # self.tableWidget.resizeColumnToContents(len(SLdata_list))
            # self.tableWidget.resizeRowToContents(2)
            # 水平方向，表格大小拓展到适当的尺寸
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            self.statusBar.showMessage('请先选择要载入的数据文件', 10000)
        self.statusBar.showMessage(str(SENSOR_ID_LIST[int(ID)]) + '数据 3-sigma方法检测完成', 10000)
        # self.textBrowser_2.clear()
        # self.textBrowser_2.append('   DATE        data(3-sigma)   ')
        # for index in range(0, len(SLMdate_list)):
        #     if index in error_index_list:
        #         self.textBrowser_2.append(
        #             "<font color='red'>" + str(SLMdate_list[index]) + '   ' + str(SLdata_list[index]) + "<font>")
        #     else:
        #         self.textBrowser_2.append(
        #             "<font color='black'>" + str(SLMdate_list[index]) + '   ' + str(SLdata_list[index]) + "<font>")

    def BOX(self):
        global ID
        global error_index_list
        global method
        method = 2
        global status
        status[2] = 1
        if file_path:
            box = box_plot()
            error_index_list = box.box_plot_train(SLdata_list)
            # 设置数据层次结构，4行4列
            self.model = QStandardItemModel(len(SLdata_list), 2)
            # 设置水平方向四个头标签文本内容
            self.model.setHorizontalHeaderLabels(['日期', '数据'])
            # 添加数据
            for row in range(len(SLdata_list)):
                for column in range(2):
                    if column == 0:
                        item = QStandardItem(SLMdate_list[row])
                        item.setEditable(False)
                        if row in error_index_list:
                            item.setBackground(QColor('yellow'))
                        else:
                            pass
                        self.model.setItem(row, column, item)
                    elif column == 1:
                        item = QStandardItem(str(SLdata_list[row]))
                        item.setEditable(False)
                        if row in error_index_list:
                            item.setBackground(QColor('yellow'))
                        else:
                            pass
                        self.model.setItem(row, column, item)
            # QTableView 绑定 数据
            self.tableView.setModel(self.model)
            # 水平方向标签拓展剩下的窗口部分，填满表格
            self.tableView.horizontalHeader().setStretchLastSection(True)
            # # 表格宽度高度随内容改变
            # self.tableWidget.resizeColumnToContents(len(SLdata_list))
            # self.tableWidget.resizeRowToContents(2)
            # 水平方向，表格大小拓展到适当的尺寸
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            self.statusBar.showMessage('请先选择要载入的数据文件', 10000)
        self.statusBar.showMessage(str(SENSOR_ID_LIST[int(ID)]) + '数据 Box_plot方法检测完成', 10000)
        # self.textBrowser_2.clear()
        # self.textBrowser_2.append('   DATE   data(box-plot)   ')
        # for index in range(0, len(SLMdate_list)):
        #     if index in error_index_list:
        #         self.textBrowser_2.append(
        #             "<font color='red'>" + str(SLMdate_list[index]) + '   ' + str(SLdata_list[index]) + "<font>")
        #     else:
        #         self.textBrowser_2.append(
        #             "<font color='black'>" + str(SLMdate_list[index]) + '   ' + str(SLdata_list[index]) + "<font>")

    def ISO_FOREST(self):
        global ID
        global error_index_list
        global method
        method = 3
        global status
        status[3] = 1
        if file_path:
            iso = iostation_forest()
            error_index_list = iso.ioslation_forest_train(SLdata_list)
            # 设置数据层次结构，4行4列
            self.model = QStandardItemModel(len(SLdata_list), 2)
            # 设置水平方向四个头标签文本内容
            self.model.setHorizontalHeaderLabels(['日期', '数据'])
            # 添加数据
            for row in range(len(SLdata_list)):
                for column in range(2):
                    if column == 0:
                        item = QStandardItem(SLMdate_list[row])
                        item.setEditable(False)
                        if row in error_index_list:
                            item.setBackground(QColor('yellow'))
                        else:
                            pass
                        self.model.setItem(row, column, item)
                    elif column == 1:
                        item = QStandardItem(str(SLdata_list[row]))
                        item.setEditable(False)
                        if row in error_index_list:
                            item.setBackground(QColor('yellow'))
                        else:
                            pass
                        self.model.setItem(row, column, item)
            # QTableView 绑定 数据
            self.tableView.setModel(self.model)
            # 水平方向标签拓展剩下的窗口部分，填满表格
            self.tableView.horizontalHeader().setStretchLastSection(True)
            # # 表格宽度高度随内容改变
            # self.tableWidget.resizeColumnToContents(len(SLdata_list))
            # self.tableWidget.resizeRowToContents(2)
            # 水平方向，表格大小拓展到适当的尺寸
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            self.statusBar.showMessage('请先选择要载入的数据文件', 10000)
        self.statusBar.showMessage(str(SENSOR_ID_LIST[int(ID)]) + '数据 Isolation-Forest方法检测完成', 10000)
        # self.textBrowser_2.clear()
        # self.textBrowser_2.append('   DATE data(iso-forest)   ')
        # for index in range(0, len(SLMdate_list)):
        #     if index in error_index_list:
        #         self.textBrowser_2.append(
        #             "<font color='red'>" + str(SLMdate_list[index]) + '   ' + str(SLdata_list[index]) + "<font>")
        #     else:
        #         self.textBrowser_2.append(
        #             "<font color='black'>" + str(SLMdate_list[index]) + '   ' + str(SLdata_list[index]) + "<font>")

    def K_MEANS(self):
        global ID
        global error_index_list
        global method
        method = 4
        global status
        status[4] = 1

        if file_path:
            km = k_means()
            error_index_list = km.k_means_train(3, SLdata_list)
            # 设置数据层次结构，4行4列
            self.model = QStandardItemModel(len(SLdata_list), 2)
            # 设置水平方向四个头标签文本内容
            self.model.setHorizontalHeaderLabels(['日期', '数据'])
            # 添加数据
            for row in range(len(SLdata_list)):
                for column in range(2):
                    if column == 0:
                        item = QStandardItem(SLMdate_list[row])
                        item.setEditable(False)
                        if row in error_index_list:
                            item.setBackground(QColor('yellow'))
                        else:
                            pass
                        self.model.setItem(row, column, item)
                    elif column == 1:
                        item = QStandardItem(str(SLdata_list[row]))
                        item.setEditable(False)
                        if row in error_index_list:
                            item.setBackground(QColor('yellow'))
                        else:
                            pass
                        self.model.setItem(row, column, item)
            # QTableView 绑定 数据
            self.tableView.setModel(self.model)
            # 水平方向标签拓展剩下的窗口部分，填满表格
            self.tableView.horizontalHeader().setStretchLastSection(True)
            # # 表格宽度高度随内容改变
            # self.tableWidget.resizeColumnToContents(len(SLdata_list))
            # self.tableWidget.resizeRowToContents(2)
            # 水平方向，表格大小拓展到适当的尺寸
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            self.statusBar.showMessage('请先选择要载入的数据文件', 10000)
        self.statusBar.showMessage(str(SENSOR_ID_LIST[int(ID)]) + '数据 K_MEANS方法检测完成', 10000)
        # self.textBrowser_2.clear()
        # self.textBrowser_2.append('   DATE    data(k-means)   ')
        # for index in range(0, len(SLMdate_list)):
        #     if index in error_index_list:
        #         self.textBrowser_2.append(
        #             "<font color='red'>" + str(SLMdate_list[index]) + '   ' + str(SLdata_list[index]) + "<font>")
        #     else:
        #         self.textBrowser_2.append(
        #             "<font color='black'>" + str(SLMdate_list[index]) + '   ' + str(SLdata_list[index]) + "<font>")

    def SVM(self):
        global ID
        global error_index_list
        global method
        method = 5
        global status
        status[5] = 1
        if file_path:
            svm = svm_()
            error_index_list = svm.svm_train_(SLdata_list)
            # 设置数据层次结构，4行4列
            self.model = QStandardItemModel(len(SLdata_list), 2)
            # 设置水平方向四个头标签文本内容
            self.model.setHorizontalHeaderLabels(['日期', '数据'])
            # 添加数据
            for row in range(len(SLdata_list)):
                for column in range(2):
                    if column == 0:
                        item = QStandardItem(SLMdate_list[row])
                        item.setEditable(False)
                        if row in error_index_list:
                            item.setBackground(QColor('yellow'))
                        else:
                            pass
                        self.model.setItem(row, column, item)
                    elif column == 1:
                        item = QStandardItem(str(SLdata_list[row]))
                        item.setEditable(False)
                        if row in error_index_list:
                            item.setBackground(QColor('yellow'))
                        else:
                            pass
                        self.model.setItem(row, column, item)
            # QTableView 绑定 数据
            self.tableView.setModel(self.model)
            # 水平方向标签拓展剩下的窗口部分，填满表格
            self.tableView.horizontalHeader().setStretchLastSection(True)
            # # 表格宽度高度随内容改变
            # self.tableWidget.resizeColumnToContents(len(SLdata_list))
            # self.tableWidget.resizeRowToContents(2)
            # 水平方向，表格大小拓展到适当的尺寸
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            self.statusBar.showMessage('请先选择要载入的数据文件', 10000)
        self.statusBar.showMessage(str(SENSOR_ID_LIST[int(ID)]) + '数据 SVM方法检测完成', 10000)
        # self.textBrowser_2.clear()
        # self.textBrowser_2.append('   DATE     data(SVM)   ')
        # for index in range(0, len(SLMdate_list)):
        #     if index in error_index_list:
        #         self.textBrowser_2.append(
        #             "<font color='red'>" + str(SLMdate_list[index]) + '   ' + str(SLdata_list[index]) + "<font>")
        #     else:
        #         self.textBrowser_2.append(
        #             "<font color='black'>" + str(SLMdate_list[index]) + '   ' + str(SLdata_list[index]) + "<font>")

    def ORI_FIG(self):
        # global method
        fig = plt.figure()
        plt.rcParams['font.size'] = 10
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(SLMdate_list, SLdata_list, linewidth=1)
        ax.set_xlabel("Date")
        ax.set_ylabel("SLData")
        # ax.set_title(SENSOR_ID_LIST[ID] + ' ' + str(METHOD[method]))
        ax.set_title(SENSOR_ID_LIST[ID])
        # print(len(error_index_list2))
        # for error_index in error_index_list2:
        #     ax.scatter(SLMdate_list[error_index], SLdata_list[error_index], c="r")
        fig.tight_layout()
        canvas = FigureCanvas(fig)
        pixmap = QtGui.QPixmap(canvas.grab().toImage())
        self.label_2.setScaledContents(True)
        # 设置背景
        self.label_2.setPixmap(pixmap)

    def DECT_FIG(self):
        global method
        global error_index_list
        if error_index_list:
            fig = plt.figure()
            plt.rcParams['font.size'] = 10
            ax = fig.add_subplot(1, 1, 1)
            ax.plot(SLMdate_list, SLdata_list, linewidth=1)
            ax.set_xlabel("Date")
            ax.set_ylabel("SLData")
            ax.set_title(SENSOR_ID_LIST[ID] + ' ' + str(METHOD[method]))
            # ax.set_title(SENSOR_ID_LIST[ID])
            print(len(error_index_list))
            for error_index in error_index_list:
                ax.scatter(SLMdate_list[error_index], SLdata_list[error_index], c="r")
            fig.tight_layout()
            canvas = FigureCanvas(fig)
            pixmap = QtGui.QPixmap(canvas.grab().toImage())
            self.label.setScaledContents(True)
            # 设置背景
            self.label.setPixmap(pixmap)
        else:
            pass
            # 这里用那个statusbar看看怎么使用

    def input_1(self):
        global ID
        # global SLdata_list
        # global SLMdate_list
        ID = 1
        # 月份设置
        i = 1
        # 读取数据文件
        file_path = r"./file"
        year_month = "2022-0" if i < 10 else "2022-"
        file_path += "/" + year_month + str(i) + ".csv"
        dl = ds_load(file_path)
        dl.sort_by_time_order()
        sensor_id = ID
        j = SENSOR_ID_LIST.index(sensor_id)
        index_list = dl.get_SLdata_index(sensor_id)  # 查找传感器数据的索引
        SLdata_list = dl.get_data_st_index(index_list, 11)  # 根据索引值得到数据
        SLMdate_list = dl.get_data_st_index(index_list, 1)
        self.textBrowser_2.append('    DATE         data   ')
        NUM = len(SLdata_list)
        for num in range(0, NUM):
            self.textBrowser_2.append(str(SLMdate_list[num]) + '   ' + str(SLdata_list[num]))

    def ori_image(self):
        global ID
        ID = self.actionSLS01.text()
        if len(SLdata_list) > 0:
            fig = plt.figure()
            plt.rcParams['font.size'] = 10
            sensor_id = ID
            # 画图并存图
            ax = fig.add_subplot(1, 1, 1)
            ax.plot(SLMdate_list, SLdata_list, linewidth=1)
            ax.set_xlabel("Date")
            ax.set_ylabel("SLData")
            ax.set_title(sensor_id + ' ')
            # print(len(error_index_list2))
            # for error_index in error_index_list2:
            #     ax.scatter(SLMdate_list[error_index], SLdata_list[error_index], c="r")
            fig.tight_layout()
            canvas = FigureCanvas(fig)
            pixmap = QtGui.QPixmap(canvas.grab().toImage())
            # self.label.setPixmap(self.label_2.scaled_pixmap)
            self.label_2.setScaledContents(True)
            # 设置背景
            self.label_2.setPixmap(pixmap)

        # # 准备绘图
        # fig = plt.figure()
        # plt.rcParams['font.size'] = 10
        # sensor_id = ID
        # j = SENSOR_ID_LIST.index(sensor_id)
        # index_list = dl.get_SLdata_index(sensor_id)  # 查找传感器数据的索引
        # SLdata_list = dl.get_data_st_index(index_list, 11)  # 根据索引值得到数据
        # SLMdate_list = dl.get_data_st_index(index_list, 0)

if __name__ == '__main__':
    # 界面的入口，在这里需要定义QApplication对象，之后界面跳转时不用重新定义，只需要调用show()函数jikt
    app = QApplication(sys.argv)
    # 显示创建的界面
    MainWindow = Window()  # 创建窗体对象
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程