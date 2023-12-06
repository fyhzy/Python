# 发工资
import random

s = 10000
for i in range(1, 21):
    grade = random.randint(1, 10)
    if grade < 5:
        print(f"员工{i},绩效分{grade},低于5,不发工资,下一位。")
        continue
    else:
        if s != 0:
            s -= 1000
            print(f"向员工{i}发放工资1000元，账户余额还剩{s}元")
        else:
            print("工资发完了，下个月再领吧")
            break

