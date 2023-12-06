# collect

from pyspark import SparkConf, SparkContext

import os

os.environ['PYSPARK_PYTHON'] = "D:/Software/ANACONDA/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

rdd_list: list = rdd.collect()
print(rdd_list)
print(type(rdd_list))

# reduce 对rdd进行两两聚合
num = rdd.reduce(lambda a, b: a + b)
print(num)

# 取出rdd前n个元素 组成list返回
take_list = rdd.take(3)
print(take_list)

# count 统计rdd内有多少条数据 返回值为数字
num_count = rdd.count()
print(num_count)

sc.stop()
