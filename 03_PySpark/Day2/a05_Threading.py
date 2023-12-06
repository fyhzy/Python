"""
    python 多线程编程
"""
import threading
import time


def sing(msg):
    print(msg)
    time.sleep(1)


def dance(msg):
    print(msg)
    time.sleep(1)


if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing, args=("唱歌",))
    dance_thread = threading.Thread(target=dance, kwargs={"msg": "跳舞"})

    sing_thread.start()
    dance_thread.start()
