name = "This is an event"
count = 0
for x in name:
    if x == "s":
        count += 1
# print(count)
# 九九乘法表

for x in range(1,10):
    for y in range(1,x+1):
        print(f"{x}*{y}={x*y}\t",end='')
    print()


