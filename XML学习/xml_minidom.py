import xml.dom.minidom
# 负责解析XML文件
from xml.dom.minidom import parse

# 使用minidom打开xml文件
DOMTree = xml.dom.minidom.parse("student.xml")

# 得到xml文档对象
doc = DOMTree.documentElement
print("根目录下的所有子节点为:{0}".format(doc.childNodes))
# 获取根目录下的所有子节点（doc.childNodes 获取所有子节点）
for ele in doc.childNodes:
    if ele.nodeName == "Teacher":
        print("--------Node名称为:{0}---------".format(ele.nodeName))
        # 获取"Teacher"节点下面的所有子节点（ele.childNodes）
        childs = ele.childNodes
        for child in childs:
            if child.nodeName == "Name":
                # data是文本节点的一个属性，表示它的值
                print("Name:{0}".format(child.childNodes[0].data))
            if child.nodeName == "Mobile":
                print("Mobile:{0}".format(child.childNodes[0].data))
            if child.nodeName == "Age":
                print("Age:{0}".format(child.childNodes[0].data))
                if child.hasAttribute("detail"):
                    print("Age-detail:{0}".format(child.getAttribute("detail")))



