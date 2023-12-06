"""
扩展：
    列表的sort方法
"""

my_list = [["a", 33], ["b", 65], ["c", 11]]

# def choose_key(element):
#     return element[1]
# my_list.sort(key=choose_key(), reverse=True)

# lambda
my_list.sort(key=lambda element: element[1], reverse=True)

print(my_list)
