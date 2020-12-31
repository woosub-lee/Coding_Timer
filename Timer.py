import sys
import threading

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from win32api import GetSystemMetrics
import os


class MyWidget(QWidget):
    path = ''
    def __init__(self):
        super().__init__()
        self.setPath()
        self.placeComponent()

    def setPath(self):
        if os.path.isfile('path.txt'):
            open_dirc = open('path.txt','r')
            with open_dirc:
                self.path = open_dirc.read()
        else:
            self.path = 'result.txt'
            make_default = open('path.txt','w')
            with make_default:
                make_default.write(self.path)
    def placeComponent(self):
        lbQuestion = QLabel('지금 할 코딩은?')
        lbTitle = QLabel()
        lbTime = QLabel()
        lbLog = QLabel()

        leTitle = QLineEdit()

        btnTitle = QPushButton('결정')
        btnStart = QPushButton('시작')
        btnStop = QPushButton('정지')
        btnEnd = QPushButton('기록')

        hour = 0
        minute = 0
        sec = -1
        timerKey = False
        result = ''

        def timer():
            counter = threading.Timer(1, timer)
            counter.setDaemon(True)

            nonlocal timerKey
            nonlocal sec
            nonlocal minute
            nonlocal hour
            nonlocal lbTime

            if timerKey == False:
                counter.cancel()

            sec += 1
            if sec > 59:
                minute += 1
                sec = 0
            if minute > 59:
                hour += 1
                minute = 0
            strS = str(sec)
            strM = str(minute)
            strH = str(hour)
            if sec < 10:
                strS = '0'+str(sec)
            if minute < 10:
                strM = '0'+str(minute)
            if hour < 10:
                strH = '0'+str(hour)

            text = strH + ':' + strM + ':' + strS
            lbTime.setText(text)
            counter.start()

        timer()

        fontTime = lbTime.font()
        fontTime.setPointSize(50)
        fontTime.setFamily('Noto Sans CJK KR Black')

        fontTitle = lbTitle.font()
        fontTitle.setBold(True)

        lbTime.setFont(fontTime)
        lbTitle.setFont(fontTitle)

        lbTime.setAlignment(Qt.AlignCenter)
        lbTitle.setAlignment(Qt.AlignLeft)

        leTitle.setFixedSize(100, 20)

        boxH1 = QHBoxLayout()
        boxH2 = QHBoxLayout()
        boxH3 = QHBoxLayout()
        boxH4 = QHBoxLayout()
        boxV = QVBoxLayout()

        boxH1.addStretch(1)
        boxH1.addWidget(lbQuestion)
        boxH1.addWidget(leTitle)
        boxH1.addWidget(btnTitle)
        boxH1.addStretch(1)

        boxH2.addStretch(1)
        boxH2.addWidget(lbLog)
        boxH2.addStretch(1)

        boxH3.addStretch(1)
        boxH3.addWidget(lbTime)
        boxH3.addStretch(1)

        boxH4.addStretch(1)
        boxH4.addWidget(btnStart)
        boxH4.addWidget(btnStop)
        boxH4.addWidget(btnEnd)
        boxH4.addStretch(1)

        boxV.addLayout(boxH1)
        boxV.addStretch(1)
        boxV.addLayout(boxH2)
        boxV.addLayout(boxH3)
        boxV.addStretch(1)
        boxV.addLayout(boxH4)
        self.setLayout(boxV)

        def decideTitle():
            nonlocal btnTitle
            nonlocal lbTitle
            nonlocal leTitle
            nonlocal boxH1
            nonlocal boxV
            title = leTitle.text()
            lbTitle.setText(title)
            boxH1.removeWidget(leTitle)
            leTitle.deleteLater()
            leTitle = None
            boxH1.removeWidget(btnTitle)
            btnTitle.deleteLater()
            btnTitle = None
            boxH1.addWidget(lbTitle)
            boxH1.addStretch(1)

        def start():
            nonlocal timerKey
            nonlocal btnStart
            timerKey = True
            btnStart.setText('재개')
            timer()

        def stop():
            nonlocal timerKey
            timerKey = False

        def recognize():
            nonlocal lbTitle
            nonlocal lbTime
            nonlocal lbLog
            nonlocal result
            nonlocal timerKey
            if timerKey == False:
                if lbTitle.text() != '':
                    result = lbTitle.text()+" "+lbTime.text()
                    with open('path.txt', 'r') as p:
                        self.path = p.read()
                    with open(self.path, 'a') as f:
                        f.write(result+"\r")
                    sys.exit(0)
                else:
                    lbLog.setText('제목을 기입해 주세요')
            if timerKey == True:
                lbLog.setText("정지 후 기록해 주세요")

        btnTitle.clicked.connect(decideTitle)
        btnStart.clicked.connect(start)
        btnStop.clicked.connect(stop)
        btnEnd.clicked.connect(recognize)




class mymainwindow(QMainWindow):
    locationX = GetSystemMetrics(0) - 450
    locationY = 50
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        widget = MyWidget()
        self.setCentralWidget(widget)
        self.initFrame()

    def initFrame(self):
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(openFile)

        self.setWindowTitle('Coding Timer')
        self.move(self.locationX, self.locationY)
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(400, 200)
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        if fname[0]:
            make_dirc = open('path.txt','w')
            with make_dirc:
                make_dirc.write(fname[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mymainwindow()
    sys.exit(app.exec_())