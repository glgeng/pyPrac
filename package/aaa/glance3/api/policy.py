import os
from . import versions
print('我的文件路径是==>',os.path.abspath(__file__))
def get():
    print('执行policy.py中的get函数')
    print('在policy.py中通过使用from . import versions来调用同级目录下的version.py中的方法')
    versions.create_resource(123)