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
        self.titleEditor = componentFactory.makeEditor()
        self.setTitleButton = componentFactory.makeButton("결정")

        self.warningLable = componentFactory.makeLable("")

        self.timeLabel = componentFactory.makeLable("00:00:00")

        self.startTimerButton = componentFactory.makeButton("시작")
        self.stopTimerButton = componentFactory.makeButton("정지")
        self.recordTimerButton = componentFactory.makeButton("기록")

    def makeComponentsList(self):
        self.ComponentsH1 = []

    def makeBoxLayout(self):
        layoutFactory = LayoutFactory()

        self.boxLayoutH1 = layoutFactory.makeHBox()
        self.boxLayoutH2 = layoutFactory.makeHBox()
        self.boxLayoutH3 = layoutFactory.makeHBox()
        self.boxLayoutH4 = layoutFactory.makeHBox()

        self.boxLayout = layoutFactory.makeVBox()


    def fillVBoxLayout(self):
        def fillHBoxLayout(layoutBox, components):
            layoutBox.addStretch(1)
            for component in components:
                layoutBox.addWidget(component)
            layoutBox.addStretch(1)
        fillHBoxLayout(self.boxLayoutH1)

        self.boxLayoutH2.addStretch(1)
        self.boxLayoutH2.addWidget(self.warningLable)
        self.boxLayoutH2.addStretch(1)

        self.boxLayoutH3.addStretch(1)
        self.boxLayoutH3.addWidget(self.timeLabel)
        self.boxLayoutH3.addStretch(1)

        self.boxLayoutH4.addStretch(1)
        self.boxLayoutH4.addWidget(self.startTimerButton)
        self.boxLayoutH4.addWidget(self.stopTimerButton)
        self.boxLayoutH4.addWidget(self.recordTimerButton)
        self.boxLayoutH4.addStretch(1)









