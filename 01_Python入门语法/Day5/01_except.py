"""
异常捕获 异常具有传递性
"""
# 普通捕获
try:
    f = open("123.txt","r",encoding="UTF-8")
except:
    f = open("123.txt","w",encoding="UTF-8")

# 指定捕获

# try:
#     print(n)
#     1 / 0
# except (NameError,ZeroDivisionError) as e:
#     print("出现了变量未定义异常")
#     print("出现了异常")
#     print(e)

# 捕获所有异常
try:
    1/0
except Exception as e:
    print(e)
else:
    #无异常执行
    print("hello")
finally:
    # 有无异常都执行
    print("end")
    f.close()