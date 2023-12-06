"""
    Python pymysql库的基础使用
"""

from pymysql import Connection

co = Connection(
    host="localhost",  # 主机名
    port=3306,  # 端口
    user="root",
    password="123456",
    autocommit=True
)

# 获取到游标对象
cursor = co.cursor()

co.select_db("test")

# cursor.execute("create table test_pymysql(id int, name varchar(128), grade int)")

cursor.execute("insert into test_pymysql values(7,'jiangjiu',83)")
# co.commit()


# cursor.execute("select* from test_pymysql")
# 结果存放在元组内
# res = cursor.fetchall()
# for r in res:
#     print(r)

# print(co.get_server_info())

co.close()
