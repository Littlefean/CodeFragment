from PyQt5.QtWidgets import *


class MyItem(QHBoxLayout):
    """表示横着的一条数据项"""

    def __init__(self, title: str, content: str):
        super().__init__()
        self.title = title
        self.content = content
        self.init()

    def init(self):
        # 标题
        labelLeft = QLabel()
        labelLeft.setText(self.title)
        labelLeft.setStyleSheet("background-color: skyblue")
        # 内容
        labelRight = QLabel()
        labelRight.setText(self.content)
        labelRight.setStyleSheet("outline: solid 1px")

        # 复制按钮
        btnCopy = QPushButton()
        btnCopy.setText("复制")
        btnCopy.setMaximumWidth(40)

        # 删除按钮
        btnDel = QPushButton()
        btnDel.setText("X")
        btnDel.setStyleSheet("background-color: pink;")
        btnDel.setMaximumWidth(20)

        # --- 添加
        self.addWidget(labelLeft)
        self.addWidget(labelRight)
        self.addWidget(btnCopy)
        self.addWidget(btnDel)
        ...

    ...
