from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/Software/ANACONDA/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([('男', 98), ('男', 99), ('女', 95), ('女', 99)])

rdd2 = rdd.reduceByKey(lambda a,b:a+b)
print(rdd2.collect())

sc.stop()
