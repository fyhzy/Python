"""
全国疫情可视化地图开发
"""
import json

from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f = open("疫情.txt", "r", encoding="UTF-8")
data = f.read()

f.close()

data_dict = json.loads(data)

# 从字典中取出省份的数据
province_data_list = data_dict["areaTree"][0]["children"]

# 组装每个省份和确诊人数为元组 并将各个省的数据都封装到列表内
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]  # 省份名称
    province_confirm = province_data["total"]["confirm"]  # 确诊人数
    data_list.append((province_name, province_confirm))

for i in range(len(data_list)):
    temp_list = list(data_list[i])
    if temp_list[0] in ["上海", "北京", "重庆"]:
        temp_list[0] += "市"
    elif temp_list[0] in ["澳门", "香港"]:
        temp_list[0] += "特别行政区"
    elif temp_list[0] in ["内蒙古", "西藏"]:
        temp_list[0] += "自治区"
    elif temp_list[0] == "广西":
        temp_list[0] += "壮族自治区"
    elif temp_list[0] == "新疆":
        temp_list[0] += "维吾尔自治区"
    elif temp_list[0] == "宁夏":
        temp_list[0] += "回族自治区"
    else:
        temp_list[0] += "省"
    data_list[i] = tuple(temp_list)

print(data_list)

map = Map()
map.add("各省份确诊人数", data_list, "china")

map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        # 是否显示
        is_show=True,
        # 是否分段
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100~999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000~4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000~9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000~99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000+", "color": "#990033"},
        ]
    )
)

# 绘图
map.render("全国疫情地图.html")
