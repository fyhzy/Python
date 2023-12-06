def PrintHs():
    print("海龟先生是一只来自广西的乐队！\n欢迎来到海龟的现场！")
    # print("欢迎来到海龟的现场！")


def Check(temperature):
    """

    :param temperature: 接受一个参数表示温度
    :return: 温度
    """
    if temperature <= 37.5:
        print(f"体温{temperature}正常")
    else:
        print(f"体温{temperature}异常")
    return temperature


tem = Check(37)
