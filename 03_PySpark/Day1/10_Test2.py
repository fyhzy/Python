import json

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/Software/ANACONDA/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 1、城市销售额排名
file_rdd = sc.textFile("orders.txt")
# 取出一个个JSON字符串
json_rdd = file_rdd.flatMap(lambda x: x.split("|"))
# 转换为字典
dict_rdd = json_rdd.map(lambda x: json.loads(x))
# print(dict_rdd.collect())
# 取出城市和销售额数据
city_money = dict_rdd.map(lambda x: (x['areaName'], int(x['money'])))

city_res = city_money.reduceByKey(lambda a, b: a + b)

res = city_res.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print(res.collect())

# 2、全部城市有哪些商品类别在售卖
category = dict_rdd.map(lambda x: x['category']).distinct()
print(category.collect())

# 3、北京有哪些商品在售卖

beijing = dict_rdd.filter(lambda x: x['areaName'] == '北京')
res = beijing.map(lambda x: x['category']).distinct()

print(res.collect())

sc.stop()
