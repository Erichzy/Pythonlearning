'''
 - Server端流程
            1. 建立socket，socket是负责具体通信的一个实例
            2. 绑定，为创建的socket指派固定的端口和ip地址
            3. 接受对方发送内容
            4. 给对方发送反馈，此步骤为非必须步骤
'''

import socket

# 建立socket
def clientFunc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = "你吃了吗"
    # 发送的数据闭学式bytes格式
    data = text.encode()

    # 发送
    sock.sendto(data,("127.0.0.1", 7852))

    # 接受反馈
    data, addr = sock.recvfrom(200)

    # 解码
    text = data.decode()
    print(text)

if __name__ == '__main__':
    clientFunc()
