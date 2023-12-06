"""
    GDP动态柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts

f = open("1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
f.close()

# 删除第一条数据
data_lines.pop(0)

# 将数据转化为字典存储
# {年份:[  [国家,gdp],[国家,gdp], ...... ],  年份: [  [国家,gdp],[国家,gdp], .......  ],  ...... }
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])  # 年份
    country = line.split(",")[1]  # 国家
    gdp = float(line.split(",")[2])  # gdp
    # 如何判断字典里面有没有指定的key?
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# print(data_dict)

# 创建时间线对象
timeline = Timeline(
    {"theme": ThemeType.LIGHT}
)

# 排序年份
sorted_year_list = sorted(data_dict.keys())
# print(sorted_year_list)

for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份前八名国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # x轴添加国家
        y_data.append(country_gdp[1])  # y轴添加gdp数据

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转xy轴
    bar.reversal_axis()
    # 设置每一年的图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前八GDP数据")
    )

    timeline.add(bar, str(year))

# 设置自动播放
timeline.add_schema(
    play_interval=500,
    is_timeline_show=True,
    is_loop_play=False,
    is_auto_play=True,
)

# 绘图
timeline.render("1960-2019全球GDP前八国家.html")
