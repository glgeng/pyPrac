import pickle

'''
Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
并且可能不同版本的Python彼此都不兼容，
因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
'''


dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}

print(type(dic))  # <class 'dict'>

j = pickle.dumps(dic)
print(type(j))  # <class 'bytes'>

f = open('序列化对象_pickle', 'wb')  # 注意是w是写入str,wb是写入bytes,j是'bytes'
f.write(j)  # -------------------等价于pickle.dump(dic,f)

f.close()
# -------------------------反序列化
import pickle

f = open('序列化对象_pickle', 'rb')

data = pickle.loads(f.read())  # 等价于data=pickle.load(f)

print(data['age'])