class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # @staticmethod
    # def display(name, age, address):
    #     print(f"学生姓名:{name}, 年龄:{age} ,地址:{address}")


for i in range(1, 11):
    print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")
    stu = Student(input("请输入学生姓名："), input("请输入学生年龄："), input("请输入学生地址："))
    print(f"第{i}位学生信息录入完毕,信息为：【学生姓名：{stu.name}, 年龄：{stu.age}, 地址：{stu.address})】")
