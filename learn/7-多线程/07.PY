import time
import threading


def fun():
    print("start fun at:", time.ctime())
    time.sleep(4)
    print("end fun at:", time.ctime())


print("start main thread at", time.ctime())

t1 = threading.Thread(target=fun, args=())
# 设置守护线程的方法,必须在start之前设置,否则无效
t1.setDaemon(True)
# 第二种设置方法t1.daemon = True
t1.start()

time.sleep(1)
print("end main thread at", time.ctime())