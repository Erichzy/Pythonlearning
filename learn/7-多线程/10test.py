import time
import threading


class Loop:
    def __init__name(self,name):
        self,name = name

    def Func(self, loop_name, sleep_time):
        print ("start {0} at {1}".format(loop_name, time.ctime()))
        time.sleep(sleep_time)
        print ("end {0} at {1}".format(loop_name, time.ctime()))

def main():
    print("start main at:",time.ctime())
    # 实例化一个类,便于后续引用类的功能
    t = Loop()
    t1 = threading.Thread(target=t.Func, args=("loop1", 5))
    t2 = threading.Thread(target=t.Func, args=("loop2", 3))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print("end main at:", time.ctime())


if __name__=="__main__":
    main()