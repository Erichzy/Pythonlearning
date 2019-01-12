import socket
def tcp_srv():
    # 1.建立所持socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )

    # 2.绑定ip和端口
    addr = ("127.0.0.1", 8998)

    sock.bind(addr)

    # 3.监听接入的访问socket
    sock.listen()

    while True:
        # 4.接受访问的socket,可以理解接受访问即建立了一个通讯链接
        # accept返回的元组第一个元素赋值给skt(虚拟通道),第二个赋值给addr
        skt,addr = sock.accept()
        # 5.接受对方发送内容,利用接收到的socket接收内容
        # 500代表接收使用的buffersize
        msg = skt.recv(500)

        msg = msg.decode()

        rst = "我收到了{0},是你吧{1}".format(msg, addr)
        # 返回消息
        skt.send(rst.encode())
        print(msg)
        print(addr)
        # 关闭链路
        skt.close()

if __name__ == "__main__":
    print('start')
    tcp_srv()
    print("end")
