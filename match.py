"""
存放匹配机制函数
"""


def m1(arr, string) -> bool:
    """
    检测输入的关键词列表是否和 目标字符串匹配
    对于arr中的每一个小字符串，检测他们是否都是string的子串
    """
    return all(content in string for content in arr)
