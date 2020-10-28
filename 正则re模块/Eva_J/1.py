# _*_ coding:utf-8 _*_
# Creating time : 2020/10/13  21:29
import re
# print(re.findall('\d+\.?\d*',"asdfasdf123as1.13df2.a12adsf1asdf3")) #['123', '1.13', '12', '1', '3']
print(re.findall(r'a\\c','a\c')) # ['a\\c']
print(re.findall('a\\c','a\c')) # 报错