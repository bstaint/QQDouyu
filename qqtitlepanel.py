from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

class QQTitlePanel(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(QQTitlePanel, self).__init__(parent)
        self.is_press = False
        self._pos : QtCore.QPoint = None
        button1 = QtWidgets.QPushButton(icon=QtGui.QIcon("./img/min.ico"))
        button1.setCursor(QtCore.Qt.PointingHandCursor)
        button2 = QtWidgets.QPushButton(icon=QtGui.QIcon("./img/close.ico"))
        button2.setCursor(QtCore.Qt.PointingHandCursor)
        spacer = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        layout = QtWidgets.QHBoxLayout(self)
        layout.addSpacerItem(spacer)
        layout.addWidget(button1)
        layout.addWidget(button2)

        button1.clicked.connect(self.window().showMinimized)
        button2.clicked.connect(self.window().close)

    def mousePressEvent(self, ev : QtGui.QMouseEvent):
        if ev.button() == QtCore.Qt.LeftButton:
            self._pos = ev.pos()

    def mouseMoveEvent(self, ev : QtGui.QMouseEvent):
        if self._pos:
            self.window().move(self.window().pos() + (ev.pos() - self._pos))

    def mouseReleaseEvent(self, ev):
        self._pos = None

    def paintEvent(self, ev : QtGui.QPaintEvent):
        opt = QtWidgets.QStyleOption()
        opt.init(self)
        painter = QtGui.QPainter(self)
        style : QtWidgets.QStyle = self.style()
        style.drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, painter, self)