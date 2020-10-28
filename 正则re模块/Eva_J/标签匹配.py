# _*_ coding:utf-8 _*_
# Creating time : 2020/10/14  10:49

import re
# ret = re.findall('>(\w+)<',r'<a>wahaha<\a>')
# print(ret) # ['wahaha']

# ret = re.search(r'<(\w+)>(\w+)</(\w+)>',r'<a>wahaha</b>')
# print(ret.group()) # <a>wahaha</b>
# print(ret.group(1)) # a
# print(ret.group(2)) # wahaha

# 分组命名
# ret = re.search("<(?P<name>\w+)>\w+</(?P=name)>","<h1>hello</h1>")
# print(ret.group('name'))  #结果 ：h1
# # print(ret.group())  #结果 ：<h1>hello</h1>
#
# ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
# print(ret.group(1))
# # print(ret.group())  #结果 ：<h1>hello</h1>

ret = re.search(r'<(?P<tag>\w+)>(?P<content>\w+)</(\w+)>',r'<a>wahaha</b>')
print(ret.group())
print(ret.group('tag'))
print(ret.group('content'))