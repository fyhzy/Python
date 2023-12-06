from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/Software/ANACONDA/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(["the way things", "go", "for", "forever"])

# 将RDD数据里面的单词一个个提取出来
rdd2 = rdd.flatMap(lambda x: x.split(" "))
print(rdd2.collect())

sc.stop()
