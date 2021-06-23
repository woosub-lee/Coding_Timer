import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QApplication, \
    QFileDialog, QMainWindow, QAction
from win32api import GetSystemMetrics


class ComponentFactory:
    @staticmethod
    def makeLable(content):
        return QLabel(content)

    @staticmethod
    def makeButton(content):
        return QPushButton(content)

    @staticmethod
    def makeEditor():
        return QLineEdit()


class LayoutFactory:
    @staticmethod
    def makeVBox():
        return QVBoxLayout()

    @staticmethod
    def makeHBox():
        return QHBoxLayout()

class MyLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.makeComponent()
        self.makeBoxLayout()
        self.makeComponentsList()
        self.fillVBoxLayout()
        self.setLayout(self.boxLayout)

    def makeComponent(self):
        self.questionLabel = ComponentFactory.makeLable("지금 할 코딩은?")
        self.titleLabel = ComponentFactory.makeLable("")
        self.titleEditor = ComponentFactory.makeEditor()
        self.setTitleButton = ComponentFactory.makeButton("결정")

        self.warningLable = ComponentFactory.makeLable("")

        self.timeLabel = ComponentFactory.makeLable("00:00:00")

        self.startTimerButton = ComponentFactory.makeButton("시작")
        self.stopTimerButton = ComponentFactory.makeButton("정지")
        self.recordTimerButton = ComponentFactory.makeButton("기록")

    def makeComponentsList(self):
        self.componentsH1 = [self.questionLabel,
                             self.titleLabel,
                             self.titleEditor,
                             self.setTitleButton]

        self.componentsH2 = [self.warningLable]

        self.componentsH3 = [self.timeLabel]

        self.componentsH4 = [self.startTimerButton,
                             self.stopTimerButton,
                             self.recordTimerButton]

    def makeBoxLayout(self):
        self.boxLayoutH1 = LayoutFactory.makeHBox()
        self.boxLayoutH2 = LayoutFactory.makeHBox()
        self.boxLayoutH3 = LayoutFactory.makeHBox()
        self.boxLayoutH4 = LayoutFactory.makeHBox()

        self.boxLayout = LayoutFactory.makeVBox()


    def fillVBoxLayout(self):
        def fillHBoxLayout(layoutBox, components):
            layoutBox.addStretch(1)
            for component in components:
                layoutBox.addWidget(component)
            layoutBox.addStretch(1)
        fillHBoxLayout(self.boxLayoutH1, self.componentsH1)
        fillHBoxLayout(self.boxLayoutH2, self.componentsH2)
        fillHBoxLayout(self.boxLayoutH3, self.componentsH3)
        fillHBoxLayout(self.boxLayoutH4, self.componentsH4)
        self.boxLayout.addLayout(self.boxLayoutH1)
        self.boxLayout.addLayout(self.boxLayoutH2)
        self.boxLayout.addLayout(self.boxLayoutH3)
        self.boxLayout.addLayout(self.boxLayoutH4)









