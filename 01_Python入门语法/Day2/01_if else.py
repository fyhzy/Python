print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
age = int(input("请输入你的年龄："))
# age = int(age)
if age >= 18:
    print("您已成年，游玩需要补票10元。")
elif age > 10:
    print("大于十岁")
elif age > 5:
    print("大于五岁")
else:
    print("小于等于五岁")
