import multiprocessing
from time import ctime

def comsumer(input_q):
    print("Into consumer:",ctime())
    while True:
        # 处理项
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q")# 此处替换为有用的工作
        input_q.task_done()# 发出信号通知任务完成
    print("out of consumer:", ctime())

def producer(sequence, output_q):
    print("Into producer:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("out of producer:", ctime())

if __name__=='__main__':
    q = multiprocessing.JoinableQueue()
    # 运行消费者进程
    con_p = multiprocessing.Process(target=comsumer, args=(q,))
    con_p.daemon = True
    con_p.start()

    # 生产多个项,sequence代表发送给消费者的项序列
    # 在实践中,这可能是生成器的输出或通过一些其他地方生产出来
    sequence = [1, 2, 3, 4]
    q.put(None)
    producer(sequence, q)
    # 等待所有项目被处理
    q.join()