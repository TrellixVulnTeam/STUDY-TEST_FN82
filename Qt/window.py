# Form implementation generated from reading ui file 'checktickets.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import PyQt6.QtCore
from PyQt6 import QtCore, QtGui, QtWidgets
from get_station import *
from query_request import *
import sys
import time


class Ui_CheckTickets(object):
    def setupUi(self, CheckTickets):
        CheckTickets.setObjectName("CheckTickets")  # 设置窗口对象名称
        CheckTickets.resize(1170, 700)  # 设置窗口大小

        CheckTickets.setMinimumSize(QtCore.QSize(1170, 700))  # 主窗口最大值
        CheckTickets.setMaximumSize(QtCore.QSize(1170, 700))  # 主窗口最小值

        self.centralwidget = QtWidgets.QWidget(CheckTickets)  # 主窗口的widget控件
        self.centralwidget.setObjectName("centralwidget")  # 设置对象名称
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(5, 5, 1160, 120))
        self.label_img.setObjectName("label_img")

        img = QtGui.QPixmap(r'img.png')  # 打开顶部位图
        self.label_img.setPixmap(img)  # 设置调色板
        self.label_img.setScaledContents(True)  # 将图片缩放为控件尺寸

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(5, 250, 1160, 450))
        self.tableView.setObjectName("tableView")
        self.model = QtGui.QStandardItemModel()  # 创建存储数据的模式
        self.tableView.horizontalHeader().setVisible(False)  # 设置表头不可见
        self.tableView.verticalHeader().setVisible(False)  # 设置纵向表头不可见
        # 设置表格内容文字大小
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableView.setFont(font)
        # 设置滚动条
        self.scrollBar = QtWidgets.QScrollBar(self.tableView)
        self.scrollBar.setGeometry(QtCore.QRect(1140, 0, 20, 430))
        self.scrollBar.setObjectName("scrollBar")

        self.widget_query = QtWidgets.QWidget(self.centralwidget)
        self.widget_query.setGeometry(QtCore.QRect(5, 125, 1165, 50))
        self.widget_query.setObjectName("widget_query")
        self.label_1 = QtWidgets.QLabel(self.widget_query)
        self.label_1.setGeometry(QtCore.QRect(5, 0, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_1.setFont(font)
        self.label_1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.widget_query)
        self.label_2.setGeometry(QtCore.QRect(300, 0, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_query)
        self.label_3.setGeometry(QtCore.QRect(600, 0, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.widget_query)
        self.pushButton.setGeometry(QtCore.QRect(950, 10, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pushButton.setObjectName("pushButton")
        self.textEdit_1 = QtWidgets.QTextEdit(self.widget_query)
        self.textEdit_1.setGeometry(QtCore.QRect(115, 10, 150, 30))
        self.textEdit_1.setObjectName("textEdit_1")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_query)
        self.textEdit_2.setGeometry(QtCore.QRect(415, 10, 150, 30))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget_query)
        self.textEdit_3.setGeometry(QtCore.QRect(715, 10, 150, 30))
        self.textEdit_3.setObjectName("textEdit_3")
        self.widget_checkbox = QtWidgets.QWidget(self.centralwidget)
        self.widget_checkbox.setGeometry(QtCore.QRect(5, 180, 1165, 50))
        self.widget_checkbox.setObjectName("widget_checkbox")
        self.label_type = QtWidgets.QLabel(self.widget_checkbox)
        self.label_type.setGeometry(QtCore.QRect(50, 0, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_type.setFont(font)
        self.label_type.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_type.setObjectName("label_type")
        self.checkBox_G = QtWidgets.QCheckBox(self.widget_checkbox)
        self.checkBox_G.setGeometry(QtCore.QRect(200, 0, 120, 50))
        self.checkBox_G.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_G.setFont(font)
        self.checkBox_G.setStyleSheet("QCheckBox::indicator {width: 30px; height: 30px;}")
        self.checkBox_G.setObjectName("checkBox_G")
        self.checkBox_D = QtWidgets.QCheckBox(self.widget_checkbox)
        self.checkBox_D.setGeometry(QtCore.QRect(350, 0, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_D.setFont(font)
        self.checkBox_D.setStyleSheet("QCheckBox::indicator {width: 30px; height: 30px;}")
        self.checkBox_D.setObjectName("checkBox_D")
        self.checkBox_Z = QtWidgets.QCheckBox(self.widget_checkbox)
        self.checkBox_Z.setGeometry(QtCore.QRect(500, 0, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Z.setFont(font)
        self.checkBox_Z.setStyleSheet("QCheckBox::indicator {width: 30px; height: 30px;}")
        self.checkBox_Z.setObjectName("checkBox_Z")
        self.checkBox_T = QtWidgets.QCheckBox(self.widget_checkbox)
        self.checkBox_T.setGeometry(QtCore.QRect(650, 0, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_T.setFont(font)
        self.checkBox_T.setStyleSheet("QCheckBox::indicator {width: 30px; height: 30px;}")
        self.checkBox_T.setObjectName("checkBox_T")
        self.checkBox_K = QtWidgets.QCheckBox(self.widget_checkbox)
        self.checkBox_K.setGeometry(QtCore.QRect(800, 0, 120, 50))
        self.checkBox_K.setSizeIncrement(QtCore.QSize(0, 0))
        self.checkBox_K.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_K.setFont(font)
        self.checkBox_K.setStyleSheet("QCheckBox::indicator {width: 30px; height: 30px;}")
        self.checkBox_K.setObjectName("checkBox_K")
        CheckTickets.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CheckTickets)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1170, 22))
        self.menubar.setObjectName("menubar")
        CheckTickets.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CheckTickets)
        self.statusbar.setObjectName("statusbar")
        CheckTickets.setStatusBar(self.statusbar)

        self.retranslateUi(CheckTickets)
        QtCore.QMetaObject.connectSlotsByName(CheckTickets)

    def retranslateUi(self, CheckTickets):
        _translate = QtCore.QCoreApplication.translate
        CheckTickets.setWindowTitle(_translate("CheckTickets", "CheckTickets"))
        # self.label_img.setText(_translate("CheckTickets", "TextLabel"))
        self.label_1.setText(_translate("CheckTickets", "出发地："))
        self.label_2.setText(_translate("CheckTickets", "目的地："))
        self.label_3.setText(_translate("CheckTickets", "出发日："))
        self.pushButton.setText(_translate("CheckTickets", "查询"))
        self.label_type.setText(_translate("CheckTickets", "车次类型："))
        self.checkBox_G.setText(_translate("CheckTickets", "GC-高铁"))
        self.checkBox_D.setText(_translate("CheckTickets", "D-动车"))
        self.checkBox_Z.setText(_translate("CheckTickets", "Z-直达"))
        self.checkBox_T.setText(_translate("CheckTickets", "T-特快"))
        self.checkBox_K.setText(_translate("CheckTickets", "K-快速"))

        self.textEdit_3.setText(get_time())
        # self.pushButton.clicked.connect(self.on_click())
        # self.checkBox_G.stateChanged.connect(self.change_G(True))
        # self.checkBox_D.stateChanged.connect(self.change_D(True))
        # self.checkBox_Z.stateChanged.connect(self.change_Z(True))
        # self.checkBox_T.stateChanged.connect(self.change_T(True))
        # self.checkBox_K.stateChanged.connect(self.change_K(True))

    # 复选框事件处理
    def change_G(self, state):
        if state:
            g_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            r_g_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    def change_D(self, state):
        if state == QtCore.Qt.CheckState:
            d_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            r_d_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    def change_Z(self, state):
        if state == QtCore.Qt.CheckState:
            z_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            r_z_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    def change_T(self, state):
        if state == QtCore.Qt.CheckState:
            t_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            r_t_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    def change_K(self, state):
        if state == QtCore.Qt.CheckState:
            k_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            r_k_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    # 将所有车次分类复选框取消勾选
    def checkBox_default(self):
        self.checkBox_G.setChecked(False)
        self.checkBox_D.setChecked(False)
        self.checkBox_Z.setChecked(False)
        self.checkBox_T.setChecked(False)
        self.checkBox_K.setChecked(False)

    # 显示消息提示框，参数title为提示框标题文字，message为提示信息
    def messageDialong(self, title, message):
        msg_box = QtWidgets.QMessageBox.warning(self.centralwidget,title, message)
        msg_box.exec()

    # 显示车次信息的表格
    def displayTable(self, train, info, data):  # train为共有多少列车(行)，info为该次列车的具体信息(列)
        self.model.clear()
        for row in range(train):
            for column in range(info):
                item = QtGui.QStandardItem(data[row][column])
                self.model.setItem(row, column, item)
        self.tableView.setModel(self.model)

    # 查询按钮的单机事件
    def on_click(self):
        get_from = self.textEdit_1.toPlainText()
        get_to = self.textEdit_2.toPlainText()
        get_date = self.textEdit_3.toPlainText()
        # 判断车站文件是否存在
        if isStations() == True:
            stations = eval(read())
            if get_from != "" and get_to != "" and get_date != "":
                if get_from in stations and get_to in stations and is_vaild_date(get_date):
                    inputYearDay = time.strptime(get_date,"%Y-%m-%d").tm_yday
                    yearToday = time.localtime(time.time()) .tm_yday
                    timeDifference = inputYearDay-yearToday
                    if 0<=timeDifference<=28:
                        from_station = stations[get_from]
                        to_station = stations[get_to]
                        data = query(get_date,from_station,to_station)
                        self.checkBox_default()
                        if len(data)!=0:
                            self.displayTable(len(data),16,data)
                        else:
                            self.messageDialong('warning','没有返回的网络数据')
                    else:
                        self.messageDialong('warning','超出查询日期的范围')
                else:
                    self.messageDialong('warning', '输入的站名不存在或日期格式不正确')
            else:
                self.messageDialong('warning', '请填写车站名称和日期')
        else:
            self.messageDialong('warning', '未下载车站查询文件')


def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)  # 实例化QAppication类，作为GUI主程序入口
    MainWindow = QtWidgets.QMainWindow()  # 创建MainWindow类
    ui = Ui_CheckTickets()  # 实例UI类
    ui.setupUi(MainWindow)  # 设置窗体UI
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec())  # 结束主循环过程


# 获取系统当前时间并转换请求数据所需要的格式
def get_time():
    now = int(time.time())
    timeStruct = time.localtime(now)
    strTime = time.strftime('%Y-%m-%d', timeStruct)
    return strTime


# 判断是否是一个有效的日期字符串
def is_vaild_date(str):
    try:
        time.strptime(str, '%Y-%m-%d')
        return True
    except:
        return False


if __name__ == '__main__':
    if isStations() == False:
        getStation()
        show_MainWindow()
    else:
        show_MainWindow()
