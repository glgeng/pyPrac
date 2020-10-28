# _*_ coding:utf-8 _*_
# Creating time : 2020/10/24  23:37

import random

def vcode():
    ret = ''
    for i in range(5):
        num = random.randint(0, 9)
        alf1 = chr(random.randint(65, 90))
        alf2 = chr(random.randint(97, 122))
        res = str(random.choice([num, alf1, alf2]))
        # ret += res
        ret = "".join([ret,str(res)])
    return ret

print(vcode())