from PySide2 import QtGui
from PySide2 import QtCore

def IconRoundPixmap(icon : QtGui.QIcon, extend: int) -> QtGui.QPixmap:
    if not icon:
        pixmap = QtGui.QPixmap(extend, extend)
        pixmap.fill(QtGui.QColor("grey"))
    else:
        pixmap : QtGui.QPixmap = icon.pixmap(extend)

    pixmap2 = pixmap.scaled(extend, extend, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)

    pixmap.fill(QtCore.Qt.transparent)
    painter = QtGui.QPainter(pixmap)
    painter.setRenderHints(QtGui.QPainter.Antialiasing
                            | QtGui.QPainter.HighQualityAntialiasing
                            | QtGui.QPainter.SmoothPixmapTransform)

    path = QtGui.QPainterPath()
    path.addRoundedRect(0, 0, extend, extend, extend/2, extend/2)
    painter.setClipPath(path)
    painter.drawPixmap(0, 0, pixmap2)
    painter.end()
    return pixmap