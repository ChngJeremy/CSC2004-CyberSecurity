# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testgui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 597)
        MainWindow.setContextMenuPolicy(Qt.CustomContextMenu)
        MainWindow.setSizeGripEnabled(False)
        self.centralwidget = QFrame(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(0, -10, 731, 611))
        self.centralwidget.setStyleSheet(u"\n"
"background-color: rgb(33, 37, 43);")
        self.centralwidget.setFrameShape(QFrame.StyledPanel)
        self.centralwidget.setFrameShadow(QFrame.Raised)
        self.titlelabel = QLabel(self.centralwidget)
        self.titlelabel.setObjectName(u"titlelabel")
        self.titlelabel.setGeometry(QRect(260, 10, 221, 51))
        font = QFont()
        font.setFamily(u"MS Gothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.titlelabel.setFont(font)
        self.titlelabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.titlelabel.setAlignment(Qt.AlignCenter)
        self.titlelabel.setIndent(0)
        self.quitButton = QPushButton(self.centralwidget)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setGeometry(QRect(630, 560, 75, 23))
        self.quitButton.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.fileencodelabel = QLabel(self.centralwidget)
        self.fileencodelabel.setObjectName(u"fileencodelabel")
        self.fileencodelabel.setGeometry(QRect(40, 80, 161, 51))
        font1 = QFont()
        font1.setFamily(u"MS Gothic")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        self.fileencodelabel.setFont(font1)
        self.fileencodelabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.fileencodelabel.setTextFormat(Qt.PlainText)
        self.fileencodelabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.fileencodelabel.setWordWrap(True)
        self.fileencodelabel.setMargin(0)
        self.fileencodelabel.setIndent(0)
        self.piclabel_3 = QLabel(self.centralwidget)
        self.piclabel_3.setObjectName(u"piclabel_3")
        self.piclabel_3.setGeometry(QRect(40, 170, 221, 51))
        self.piclabel_3.setFont(font1)
        self.piclabel_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.piclabel_3.setTextFormat(Qt.PlainText)
        self.piclabel_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.piclabel_3.setWordWrap(True)
        self.piclabel_3.setMargin(0)
        self.piclabel_3.setIndent(0)
        self.encodeButton = QPushButton(self.centralwidget)
        self.encodeButton.setObjectName(u"encodeButton")
        self.encodeButton.setGeometry(QRect(290, 560, 75, 23))
        self.encodeButton.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(220, 90, 211, 22))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        self.comboBox.setFont(font2)
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(220, 190, 211, 22))
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.comboBox_2.setFont(font3)
        self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_2.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.pictureframe = QFrame(self.centralwidget)
        self.pictureframe.setObjectName(u"pictureframe")
        self.pictureframe.setGeometry(QRect(30, 320, 291, 231))
        self.pictureframe.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.pictureframe.setFrameShape(QFrame.StyledPanel)
        self.pictureframe.setFrameShadow(QFrame.Raised)
        self.label_before = QLabel(self.pictureframe)
        self.label_before.setObjectName(u"label_before")
        self.label_before.setGeometry(QRect(0, 0, 291, 231))
        self.label_before.setPixmap(QPixmap(u"../../../../Downloads/photo-1553949285-bdcb31ec5cba.jpg"))
        self.label_before.setScaledContents(True)
        self.encodeframe = QFrame(self.centralwidget)
        self.encodeframe.setObjectName(u"encodeframe")
        self.encodeframe.setGeometry(QRect(330, 320, 281, 231))
        self.encodeframe.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.encodeframe.setFrameShape(QFrame.StyledPanel)
        self.encodeframe.setFrameShadow(QFrame.Raised)
        self.originalpiclabel = QLabel(self.centralwidget)
        self.originalpiclabel.setObjectName(u"originalpiclabel")
        self.originalpiclabel.setGeometry(QRect(100, 300, 141, 16))
        self.originalpiclabel.setFont(font1)
        self.originalpiclabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.originalpiclabel.setTextFormat(Qt.PlainText)
        self.originalpiclabel.setAlignment(Qt.AlignCenter)
        self.originalpiclabel.setWordWrap(True)
        self.originalpiclabel.setMargin(0)
        self.originalpiclabel.setIndent(0)
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
        self.txtradioButton = QRadioButton(self.centralwidget)
        self.txtradioButton.setObjectName(u"txtradioButton")
        self.txtradioButton.setGeometry(QRect(480, 90, 101, 17))
        font4 = QFont()
        font4.setFamily(u"MS Gothic")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.txtradioButton.setFont(font4)
        self.txtradioButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtradioButton.setIconSize(QSize(20, 20))
        self.txtradioButton.setChecked(False)
        self.mp4radioButton = QRadioButton(self.centralwidget)
        self.mp4radioButton.setObjectName(u"mp4radioButton")
        self.mp4radioButton.setGeometry(QRect(480, 110, 101, 17))
        self.mp4radioButton.setFont(font4)
        self.mp4radioButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.mp4radioButton.setIconSize(QSize(20, 20))
        self.mp4radioButton.setChecked(False)
        QWidget.setTabOrder(self.comboBox, self.txtradioButton)
        QWidget.setTabOrder(self.txtradioButton, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.quitButton)
        QWidget.setTabOrder(self.quitButton, self.encodeButton)
        QWidget.setTabOrder(self.encodeButton, self.mp4radioButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Test GUI", None))
        self.titlelabel.setText(QCoreApplication.translate("MainWindow", u"LSB Encoder", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.fileencodelabel.setText(QCoreApplication.translate("MainWindow", u"Select file to be encoded:", None))
        self.piclabel_3.setText(QCoreApplication.translate("MainWindow", u"Select Picture to be encoded to:", None))
        self.encodeButton.setText(QCoreApplication.translate("MainWindow", u"Encode!", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"example.txt", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"sample.mp4", None))
        self.comboBox.setItemText(2, "")

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Picture1.png", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Picture2.jpeg", None))

        self.label_before.setText("")
        self.originalpiclabel.setText(QCoreApplication.translate("MainWindow", u"Original Picture", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Encoded Picture", None))
        self.txtradioButton.setText(QCoreApplication.translate("MainWindow", u".txt file", None))
        self.mp4radioButton.setText(QCoreApplication.translate("MainWindow", u".mp4 file", None))
    # retranslateUi

Error: testgui.ui: Warning: Tab-stop assignment: 'pushButton_3' is not a valid widget.

testgui.ui: Warning: Tab-stop assignment: 'pushButton_4' is not a valid widget.

testgui.ui: Warning: Tab-stop assignment: 'comboBox_3' is not a valid widget.

testgui.ui: Warning: Tab-stop assignment: 'comboBox_4' is not a valid widget.

testgui.ui: Warning: Tab-stop assignment: 'radioButton_2' is not a valid widget.


while executing 'C:\Users\chng_\AppData\Local\Programs\Python\Python39\lib\site-packages\PySide2\uic -g python testgui.ui'
