import sys
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
from ui_qq import Ui_Form

class QQListItem(QtWidgets.QWidget):

    def __init__(self, parent=None, nickname="", desc="", icon : QtGui.QIcon = None):
        super(QQListItem, self).__init__(parent)
        self.avater = QtWidgets.QLabel(self)
        # 圆形头像
        pixmap : QtGui.QPixmap = icon.pixmap(45)
        pixmap.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(pixmap)
        painter.setRenderHints(QtGui.QPainter.Antialiasing
                             | QtGui.QPainter.HighQualityAntialiasing
                             | QtGui.QPainter.SmoothPixmapTransform)
        pixmap2 = icon.pixmap(45).scaled(45, 45, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)
        path = QtGui.QPainterPath()
        path.addRoundedRect(0, 0, 45, 45, 25, 25)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap2)
        painter.end()
        self.avater.setPixmap(pixmap)

        self.nickname = nickname
        self.desc = desc

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setFont(QtGui.QFont("微软雅黑", 14))
        self.label1.setText(nickname)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setStyleSheet("color: grey;")
        self.label2.setText(desc)

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(15, 5, 5, 5)
        inline_layout = QtWidgets.QVBoxLayout()
        inline_layout.addWidget(self.label1)
        inline_layout.addWidget(self.label2)

        layout.addWidget(self.avater)
        layout.addLayout(inline_layout)
        layout.setStretch(0, 1)
        layout.setStretch(1, 3)


class MyApp(QtWidgets.QWidget):

    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.ui.pushButton.clicked.connect(self.on_button_clicked)
        self.ui.listWidget.itemDoubleClicked.connect(self.on_listWidgetItem_clicked)
        self.ui.widget.emoji_clicked.connect(self.on_panel_clicked)
        self.ui.widget.font_clicked.connect(self.on_panel_clicked)
        self.ui.widget.history_clicked.connect(self.on_panel_clicked)
        # self.ui.textEdit.setReadOnly(True)

        for i in range(1, 20):
            item = QQListItem(self, f"asdfasd{i}", "asdf", QtGui.QIcon(f"./img/qq1.ico"))
            raw_item = QtWidgets.QListWidgetItem()
            raw_item.setSizeHint(QtCore.QSize(0, 55))
            self.ui.listWidget.addItem(raw_item)
            self.ui.listWidget.setItemWidget(raw_item, item)

    def on_button_clicked(self):
        self.ui.textEdit.append("asfdadsf")

    def on_listWidgetItem_clicked(self, item: QtWidgets.QListWidgetItem):
        w : QQListItem = self.ui.listWidget.itemWidget(item)
        print(w.nickname, w.desc)

    def on_panel_clicked(self):
        print("panel clicked")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    w = MyApp()
    w.show()

    sys.exit(app.exec_())