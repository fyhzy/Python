"""
    面向对象 ———— 数据案例分析
"""
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pymysql import Connection

from FIle_Define import TextFileReader, JsonFileReader
from Data_Define import *
from pyecharts.options import *

textFileReader = TextFileReader("2011年1月销售数据.txt")
jsonFileReader = JsonFileReader("2011年2月销售数据JSON.txt")

Jan_data: list[Record] = textFileReader.read_data()
Feb_data: list[Record] = jsonFileReader.read_data()

# 将两个月份的数据合并为一个list存储
all_data: list[Record] = Jan_data + Feb_data

# print(all_data)

# 构建mysql 链接对象
co = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)
# 获得游标对象
cursor = co.cursor()

# 选择数据库
co.select_db("py_sql")

# 组织sql语句
for record in all_data:
    sql = f"insert into orders(order_date,order_id,money,province)" \
          f"values('{record.date}','{record.order_id}',{record.money},'{record.province}')"
    cursor.execute(sql)

co.close()
