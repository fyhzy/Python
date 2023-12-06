# from pymysql import Connection
#
# co = Connection(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="123456",
#     autocommit=True
# )
#
# f = open("homework", "w", encoding="UTF-8")
#
# co.select_db("py_sql")
# cursor = co.cursor()
# sql = "select order_date,order_id,money,province from orders"
# cursor.execute(sql)
#
# data = cursor.fetchall()
#
# json_data = {}
#
# for record in data:
#     json_data[data]
#
# f.write(str(json_data))
#
# f.close()
# co.close()
