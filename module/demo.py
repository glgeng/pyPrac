# _*_ coding:utf-8 _*_
# Creating time : 2020/10/14  20:02

# 模块可以包含可执行的语句和函数的定义，这些语句的目的是初始化模块，
# 它们只在模块名第一次遇到导入import语句时才执行
# （import语句是可以在程序中的任意位置使用的,且针对同一个模块很import多次,
# 为了防止重复导入，python的优化手段是：第一次导入后就将模块名加载到内存了，
# 后续的import语句仅是对已经加载大内存中的模块对象增加了一次引用，不会重新执行模块内的语句）

import my_module # 只在第一次导入时才执行my_module.py内代码(执行的结果就是 相当于 在my_module.py文件中执行),
                 # 此处的显式效果是只是打印
                 # 但是my_module.py其他的代码也都被执行了,只不过没有显示效果.
import my_module
import my_module
import my_module


'''
执行结果：
from the my_module
D:\pythonPrac\常用包py语言点\module\my_module.py
'''

'''
使用import my_module的时候发生了哪些事情？
    1.找到这个my_module.py模块
    2.创建一个属于my_module.py的内存空间
    3.执行my_module.py文件(加载my_module.py文件中的变量和方法到内存)
    4.  在本文件(自己的内存空间中)中创建一个名字叫做my_module的变量
        并让这个变量指向my_module.py
'''