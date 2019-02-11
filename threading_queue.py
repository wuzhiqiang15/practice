import queue
import time
import threading
import logging

# 设置log
log = logging.getLogger()
log.setLevel(logging.INFO)
handler = logging.FileHandler("threading_queue.txt")
format = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
handler.setFormatter(format)
log.addHandler(handler)

# 生产者
class Producer(threading.Thread):
    def run(self):
        global queue_1
        count = 0
        while True:
            # qsize() 放回queue的内容长度
            if queue_1.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = "生产的产品" + str(count)
                    # put() 是往queue中放入内容
                    queue_1.put(msg)
                    #print(msg)
                    log.info(msg)
            time.sleep(0.5)

# 消费者
class Consumer(threading.Thread):
    def run(self):
        global queue_1
        while True:
            if queue_1.qsize() > 100:
                for i in range(3):
                    # get()是从queue从取出一个值
                    # 这里get()取到的值，是之前用put()方法放进queue中的内容
                    msg = self.name + "消费了" + queue_1.get()
                    #print(msg)
                    log.info(msg)
            time.sleep(1)

if __name__ == "__main__":
    # 生成queue队列的实例
    queue_1 = queue.Queue()
    for i in range(500):
        queue_1.put("初始化产品"+ str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()