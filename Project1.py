# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WorkWindow(object):
    def setupUi(self, WorkWindow):
        WorkWindow.setObjectName("WorkWindow")
        WorkWindow.resize(978, 726)
        WorkWindow.setStyleSheet("background-color: rgb(216, 191, 216);")
        self.centralwidget = QtWidgets.QWidget(WorkWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Works = QtWidgets.QTabWidget(self.centralwidget)
        self.Works.setGeometry(QtCore.QRect(-6, -1, 951, 671))
        self.Works.setStyleSheet("background-color: rgb(255, 240, 245)")
        self.Works.setObjectName("Works")
        self.Screen = QtWidgets.QWidget()
        self.Screen.setStyleSheet("background-color: rgb(255, 240, 245)")
        self.Screen.setObjectName("Screen")
        self.graphicsView = PlotWidget(self.Screen)
        self.graphicsView.setGeometry(QtCore.QRect(375, 131, 481, 371))
        self.graphicsView.setStyleSheet("background-color: rgb(250, 218, 221);")
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.Screen)
        self.pushButton.setGeometry(QtCore.QRect(50, 550, 251, 51))
        self.pushButton.setStyleSheet("background-color: rgb(216, 191, 216);\n"
"font: 75 10pt \"Segoe Script\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Screen)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 550, 491, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(216, 191, 216);\n"
"font: 75 10pt \"Segoe Script\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(self.Screen)
        self.frame.setGeometry(QtCore.QRect(19, 110, 321, 411))
        self.frame.setStyleSheet("background-color: rgb(250, 218, 221);\n"
"border-radius: 30;\n"
"font: 75 10pt \"Segoe Script\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 291, 371))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.frame_2 = QtWidgets.QFrame(self.Screen)
        self.frame_2.setGeometry(QtCore.QRect(380, 10, 511, 101))
        self.frame_2.setStyleSheet("background-color: rgb(250, 218, 221);\n"
"border-radius: 30;\n"
"font: 75 10pt \"Segoe Script\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(-40, 20, 581, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 491, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.Screen)
        self.label.setGeometry(QtCore.QRect(30, 20, 291, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("data/pict1.png"))
        self.label.setObjectName("label")
        self.Works.addTab(self.Screen, "")
        self.Tasks = QtWidgets.QWidget()
        self.Tasks.setObjectName("Tasks")
        self.label_13 = QtWidgets.QLabel(self.Tasks)
        self.label_13.setGeometry(QtCore.QRect(30, 10, 661, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("font: 75 8pt \"Segoe Script\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Tasks)
        self.label_14.setGeometry(QtCore.QRect(70, 60, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("font: 75 10pt \"Segoe Script\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.Tasks)
        self.label_15.setGeometry(QtCore.QRect(450, 80, 55, 16))
        self.label_15.setStyleSheet("font: 75 8pt \"Segoe Script\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.Tasks)
        self.label_16.setGeometry(QtCore.QRect(530, 80, 81, 16))
        self.label_16.setStyleSheet("font: 75 8pt \"Segoe Script\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.Tasks)
        self.label_17.setGeometry(QtCore.QRect(620, 80, 55, 16))
        self.label_17.setStyleSheet("font: 75 8pt \"Segoe Script\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.Tasks)
        self.label_18.setGeometry(QtCore.QRect(680, 80, 71, 16))
        self.label_18.setStyleSheet("font: 75 8pt \"Segoe Script\";")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.Tasks)
        self.label_19.setGeometry(QtCore.QRect(770, 80, 81, 16))
        self.label_19.setStyleSheet("font: 75 8pt \"Segoe Script\";")
        self.label_19.setObjectName("label_19")
        self.pushButton_3 = QtWidgets.QPushButton(self.Tasks)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 20, 171, 41))
        self.pushButton_3.setStyleSheet("font: 75 8pt \"Segoe Script\";\n"
"background-color: rgb(255, 184, 198);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Tasks)
        self.pushButton_4.setGeometry(QtCore.QRect(760, 580, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("font: 75 8pt \"Segoe Script\";\n"
"background-color: rgb(255, 184, 198);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_25 = QtWidgets.QLabel(self.Tasks)
        self.label_25.setGeometry(QtCore.QRect(30, 30, 641, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("font: 75 8pt \"Segoe Script\";")
        self.label_25.setObjectName("label_25")
        self.frame_3 = QtWidgets.QFrame(self.Tasks)
        self.frame_3.setGeometry(QtCore.QRect(40, 100, 861, 461))
        self.frame_3.setStyleSheet("background-color: rgb(255, 209, 220);\n"
"border-radius: 30;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.Tasks)
        self.label_2.setGeometry(QtCore.QRect(224, 575, 511, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("data/pict5.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.Tasks)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 580, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("font: 75 8pt \"Segoe Script\";\n"
"background-color: rgb(255, 184, 198);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.Works.addTab(self.Tasks, "")
        self.Matrix_2 = QtWidgets.QWidget()
        self.Matrix_2.setObjectName("Matrix_2")
        self.label_8 = QtWidgets.QLabel(self.Matrix_2)
        self.label_8.setGeometry(QtCore.QRect(220, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 75 10pt \"Segoe Script\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Matrix_2)
        self.label_9.setGeometry(QtCore.QRect(510, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 75 10pt \"Segoe Script\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Matrix_2)
        self.label_10.setGeometry(QtCore.QRect(30, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 75 10pt \"Segoe Script\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Matrix_2)
        self.label_11.setGeometry(QtCore.QRect(30, 320, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font: 75 10pt \"Segoe Script\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Matrix_2)
        self.label_12.setGeometry(QtCore.QRect(50, 290, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("font: 75 10pt \"Segoe Script\";")
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(self.Matrix_2)
        self.label_3.setGeometry(QtCore.QRect(710, 30, 221, 171))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("data/pict4.png"))
        self.label_3.setObjectName("label_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.Matrix_2)
        self.pushButton_7.setGeometry(QtCore.QRect(320, 540, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("font: 75 8pt \"Segoe Script\";\n"
"background-color: rgb(255, 184, 198);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.listWidget = QtWidgets.QListWidget(self.Matrix_2)
        self.listWidget.setGeometry(QtCore.QRect(110, 60, 281, 161))
        self.listWidget.setStyleSheet("background-color: rgb(255, 102, 204);\n"
"border: 2px solid rgb(85, 85, 85);\n"
"border-radius: 20;\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.Matrix_2)
        self.listWidget_2.setGeometry(QtCore.QRect(410, 60, 281, 161))
        self.listWidget_2.setStyleSheet("background-color: rgb(255, 153, 204);\n"
"border: 2px solid rgb(85, 85, 85);\n"
"border-radius: 20;")
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_3 = QtWidgets.QListWidget(self.Matrix_2)
        self.listWidget_3.setGeometry(QtCore.QRect(110, 240, 281, 161))
        self.listWidget_3.setStyleSheet("background-color: rgb(255, 204, 204);\n"
"border: 2px solid rgb(85, 85, 85);\n"
"border-radius: 20;")
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_4 = QtWidgets.QListWidget(self.Matrix_2)
        self.listWidget_4.setGeometry(QtCore.QRect(410, 240, 281, 161))
        self.listWidget_4.setStyleSheet("background-color: rgb(255, 252, 204);\n"
"border: 2px solid rgb(85, 85, 85);\n"
"border-radius: 20;")
        self.listWidget_4.setObjectName("listWidget_4")
        self.listWidget_5 = QtWidgets.QListWidget(self.Matrix_2)
        self.listWidget_5.setGeometry(QtCore.QRect(740, 330, 191, 291))
        self.listWidget_5.setStyleSheet("background-color: rgb(230, 230, 250);\n"
"border: 2px solid rgb(85, 85, 85);\n"
"border-radius: 20;\n"
"text-decoration: line-through;")
        self.listWidget_5.setObjectName("listWidget_5")
        self.label_26 = QtWidgets.QLabel(self.Matrix_2)
        self.label_26.setGeometry(QtCore.QRect(770, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("font: 75 10pt \"Segoe Script\";")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.Matrix_2)
        self.label_27.setGeometry(QtCore.QRect(770, 250, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("font: 75 10pt \"Segoe Script\";")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.Matrix_2)
        self.label_28.setGeometry(QtCore.QRect(770, 280, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("font: 75 10pt \"Segoe Script\";")
        self.label_28.setObjectName("label_28")
        self.label_5 = QtWidgets.QLabel(self.Matrix_2)
        self.label_5.setGeometry(QtCore.QRect(260, 420, 311, 101))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("data/pict1.png"))
        self.label_5.setObjectName("label_5")
        self.Works.addTab(self.Matrix_2, "")
        self.Literature = QtWidgets.QWidget()
        self.Literature.setObjectName("Literature")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Literature)
        self.scrollArea_2.setGeometry(QtCore.QRect(29, 240, 881, 321))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 879, 319))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 861, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_24 = QtWidgets.QLabel(self.Literature)
        self.label_24.setGeometry(QtCore.QRect(490, 30, 401, 20))
        self.label_24.setStyleSheet("font: 75 9pt \"Segoe Script\";")
        self.label_24.setObjectName("label_24")
        self.frame_4 = QtWidgets.QFrame(self.Literature)
        self.frame_4.setGeometry(QtCore.QRect(30, 60, 391, 171))
        self.frame_4.setStyleSheet("background-color: rgb(230, 230, 250);\n"
"border-radius: 20;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 231, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(85, 85, 85);\n"
"border-radius: 10;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 20, 231, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(85, 85, 85);\n"
"border-radius: 10;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 120, 231, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(85, 85, 85);\n"
"border-radius: 10;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_22 = QtWidgets.QLabel(self.frame_4)
        self.label_22.setGeometry(QtCore.QRect(10, 130, 55, 16))
        self.label_22.setStyleSheet("font: 75 8pt \"Segoe Script\";")
        self.label_22.setObjectName("label_22")
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        self.label_21.setGeometry(QtCore.QRect(10, 80, 55, 16))
        self.label_21.setStyleSheet("font: 75 8pt \"Segoe Script\";")
        self.label_21.setObjectName("label_21")
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_20.setStyleSheet("font: 75 8pt \"Segoe Script\";")
        self.label_20.setObjectName("label_20")
        self.frame_5 = QtWidgets.QFrame(self.Literature)
        self.frame_5.setGeometry(QtCore.QRect(710, 60, 161, 101))
        self.frame_5.setStyleSheet("background-color: rgb(230, 230, 250);\n"
"border-radius: 20;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 20, 113, 51))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(85, 85, 85);\n"
"border-radius: 10;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.Literature)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 580, 271, 51))
        self.pushButton_5.setStyleSheet("font: 75 8pt \"Segoe Script\";\n"
"background-color: rgb(204, 204, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.Literature)
        self.pushButton_6.setGeometry(QtCore.QRect(590, 580, 271, 51))
        self.pushButton_6.setStyleSheet("font: 75 8pt \"Segoe Script\";\n"
"background-color: rgb(204, 204, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_4 = QtWidgets.QLabel(self.Literature)
        self.label_4.setGeometry(QtCore.QRect(440, 170, 471, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("data/pict2.png"))
        self.label_4.setObjectName("label_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.Literature)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 80, 171, 51))
        self.pushButton_9.setStyleSheet("font: 75 8pt \"Segoe Script\";\n"
"background-color: rgb(204, 204, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.Literature)
        self.pushButton_10.setGeometry(QtCore.QRect(30, 10, 271, 41))
        self.pushButton_10.setStyleSheet("font: 75 8pt \"Segoe Script\";\n"
"background-color: rgb(204, 204, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.Works.addTab(self.Literature, "")
        WorkWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WorkWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 26))
        self.menubar.setObjectName("menubar")
        WorkWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WorkWindow)
        self.statusbar.setObjectName("statusbar")
        WorkWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WorkWindow)
        self.Works.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(WorkWindow)

    def retranslateUi(self, WorkWindow):
        _translate = QtCore.QCoreApplication.translate
        WorkWindow.setWindowTitle(_translate("WorkWindow", "MyPlaner"))
        self.pushButton.setText(_translate("WorkWindow", "Сохранить настроение"))
        self.pushButton_2.setText(_translate("WorkWindow", "Показать график настроения за последние 7 дней"))
        self.radioButton_2.setText(_translate("WorkWindow", "Готов ко всему!"))
        self.radioButton_5.setText(_translate("WorkWindow", "Рабочее"))
        self.radioButton_4.setText(_translate("WorkWindow", "Непостоянное"))
        self.radioButton_3.setText(_translate("WorkWindow", "Вообще не готов работать..."))
        self.radioButton.setText(_translate("WorkWindow", "Хочется только спать."))
        self.label_6.setText(_translate("WorkWindow", "Какое у вас сейчас настроение?"))
        self.label_7.setText(_translate("WorkWindow", "Совет: отмечайте свое настроение каждый день :)"))
        self.Works.setTabText(self.Works.indexOf(self.Screen), _translate("WorkWindow", "Экран настроения"))
        self.label_13.setText(_translate("WorkWindow", "Совет: не ставьте себе на день слишком много задач. Цели должны быть реальными :)"))
        self.label_14.setText(_translate("WorkWindow", "Задачи:"))
        self.label_15.setText(_translate("WorkWindow", "Срочно"))
        self.label_16.setText(_translate("WorkWindow", "Не срочно"))
        self.label_17.setText(_translate("WorkWindow", "Важно"))
        self.label_18.setText(_translate("WorkWindow", "Не важно"))
        self.label_19.setText(_translate("WorkWindow", "Выполнено"))
        self.pushButton_3.setText(_translate("WorkWindow", "Добавить задачу"))
        self.pushButton_4.setText(_translate("WorkWindow", "Сохранить"))
        self.label_25.setText(_translate("WorkWindow", "Не забывайте каждый раз после написания задачи нажать кнопку \"сохранить\""))
        self.pushButton_8.setText(_translate("WorkWindow", "Удалить все задачи"))
        self.Works.setTabText(self.Works.indexOf(self.Tasks), _translate("WorkWindow", "Задачи"))
        self.label_8.setText(_translate("WorkWindow", "Срочно"))
        self.label_9.setText(_translate("WorkWindow", "Не срочно"))
        self.label_10.setText(_translate("WorkWindow", "Важно"))
        self.label_11.setText(_translate("WorkWindow", "важно"))
        self.label_12.setText(_translate("WorkWindow", "Не"))
        self.pushButton_7.setText(_translate("WorkWindow", "Обновить матрицу"))
        self.label_26.setText(_translate("WorkWindow", "Список"))
        self.label_27.setText(_translate("WorkWindow", "выполненных"))
        self.label_28.setText(_translate("WorkWindow", "задач:"))
        self.Works.setTabText(self.Works.indexOf(self.Matrix_2), _translate("WorkWindow", "Матрица Эйзенхауэра"))
        self.label_24.setText(_translate("WorkWindow", "Введите id книги, которую хотите удалить:"))
        self.label_22.setText(_translate("WorkWindow", "Жанр"))
        self.label_21.setText(_translate("WorkWindow", "Автор"))
        self.label_20.setText(_translate("WorkWindow", "Название"))
        self.pushButton_5.setText(_translate("WorkWindow", "Загрузить книги из файла"))
        self.pushButton_6.setText(_translate("WorkWindow", "Записать книги в файл"))
        self.pushButton_9.setText(_translate("WorkWindow", "Удалить"))
        self.pushButton_10.setText(_translate("WorkWindow", "Добавить книгу в список:"))
        self.Works.setTabText(self.Works.indexOf(self.Literature), _translate("WorkWindow", "Список литературы"))
from pyqtgraph import PlotWidget
