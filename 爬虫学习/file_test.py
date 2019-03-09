import os,sys

fd = open("file_test.txt", 'r')
print(fd)

# 打开文件
fo = os.open("file_test.txt", os.O_RDWR|os.O_CREAT)
print("文件名为：", fo)

fo = os.fdopen(fo, 'w+')
print(fo)

# # 读取文件
# line = fo.readline()
# print("读取的数据为：{0}".format(line))

# 使用 tell()方法，获取当前文件的位置
# pos = fo.tell()
# print("当前位置：{0}".format(pos))

#fo.close()
#os.close(fo)