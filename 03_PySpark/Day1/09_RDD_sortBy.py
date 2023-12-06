from pyspark import SparkConf, SparkContext

import os

os.environ['PYSPARK_PYTHON'] = "D:/Software/ANACONDA/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.textFile("hello.txt")
word_rdd = rdd.flatMap(lambda x: x.split(" "))
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
res = word_with_one_rdd.reduceByKey(lambda a, b: a + b)

final_rdd = res.sortBy(lambda x: x[1], ascending=False, numPartitions=1)

print(final_rdd.collect())

# func: 按rdd中哪个数据进行排序
# ascending: true升序 false降序
# numPartition: 设置分区数为1

sc.stop()
