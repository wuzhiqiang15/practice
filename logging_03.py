'''
需求内容：
1）要求将所有级别的所有日志都写入磁盘文件中
2）all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
3）error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
4）要求all.log在每天凌晨进行日志切割
'''

import logging
#import logging.handlers
from logging import handlers
import datetime

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 设置两个format，用于不同的输出格式
format_all = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%m/%d/%Y %H:%M:%S")
format_error = logging.Formatter(fmt="%(asctime)s - %(levelname)s -%(filename)s[:%(lineno)d] - %(message)s")

# 设置两个handler
all_handler = logging.handlers.TimedRotatingFileHandler("all.log", when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
error_handler = logging.FileHandler("error.log")

# error.log单独记录error级别的日志，所以需要单独设置
error_handler.setLevel(logging.ERROR)

# 为两个handler分别设置format
all_handler.setFormatter(format_all)
error_handler.setFormatter(format_error)

# 为日志设置添加两个handler对象，用来将日志记录到不同的文本中
logger.addHandler(all_handler)
logger.addHandler(error_handler)

# 输出内容
logger.debug("this is a debug log")
logger.info("this is a info log")
logger.warning("this is a warning log")
logger.error("this is a error log")
logger.critical("this is a critical log")
