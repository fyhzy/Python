
s = 5000000


def select():
    global s
    print("------------查询余额------------")
    print(f"您的余额剩余{s}元")


def cunk():
    global s
    print("------------存款------------")
    s += 50000
    print(f"您存款50000成功，剩余{s}元")


def quk():
    print("------------取款------------")
    global s
    s -= 50000
    print(f"您取款50000成功，剩余{s}元")


def menu():
    print("------------主菜单------------")
    print("您好，欢迎来到fy银行，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    print("请输入您的选择：")
    return input()


while True:
    op = menu()
    if op == "1":
        select()
        continue
    elif op == "2":
        cunk()
        continue
    elif op == "3":
        quk()
        continue
    elif op == "4":
        break
