"""
控制台版本

"""
import os
from match import m1
import win32clipboard
import win32con
import sys
import ctypes

inputWord = ""
dic = {}  # 数字编号 int ：文件名 str


def init():
    # 初始化 dic
    for i, fileName in enumerate(os.listdir("myData")):
        dic[i] = fileName


def showList():
    for i, fileName in enumerate(os.listdir("myData")):
        print(str(i).zfill(3), fileName)


def getContentToClipboard(fileName):
    with open(f"myData/{fileName}", encoding="utf-8") as f:
        content = f.read()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, content)
    win32clipboard.CloseClipboard()


def changeColor(color: int):
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
    return ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color)


def main():
    global inputWord
    init()
    showList()
    print("======")
    while True:
        # os.system("cls")
        print("请输入搜索关键字，空格隔开，如果只输入数字表示选定")
        inputWord = input(">>>")
        if inputWord.isdigit():
            # 纯数字，表示选定了
            inputNum = int(inputWord)
            if inputNum in dic:
                getContentToClipboard(dic[inputNum])
                print("内容已经进入您的粘贴板！")
            else:
                print("您输入的数字超出范围")
        elif inputWord == "open":
            os.system(f'start {os.path.abspath("myData")}')
        else:
            # 是正常的检索
            isFind = False
            for i, fileName in enumerate(os.listdir("myData")):
                if m1(inputWord.split(), fileName):
                    isFind = True
                    changeColor(10)
                    sys.stdout.write(str(i).zfill(3) + " " + fileName + '\n')
            changeColor(15)
            if not isFind:
                changeColor(12)
                sys.stdout.write("没有搜索到相关内容" + '\n')


if __name__ == "__main__":
    main()
