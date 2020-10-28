import json

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
print(type(dic))  # <class 'dict'>

j = json.dumps(dic)
print(type(j))  # <class 'str'>

f = open('序列化对象', 'w')
f.write(j)  # -------------------等价于json.dump(dic,f) 写入文本的必须是字符串类型
f.close()

dicdump = {"王娜": "SB"}
fdump = open('序列化对象dump', 'w')
json.dump(dicdump, fdump)

# -----------------------------反序列化<br>
import json

f = open('序列化对象')
data = json.loads(f.read())  # 等价于data=json.load(f)
print(data, type(data))
