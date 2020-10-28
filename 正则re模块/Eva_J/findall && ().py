# _*_ coding:utf-8 _*_
# Creating time : 2020/10/14  09:16

# 使用findall会优先显示分组中的内容
# 虽然仍然是按照写的正则规则进行匹配，但只显示分组中的内容
# search 和 match 没有分组优先这个问题

import re


ret = re.findall('-0\.\d+|-[1-9]\d*(\.\d+)?','-1asdada-200')
print(ret) # ['', '']

ret = re.findall('www.baidu.com|www.oldboy.com','www.oldboy.com')
print(ret) # ['www.oldboy.com']

ret = re.findall('www.(baidu|oldboy).com','www.oldboy.com')   # findall中的正则表达式有()，在匹配成功后只显示()里面对应的匹配的内容
print(ret) # ['oldboy']

ret = re.findall('www.(?:baidu|oldboy).com','www.oldboy.com')   # 加上?:  取消findall只显示分组的内容
print(ret) # ['www.oldboy.com']

ret = re.findall('-0\.\d+|-[1-9]\d*(?:\.\d+)?','-1asdada-200')
print(ret) # ['-1', '-200']





# ret = re.split('\d+','alex83egon20taibai40')
# print(ret) # ['alex', 'egon', 'taibai', '']

# ret = re.split('(\d+)','alex83egon20taibai40') # split遇见()分组的时候  会帮助保留分组内的被切掉的内容
# print(ret) # ['alex', '83', 'egon', '20', 'taibai', '40', '']




# 分组遇见search
ret = re.search('\d+(.\d+)(.\d+)(.\d+)?','1.2.3.4-2*(60+(-40.35/5)-(-4*3))')
print(ret.group()) # 1.2.3.4
print(ret.group(1)) # 只显示匹配结果  对应第一个()里的内容  .2
print(ret.group(2)) # 只显示匹配结果  对应第二个()里的内容  .3
print(ret.group(3)) # 只显示匹配结果  对应第三个()里的内容  .4





# ret=re.compile('-0\.\d+|-[1-9]\d*(\.\d+)?')
# c=ret.search('-1asdada-200')
# print(c.group())
# c1=ret.findall('-1asdada-200')
# print(c1)