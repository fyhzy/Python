from pyspark import SparkConf, SparkContext

import os

os.environ['PYSPARK_PYTHON'] = "D:/Software/ANACONDA/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 1, 3, 3, 5, 6, 7, 8])

# 去重
rdd2 = rdd.distinct()

print(rdd2.collect())

sc.stop()