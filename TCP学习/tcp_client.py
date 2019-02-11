# tcp的客户端服务
import socket


def tcp_cli():
    # 1、建立通信的socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2、链接对方，使用connect()方法请求跟对方建立通路，这里要访问server端的ip和端口
    addr = ("127.0.0.1", 8998)
    sock.connect(addr)

    # 3、发送内容到对方服务器，这里注意要使用encode()将内容进行编码
    msg = "I like Python"
    sock.send(msg.encode())

    # 4、接收对方的返回内容
    rst = sock.recv(500)
    print(rst.decode())

    # 5、关闭链接通路
    sock.close()

if __name__ == "__main__":
    tcp_cli()
