"""
set集合 不可以重复 无序存储 不支持while遍历
可以修改
不支持下标索引
"""

# myset = {1, 2, 3}
#
# myset.add(4)  # 添加一个
#
# myset.remove(1)  # 移除一个
#
# element = myset.pop()  # 随机取一个
#
# myset.clear()  # 清空
#
# print(myset)


# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# set3 = set2.difference(set1)  # 取差集 set2有 1没有
#
# set1.difference_update(set2)  # 消除1中和2相同的元素
#
# set4 = set1.union(set2) # 合并
#
# print(set3)
# print(set1)
# print(set4)

list = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8]
set = set()
for i in list:
    set.add(i)
print(set)
