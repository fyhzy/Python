"""
数据可视化  ———— 折线图开发

"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# 数据处理
f_us = open("美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
f_jp = open("日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()
f_in = open("印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()
# 去掉不合规范的
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# 去掉最后两个字符
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]
# json转字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# print(type(us_dict))
# print(us_dict)

us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 取日期 x轴
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 确诊人数 y轴
us_y_data = us_trend_data['list'][0]['data']
jp_y_data = jp_trend_data['list'][0]['data']
in_y_data = in_trend_data['list'][0]['data']

line = Line()

# x轴是共用的
line.add_xaxis(us_x_data)

# y轴
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局选项

line.set_global_opts(
    # 标题
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")

)

line.render()

f_in.close()
f_jp.close()
f_us.close()
