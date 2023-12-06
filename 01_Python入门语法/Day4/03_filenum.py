f = open("word.txt", "r", encoding="UTF-8")

# 法1
# content = f.read()
# count = content.count("th")
# print(count)

count = 0
for line in f:
    line = line.strip() # 去除开头和结尾的空格以及换行符
    words = line.split(" ")
    for word in words:
        if word == "within":
            count += 1

print(count)
f.close()
