# _*_ coding:utf-8 _*_
# Creating time : 2020/10/24  21:16
# 为何要进行文件一致性校验？
# 为了确保得到的文件是正确的版本，而没有被注入病毒和木马程序
# 例如,我们经常在网上下载软件，而这些软件已经被注入了一些广告和病毒等，
# 如果不进行文件与原始发布商的一致性校验的话，可能会给我们带来一定的损失。

# 文件一致性校验原理
# 要进行文件的一致性校验，我们不可能像文本文件比较那样，将两个文件放到一起对比，因为很多的时候文件很大。
# 目前最理想的办法就是，是通过加密算法，对文件生成对应的值，通过生成的值与发布商提供的值比较来确认两个文件是否一致。

import hashlib


# 有一个坑就是使用hashlib时候，检验不同的字符串的时候都必须重新创建md5对象，也就是再写一遍 md5_obj = hashlib.md5()

# 初级版本
def check(filename1, filename2):
    md5_obj = hashlib.md5()  # 创建md5对象
    with open(filename1, 'rb') as f:
        content = f.read()  # 一次性读取文件所有内容
        md5_obj.update(content)
        res1 = md5_obj.hexdigest()

    md5_obj = hashlib.md5()  # 创建md5对象
    with open(filename2, 'rb') as f:
        content = f.read()  # 一次性读取文件所有内容
        md5_obj.update(content)
        res2 = md5_obj.hexdigest()

    print(res1, res2)
    return True if res1 == res2 else False


print(check('校验文件1.txt', '校验文件2.txt'))
