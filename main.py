# -*- encoding: utf-8 -*-
"""
代码片段管理器
"""

import sys

from PyQt5.QtWidgets import *
from myitem import MyItem


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.setWindowTitle("sss")
        self.resize(800, 500)

        # ====
        layoutMain = QVBoxLayout()

        # == 第一行
        layoutTopLine = QHBoxLayout()
        btnNew = QPushButton("新建")
        btnNew.setStyleSheet("background-color: rgba(255, 0, 0, 0.5);color:white")

        btnSearch = QPushButton("搜索")
        inputDiv = QLineEdit()

        layoutTopLine.addWidget(btnNew)
        layoutTopLine.addWidget(inputDiv)
        layoutTopLine.addWidget(btnSearch)

        layoutMain.addLayout(layoutTopLine)

        # 下面的列表
        layoutList = QVBoxLayout()

        scrollDiv = QWidget()

        layoutScrollDiv = QVBoxLayout()
        scrollDiv.setLayout(layoutScrollDiv)

        for i in range(50):
            if i == 30:
                layoutScrollDiv.addLayout(MyItem("aaa" * 10, "bb"))
            else:
                layoutScrollDiv.addLayout(MyItem("aaa", "bb"))

        scroll = QScrollArea()
        scroll.setMinimumHeight(500)
        scroll.setWidget(scrollDiv)
        # ==== 追加纵向布局

        layoutMain.addLayout(layoutList)
        layoutMain.addWidget(scroll)

        self.setLayout(layoutMain)
        return


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()


if __name__ == "__main__":
    main()
