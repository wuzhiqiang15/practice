import xml.etree.ElementTree

# 用etree打开xml文件
root = xml.etree.ElementTree.parse("student.xml")

# 利用getiterator访问xml对象（可以获取到xml下的所有子节点信息）
nodes = root.getiterator()
for node in nodes:
    print("节点属性为：{0}--{1}".format(node.tag, node.text))

# 利用find和findall方法
ele_teacher = root.find("Teacher")
#print(type(ele_teacher))
print("\n"+"Teacher节点的属性是：{0}--{1}".format(ele_teacher.tag, ele_teacher.text))

ele_stus = root.findall("Student")
#print(type(ele_stus))
for ele in ele_stus:
    print("\n"+"Student节点的属性为：{0}--{1}".format(ele.tag, ele.text))
    # 获取"Student"节点下的所有子节点信息
    for sub in ele.getiterator():
        if sub.tag == "Name":
            if "Other" in sub.attrib.keys():
                print(sub.attrib["Other"])