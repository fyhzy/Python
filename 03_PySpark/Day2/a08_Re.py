"""
    python正则表达式re模块的3个基础匹配方法
"""

import re

# match 从头匹配
# s = "1python way"
#
# res = re.match("python", s)
# print(res)
# print(res.group())

# search 找到第一个后停止
# s = "the way things go"
# res = re.search("way", s)
# print(res)

# findall 全部查找
s = "the way things go way"
res = re.findall("way", s)
print(res)
