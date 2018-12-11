import time
import threading

def fun():
    print("start fun at:", time.ctime())
    time.sleep(4)
    print("end fun at:", time.ctime())

print("start main thread at", time.ctime())

t1 = threading.Thread(target=fun,args=())
t1.start()

time.sleep(1)
print("end main thread at", time.ctime())
