# ThreadLoacl的使用
import threading

# 创建全局ThreadLocal对象
# 这里要注意，local_school是ThreadLocal类的实例化对象，用来在下面进行各个线程之间参数的传递
local_school = threading.local()

# 该方法主要用来“读取”ThreadLocal对象的属性
def process_student():
    # 定义一个std变量，用来获取当前线程关联的student属性（student变量是在下面的process_thread()方法中定义的）
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

# 该方法主要用来“写”ThreadLocal对象的属性
def process_thread(name_1):
    # 给ThreadLocal创建一个student属性，并且将process_thread函数的参数赋值给student
    local_school.student = name_1
    process_student()   # 这里主要是为了将local_school.student的值传递给上面定义的process_student()方法，采用了闭包

# 分别定义两个线程 t1、t2
t1 = threading.Thread(target= process_thread, args=('Alice',), name= 'Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()