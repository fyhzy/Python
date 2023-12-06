from pyspark import SparkConf, SparkContext

# 创建SparkConf对象 --链式调用
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# conf = SparkConf()
# conf.setMaster("local[*]")
# conf.setAppName("test_name")

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)
print(sc.version)

sc.stop()
