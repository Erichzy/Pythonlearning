import threading

sum = 0
loopSum = 1000000
def myAdd():
    global sum, loopSum
    for i in range(1, loopSum+1):
        sum += 1

def myMinu():
    global sum, loopSum
    for i in range(1, loopSum+1):
        sum -= 1





if __name__ =="__main__":
    print("starting at sum = {0}".format(sum))

    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("end at sum = {0}".format(sum))