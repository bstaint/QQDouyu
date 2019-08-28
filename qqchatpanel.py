from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

class QQChatPanel(QtWidgets.QWidget):

    emoji_clicked = QtCore.Signal()
    font_clicked = QtCore.Signal()
    history_clicked = QtCore.Signal()

    def __init__(self, parent=None):
        super(QQChatPanel, self).__init__(parent)

        button1 = QtWidgets.QPushButton(icon=QtGui.QIcon("./img/font.ico"))
        button2 = QtWidgets.QPushButton(icon=QtGui.QIcon("./img/emoji.ico"))
        button3 = QtWidgets.QPushButton("消息记录")
        button3.setFont(QtGui.QFont("微软雅黑", 11))
        button3.setStyleSheet("color: grey;")
        spacer = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(10, 3, 10, 3)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addSpacerItem(spacer)
        layout.addWidget(button3)

        button1.clicked.connect(self.font_clicked)
        button2.clicked.connect(self.emoji_clicked)
        button3.clicked.connect(self.history_clicked)