# 相对导入
# 使用了相对导入的模块只能被当作模块执行
# 不能被当作脚本执行

# import aaa.glance3
# aaa.glance3.api.policy.get()

# 上面这两句等价于下面这两句

from aaa import glance3
glance3.api.policy.get()

'''
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\__init__.py
我是aaa下的__init__.py文件
执行aaa下的__init__.py文件
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance3\__init__.py
我是glance3下的__init__.py文件
执行glance3下的__init__.py文件
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance3\api\__init__.py
我是api下的__init__.py文件
执行api下的__init__.py文件
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance3\api\versions.py
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance3\api\policy.py
执行policy.py中的get函数
在policy.py中通过使用from . import versions来调用同级目录下的version.py中的方法
执行versions.py中的create_resource函数 123
'''