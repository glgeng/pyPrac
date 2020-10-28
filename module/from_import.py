# _*_ coding:utf-8 _*_
# Creating time : 2020/10/14  20:26

from mymodule import read1
'''
1. from mymodule 做了些什么事？
    找my_module模块
    开辟一块属于这个模块的命令空间
    执行这个模块

2. import read1 做了些什么事
    知道了import的是login这个名字
    那么就会在本文件中创建一个变量login
    指向模块命令空间中的login函数
'''