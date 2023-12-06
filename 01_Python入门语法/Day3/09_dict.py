"""
dict字典 不可使用下标索引 不支持while遍历 无序
键值对
"""
dic = {"zhangsan": 100, "lisi": 99, "wangwu": 40}

# print(dic["zhangsan"])  # 取键对应值

# 嵌套
stu_score_dict = {
    "zhangsan": {
        "yuwen": 100,
        "shuxue": 100
    }, "lisi": {
        "yuwen": 99,
        "shuxue": 95
    }, "wangwu": {
        "yuwen": 98,
        "shuxue": 90
    }
}

score = stu_score_dict["zhangsan"]["yuwen"]

# 新增
dic["zhaoliu"] = 99
print(dic)

# 更新
dic["zhaoliu"] = 100
print(dic)

# 删除
dic.pop("zhaoliu")
print(dic)

# 清空
# dic.clear()
print(dic)

# 获取全部key
keys = dic.keys()
print(keys)
# 遍历1
for i in keys:
    print(i)
    print(dic[i])

# 遍历2
for key in dic:
    print(key)
    print(dic[i])

# 元素数量
len = len(dic)

print(len)
