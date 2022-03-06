# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets

import csv
import sqlite3
import sys
from time import time
from random import randint
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QGroupBox, QFormLayout, QInputDialog

NAME, POINTS = '', 0
sqlite_connection = sqlite3.connect('PyQuiz.db')
cur = sqlite_connection.cursor()
result = cur.execute("""SELECT id FROM Authors""")
ID = 1
list1 = []
for i in result:
    list1.append(i[0])
while ID in list1:
    ID = randint(1, 1000)
sqlite_connection.commit()
cur.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 519)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.first_window = QtWidgets.QWidget(self.centralwidget)
        self.first_window.setEnabled(True)
        self.first_window.setGeometry(QtCore.QRect(0, 0, 791, 561))
        self.first_window.setStyleSheet("QWidget {\n"
"    background-color: none;\n"
"}")
        self.first_window.setObjectName("first_window")
        self.pyquiz_label = QtWidgets.QLabel(self.first_window)
        self.pyquiz_label.setGeometry(QtCore.QRect(140, 60, 221, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(25, 102, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 34, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 102, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 102, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 34, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 34, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 102, 244, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 102, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 34, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 102, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 102, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 34, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 34, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 102, 244, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 102, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 34, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 102, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 102, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 34, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 34, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 102, 244, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.pyquiz_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pyquiz_label.setFont(font)
        self.pyquiz_label.setStyleSheet("QLabel {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.pyquiz_label.setWordWrap(False)
        self.pyquiz_label.setObjectName("pyquiz_label")
        self.start_button = QtWidgets.QPushButton(self.first_window)
        self.start_button.setGeometry(QtCore.QRect(135, 285, 221, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 20;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.start_button.setObjectName("start_button")
        self.pushButton_info = QtWidgets.QPushButton(self.first_window)
        self.pushButton_info.setGeometry(QtCore.QRect(40, 460, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_info.setFont(font)
        self.pushButton_info.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: rgb(120, 120, 120);\n"
"    border-radius: 10;\n"
"}")
        self.pushButton_info.setObjectName("pushButton_info")
        self.name_window = QtWidgets.QWidget(self.centralwidget)
        self.name_window.setGeometry(QtCore.QRect(0, 0, 791, 561))
        self.name_window.setObjectName("name_window")
        self.name_label = QtWidgets.QLabel(self.name_window)
        self.name_label.setGeometry(QtCore.QRect(70, 110, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("QLabel {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.name_label.setObjectName("name_label")
        self.enter_name_LE = QtWidgets.QLineEdit(self.name_window)
        self.enter_name_LE.setGeometry(QtCore.QRect(60, 270, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enter_name_LE.setFont(font)
        self.enter_name_LE.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(10, 162, 10);\n"
"    border-radius: 10;\n"
"}")
        self.enter_name_LE.setObjectName("enter_name_LE")
        self.enter_name_bt = QtWidgets.QPushButton(self.name_window)
        self.enter_name_bt.setGeometry(QtCore.QRect(150, 390, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.enter_name_bt.setFont(font)
        self.enter_name_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 20;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.enter_name_bt.setObjectName("enter_name_bt")
        self.no_name = QtWidgets.QLabel(self.name_window)
        self.no_name.setGeometry(QtCore.QRect(80, 335, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.no_name.setFont(font)
        self.no_name.setStyleSheet("QLabel {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.no_name.setObjectName("no_name")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(930, 10, 20, 20))
        self.exit_button.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: rgb(13, 208, 16);\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}\n"
"")
        self.exit_button.setObjectName("exit_button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-250, 0, 1221, 631))
        self.label_4.setStyleSheet("QLabel {\n"
"    border-radius: 30px;\n"
"}")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Python.jpg"))
        self.label_4.setObjectName("label_4")
        self.glhf_window = QtWidgets.QWidget(self.centralwidget)
        self.glhf_window.setGeometry(QtCore.QRect(0, 0, 790, 560))
        self.glhf_window.setObjectName("glhf_window")
        self.glhf_lb = QtWidgets.QLabel(self.glhf_window)
        self.glhf_lb.setGeometry(QtCore.QRect(20, 100, 451, 201))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.glhf_lb.setFont(font)
        self.glhf_lb.setStyleSheet("QLabel {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.glhf_lb.setObjectName("glhf_lb")
        self.start_test_bt = QtWidgets.QPushButton(self.glhf_window)
        self.start_test_bt.setGeometry(QtCore.QRect(160, 330, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.start_test_bt.setFont(font)
        self.start_test_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 20;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.start_test_bt.setObjectName("start_test_bt")
        self.first_quest = QtWidgets.QWidget(self.centralwidget)
        self.first_quest.setGeometry(QtCore.QRect(0, 0, 911, 560))
        self.first_quest.setObjectName("first_quest")
        self.comics = QtWidgets.QLabel(self.first_quest)
        self.comics.setGeometry(QtCore.QRect(390, -80, 591, 681))
        self.comics.setText("")
        self.comics.setPixmap(QtGui.QPixmap("python_xkcd.png"))
        self.comics.setObjectName("comics")
        self.about_comics_text = QtWidgets.QLabel(self.first_quest)
        self.about_comics_text.setGeometry(QtCore.QRect(50, 40, 311, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.about_comics_text.setFont(font)
        self.about_comics_text.setStyleSheet("QLabel {\n"
"    color: rgb(13, 208, 16);\n"
"}")
        self.about_comics_text.setObjectName("about_comics_text")
        self.false_2 = QtWidgets.QRadioButton(self.first_quest)
        self.false_2.setGeometry(QtCore.QRect(90, 210, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.false_2.setFont(font)
        self.false_2.setStyleSheet("QRadioButton {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.false_2.setObjectName("false_2")
        self.false_4 = QtWidgets.QRadioButton(self.first_quest)
        self.false_4.setGeometry(QtCore.QRect(90, 250, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.false_4.setFont(font)
        self.false_4.setStyleSheet("QRadioButton {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.false_4.setObjectName("false_4")
        self.true_2 = QtWidgets.QRadioButton(self.first_quest)
        self.true_2.setGeometry(QtCore.QRect(90, 290, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.true_2.setFont(font)
        self.true_2.setStyleSheet("QRadioButton {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.true_2.setObjectName("true_2")
        self.false_3 = QtWidgets.QRadioButton(self.first_quest)
        self.false_3.setGeometry(QtCore.QRect(90, 330, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.false_3.setFont(font)
        self.false_3.setStyleSheet("QRadioButton {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.false_3.setObjectName("false_3")
        self.false_5 = QtWidgets.QRadioButton(self.first_quest)
        self.false_5.setGeometry(QtCore.QRect(90, 370, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.false_5.setFont(font)
        self.false_5.setStyleSheet("QRadioButton {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.false_5.setObjectName("false_5")
        self.ans_fir_bt = QtWidgets.QPushButton(self.first_quest)
        self.ans_fir_bt.setGeometry(QtCore.QRect(90, 440, 131, 28))
        self.ans_fir_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.ans_fir_bt.setObjectName("ans_fir_bt")
        self.last_bt_test_w = QtWidgets.QWidget(self.centralwidget)
        self.last_bt_test_w.setGeometry(QtCore.QRect(0, 0, 790, 560))
        self.last_bt_test_w.setObjectName("last_bt_test_w")
        self.label = QtWidgets.QLabel(self.last_bt_test_w)
        self.label.setGeometry(QtCore.QRect(40, 80, 381, 221))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: rgb(13, 208, 16);\n"
"}")
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.nothing = QtWidgets.QPushButton(self.last_bt_test_w)
        self.nothing.setGeometry(QtCore.QRect(150, 380, 141, 31))
        self.nothing.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.nothing.setText("")
        self.nothing.setObjectName("nothing")
        self.results_w = QtWidgets.QWidget(self.centralwidget)
        self.results_w.setGeometry(QtCore.QRect(0, 0, 760, 560))
        self.results_w.setObjectName("results_w")
        self.scrollArea = QtWidgets.QScrollArea(self.results_w)
        self.scrollArea.setGeometry(QtCore.QRect(20, 80, 431, 351))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("background-color: rgb(98, 139, 85);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 429, 349))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.res_l = QtWidgets.QLabel(self.results_w)
        self.res_l.setGeometry(QtCore.QRect(160, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.res_l.setFont(font)
        self.res_l.setStyleSheet("QLabel {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.res_l.setObjectName("res_l")
        self.cr_csv_bt = QtWidgets.QPushButton(self.results_w)
        self.cr_csv_bt.setGeometry(QtCore.QRect(40, 460, 171, 31))
        self.cr_csv_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.cr_csv_bt.setObjectName("cr_csv_bt")
        self.clear_bd_bt = QtWidgets.QPushButton(self.results_w)
        self.clear_bd_bt.setGeometry(QtCore.QRect(260, 460, 171, 31))
        self.clear_bd_bt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.clear_bd_bt.setObjectName("clear_bd_bt")
        self.sec_quest_window = QtWidgets.QWidget(self.centralwidget)
        self.sec_quest_window.setGeometry(QtCore.QRect(0, 0, 760, 560))
        self.sec_quest_window.setObjectName("sec_quest_window")
        self.label_3 = QtWidgets.QLabel(self.sec_quest_window)
        self.label_3.setGeometry(QtCore.QRect(140, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: rgb(13, 208, 16);\n"
"}")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.sec_quest_window)
        self.lineEdit.setGeometry(QtCore.QRect(170, 393, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(139, 139, 139);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.sec_quest_window)
        self.label_5.setGeometry(QtCore.QRect(90, 380, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(223, 149, 0)")
        self.label_5.setObjectName("label_5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.sec_quest_window)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 110, 491, 231))
        self.plainTextEdit.setStyleSheet("background-color: rgb(140, 255, 105);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton = QtWidgets.QPushButton(self.sec_quest_window)
        self.pushButton.setGeometry(QtCore.QRect(150, 450, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.fird_ques_window = QtWidgets.QWidget(self.centralwidget)
        self.fird_ques_window.setGeometry(QtCore.QRect(0, 0, 760, 560))
        self.fird_ques_window.setObjectName("fird_ques_window")
        self.label_6 = QtWidgets.QLabel(self.fird_ques_window)
        self.label_6.setGeometry(QtCore.QRect(30, 40, 441, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel {\n"
"    color: rgb(13, 208, 16);\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.fird_ques_window)
        self.label_7.setGeometry(QtCore.QRect(140, 170, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(199, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.fird_ques_window)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 310, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.fird_ques_window)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 400, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 20;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.four_ques_window = QtWidgets.QWidget(self.centralwidget)
        self.four_ques_window.setGeometry(QtCore.QRect(0, 0, 760, 560))
        self.four_ques_window.setObjectName("four_ques_window")
        self.label_8 = QtWidgets.QLabel(self.four_ques_window)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 431, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel {\n"
"    color: rgb(162, 83, 165);\n"
"}")
        self.label_8.setObjectName("label_8")
        self.true_3 = QtWidgets.QRadioButton(self.four_ques_window)
        self.true_3.setGeometry(QtCore.QRect(240, 290, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.true_3.setFont(font)
        self.true_3.setStyleSheet("QRadioButton {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.true_3.setObjectName("true_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.four_ques_window)
        self.radioButton_2.setGeometry(QtCore.QRect(70, 230, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("QRadioButton {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.four_ques_window)
        self.radioButton_3.setGeometry(QtCore.QRect(70, 170, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("QRadioButton {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.four_ques_window)
        self.radioButton_4.setGeometry(QtCore.QRect(70, 290, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("QRadioButton {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.four_ques_window)
        self.radioButton_5.setGeometry(QtCore.QRect(240, 230, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setStyleSheet("QRadioButton {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.four_ques_window)
        self.radioButton_6.setGeometry(QtCore.QRect(240, 170, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setStyleSheet("QRadioButton {\n"
"    color: rgb(25, 102, 244);\n"
"}")
        self.radioButton_6.setObjectName("radioButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.four_ques_window)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 390, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.five_quest_window = QtWidgets.QWidget(self.centralwidget)
        self.five_quest_window.setGeometry(QtCore.QRect(0, 0, 760, 560))
        self.five_quest_window.setObjectName("five_quest_window")
        self.label_9 = QtWidgets.QLabel(self.five_quest_window)
        self.label_9.setGeometry(QtCore.QRect(0, 60, 541, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel {\n"
"    color: rgb(218, 107, 255);\n"
"}")
        self.label_9.setObjectName("label_9")
        self.radioButton_7 = QtWidgets.QRadioButton(self.five_quest_window)
        self.radioButton_7.setGeometry(QtCore.QRect(120, 230, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setStyleSheet("color: rgb(109, 188, 212);")
        self.radioButton_7.setObjectName("radioButton_7")
        self.true_4 = QtWidgets.QRadioButton(self.five_quest_window)
        self.true_4.setGeometry(QtCore.QRect(120, 280, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.true_4.setFont(font)
        self.true_4.setStyleSheet("color: rgb(109, 188, 212);")
        self.true_4.setObjectName("true_4")
        self.radioButton_9 = QtWidgets.QRadioButton(self.five_quest_window)
        self.radioButton_9.setGeometry(QtCore.QRect(120, 330, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setStyleSheet("color: rgb(109, 188, 212);")
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.five_quest_window)
        self.radioButton_10.setGeometry(QtCore.QRect(120, 380, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setStyleSheet("color: rgb(109, 188, 212);")
        self.radioButton_10.setObjectName("radioButton_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.five_quest_window)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 450, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.six_q_window = QtWidgets.QWidget(self.centralwidget)
        self.six_q_window.setGeometry(QtCore.QRect(0, 0, 760, 560))
        self.six_q_window.setObjectName("six_q_window")
        self.label_10 = QtWidgets.QLabel(self.six_q_window)
        self.label_10.setGeometry(QtCore.QRect(0, 90, 581, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(170, 170, 255);")
        self.label_10.setObjectName("label_10")
        self.spinBox = QtWidgets.QSpinBox(self.six_q_window)
        self.spinBox.setGeometry(QtCore.QRect(230, 250, 71, 41))
        self.spinBox.setObjectName("spinBox")
        self.pushButton_5 = QtWidgets.QPushButton(self.six_q_window)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 380, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.seven_q_window = QtWidgets.QWidget(self.centralwidget)
        self.seven_q_window.setGeometry(QtCore.QRect(0, 0, 760, 560))
        self.seven_q_window.setObjectName("seven_q_window")
        self.label_11 = QtWidgets.QLabel(self.seven_q_window)
        self.label_11.setGeometry(QtCore.QRect(160, 80, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(170, 170, 127);")
        self.label_11.setObjectName("label_11")
        self.spinBox_2 = QtWidgets.QSpinBox(self.seven_q_window)
        self.spinBox_2.setGeometry(QtCore.QRect(220, 220, 71, 41))
        self.spinBox_2.setObjectName("spinBox_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.seven_q_window)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 410, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.eight_q_w = QtWidgets.QWidget(self.centralwidget)
        self.eight_q_w.setGeometry(QtCore.QRect(0, 0, 760, 560))
        self.eight_q_w.setObjectName("eight_q_w")
        self.label_12 = QtWidgets.QLabel(self.eight_q_w)
        self.label_12.setGeometry(QtCore.QRect(180, 100, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_12.setObjectName("label_12")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.eight_q_w)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 270, 113, 22))
        self.lineEdit_3.setStyleSheet("background-color: rgb(177, 177, 177);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.eight_q_w)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 410, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(13, 208, 16);\n"
"    color: black;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(12, 184, 12);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_4.raise_()
        self.first_window.raise_()
        self.name_window.raise_()
        self.exit_button.raise_()
        self.glhf_window.raise_()
        self.first_quest.raise_()
        self.last_bt_test_w.raise_()
        self.results_w.raise_()
        self.sec_quest_window.raise_()
        self.fird_ques_window.raise_()
        self.four_ques_window.raise_()
        self.five_quest_window.raise_()
        self.six_q_window.raise_()
        self.seven_q_window.raise_()
        self.eight_q_w.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pyquiz_label.setText(_translate("MainWindow", "PyQuiz"))
        self.start_button.setText(_translate("MainWindow", "НАЧАТЬ"))
        self.pushButton_info.setToolTip(_translate("MainWindow", "<html><head/><body><p>PyQuiz <span style=\" font-weight:400;\">-это приложение, созданное для вычисления самого умного человека в твоём окружении.</span></p><p><span style=\" font-weight:400;\">Квиз состоит из вопросов на тему программирования на Python, на которые тебе предстоит ответить. Времени на открытие учебника нет!</span></p><p><span style=\" font-weight:400;\">Повтори всё, что ты уже знаешь (а тем более, какие-нибудь интересные особенности нашего языка).</span></p><p><span style=\" font-weight:400;\">Секунды играют важную роль на твой конечный балл. После прохождения всех преград, ты узнаешь своё место в рейтинге.</span></p></body></html>"))
        self.pushButton_info.setText(_translate("MainWindow", "?"))
        self.name_label.setText(_translate("MainWindow", "Введите Ваше имя"))
        self.enter_name_bt.setText(_translate("MainWindow", "Далее"))
        self.no_name.setText(_translate("MainWindow", "Такого имени точно не существует;)"))
        self.exit_button.setText(_translate("MainWindow", "X"))
        self.glhf_lb.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Счастливого Вам тестирования,</p><p align=\"center\">и пусть удача, всегда будет с Вами!</p></body></html>"))
        self.start_test_bt.setText(_translate("MainWindow", "Начать"))
        self.about_comics_text.setText(_translate("MainWindow", "<html><head/><body><p>Почти все любят комиксы, в том</p><p>числе и сообщество Python</p><p>Что стоит прописать в своём коде,</p><p>чтобы прочесть комикс справа?</p></body></html>"))
        self.false_2.setText(_translate("MainWindow", "print(comics)"))
        self.false_4.setText(_translate("MainWindow", "comics.show()"))
        self.true_2.setText(_translate("MainWindow", "import antigravity"))
        self.false_3.setText(_translate("MainWindow", "print(antigravity)"))
        self.false_5.setText(_translate("MainWindow", "antigravity.show()"))
        self.ans_fir_bt.setText(_translate("MainWindow", "Ответить"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Молодец! Ты ответил на все вопросы!</p><p align=\"center\">Теперь жми на кнопку снизу и</p><p align=\"center\">останавливай своё время!</p></body></html>"))
        self.nothing.setText(_translate("MainWindow", "Стоп"))
        self.res_l.setText(_translate("MainWindow", "Результаты"))
        self.cr_csv_bt.setText(_translate("MainWindow", "Создать .csv файл"))
        self.clear_bd_bt.setText(_translate("MainWindow", "Очистить результаты"))
        self.label_3.setText(_translate("MainWindow", "Без лишних слов"))
        self.label_5.setText(_translate("MainWindow", "import"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Beautiful is better than ugly.\n"
                                                                 "Explicit is better than implicit.\n"
                                                                 "Simple is better than complex.\n"
                                                                 "Complex is better than complicated.\n"
                                                                 "Flat is better than nested.\n"
                                                                 "Sparse is better than dense.\n"
                                                                 "Readability counts.\n"
                                                                 "Special cases aren\'t special enough to break the rules.\n"
                                                                 "Although practicality beats purity.\n"
                                                                 "Errors should never pass silently.\n"
                                                                 "Unless explicitly silenced.\n"
                                                                 "In the face of ambiguity, refuse the temptation to guess.\n"
                                                                 "There should be one-- and preferably only one --obvious way to do it.\n"
                                                                 "Although that way may not be obvious at first unless you\'re Dutch.\n"
                                                                 "Now is better than never.\n"
                                                                 "Although never is often better than *right* now.\n"
                                                                 "If the implementation is hard to explain, it\'s a bad idea.\n"
                                                                 "If the implementation is easy to explain, it may be a good idea.\n"
                                                                 "Namespaces are one honking great idea -- let\'s do more of those!"))
        self.pushButton.setText(_translate("MainWindow", "Далее"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Что после выполнения данной программы</p><p align=\"center\">выведется в консоли?</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "print(hash(float(\'nan\')))"))
        self.pushButton_2.setText(_translate("MainWindow", "Далее"))
        self.label_8.setText(_translate("MainWindow", "Какого типа данных не существует в Python?"))
        self.true_3.setText(_translate("MainWindow", "len"))
        self.radioButton_2.setText(_translate("MainWindow", "dict"))
        self.radioButton_3.setText(_translate("MainWindow", "set"))
        self.radioButton_4.setText(_translate("MainWindow", "tup"))
        self.radioButton_5.setText(_translate("MainWindow", "list"))
        self.radioButton_6.setText(_translate("MainWindow", "float"))
        self.pushButton_3.setText(_translate("MainWindow", "Далее"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Все мы знаем, что Python 3 не разрешает </p><p align=\"center\">смешивать табуляцию и пробелы</p><p align=\"center\">А что делал Python 2?</p></body></html>"))
        self.radioButton_7.setText(_translate("MainWindow", "менял пробелы на табуляцию"))
        self.true_4.setText(_translate("MainWindow", "менял табуляцию на пробелы"))
        self.radioButton_9.setText(_translate("MainWindow", "игнорировал смешивание"))
        self.radioButton_10.setText(_translate("MainWindow", "табуляция не работала в Python 2"))
        self.pushButton_4.setText(_translate("MainWindow", "Далее"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Какая максимальная длина комментария </p><p align=\"center\">по стандарту PEP 8?</p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Далее"))
        self.label_11.setText(_translate("MainWindow", "А обычной строки?"))
        self.pushButton_6.setText(_translate("MainWindow", "Далее"))
        self.label_12.setText(_translate("MainWindow", "Love is True?"))
        self.pushButton_7.setText(_translate("MainWindow", "Далее"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sec_quest_window.hide()
        self.name_window.hide()
        self.fird_ques_window.hide()
        self.four_ques_window.hide()
        self.five_quest_window.hide()
        self.six_q_window.hide()
        self.seven_q_window.hide()
        self.eight_q_w.hide()
        self.name_window.hide()
        self.no_name.hide()
        self.last_bt_test_w.hide()
        self.results_w.hide()
        self.glhf_window.hide()
        self.first_quest.hide()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.clicked.connect(sys.exit)
        self.start_button.clicked.connect(self.sec_w)
        self.enter_name_bt.clicked.connect(self.fir_w)
        self.ans_fir_bt.clicked.connect(self.sec_ans)
        self.start_test_bt.clicked.connect(self.first_ans)
        self.nothing.clicked.connect(self.resul)
        self.cr_csv_bt.clicked.connect(self.save_csv)
        self.clear_bd_bt.clicked.connect(self.clear_bd)
        self.pushButton.clicked.connect(self.fird_ans)
        self.pushButton_2.clicked.connect(self.four_ans)
        self.pushButton_3.clicked.connect(self.five_ans)
        self.pushButton_4.clicked.connect(self.six_ans)
        self.pushButton_5.clicked.connect(self.seven_ans)
        self.pushButton_6.clicked.connect(self.eight_ans)
        self.pushButton_7.clicked.connect(self.last_ans)

    def clear_bd(self):
        sqlite_connection = sqlite3.connect('PyQuiz.db')
        cur = sqlite_connection.cursor()
        count = cur.execute("""DELETE FROM Authors""")
        #coun = cur.execute("""INSERT INTO Authors
        #                                  (id, Author, Points)
        #                                  VALUES
        #                                  (1, 'God', 100000);""")
        result = cur.execute("""SELECT Author, Points FROM Authors""")
        li = []
        for elem in result:
            li.append(elem)
        for j in range(0, len(li) - 1):
            for i in range(0, len(li) - j - 1):
                if li[i][-1] < li[i + 1][-1]:
                    li[i], li[i + 1] = li[i + 1], li[i]
        layout = QGroupBox()
        k = QFormLayout()
        a = []
        for i in range(len(li)):
            a.append(QLabel(str(li[i][0]) + ' - ' + str(li[i][1]) + ' баллов'))
            k.addRow(a[i])
        layout.setLayout(k)
        self.scrollArea.setWidget(layout)
        sqlite_connection.commit()
        cur.close()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter file’s name:')
        if ok:
            return text

    def add_bd(self):
        global POINTS, NAME, ID
        POINTS = int(POINTS / round(time() - self.start_time, 2) * 1000)
        sq_c = sqlite3.connect('PyQuiz.db')
        cur = sq_c.cursor()
        a = (ID, NAME, POINTS)
        sqlite_insert_query = """INSERT INTO Authors
                                  (id, Author, Points)
                                  VALUES
                                  (?, ?, ?);"""
        cur.execute(sqlite_insert_query, a)
        sq_c.commit()
        cur.close()

    def save_csv(self):
        sq_c = sqlite3.connect('PyQuiz.db')
        sql3_cursor = sq_c.cursor()
        sql3_cursor.execute('SELECT * FROM Authors')
        name = self.showDialog() + '.csv'
        with open(name, 'w') as out_csv_file:
            csv_out = csv.writer(out_csv_file)
            csv_out.writerow([d[0] for d in sql3_cursor.description])
            for result in sql3_cursor:
                csv_out.writerow(result)
        sq_c.close()

    def resul(self):
        self.add_bd()
        self.last_bt_test_w.hide()
        self.results_w.show()
        con = sqlite3.connect('PyQuiz.db')
        cur = con.cursor()
        result = cur.execute("""SELECT Author, Points FROM Authors""")
        li = []
        for elem in result:
            li.append(elem)
        for j in range(0, len(li) - 1):
            for i in range(0, len(li) - j - 1):
                if li[i][-1] < li[i + 1][-1]:
                    li[i], li[i + 1] = li[i + 1], li[i]
        layout = QGroupBox()
        k = QFormLayout()
        a = []
        for i in range(len(li)):
            a.append(QLabel(str(li[i][0]) + ' - ' + str(li[i][1]) + ' баллов'))
            k.addRow(a[i])
        layout.setLayout(k)
        self.scrollArea.setWidget(layout)

    def sec_w(self):
        self.first_window.hide()
        self.name_window.show()

    def fir_w(self):
        global NAME
        if self.enter_name_LE.text() == '':
            self.no_name.show()
        else:
            NAME = self.enter_name_LE.text()
            self.name_window.hide()
            self.glhf_window.show()

    def first_ans(self):
        self.glhf_window.hide()
        self.start_time = time()
        self.first_quest.show()

    def sec_ans(self):
        global POINTS
        if self.true_2.isChecked():
            POINTS += 10
        self.first_quest.hide()
        self.sec_quest_window.show()

    def fird_ans(self):
        global POINTS
        if self.lineEdit.text() == 'this':
                POINTS += 10
        self.sec_quest_window.hide()
        self.fird_ques_window.show()

    def four_ans(self):
        global POINTS
        if self.lineEdit_2.text() == '0':
                POINTS += 10
        self.four_ques_window.show()
        self.fird_ques_window.hide()

    def five_ans(self):
        global POINTS
        if self.true_3.isChecked():
            POINTS += 10
        self.four_ques_window.hide()
        self.five_quest_window.show()

    def six_ans(self):
        global POINTS
        if self.true_4.isChecked():
            POINTS += 10
        self.five_quest_window.hide()
        self.six_q_window.show()

    def seven_ans(self):
        global POINTS
        if self.spinBox.value() == 72:
            POINTS += 10
        self.seven_q_window.show()
        self.six_q_window.hide()

    def eight_ans(self):
        global POINTS
        if self.spinBox_2.value() == 79:
                POINTS += 10
        self.seven_q_window.hide()
        self.eight_q_w.show()

    def last_ans(self):
        global POINTS
        if self.lineEdit_3.text() == 'False':
            POINTS += 10
        self.eight_q_w.hide()
        self.last_bt_test_w.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
