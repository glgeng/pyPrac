import os
#具体应用
import os,sys
possible_topdir = os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    os.pardir, #上一级
    os.pardir,
   os.pardir
))

# print(possible_topdir,type(possible_topdir))
# sys.path.insert(0,possible_topdir)

# print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

print( "".join(os.path.abspath(os.path.dirname(__file__)))) #D:\python练习\常用包py语言点
print("\\".join(os.path.abspath(os.path.dirname(__file__)))) #D\:\\\p\y\t\h\o\n\练\习\\\常\用\包\p\y\语\言\点  \\转义
print("\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\"))) #D:\python练习\常用包py语言点
print("\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])) #D:\python练习
