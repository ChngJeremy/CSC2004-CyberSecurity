# -*- coding: utf-8 -*-

################################################################################
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 600)
        MainWindow.setContextMenuPolicy(Qt.CustomContextMenu)
        MainWindow.setSizeGripEnabled(False)
        self.centralwidget = QFrame(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(0, -10, 731, 601))
        self.centralwidget.setStyleSheet(u"\n"
"background-color: rgb(33, 37, 43);")
        self.centralwidget.setFrameShape(QFrame.StyledPanel)
        self.centralwidget.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 221, 51))
        font = QFont()
        font.setFamily(u"MS Gothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(0)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(630, 560, 75, 23))
        self.pushButton.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 80, 161, 51))
        font1 = QFont()
        font1.setFamily(u"MS Gothic")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(0)
        self.label_2.setIndent(0)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 170, 221, 51))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(0)
        self.label_3.setIndent(0)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 560, 75, 23))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(220, 90, 211, 22))
        self.comboBox.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(220, 190, 211, 22))
        self.comboBox_2.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 320, 291, 231))
        self.frame.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(330, 320, 281, 231))
        self.frame_2.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 300, 141, 16))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(0)
        self.label_4.setIndent(0)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(400, 300, 141, 20))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setTextFormat(Qt.PlainText)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setMargin(0)
        self.label_5.setIndent(0)
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(480, 90, 101, 17))
        font2 = QFont()
        font2.setFamily(u"MS Gothic")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.radioButton.setFont(font2)
        self.radioButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.radioButton.setIconSize(QSize(20, 20))
        self.radioButton.setChecked(False)
        self.radioButton2 = QRadioButton(self.centralwidget)
        self.radioButton2.setObjectName(u"radioButton2")
        self.radioButton2.setGeometry(QRect(480, 110, 101, 17))
        self.radioButton2.setFont(font2)
        self.radioButton2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.radioButton2.setIconSize(QSize(20, 20))
        self.radioButton2.setChecked(False)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Test GUI", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LSB Encoder", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select file to be encoded:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select Picture to be encoded to:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Encode!", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Original Picture", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Encoded Picture", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u".txt file", None))
        self.radioButton2.setText(QCoreApplication.translate("MainWindow", u".mp4 file", None))
    # retranslateUi

