def func(computer):
    result = computer(1, 2)
    print(result)


# lambda 临时匿名函数 只能写一行

func(lambda x, y: x - y)
