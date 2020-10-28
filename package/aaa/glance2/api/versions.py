import os
print('我的文件路径是==>',os.path.abspath(__file__))
def create_resource(conf):
    print('执行versions.py中的create_resource函数',conf)