import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit
from win32api import GetSystemMetrics


class ComponentFactory:
    def makeLable(self, content):
        return QLabel(content)

    def makeButton(self, content):
        return QPushButton(content)

    def makeEditor(self):
        return QLineEdit()


class LayoutFactory:
    def makeVBox(self):
        return QVBoxLayout()

    def makeHBox(self):
        return QHBoxLayout()

class MyLayout(QWidget):
    def __init__(self):
        super().__init__()


    def makeComponent(self):
        componentFactory = ComponentFactory()

        self.questionLabel = componentFactory.makeLable("지금 할 코딩은?")
        self.titleLabel = componentFactory.makeLable("")
        self.timeLabel = componentFactory.makeLable("00:00:00")

        self.setTitleButton = componentFactory.makeButton("결정")
        self.startTimerButton = componentFactory.makeButton("시작")
        self.stopTimerButton = componentFactory.makeButton("정지")
        self.recordTimerButton = componentFactory.makeButton("기록")

        self.titleEditor = componentFactory.makeEditor()


    def makeBoxLayout(self):
        layoutFactory = LayoutFactory()

        self.boxLayoutH1 = layoutFactory.makeHBox()
        self.boxLayoutH2 = layoutFactory.makeHBox()
        self.boxLayoutH3 = layoutFactory.makeHBox()
        self.boxLayoutH4 = layoutFactory.makeHBox()

        self.boxLayout = layoutFactory.makeVBox()


    def fillBoxLayout(self):
        self.titleLabel.setVisible(False)

        self.boxLayoutH1.addStretch(1)
        self.boxLayoutH1.addWidget(self.questionLabel)
        self.boxLayoutH1.addWidget(self.titleEditor)
        self.boxLayoutH1.addWidget(self.titleLabel)
        self.boxLayoutH1.addWidget(self.setTitleButton)
        self.boxLayoutH1.addStretch(1)






