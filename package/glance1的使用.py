# 在包中直接导入模块 方法一(麻烦)
# import aaa.glance1.api.policy # import 包.包.模块
# aaa.glance1.api.policy.get() # 包.包.模块.变量
'''
运行结果
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\__init__.py
我是aaa下的__init__.py文件
执行aaa下的__init__.py文件
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance1\__init__.py
我是glance1下的__init__.py文件
执行glance1下的__init__.py文件
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance1\api\__init__.py
我是api下的__init__.py文件
执行api下的__init__.py文件
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance1\api\policy.py
执行policy.py中的get函数
'''

# 在包中直接导入模块 方法一(麻烦)
# import aaa.glance1.api.policy as policy
# policy.get()
'''
运行结果
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\__init__.py
我是aaa下的__init__.py文件
执行aaa下的__init__.py文件
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance1\__init__.py
我是glance1下的__init__.py文件
执行glance1下的__init__.py文件
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance1\api\__init__.py
我是api下的__init__.py文件
执行api下的__init__.py文件
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance1\api\policy.py
执行policy.py中的get函数
'''

# 在包中直接导入模块 方法二(推荐)
# from aaa.glance1.api import policy # from 包.包 import 模块
# policy.get() # 模块.变量
'''
运行结果
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\__init__.py
我是aaa下的__init__.py文件
执行aaa下的__init__.py文件
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance1\__init__.py
我是glance1下的__init__.py文件
执行glance1下的__init__.py文件
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance1\api\__init__.py
我是api下的__init__.py文件
执行api下的__init__.py文件
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance1\api\policy.py
执行policy.py中的get函数
'''


