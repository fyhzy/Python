"""
    面向对象 ———— 数据案例分析
"""
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

from FIle_Define import TextFileReader, JsonFileReader
from Data_Define import *
from pyecharts.options import *

textFileReader = TextFileReader("2011年1月销售数据.txt")
jsonFileReader = JsonFileReader("2011年2月销售数据JSON.txt")

Jan_data: list[Record] = textFileReader.read_data()
Feb_data: list[Record] = jsonFileReader.read_data()

# 将两个月份的数据合并为一个list存储
all_data: list[Record] = Jan_data + Feb_data

# 开始进行数据计算
# {"2011-01-01": 1312,"2011-01-02": 200, ...}
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日期有记录 和老记录做累加
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# print(data_dict)

# 可视化图表开发

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("每日销售额柱状图.html")
