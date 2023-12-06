"""
    python的闭包特性
"""


# 简单闭包
# def outer(logo):
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
# fn1 = outer("fy")
# fn1("大家好")
# fn1("大家好")
#
# fn2 = outer("zy")
# fn2("大家好")


# 使用 nonlocal 关键字修改外部函数的值
# def outer(num1):
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#
#     return inner
#
#
# fn = outer(10)
# fn(10)
# fn(10)


# ATM 小案例
def account_create(initial_account=0):
    def ATM(num, deposit=True):
        nonlocal initial_account
        if deposit:
            initial_account += num
            print(f"存款:+{num},余额{initial_account}")
        else:
            initial_account -= num
            print(f"取款:-{num},余额{initial_account}")

    return ATM


atm = account_create()
atm(100)
atm(100)
atm(100, False)
