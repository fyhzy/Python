from pyspark import SparkConf, SparkContext

import os

os.environ['PYSPARK_PYTHON'] = "D:/Software/ANACONDA/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

file_rdd = sc.textFile("search_log.txt", 1)
# 1、热门搜索时间段Top3
"""
    取出全部时间并转换为小时
    转换为(小时,1)的二元元组
    Key分组聚合value
    降序排序
    取前三
"""
res1 = file_rdd.map(lambda x: (x.split("\t")[0][:2], 1)). \
    reduceByKey(lambda a, b: a + b). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(3)
print(res1)

# 2、热门搜索词Top3
"""
    取出全部搜索词
    二元元组
    分组聚合
    排序
    Top3
"""
res2 = file_rdd.map(lambda x: (x.split("\t")[2], 1)). \
    reduceByKey(lambda a, b: a + b). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(3)
print(res2)

# 3、统计黑马程序员关键字在什么时段被搜索的最多
"""
    过滤内容 只保留黑马程序员关键字
    转换为二元元组
    分组聚合
    排序
    取Top1
"""
res3 = file_rdd.map(lambda x: x.split("\t")). \
    filter(lambda x: x[2] == '黑马程序员'). \
    map(lambda x: (x[0][:2], 1)). \
    reduceByKey(lambda a, b: a + b). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(1)
print(res3)

# 4、将数据转化为JSON格式 写出到文件中
"""
    转化为JSON格式的RDD
    写出为文件
"""
file_rdd.map(lambda x: x.split("\t")). \
    map(lambda x: {"time": x[0], "user_id": x[1], "key_word": x[2], "rank1": x[3], "rank": x[4], "url": x[5]}). \
    saveAsTextFile("output_json")
