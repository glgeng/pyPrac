# _*_ coding:utf-8 _*_
# Creating time : 2020/10/14  20:00
print('from the my_module')
import os,sys
print(os.path.abspath(__file__))
print(sys.path)

money = 100

def read1():
    print('my_module->read1->money',money)

def read2():
    print('my_module->read2 calling read1')
    read1()

def change():
    global money
    money = 0