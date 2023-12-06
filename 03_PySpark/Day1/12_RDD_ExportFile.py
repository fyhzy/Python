from pyspark import SparkConf, SparkContext

import os

os.environ['PYSPARK_PYTHON'] = "D:/Software/ANACONDA/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1, 2, 3, 4, 5])

rdd2 = sc.parallelize([("hello", 3), ("spark", 5), ("hadoop", 6)], 1)

rdd3 = sc.parallelize([[1, 3, 4], [2, 3, 5], [11, 32, 36]], 1)

rdd1.saveAsTextFile("output1")
rdd2.saveAsTextFile("output2")
rdd3.saveAsTextFile("output3")

sc.stop()
