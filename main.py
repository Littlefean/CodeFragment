# -*- encoding: utf-8 -*-
"""
代码片段管理器
"""

import sys
import os
import threading
import time

from PyQt5.QtWidgets import *
from pynput.keyboard import Listener

from myitem import MyItem


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.dic = {}  # {title: divEle}
        # 主纵向布局
        self.layoutMain = QVBoxLayout()
        # 第一行布局
        self.layoutTopLine = QHBoxLayout()

        self.layoutList = QVBoxLayout()
        self.layoutScrollDiv = QVBoxLayout()

        self.init()
        print("init End")

    def init(self):
        self.setWindowTitle("sss")
        self.resize(800, 500)

        # ====
        self.layoutMain = QVBoxLayout()

        # == 第一行

        btnNew = QPushButton("打开")
        btnNew.setStyleSheet("background-color: rgba(255, 0, 0, 0.5);color:white")

        btnSearch = QPushButton("搜索")
        inputDiv = QLineEdit()
        inputDiv.setPlaceholderText("请输入内容")
        inputDiv.textChanged[str].connect(self.inputChangeFunc)

        # layoutTopLine.addWidget(btnNew)
        self.layoutTopLine.addWidget(inputDiv)
        self.layoutTopLine.addWidget(btnSearch)

        self.layoutMain.addLayout(self.layoutTopLine)

        # 下面的列表

        scrollDiv = QWidget()

        scrollDiv.setLayout(self.layoutScrollDiv)

        # 读取追加
        for fileName in os.listdir("myData"):
            oneItem = MyItem.fromFileName(fileName)
            self.layoutScrollDiv.addLayout(oneItem)
            self.dic[fileName] = oneItem

        scroll = QScrollArea()
        scroll.setMinimumHeight(500)
        scroll.setWidget(scrollDiv)
        # ==== 追加纵向布局

        self.layoutMain.addLayout(self.layoutList)
        self.layoutMain.addWidget(scroll)

        self.setLayout(self.layoutMain)
        return

    def inputChangeFunc(self, string):
        """搜索某个条目"""
        print(string)
        print(self.layoutScrollDiv.count())

        for k, v in self.dic.items():
            v.clear()

        ...


def addHook():
    """绑定热键"""
    lastKey = None

    def on_press(key):
        nonlocal lastKey
        if str(key) == "Key.alt_l" and str(lastKey) == "'1'":
            print("成了")
        lastKey = key

    def f():
        with Listener(on_press=on_press) as listener:
            listener.join()

    threading.Thread(target=f).start()


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()


if __name__ == "__main__":
    main()
