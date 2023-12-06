"""
对序列进行切片
string[1,2,3]   tuple list 都一个道理
1:起始下标 不填就是从头
2:结束下标 不填就是结尾
3:步长 不多说
"""
string = "12346789"
res = string[::-1]  # 倒序

print(res)
