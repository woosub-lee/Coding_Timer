import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.placeComponent()

    def placeComponent(self):
        lbTitle = QLabel('지금 할 코딩은?')
        leTitle = QLineEdit()
        lbTime = QLabel('00:00:00')
        btnStart = QPushButton('시작')
        btnEnd = QPushButton('종료')

        fontTime = lbTime.font()
        fontTime.setPointSize(50)
        fontTime.setFamily('Noto Sans CJK KR Black')
        lbTime.setFont(fontTime)

        boxH1 = QHBoxLayout()
        boxH2 = QHBoxLayout()
        boxH3 = QHBoxLayout()
        boxV = QVBoxLayout()

        boxH1.addStretch(1)
        boxH1.addWidget(lbTitle)
        lbTitle.setAlignment(Qt.AlignCenter)
        boxH1.addWidget(leTitle)
        leTitle.setFixedSize(100,20)
        boxH1.addStretch(1)

        boxH2.addStretch(1)
        boxH2.addWidget(lbTime)
        lbTime.setAlignment(Qt.AlignCenter)
        boxH2.addStretch(1)

        boxH3.addStretch(1)
        boxH3.addWidget(btnStart)
        boxH3.addWidget(btnEnd)
        boxH3.addStretch(1)

        boxV.addLayout(boxH1)
        boxV.addStretch(1)
        boxV.addLayout(boxH2)
        boxV.addStretch(1)
        boxV.addLayout(boxH3)
        self.setLayout(boxV)

class mymainwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        widget = MyWidget()
        self.setCentralWidget(widget)
        self.initFrame()

    def initFrame(self):
        self.setWindowTitle('Coding Timer')
        self.move(300, 300)
        self.setFixedSize(400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mymainwindow()
    sys.exit(app.exec_())