# 单词统计

import os

from pyspark import SparkConf, SparkContext

os.environ['PYSPARK_PYTHON'] = "D:/Software/ANACONDA/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 读取数据挖掘
rdd = sc.textFile("hello.txt")

# 取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(" "))

# print(word_rdd.collect())

# 把所有单词都转换成二元元组 单词key value:1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
# 分组求和
res = word_with_one_rdd.reduceByKey(lambda a, b: a + b)

print(res.collect())

sc.stop()
