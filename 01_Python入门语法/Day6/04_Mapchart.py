from pyecharts.charts import Map
from pyecharts.options import global_options, VisualMapOpts

# 准备地图对象
map = Map()

# 准备数据
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省", 499)
]

map.add("测试地图", data, "china")

# 设置全局选项

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#123f56"},
            {"min": 10, "max": 99, "label": "1-9", "color": "#564c12"},
            {"min": 100, "max": 500, "label": "1-9", "color": "#561217"}
        ]
    )
)

map.render()
