# _*_ coding:utf-8 _*_
# Creating time : 2020/10/27  10:25

import sys
li = sys.argv

if li[1] == "post":
    print("post")
elif li[1] == "down":
    print("1111")

# 怎么用呢
    # 在终端切换至当前目录
    # 输入命令 python sys.argv的使用.py post si
    # 结果为 post

'''
Ex2
# -*- coding: UTF-8 -*-

import sys

print '参数个数为:', len(sys.argv), '个参数。'
print '参数列表:', str(sys.argv)




$ python test.py arg1 arg2 arg3
参数个数为: 4 个参数。
参数列表: ['test.py', 'arg1', 'arg2', 'arg3']
'''