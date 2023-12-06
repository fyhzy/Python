import time

f = open("test.txt", "r", encoding="UTF-8")

print(type(f))

# read(n) 读取n个字节
# print(f.read())

# 接着上一个read读取
# print(f.read(10))

# readlines() 读取全部行 封装到列表中
# print(f.readlines())

# readline() 读取一行数据
# print(f.readline())
# print(f.readline())
# print(f.readline())
lines = f.readline()
for i in lines:
    print(i)

# f.close()

# with open 可以自动关闭文件

with open("test.txt", "r", encoding="UTF-8") as f:
    for i in lines:
        print(i)
