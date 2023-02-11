# -*- encoding: utf-8 -*-
"""
代码片段管理器
"""

import sys
import os
import threading

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from pynput.keyboard import Listener

from match import m1
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
            oneItem = MyItem.fromFileName(fileName, self.layoutScrollDiv)
            self.layoutScrollDiv.addLayout(oneItem)
            self.dic[fileName] = oneItem
        # 最下面再加个弹簧
        self.layoutScrollDiv.addStretch()

        scroll = QScrollArea()
        # scroll.setMinimumHeight(1000)
        scroll.setWidget(scrollDiv)
        # ==== 追加纵向布局

        self.layoutMain.addLayout(self.layoutList)
        self.layoutMain.addWidget(scroll)

        self.setLayout(self.layoutMain)
        return

    def clearAll(self):
        # 先清空所有
        for k, v in self.dic.items():
            v.clearContent()
            self.layoutScrollDiv.removeItem(v)
        for i in reversed(range(self.layoutScrollDiv.count())):
            item = self.layoutScrollDiv.itemAt(i)
            self.layoutScrollDiv.removeItem(item)
            ...

    def inputChangeFunc(self, string: str):
        """搜索某个条目"""
        print(string)
        print("清理前的count", self.layoutScrollDiv.count())
        self.clearAll()
        print("清理后的count", self.layoutScrollDiv.count())
        # if string.strip() == "":
        #     return
        # 根据输入进行筛选
        arr = string.split()  # 根据空格分割关键词
        print("---开始匹配")
        for k, v in self.dic.items():
            if m1(arr, k):
                print(k)
                # 如果匹配，就添加上
                oneItem = MyItem.fromFileName(k, self.layoutScrollDiv)
                self.layoutScrollDiv.addLayout(oneItem)
        # 最下面再加个弹簧
        self.layoutScrollDiv.addStretch()
        print("-------")
        print("追加后的count", self.layoutScrollDiv.count())
        ...


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setWindowIcon(QIcon('icon.png'))
    w.show()
    def addHook():
        """绑定热键"""
        lastKey = None

        def on_press(key):
            nonlocal lastKey
            if str(key) == "Key.alt_l" and str(lastKey) == "'1'":
                print("成了")
                # w.show() 如何显示在最上层
            lastKey = key

        def f():
            with Listener(on_press=on_press) as listener:
                listener.join()

        threading.Thread(target=f).start()

    addHook()
    app.exec_()


if __name__ == "__main__":
    main()
