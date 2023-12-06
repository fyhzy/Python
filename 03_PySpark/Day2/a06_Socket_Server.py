"""
    Socket服务端开发
"""
import socket

# 创建对象
socket_server = socket.socket()
# 绑定ip地址和端口
socket_server.bind(("localhost", 8080))
# 监听端口
socket_server.listen(1)
# listen方法内接受一个整数传参数 表示接收的链接数量
# 等待客户端链接
# res: tuple = socket_server.accept()
# co = res[0]         # 客户端和服务端的链接对象
# address = res[1]    # 客户端的地址信息
co, address = socket_server.accept()
# accept 方法返回的使二元元组(链接对象，客户端地址信息)
# 可以通过变量1,变量2 = socket_server.accept()的形式 直接接收二元元组内的两个元素
# accept()方法 使阻塞的方法 等待客户端的连接 如果没有连接 就卡在这一行
print(f"接收到了客户端的链接 客户端的信息使{address}")
while True:
    # 接收客户端信息
    data: str = co.recv(1024).decode("UTF-8")
    # recv 接收的数据是缓冲区大小 返回值是一个bytes对象 不是字符串 通过decode方法解码 将字节数组转换为字符串对象
    print(f"客户端发来的消息是：{data}")
    # 发送回复消息
    msg = input("请输入你要和客户端回复的信息：")  # encode可以将字符串编码为字节数组对象
    if msg == 'exit':
        break
    co.send(msg.encode("UTF-8"))
# 关闭链接
co.close()
socket_server.close()
