# 使用logging.basicConfig()方法对logging进行一系列基本配置
# logging,basicConfig()是一次性配置的，调用一次后，后续再次调用不会生效
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S"

logging.basicConfig(filename="test01.txt", level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

logging.debug("this is a debug log.")
logging.info("this is a info log.")
logging.warning("this is a warning log")
logging.error("this is a error log")
logging.critical("this is a critical log")
logging.log(logging.WARNING, "%s is %d years old.", 'Tom', 15)
