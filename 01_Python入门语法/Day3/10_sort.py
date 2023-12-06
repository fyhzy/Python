"""
排序： sorted(容器,reverse = True)降序
得到新的容器
默认升序
字典会丢失value
"""
list =[1, 2, 2, 4, 2, 3, 5]

list = sorted(list)
print(list)

list = sorted(list, reverse=True)
print(list)
