from PyQt5 import QtWidgets, QtCore, QtGui
import qrcode
import StringIO

class Image(qrcode.image.base.BaseImage):
    def __init__(self, border, width, box_size):
        self.border = border
        self.width = width
        self.box_size = box_size
        size = (width + border * 2) * box_size
        self._image = QtGui.QImage(
            size, size, QtGui.QImage.Format_RGB16)
        self._image.fill(QtCore.Qt.white)

    def pixmap(self):
        return QtGui.QPixmap.fromImage(self._image)

    def drawrect(self, row, col):
        painter = QtGui.QPainter(self._image)
        painter.fillRect(
            (col + self.border) * self.box_size,
            (row + self.border) * self.box_size,
            self.box_size, self.box_size,
            QtCore.Qt.black)

    def save(self, stream, kind=None):
        pass

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.label = QtWidgets.QLabel(self)
        self.edit = QtWidgets.QLineEdit(self)
        self.edit.returnPressed.connect(self.handleTextEntered)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.edit)

    def handleTextEntered(self):
        text = unicode(self.edit.text())
        buf = StringIO.StringIO()
        img = qrcode.make(text)
        img.save(buf, "PNG")
        qt_pixmap = QtGui.QPixmap()
        qt_pixmap.loadFromData(buf.getvalue(), "PNG")
        self.label.setPixmap(qt_pixmap)
        self.label.show()
        self.label.resize(500,500)
        self.label.move(100,100)
        print('set')

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 200, 200)
    window.show()
    sys.exit(app.exec_())