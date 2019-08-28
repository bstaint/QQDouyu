# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qq.ui',
# licensing of 'qq.ui' applies.
#
# Created: Sat Aug 24 22:03:45 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(777, 567)
        Form.setStyleSheet("#Form{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#pushButton {\n"
"    background-color: rgb(85, 170, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#pushButton:pressed {\n"
"    background-color:rgb(125, 190, 255); \n"
"    border-style: inset;\n"
"}\n"
"\n"
"QListWidget,QTextEdit,QPushButton {\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"#listWidget {\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"#listWidget::Item:hover{\n"
"    background-color: rgb(208, 208, 208);\n"
"}\n"
"\n"
"#listWidget_2 {\n"
"   border-bottom : 1px solid #f1f1f1;\n"
"}\n"
"\n"
"#listWidget,#listWidget_2 {\n"
"    outline:0px;\n"
"}\n"
"\n"
"#listWidget::item:selected{\n"
"    background-color:rgb(226, 226, 226);\n"
"}\n"
"\n"
"#listWidget_2::Item:hover, #listWidget_2::item:selected{\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QScrollBar:vertical {              \n"
"    width:10px;\n"
"    margin: 0px;\n"
"    background:transparent;\n"
"    padding:0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background:rgba(0,0,0,15%);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    background:none;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover, QScrollBar::handle:vertical:pressed {\n"
"    background:rgba(0,0,0,30%);\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QQTitlePanel(Form)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 35))
        self.widget_2.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setMaximumSize(QtCore.QSize(210, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QQAvatarPanel(Form)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout.addWidget(self.widget_3)
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setMinimumSize(QtCore.QSize(500, 0))
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout.addWidget(self.listWidget_2)
        self.widget = QQChatPanel(Form)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 5, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 25))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 6)
        self.verticalLayout.setStretch(3, 2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "发送(&S)", None, -1))

from qqtitlepanel import QQTitlePanel
from qqchatpanel import QQChatPanel
from qqavatarpanel import QQAvatarPanel
