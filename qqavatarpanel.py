from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
from painter import IconRoundPixmap

class QQAvatarPanel(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(QQAvatarPanel, self).__init__(parent)
        self.label1 = QtWidgets.QLabel(self)
        self.label2 = QtWidgets.QLabel(self)
        self.label3 = QtWidgets.QLabel(self)
        pixmap = IconRoundPixmap(None, 38)
        self.label1.setPixmap(pixmap)

        self.setStyleSheet("font: 9pt \"微软雅黑\";")

        inline_layout = QtWidgets.QVBoxLayout()
        inline_layout.addWidget(self.label2)
        inline_layout.addWidget(self.label3)

        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.label1)
        layout.addLayout(inline_layout)

        self.label1.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                                        QtWidgets.QSizePolicy.Fixed))
        self.label3.setStyleSheet("color: grey;")

        self.label2.setText("nickname")
        self.label3.setText("adfadsblabla")

    def setText(self, title: str, desc: str, icon: QtGui.QIcon):
        self.label1.setPixmap(IconRoundPixmap(icon, 38))
        self.label2.setText(title)
        self.label3.setText(desc)
