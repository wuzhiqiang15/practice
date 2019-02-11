# 修改xml文件，这里使用的是etree

import xml.etree.ElementTree as et

tree = et.parse(r"to_edit.xml")

root = tree.getroot()

# 找到所有名为"Name"的子节点
for e in root.iter("Name"):
    print(e.text)

for stu in root.iter("Student"):
    name = stu.find("Name")

    if name != None:
        name.set("test_01", name.text * 2)

stu = root.find("Student")

# 生成一个新的元素
e = et.Element("ADDer")
e.attrib = {"a": "b"}
e.text = "test001"

stu.append(e)

# 一定要把修改后的内容写进文件，否则修改无效（未执行这一步之前，修改的内容，都没有被保存到文件中）
tree.write("to_edit.xml")
