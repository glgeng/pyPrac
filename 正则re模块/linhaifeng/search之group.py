# python中的search的group(0),group(1)…的方法
# group（）在正则表达式中用于获取分段截获的字符串，解释如下

import re
a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0)) #123abc456      返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)) #123
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2)) #abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3)) #456

# 可以看出，正则表达式按照数字-字母-数字的顺序来获取相应字符串，
# 那么分别就是“数字（group（1））–字母（group（2））–数字（group（3））”的对应关系，
# 这里一定要注意group(0)和group(1)的区别

# 其中，group（0）和group（）效果相同，均为获取取得的字符串整体
# 一般，m.group(N) 返回第N组括号匹配的字符。
# 而m.group() == m.group(0) == 所有匹配的字符，与括号无关，这个是API规定的。
