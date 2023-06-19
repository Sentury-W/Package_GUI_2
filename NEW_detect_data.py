from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from error_detect import detect_st_threshold, fill_point_B_spline1
from error_detect import three_sigma, JY_error, box_plot, iostation_forest, k_means, svm_
from sensor_id_list import SENSOR_ID_LIST
# from sklearn.cluster import DBSCAN

"""
仅在1方法下有基于阈值的数据筛选和补值 其余均为直接检测异常值
"""

METHOD = ['JY', 'box_plot', 'isolation_forest', 'k_means', 'svm']
method = 1    # 五种方法 按照上面的列表选择1~5


"""只改这里就好"""
model = 2     # 模式选择  1-单索力监测  2-某月的所有索力结果汇集在一张图
month = 1     # 进行月份的选择
id = 'SLS20'  # 索力选择 用于监测某月 某一个索力数据  【model=2时 该参数无用】
"""只改这里就好"""


class ds_load():
    def __init__(self, file_path):
        self.file_path = file_path
        self.ds = pd.read_csv(self.file_path, encoding='ANSI', parse_dates=['MDATE'],
                              date_parser=lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))

        self.rows = len(self.ds)
        self.cols = len(self.ds.columns)

        self.SLData_dict = {}
        self.SLMdata_dict = {}

    def sort_by_time_order(self):
        """
        根据时间顺序进行排序
        """
        self.ds = self.ds.sort_values(by='MDATE')
        self.ds = self.ds.reset_index(drop=True)

    def get_SLdata_index(self, sensor_id):
        """
        arg:sensor_id type str
        return: index_list 某一个传感器的全部数据的索引列表
        """
        sensor_id_df = self.ds[['SENSOR_ID']]
        index_list = []
        for i in range(self.rows):
            if str(sensor_id_df.iloc[i, 0]) == sensor_id:
                index_list.append(i)
        return index_list

    def get_data_st_index(self, index_list, column_index):
        """
        arg:index_list type list 数据的行索引列表 colunm_index type int 需要取得的数据的列索引
        return: SLdata_list type list 根据索引值得到数据列表
        根据行索引列表以及列索引取得相应数据列表
        """
        SLdata_list = []
        for index in index_list:
            SLdata_list.append(self.ds.iloc[index, column_index])
        return SLdata_list

    def df2dict_SLData_Date(self, country_id):
        """
        arg:country_id type bool China 0 Russsia 1
        将索力数据转换成字典形式
        example: {"SLS01": [1, 3, 5, 6 ,7], "SLS02":[2, 5, 7 ,8], ...}
        """
        self.SLData_dict = {}
        self.SLMdata_dict = {}
        SENSOR_PRIFIX = "SLS" if country_id == 0 else "SLX"
        for i in range(1, 25, 1):
            if i < 10:
                sensor_id = SENSOR_PRIFIX + "0" + str(i)
            elif 9 < i < 25:
                sensor_id = SENSOR_PRIFIX + str(i)
            # print(sensor_id)
            index_list = self.get_SLdata_index(sensor_id)
            SLdata_list = self.get_data_st_index(index_list, 11)
            SLMDATE_list = self.get_data_st_index(index_list, 0)
            self.SLData_dict[str(sensor_id)] = SLdata_list
            self.SLMdata_dict[str(sensor_id)] = SLMDATE_list

    # def get_one_day_index(self, sensor_id, day_id):
    #     """
    #     取出某传感器某一天的数据
    #     """
    #     one_day_index = []
    #     for i in range(self.rows):
    #         # print(type(self.ds.iloc[i, 0].day), type(self.ds.iloc[i, 2]))
    #         if self.ds.iloc[i, 0].day == day_id and self.ds.iloc[i, 2] == sensor_id:
    #             # print(self.ds.iloc[i, 0].day, self.ds.iloc[i, 2])
    #             one_day_index.append(i)
    #     return one_day_index


class get_value(object):
    def get_mean(self, SLdata_list, error_index_list):
        new_SLdata_list = []
        for i in range(len(SLdata_list)):
            if i in error_index_list:
                pass
            else:
                new_SLdata_list.append(SLdata_list[i])
        return np.mean(new_SLdata_list), np.std(new_SLdata_list)

    def get_center_distance(self, SLdata_list, error_index_list):
        new_SLdata_list = []
        for i in range(len(SLdata_list)):
            if i in error_index_list:
                pass
            else:
                new_SLdata_list.append(SLdata_list[i])
        SLdata_mean = np.mean(new_SLdata_list)
        # print(SLdata_mean)
        # print(len(new_SLdata_list))
        # print(np.sum(new_SLdata_list))
        # print(len(new_SLdata_list) * SLdata_mean)
        # print(np.max(new_SLdata_list) - SLdata_mean)
        return (np.sum(new_SLdata_list) - len(new_SLdata_list) * SLdata_mean) / len(new_SLdata_list)


def Z_score(SLdata_list):
    new_list = []
    if np.std(SLdata_list) != 0:
        for data in SLdata_list:
            new_list.append((data - np.mean(SLdata_list)) / np.std(SLdata_list))
    else:
        new_list = eval("[" + ",".join("0" * len(SLdata_list)) + "]")
    return new_list

# @return_index
# def Dbscan_train(SLdata_list):
#     db = DBSCAN(eps=0.65, min_samples=25).fit(np.array(SLdata_list).reshape(-1, 1))
#     return db.labels_


if __name__ == "__main__":
    # 读取对应月份的数据
    i = month
    file_path = r"./file"
    year_month = "2022-0" if i < 10 else "2022-"
    file_path += "/" + year_month + str(i) + ".csv"
    dl = ds_load(file_path)
    dl.sort_by_time_order()

    if model == 1:
        fg = plt.figure(figsize=(15, 10))
        sensor_id = id
        j = SENSOR_ID_LIST.index(sensor_id)
        index_list = dl.get_SLdata_index(sensor_id)  # 查找传感器数据的索引
        SLdata_list = dl.get_data_st_index(index_list, 11)  # 根据索引值得到数据
        SLMdate_list = dl.get_data_st_index(index_list, 0)

        if method == 1:
            LIM_file = "./file/2022_suoli_lim.csv"
            data = pd.read_csv(LIM_file)
            MIN_data = data['MINDATA'].tolist()
            MAX_data = data['MAXDATA'].tolist()
            BASE_data = data['BASE'].tolist()

            ts = three_sigma()
            error_index_list2 = JY_error(SLdata_list, MAXDATA=MAX_data[j], MINDATA=MIN_data[j])
            # error_index_list = detect_st_threshold(SLdata_list, sensor_id)
            # new_list = fill_point_B_spline1(SLdata_list, error_index_list)
            # error_index_list2 = ts.three_sigma2_(new_list, np.mean(new_list), np.std(new_list), MAX=MAX_data[j],
            #                                      MIN=MIN_data[j])
            # SLdata_list = new_list

        elif method == 2:
            box = box_plot()
            error_index_list2 = box.box_plot_train(SLdata_list)
        elif method == 3:
            iso = iostation_forest()
            error_index_list2 = iso.ioslation_forest_train(SLdata_list)
        elif method == 4:
            km = k_means()
            error_index_list2 = km.k_means_train(3, SLdata_list)
        elif method == 5:
            svm = svm_()
            error_index_list2 = svm.svm_train_(SLdata_list)
        # elif method == 6:
        #     # DB = DBscan()
        #     new_SLdata_list = Z_score(SLdata_list)
        #     error_index_list2 = Dbscan_train(new_SLdata_list)
        else:
            print('ERROR METHOD!!!')

        ax = fg.add_subplot(1, 1, 1)
        ax.plot(SLMdate_list, SLdata_list)
        ax.set_xlabel("Date")
        ax.set_ylabel("SLDate")
        ax.set_title(sensor_id + ' ' + METHOD[method - 1])
        for error_index in error_index_list2:
            ax.scatter(SLMdate_list[error_index], SLdata_list[error_index], c="r")
        fg.savefig(str(i) + "-" + sensor_id + ' ' + METHOD[method - 1] + '.jpg')


    elif model == 2:
        fg = plt.figure(figsize=(50, 40))
        for sensor_id in SENSOR_ID_LIST:
            index_list = dl.get_SLdata_index(sensor_id)  # 查找传感器数据的索引
            SLdata_list = dl.get_data_st_index(index_list, 11)  # 根据索引值得到数据
            SLMdate_list = dl.get_data_st_index(index_list, 0)
            j = SENSOR_ID_LIST.index(sensor_id)

            if method == 1:
                LIM_file = "F:/2022_suoli_lim.csv"
                data = pd.read_csv(LIM_file)
                MIN_data = data['MINDATA'].tolist()
                MAX_data = data['MAXDATA'].tolist()
                BASE_data = data['BASE'].tolist()

                ts = three_sigma()
                error_index_list2 = JY_error(SLdata_list, MAXDATA=MAX_data[j], MINDATA=MIN_data[j])
                # new_list = fill_point_B_spline1(SLdata_list, error_index_list)
                # error_index_list2 = ts.three_sigma2_(new_list, np.mean(new_list), np.std(new_list), MAX=MAX_data[j],
                #                                      MIN=MIN_data[j])
            elif method == 2:
                box = box_plot()
                error_index_list2 = box.box_plot_train(SLdata_list)
            elif method == 3:
                iso = iostation_forest()
                error_index_list2 = iso.ioslation_forest_train(SLdata_list)
            elif method == 4:
                km = k_means()
                error_index_list2 = km.k_means_train(3, SLdata_list)
            elif method == 5:
                svm = svm_()
                error_index_list2 = svm.svm_train_(SLdata_list)
            # elif method == 6:
            #     # DB = DBscan()
            #     new_SLdata_list = Z_score(SLdata_list)
            #     error_index_list2 = Dbscan_train(new_SLdata_list)
            else:
                print('ERROR METHOD!!!')

            # ax = fg.add_subplot(24, 2, SENSOR_ID_LIST.index(sensor_id) + 1)
            ax = fg.add_subplot(12, 4, SENSOR_ID_LIST.index(sensor_id) + 1)
            ax.plot(SLMdate_list, SLdata_list)
            ax.set_xlabel("Date")
            ax.set_ylabel("SLDate")
            ax.set_title(sensor_id + ' ' + METHOD[method - 1])
            for error_index in error_index_list2:
                ax.scatter(SLMdate_list[error_index], SLdata_list[error_index], c="r")
        fg.tight_layout()
        fg.savefig(str(i) + '月 ' + METHOD[method - 1] + '.jpg')
        # fg.savefig(str(i) + '月 ' + '-JY' + '.jpg')
