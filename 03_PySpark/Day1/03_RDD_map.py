# map 算子  rdd成员方法

from pyspark import SparkConf, SparkContext
# 找到python解释器
import os

os.environ['PYSPARK_PYTHON'] = "D:/Software/ANACONDA/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

# lambda匿名函数
rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)

print(rdd2.collect())
# (T) -> U 传入一个值 返回一个值
# (T) -> T 传入和返回类型要一致

sc.stop()
