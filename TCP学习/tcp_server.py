# 使用TCP服务

import socket


def tcp_srv():
    """
    1、建立socket负责具体通信，这个socket其实只负责接受对方的请求
    需要用到两个参数
    AF_INET：代表使用ipv4协议
    SOCK_STREAM：表明是使用 tcp 进行通信
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """
    2、绑定端口和地址
    此地址信息是一个元祖类型内容，元祖分两部分，第一部分为字符串，代表IP，第二部分代表端口
    """
    addr = ("127.0.0.1", 8998)
    sock.bind(addr)
    """
    3、监听接入的访问socket
    """
    sock.listen()

    while True:
        """
        4、接受访问的socket，可以理解接受访问即和客户端之间建立了一个通讯的连接通路
        accept()返回的第一个元素是socket标识符
        accept()返回的socket标识符赋值给变量skt（后续通过skt跟客户端的socket建立连接），返回的地址赋值给变量addr
        """
        skt, addr = sock.accept()
        """
        5、接收对方的发送内容，利用接收到的socket接受内容
        recv(500)代表接收使用的缓存区
        """
        msg = skt.recv(500)
        """
        接收到的必须是bytes格式内容
        所以需要用decode()方法进行解码
        """
        msg = msg.decode()

        rst = "Received msg:{0} from {1}".format(msg, addr)
        print(rst)
        """
        6、如果有必要，可以使用send()方法，给对方发送反馈信息
        要注意，这里用的是已经建立的socket通路，即被赋值后的变量skt
        """
        skt.send(rst.encode())
        """
        7、关闭链接通路
        """
        skt.close()

if __name__ == "__main__":
    print("Starting tcp server......")
    tcp_srv()
    print("End tcp server......")

