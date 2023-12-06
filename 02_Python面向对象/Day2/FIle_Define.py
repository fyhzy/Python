import json

from Data_Define import Record


class FileReader:
    def read_data(self) -> list[Record]:
        """ 读取文件的数据 读到的每一条数据都转化位Record对象 将他们都封装到List中返回 """
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        # 定义成员变量 记录文件的路径
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            # 消除数据中每一行的\n
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    textFileReader = TextFileReader("2011年1月销售数据.txt")
    jsonFileReader = JsonFileReader("2011年2月销售数据JSON.txt")

    list1 = textFileReader.read_data()
    list2 = jsonFileReader.read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)
