# -*- encoding : utf-8 -*-
from PyQt5.QtWidgets import *

import win32clipboard
import win32con


class MyItem(QHBoxLayout):
    """表示横着的一条数据项"""

    def __init__(self, title: str, content: str):
        super().__init__()
        self.title = title
        self.content = content
        # ====
        # 标题
        self.labelLeft = QLabel()
        # 内容
        self.labelRight = QLabel()
        # 复制按钮
        self.btnCopy = QPushButton("复制")
        # # 删除按钮
        # self.btnDel = QPushButton("X")
        # ====
        self.init()

    def copyAction(self):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, self.content)
        win32clipboard.CloseClipboard()

    def init(self):

        self.labelLeft.setText(self.title)
        self.labelLeft.setStyleSheet("background-color: skyblue")

        self.labelRight.setText(self.showContent())
        self.labelRight.setStyleSheet("outline: solid 1px")

        self.btnCopy.clicked.connect(self.copyAction)
        self.btnCopy.setMaximumWidth(40)

        # self.btnDel.setStyleSheet("background-color: pink;")
        # self.btnDel.setMaximumWidth(20)

        # --- 添加
        self.addWidget(self.labelLeft)
        self.addWidget(self.labelRight)
        self.addWidget(self.btnCopy)
        # self.addWidget(self.btnDel)
        ...

    def showContent(self):
        """返回显示在界面上的简短缩略的内容"""
        res = self.content[:30]
        res = res.replace("\n", " ")
        return res

    @classmethod
    def fromFileName(cls, fileName: str):
        """通过文件名读取"""
        try:
            with open(f"myData/{fileName}", encoding="utf-8") as f:
                content = f.read()
            # if len(content) > 15:
            #     content = content[:15] + "..."
            return cls(fileName, content)
        except UnicodeDecodeError:
            print(fileName, "无法读取内容或者文件名")

    def clear(self):
        """清空当前这个条目里的所有内容"""
        print("触发了clear")
        self.removeWidget(self.btnCopy)
        self.btnCopy.setParent(None)

        # self.removeWidget(self.btnDel)
        self.removeWidget(self.labelLeft)
        self.labelLeft.setParent(None)
        self.removeWidget(self.labelRight)
        self.labelRight.setParent(None)
        ...

    ...
