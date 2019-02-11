# 负责启动WSGI服务器，加载application()
# 从WSGI服务器导入
from wsgiref.simple_server import make_server

# 导入我们自己编写的hello_web模块中的application函数
from WSGI_01.hello_web import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application
httpd = make_server('', 8000, application)

print('Serving HTTP on port 8000...')

# 开始监听HTTP请求：
httpd.serve_forever()