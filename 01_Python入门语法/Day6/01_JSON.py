import json

data = [{"name": "张三", "age": 11}, {"name": "李四", "age": 15}, {"name": "王五", "age": 17}]

json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

d = {"name": "张三", "age": 11}
json_str = json.dumps(d, ensure_ascii=False)
print(json_str)

s = '[{"name": "张三", "age": 11}, {"name": "李四", "age": 15}, {"name": "王五", "age": 17}]'
l = json.loads(s)
print(type(l))
print(l)
