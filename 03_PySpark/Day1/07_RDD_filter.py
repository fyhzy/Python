from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/Software/ANACONDA/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

rdd2 = rdd.filter(lambda num: num % 2 == 0)

print(rdd2.collect())

sc.stop()
