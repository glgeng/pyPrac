import re



# print(re.findall('a\\c','a\c')) #对于正则来说a\\c确实可以匹配到a\c,但是在python解释器读取a\\c时，会发生转义，然后交给re去执行，所以抛出异常
# print(re.findall(r'a\\c','a\\\c')) #['a\\c']  r代表告诉解释器使用rawstring，即原生字符串，把我们正则内的所有符号都当普通字符处理，不要转义
# print(re.findall('a\\\\c','a\c')) #['a\\c']  同上面的意思一样，和上面的结果一样都是['a\\c']
# print(re.findall('href="(.*?)"','<a href="http://www.baidu.com">点击</a>')) #['http://www.baidu.com']
# print(re.findall('href="(?:.*?)"','<a href="http://www.baidu.com">点击</a>')) #['href="http://www.baidu.com"']
# print(re.findall('compan(?:y|ies)','Too many companies have gone bankrupt, and the next one is my company')) # ['companies', 'company']
# print(re.findall('compan(y|ies)','Too many companies have gone bankrupt, and the next one is my company')) # ['ies', 'y']
# print(re.findall('company|ies','Too many companies have gone bankrupt, and the next one is my company')) # ['ies', 'company']
# print('===>',re.sub('^(\w+)(.*?\s)(\w+)(.*?\s)(\w+)(.*?)$',r'\1\2\3\4\5','alex make love'))

# obj=re.compile('\d{2}')
# print(obj.search('abc123eeee').group()) #12
# print(obj.findall('abc123eeee')) #['12'],重用了obj


# print(re.findall("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>")) #['h1']
# print(re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>").group()) #<h1>hello</h1>
# print(re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>").groupdict()) #{'tag_name': 'h1'}
# print(re.search("<(\w+)>\w+</(\w+)>","<h1>hello</h1>").group()) #<h1>hello</h1>

# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)


# s = 'A23G4HFD567'
# print(re.findall('(?P<value>\d+)',s)) #['23', '4', '567']
# print(re.findall('(\d+)',s)) #['23', '4', '567']
# print(re.search("(?P<value>\d+)",s).group()) #23
# print(re.search("(?P<value>\d+)",s).groupdict()) #{'value': '23'}
# print(re.sub('(?P<value>\d+)', double, s)) #A46G8HFD1134
# print(re.search('e','alex make love').group()) #e


# print(re.search('\(([\+\-\*\/]*\d+\.?\d*)+\)',"1-12*(60+(-40.35/5)-(-4*3))").group()) #(-40.35/5)
# print(re.search('\(([\+\-\*\/]*\d+\.?\d*)+\)',"1-12*(60+(-40.35/5)-(-4*3))").group(0)) #(-40.35/5)
# print(re.search('\(([\+\-\*\/]*\d+\.?\d*)+\)',"1-12*(60+(-40.35/5)-(-4*3))").group(1)) #/5
# print(re.findall('\(([\+\-\*\/]*\d+\.?\d*)+\)',"1-12*(60+(-40.35/5)-(-4*3))")) #['/5', '*3']
# print(re.findall('(\(([\+\-\*\/]*\d+\.?\d*)+\))',"1-12*(60+(-40.9222/5)-(-4*3))")) #[('(-40.35/5)', '/5'), ('(-4*3)', '*3')]

# content='Hello 123 456 World_This is a Regex Demo'
# res=re.match('^Hello.*Demo',content)
# print(res.group())



# print(re.findall('a[1*-]b','a1b a*b a-b'))
# print(re.findall('a[^1*-]b','a1b a*b a-b a=b'))
# print(re.findall('a[0-9]b','a1b a*b a-b a=b'))
# print(re.findall('a[a-z]b','a1b a*b a-b a=b aeb'))
# print(re.findall('a[a-zA-Z]b','a1b a*b a-b a=b aeb aEb'))

# print(re.findall('www[baidu,souhu]*','wwwbaiduyunwwwsouhudf'))
# print(re.findall('www[baidu,souhu]','wwwbaiduyunwwwsouhudf'))
# print(re.findall("\([^()]*\)","12*(36*2-(6-3)")) #['(6-3)']  ^排除字符  排除(和）

# print(re.findall(r'I\b','hello I am LIST.'))
# print(re.findall('I\\b','hello I am LIST.'))

# print(re.findall(r'a\\c','a\c'))

# print(re.findall('ab{2,4}','abbbbbbb'))
# print(re.findall('a[1*-]b','a1b a*b a-b'))
# print(re.findall('(?:ab)+123','ababab123'))
# print(re.findall('(ab)+123','ababab123'))

# print(re.search("(?P<name>[a-z]+)(?P<age>\d+)","alex36ggl20").group("name")) #alex
# print(re.findall('href="(.*)"','<a href="http://www.baidu.com">点击</a>')) #['http://www.baidu.com']

#compile方法：
# obj=re.compile('\d{2}')
# print(obj.search('abc123eeee').group()) #12
# print(obj.findall('abc123eeee')) #['12'],重用了obj

# com=re.finditer("\d+","sd5sd2356sd22")
# print(next(com).group())

# 字符：
#
# 　　. 匹配除换行符以外的任意字符
# 　　\w 匹配字母或数字或下划线或汉字
# 　　\s 匹配任意的空白符
# 　　\d 匹配数字
# 　　\b 匹配单词的开始或结束
# 　　^ 匹配字符串的开始
# 　　$ 匹配字符串的结束



# 次数：
#
# 　　* 重复零次或更多次
# 　　+ 重复一次或更多次
# 　　? 重复零次或一次
# 　　{n} 重复n次
# 　　{n,} 重复n次或更多次
# 　　{n,m} 重复n到m次


# =================================匹配模式=================================
#一对一的匹配
# 'hello'.replace(old,new)
# 'hello'.find('pattern')

#正则匹配

# \w与\W
# print(re.findall('\w','hello egon 123')) #['h', 'e', 'l', 'l', 'o', 'e', 'g', 'o', 'n', '1', '2', '3']
# print(re.findall('\W','hello egon 123')) #[' ', ' ']



# \s与\S
# print(re.findall('\s','hello  egon  123')) #[' ', ' ', ' ', ' ']
# print(re.findall('\S','hello  egon  123')) #['h', 'e', 'l', 'l', 'o', 'e', 'g', 'o', 'n', '1', '2', '3']



# \n \t都是空,都可以被\s匹配
# print(re.findall('\s','hello \n egon \t 123')) #[' ', '\n', ' ', ' ', '\t', ' ']



# \n与\t
# print(re.findall(r'\n','hello egon \n123')) #['\n']
# print(re.findall(r'\t','hello egon\t123')) #['\n']



# \d与\D
# print(re.findall('\d','hello egon 123')) #['1', '2', '3']
# print(re.findall('\D','hello egon 123')) #['h', 'e', 'l', 'l', 'o', ' ', 'e', 'g', 'o', 'n', ' ']



# \A与\Z
# print(re.findall('\Ahe','hello egon 123')) #['he'],\A==>^
# print(re.findall('123\Z','hello egon 123')) #['he'],\Z==>$



# ^与$
# print(re.findall('^h','hello egon 123')) #['h']
# print(re.findall('3$','hello egon 123')) #['3']



#  重复匹配：| . | * | ? | .* | .*? | + | {n,m} |


# .
# print(re.findall('a.b','a1b')) #['a1b']
# print(re.findall('a.b','a1b a*b a b aaab')) #['a1b', 'a*b', 'a b', 'aab']
# print(re.findall('a.b','a\nb')) #[]
# print(re.findall('a.b','a\nb',re.S)) #['a\nb']
# print(re.findall('a.b','a\nb',re.DOTALL)) #['a\nb']同上一条意思一样



# *
# print(re.findall('ab*','bbbbbbb')) #[]
# print(re.findall('ab*','a')) #['a']
# print(re.findall('ab*','abbbb')) #['abbbb']
# print(re.findall('ab*','ab')) #['ab']



# ?
# print(re.findall('ab?','a')) #['a']
# print(re.findall('ab?','abbb')) #['ab']
# #匹配所有包含小数在内的数字
# print(re.findall('\d+\.?\d*',"asdfasdf123as1.13dfa12adsf1asdf3")) #['123', '1.13', '12', '1', '3']
# print(re.findall('\d+\.?\d+',"asdfasdf123as1.13dfa12adsf1asdf3")) #['123', '1.13', '12']



# .*默认为贪婪匹配
# print(re.findall('a.*b','a1b22222222b')) #['a1b22222222b']



# .*?为非贪婪匹配：推荐使用
# print(re.findall('a.*?b','a1b22222222b')) #['a1b']



# +
# print(re.findall('ab+','abbb')) #['abbb']
# print(re.findall('ab+','a')) #[]
# print(re.findall('ab+','ab')) #['ab']



# {n,m}
# print(re.findall('ab{2}','abbb')) #['abb']
# print(re.findall('ab{2,4}','abbb')) #['abb']
# print(re.findall('ab{1,}','abbb')) #'ab{1,}' ===> 'ab+'
# print(re.findall('ab{0,}','abbb')) #'ab{0,}' ===> 'ab*'



# []
# print(re.findall('a[1*-]b','a1b a*b a-b')) #[]内的都为普通字符了，且如果-没有被转意的话，应该放到[]的开头或结尾
# print(re.findall('a[^1*-]b','a1b a*b a-b a=b')) #[]内的^代表的意思是取反，所以结果为['a=b']
# print(re.findall('a[0-9]b','a1b a*b a-b a=b')) #[]内的^代表的意思是取反，所以结果为['a=b']
# print(re.findall('a[a-z]b','a1b a*b a-b a=b aeb')) #[]内的^代表的意思是取反，所以结果为['a=b']
# print(re.findall('a[a-zA-Z]b','a1b a*b a-b a=b aeb aEb')) #[]内的^代表的意思是取反，所以结果为['a=b']

# #\# print(re.findall('a\\c','a\c')) #对于正则来说a\\c确实可以匹配到a\c,但是在python解释器读取a\\c时，会发生转义，然后交给re去执行，所以抛出异常
# print(re.findall(r'a\\c','a\c')) #r代表告诉解释器使用rawstring，即原生字符串，把我们正则内的所有符号都当普通字符处理，不要转义
# print(re.findall('a\\\\c','a\c')) #同上面的意思一样，和上面的结果一样都是['a\\c']



# #():分组
# print(re.findall('ab+','ababab123')) #['ab', 'ab', 'ab']
# print(re.findall('(ab)+123','ababab123')) #['ab']，匹配到末尾的ab123中的ab
# print(re.findall('(?:ab)+123','ababab123')) # ['ababab123'] findall的结果不是匹配的全部内容，而是组内的内容,?:可以让结果为匹配的全部内容
# print(re.findall('href="(.*?)"','<a href="http://www.baidu.com">点击</a>'))#['http://www.baidu.com']
# print(re.findall('href="(?:.*?)"','<a href="http://www.baidu.com">点击</a>'))#['href="http://www.baidu.com"']


# |
# 非获取匹配，匹配pattern但不获取匹配结果，不进行存储供以后使用。这在使用或字符“(|)”来组合一个模式的各个部分是很有用
# 例如“industr(?:y|ies)”就是一个比“industry|industries”更简略的表达式。
"""
想在一篇文章中找"program"和"project"这两个单词
正则表达式可表示为 program|project
也可表示为 pro(gram|ject)
但用了（）就表示会匹配括号里存在的内容且存储一份
用 | 隔开了 也就是说 gram和ject 都被存储了一份 但这样存储的内容是无意义的
所以表达式写成这样 pro(?:gram|ject)
一是显得比较简洁
二是不会存储无意义的内容
"""
# print(re.findall('compan(?:y|ies)','Too many companies have gone bankrupt, and the next one is my company')) #['companies', 'company']
# print(re.findall('compan(y|ies)','Too many companies have gone bankrupt, and the next one is my company')) #['ies', 'y']




# # ===========================re模块提供的方法介绍===========================
# import re
# #1
# print(re.findall('e','alex make love') )   #['e', 'e', 'e'],返回所有满足匹配条件的结果,放在列表里
# #2
# print(re.search('e','alex make love').group()) #e,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
#
# #3
# print(re.match('e','alex make love'))    #None,同search,不过在字符串开始处进行匹配,完全可以用search+^代替match
#
# #4
# print(re.split('[ab]','abcd'))     #['', '', 'cd']，先按'a'分割得到''和'bcd',再对''和'bcd'分别按'b'分割
#
# #5
# print('===>',re.sub('a','A','alex make love')) #===> Alex mAke love，不指定n，默认替换所有
# print('===>',re.sub('a','A','alex make love',1)) #===> Alex make love
# print('===>',re.sub('a','A','alex make love',2)) #===> Alex mAke love
# print('===>',re.sub('^(\w+)(.*?\s)(\w+)(.*?\s)(\w+)(.*?)$',r'\5\2\3\4\1','alex make love')) #===> love make alex
#
# print('===>',re.subn('a','A','alex make love')) #===> ('Alex mAke love', 2),结果带有总共替换的个数
#
#
# #6
# obj=re.compile('\d{2}')
#
# print(obj.search('abc123eeee').group()) #12
# print(obj.findall('abc123eeee')) #['12'],重用了obj


#为何同样的表达式search与findall却有不同结果:
# print(re.search('\(([\+\-\*\/]*\d+\.?\d*)+\)',"1-12*(60+(-40.35/5)-(-4*3))").group()) #(-40.35/5)
# print(re.findall('\(([\+\-\*\/]*\d+\.?\d*)+\)',"1-12*(60+(-40.35/5)-(-4*3))")) #['/5', '*3']

#看这个例子:(\d)+相当于(\d)(\d)(\d)(\d)...,是一系列分组
# print(re.search('(\d)+','123').group()) #group的作用是将所有组拼接到一起显示出来 123
# print(re.findall('(\d)+','123')) #findall结果是组内的结果,且是最后一个组的结果 ['3']
# print(re.findall('(abc)+','abcabcabc')) #['abc']
# print(re.search('(abc)+','abcabcabcasasabcabc').group()) #abcabcabc
# print(re.findall('(?:abc)+','abcabcabc'))  #['abcabcabc']
# print(re.findall('(?:abc)','abcabcabc'))  #['abc', 'abc', 'abc']
# print(re.findall('(abc)','abcabcabc'))  #['abc', 'abc', 'abc']
# print(re.findall('abc+','abcabcabcasdfabc')) #['abc', 'abc', 'abc', 'abc']


# search与findall
# 正则表达式中，group()用来提出分组截获的字符串，()用来分组

# import re
# a = "123abc456"
# print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0)   #123abc456,返回整体
# print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)   #123
# print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2)   #abc
# print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3)   #456




# pattern = r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
# str = '127.0.0.1 192.168.1.66'
# match = re.findall(pattern,str)
# match1 = re.search(pattern,str).group(0) #127.0.0.1
# match2 = re.search(pattern,str).group(1) #127.0.0.1
# match3 = re.search(pattern,str).group(2) #.1
# print(match1)
# print(match2)
# print(match3)
# print(match) # [('127.0.0.1', '.1'), ('192.168.1.66', '.66')] # findall结果是组内的结果,且是最后一个组的结果
# for item in match:
#     print(item[0])













