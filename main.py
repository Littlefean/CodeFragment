"""
控制台版本

"""
import os
import sys
from typing import Dict
import ctypes

import win32clipboard
import win32con
import keyboard

from match import m1

DICT: Dict[int, str] = {}  # 数字编号 int ：文件名 str


def refresh_dic():
    """刷新操作，此操作影响全局变量DICT"""
    # 初始化 dic
    DICT.clear()
    for i, file_name in enumerate(os.listdir("code")):
        DICT[i] = file_name


def show_list():
    """展示全部的代码文件列表"""
    for i, file_name in enumerate(os.listdir("code")):
        print(str(i).zfill(3), file_name)


def get_content_to_clipboard(file_name):
    """
    根据文件名，把文件名复制到粘贴板
    file_name: "xxx.txt"
    """
    with open(f"code/{file_name}", encoding="utf-8") as f:
        content = f.read()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, content)
    win32clipboard.CloseClipboard()


def change_color(color: int):
    """更改打印颜色"""
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
    return ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color)


def main():
    # 注册事件回调函数
    import key_hooks
    keyboard.hook(key_hooks.on_ctrl_s)

    print('注册完毕')
    refresh_dic()
    show_list()
    print("======")
    while True:
        # os.system("cls")
        print("请输入搜索关键字，空格隔开，如果只输入数字表示选定")
        input_word = input(">>>")
        if input_word.isdigit():
            # 纯数字，表示选定了
            input_num = int(input_word)
            if input_num in DICT:
                get_content_to_clipboard(DICT[input_num])
                print("内容已经进入您的粘贴板！")
            else:
                print("您输入的数字超出范围")
        elif input_word == "open":
            os.system(f'start {os.path.abspath("code")}')
        elif input_word == "refresh":
            refresh_dic()
            change_color(10)
            sys.stdout.write("已经刷新\n")
            change_color(15)
        elif input_word == "help":
            print("open  打开存放数据的文件夹")
            print("help  查看帮助")
            print("数字  选定某个标号的代码片段，复制到粘贴板")
            print("refresh  刷新数据文件，当你更改了数据文件夹里的文件时候用")

        else:
            # 是正常的检索
            is_find = False
            for i, file_name in enumerate(os.listdir("code")):
                if m1(input_word.split(), file_name):
                    is_find = True
                    change_color(10)
                    sys.stdout.write(str(i).zfill(3) + " " + file_name + '\n')
            change_color(15)
            if not is_find:
                change_color(12)
                sys.stdout.write("没有搜索到相关内容" + '\n')
                change_color(15)


if __name__ == "__main__":
    main()
