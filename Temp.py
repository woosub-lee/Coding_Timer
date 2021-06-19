import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from win32api import GetSystemMetrics


class Components:
    questionLabel = QLabel()
    titleLabel = QLabel()
    timeLabel = QLabel()
    logLabel = QLabel()
    titleSettingButton = QPushButton()
    timerStartingButton = QPushButton()
    timerStoppingButton = QPushButton()
    recordingButton = QPushButton()
    titleLineEdit = QLineEdit()


class LayoutBoxes:
    horizontalBox1 = QHBoxLayout()
    horizontalBox2 = QHBoxLayout()
    horizontalBox3 = QHBoxLayout()
    horizontalBox4 = QHBoxLayout()
    verticalBox = QVBoxLayout()


class GuiMaker(QWidget):
    def __init__(self):
        super().__init__()
        self.settingComponent()
    layoutBoxes = LayoutBoxes()
    components = Components()

    def settingComponent(self):
        nonlocal component
        component.titleSettingButton.setText("")

    def settingLayout(self):
        nonlocal layoutBoxes


class mymainwindow(QMainWindow):
    locationX = GetSystemMetrics(0) - 450
    locationY = 50
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        widget = GuiMaker()
        self.setCentralWidget(widget)
        self.initFrame()

    def initFrame(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        self.setWindowTitle('Coding Timer')
        self.move(self.locationX, self.locationY)
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(400, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mymainwindow()
    sys.exit(app.exec_())