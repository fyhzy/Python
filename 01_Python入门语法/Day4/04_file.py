fr = open("file.txt", "r", encoding="UTF-8")
fw = open("file.txt.bak", "w", encoding="UTF-8")

for line in fr:
    line = line.strip()
    if line.split(",")[4] == "测试":
        continue
    else:
        # 写出内容 包括换行符
        fw.write(line)
        fw.write("\n")

fr.close()
fw.close()
