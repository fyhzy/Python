"""
    装饰器的用法
"""
import random, time


# 装饰器的一般写法 闭包

# def outer(func):
#     def inner():
#         print("我睡觉了")
#         func()
#         print("我起床了")
#
#     return inner
#
#
# def sleep():
#     import random, time
#     print("睡眠中......")
#     time.sleep(random.randint(1, 5))
#
#
# fn = outer(sleep)
# fn()


# 装饰器快捷写法 语法糖
def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我起床了")

    return inner


@outer
def sleep():
    print("睡眠中......")
    time.sleep(random.randint(1, 5))


sleep()