import os
import sys
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
from ui_qq import Ui_Form
from douyu import DouyuMessageRunnable
from pixmap import IconRoundPixmap

os.chdir(os.path.dirname(os.path.realpath(__file__)))

class QQGiftItem(QtWidgets.QWidget):
    def __init__(self, parent=None, nickname="", gfid=""):
        super(QQGiftItem, self).__init__(parent)
        self.nickname = nickname
        self.gfid = gfid

        label1 = QtWidgets.QLabel(self)
        label1.setText(f"{nickname} 赠送 {gfid}")
        label1.setStyleSheet("color: grey;")
        layout = QtWidgets.QHBoxLayout(self)
        layout.addStretch()
        layout.addWidget(label1)
        layout.addStretch()


class QQChatItem(QtWidgets.QWidget):

    def __init__(self, parent=None, level="", nickname="", text=""):
        super(QQChatItem, self).__init__(parent)
        self.nickname = nickname
        self.text = text
        self.setStyleSheet("font: 10pt \"微软雅黑\";")

        label1 = QtWidgets.QLabel(self)
        label1.setPixmap(IconRoundPixmap(None, 36))

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText(f"【level: {level}】 {nickname}")
        self.label2.setStyleSheet("color: grey;")
        
        inline1_layout = QtWidgets.QVBoxLayout()
        inline1_layout.addWidget(label1)
        inline1_layout.addStretch()

        inline2_layout = QtWidgets.QVBoxLayout()
        inline2_layout.addWidget(self.label2)
        inline2_layout.addStretch()

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(8, 2, 8, 0)
        layout.addLayout(inline1_layout)
        layout.addLayout(inline2_layout)
        layout.addStretch()


    def paintEvent(self, ev: QtGui.QPaintEvent):
        super(QQChatItem, self).paintEvent(ev)
        pos = self.label2.pos()
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtGui.QColor("#cacaca")))
        painter.setBrush(QtGui.QBrush(QtGui.QColor("#cacaca")))
        path = QtGui.QPainterPath()
        path.addRect(pos.x() + 5, pos.y() + 20, self.width() - (pos.x() + 5 + 8), pos.y() + 20 + 10)
        path.moveTo(pos.x() + 5, pos.y() + 20 + 6)
        path.lineTo(pos.x() - 3, pos.y() + 20 + 10)
        path.lineTo(pos.x() + 5, pos.y() + 20 + 14)
        painter.drawPath(path)
        painter.setPen(QtGui.QPen("black"))
        painter.drawText(QtCore.QPoint(pos.x() + 12, pos.y() + 20 + 20), self.text)

class QQListItem(QtWidgets.QWidget):

    def __init__(self, parent=None, rid=0, desc="", icon : QtGui.QIcon = None):
        super(QQListItem, self).__init__(parent)
        self.avatar = QtWidgets.QLabel(self)
        # 圆形头像
        pixmap = IconRoundPixmap(icon, 45)
        self.avatar.setPixmap(pixmap)

        self.rid = rid
        self.desc = desc
        self.icon = icon

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setFont(QtGui.QFont("微软雅黑", 14))
        self.label1.setText(f"{rid}")

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setStyleSheet("color: grey;")
        self.label2.setText(desc)

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 5, 5)
        inline_layout = QtWidgets.QVBoxLayout()
        inline_layout.addWidget(self.label1)
        inline_layout.addWidget(self.label2)

        layout.addWidget(self.avatar)
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

        self.task = None

        for rid, txt in [
            (74751, "我可能玩了假的马里奥"), 
            (9999, "清扬无懈可击：解说TI9国际邀请赛"), 
            (156277, "据说是黑魂类的射击游戏？"),
            (100, "【PCL】夏季赛第一周周决赛"),
        ]:
            self.add_chat_item(f"{rid}", txt, f"./img/{rid}.png")

    def handle_listwidget(self, *args):
        if self.ui.listWidget_2.count() > 100:
            self.ui.listWidget_2.clear()

        if len(args) == 2:
            self.add_gift_item(*args)
        elif len(args) == 3:
            self.add_message_item(*args)

        self.ui.listWidget_2.scrollToBottom()

    def closeEvent(self, ev):
        self.hide()
        if self.task:
            self.task.requestInterruption()
            self.task.wait()
            # self.task.signals.finishd.emit()
            # QtCore.QThreadPool().waitForDone()

        super(MyApp, self).closeEvent(ev)

    def on_button_clicked(self):
        # self.add_message_item("sadf", "adfasdf", "adfa")
        # self.add_join_item("asdfafd")
        self.ui.listWidget_2.scrollToBottom()

    def on_listWidgetItem_clicked(self, item: QtWidgets.QListWidgetItem):
        w : QQListItem = self.ui.listWidget.itemWidget(item)
        self.ui.widget_3.setText(f"房间号：{w.rid}", w.desc, w.icon)
        if self.task:
            self.task.requestInterruption()
            self.task.wait()

        self.ui.listWidget_2.clear()
        self.task = None

        self.connect_server(w.rid)

    def on_panel_clicked(self):
        print("panel clicked")

    def connect_server(self, rid : int):
        self.task = DouyuMessageRunnable(rid)
        self.task.signals.say.connect(self.handle_listwidget)
        self.task.signals.gift.connect(self.handle_listwidget)
        self.task.start()

    def add_chat_item(self, rid: int, desc: str, ico: str):
        raw_item = QtWidgets.QListWidgetItem()
        raw_item.setSizeHint(QtCore.QSize(0, 55))
        item = QQListItem(self, rid, desc, QtGui.QIcon(ico))
        self.ui.listWidget.addItem(raw_item)
        self.ui.listWidget.setItemWidget(raw_item, item)

    def add_gift_item(self, nickname: str, gfid: str):
        raw_item = QtWidgets.QListWidgetItem()
        raw_item.setSizeHint(QtCore.QSize(0, 30))
        item = QQGiftItem(self, nickname, gfid)
        self.ui.listWidget_2.addItem(raw_item)
        self.ui.listWidget_2.setItemWidget(raw_item, item)

    def add_message_item(self, level: str, nickname: str, text: str):
        raw_item = QtWidgets.QListWidgetItem()
        raw_item.setSizeHint(QtCore.QSize(0, 60))
        item = QQChatItem(self, level, nickname, text)
        self.ui.listWidget_2.addItem(raw_item)
        self.ui.listWidget_2.setItemWidget(raw_item, item)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    w = MyApp()
    w.show()

    sys.exit(app.exec_())