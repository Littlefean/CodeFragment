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


def refreshDic():
    # 初始化 dic
    dic.clear()
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
    refreshDic()
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
        elif inputWord == "refresh":
            refreshDic()
            changeColor(10)
            sys.stdout.write("已经刷新\n")
            changeColor(15)
        elif inputWord == "help":
            print("open  打开存放数据的文件夹")
            print("help  查看帮助")
            print("数字  选定某个标号的代码片段，复制到粘贴板")
            print("refresh  刷新数据文件，当你更改了数据文件夹里的文件时候用")

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
                changeColor(15)


if __name__ == "__main__":
    main()
