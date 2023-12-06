"""
list.index() --找元素下标
list[下标] = x --修改
list.insert(下标，元素) --插入
list.append(元素) --尾部追加单个元素
list.extend(list2) --尾部追加列表
del list[下标] --删除单个元素
element（取出的元素）= list.pop(下标)  --取出并删除单个元素
list.remove(列表中的元素) --删除从左往右第一个指定元素
list.clear() --清空列表
count = list.count(元素) --输出元素出现的次数
len = len(列表) --输出列表元素个数
"""

list = [21, 25, 21, 23, 22, 20]

list.append(31)
list.extend([29, 33, 30])
first = list[0]
end = list[len(list)-1]
index = list.index(31)


print(list)
print(first)
print(end)
print(index)