import os
print('我的文件路径是==>',os.path.abspath(__file__))
print('我是glance3下的__init__.py文件')
print('执行glance3下的__init__.py文件')

# 相对导入
# 使用了相对导入的模块只能被当作模块执行
# 不能被当作脚本执行
# .表示在当前目录，__init__.py 所在的当前目录是 aaa\\glance3
from . import api