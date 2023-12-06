"""
string 只可以存储字符串 不可修改
str.replace(字符串1，字符串2) 替换1为2 得到一个新的字符串
str.split(间隔符) 分割得到列表
str.strip() 消除前后空格
str.strip(字符串) 不是简单的一个元素或者字符串 消除前后该字符串
"""

str = "it makes me so hysterical the way things go"
count = str.count("th")
str_ = str.replace(" ", "|")
list = str_.split("|")

print(count)
print(str_)
print(list)