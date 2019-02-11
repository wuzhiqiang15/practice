# 协程的使用
# 协程是python 3.4 版本之后加入的
# 从技术角度上讲，协程就是一个你可以暂停执行的函数，或者干脆把协程理解为生成器

def simple_coroutine():
    print("-> start")
    x = yield  # 执行到yield时，会退出，然后下次执行，从yield的下一步开始
    print('->recived', x)

# 主线程
sc = simple_coroutine()
print(11111)
# 这里也可以使用 sc.send(None)，效果一样
next(sc)   # 预激

print(22222)
sc.send('test')