# logging模块的四大组件（四个实现类）
# 日志器  Logger   提供了应用程序可一直使用的接口
# 处理器  Handler  将logger创建的日志发送到对应路径
# 过滤器  Filter   提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
# 格式器  Formatter  决定日志内容的输出格式

# 需要注意的是，Logger、Handler、Filter和Formatter都是类，可以被继承和实例化
import logging

# 创建一个logger类的对象
log_1 = logging.getLogger()
# 设置logger类的日志级别
log_1.setLevel(logging.DEBUG)
# 创建一个Handler类对象，并指定日志输出的文件
handler_1 = logging.FileHandler("test_02.txt")
# 构造Formatter类，指定日志输出的格式
format_1 = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%m/%d/%Y %H:%M:%S")
# 为Handler设置format对象（以本次为例，设置test_02.txt文件使用format_1中指定的格式）
handler_1.setFormatter(format_1)
# 为logger对象指定格式器（这里选择了handler_1格式器，所以会使用handler_1中设置的日志输出文件以及格式）
log_1.addHandler(handler_1)
# 打印一条日志内容（由于前面选择了handler和formatter，所以这里输出的内容会包含以上的设置）
log_1.warning("a warning log will be print")
log_1.error("this is a error log")

