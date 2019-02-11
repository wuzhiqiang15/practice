# 使用DOM来解析xml文件

from xml.dom.minidom import parse
import xml.dom.minidom

'''
minidom的方法：
- minidom.parse(filename):加载读取的xml文件，filename也可以是xml代码
- documentElement:获取xml文档对象，一个xml文件只有一个文档对象
- getAttribute(attr_name)：获取xml节点的属性值
- getElementsByTagName(tage_name)：得到一个节点的对象集合
- childNodes:获取所有的子节点
- childNodes[index].nodeValue：获取单个节点值
- firstNode：获取第一个节点，等价于childNodes[0]
- attributes[tage_name]
'''

# 使用minidom解析器打开xml文档
DOMTree = xml.dom.minidom.parse("test_01.xml")

# 获取xml的文档对象，一个xml文件只有一个文档对象
collection = DOMTree.documentElement

if collection.hasAttribute("shelf"):
    print("Root element : %s" % collection.getAttribute("shelf"))

# 获取所有的子节点
movies = collection.getElementsByTagName("movie")
print("movies的内容是：{0}".format(movies))

for movie in movies:
    print("-------------------Movie------------------------")
    if movie.hasAttribute("title"):
        print("Title为:%s" % movie.getAttribute("title"))

    type = movie.getElementsByTagName("type")[0]
    print("type的值为:{0}".format(type.childNodes[0].data))

    format = movie.getElementsByTagName("format")[0]
    print("format的值为:%s" % format.childNodes[0].data)

    description = movie.getElementsByTagName("description")[0]
    print("description的值为：{0}".format(description.childNodes[0].data))


