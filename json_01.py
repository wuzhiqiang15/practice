import json

# 此时的student是一个dict格式的内容，不是json
student = {
    "name": "wuzhiqiang",
    "age": 18,
    "mobile": 18989478268
}

print(type(student))

# 把dict内容，转换为json格式
stu_json = json.dumps(student)
print(type(stu_json))
print("JSON对象:{0}".format(stu_json)+"\n")

# 把json格式，转换为dict内容
stu_dict = json.loads(stu_json)
print(type(stu_dict))
print("dict的对象:{0}".format(stu_dict))
