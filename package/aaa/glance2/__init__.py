import os,sys
print('我的文件路径是==>',os.path.abspath(__file__))
print('我是glance2下的__init__.py文件')
print('执行glance2下的__init__.py文件')

print(sys.path)
print(os.getcwd())

# import api # 写入这句话以后，
             # 在当前文件执行时不会出错的，但是你需要明确，包的目的是为了被调用，而不是把这个包当做脚本执行

             # 在 glance2的使用.py 第二个标题下 运行会报错  为什么？ 见 包.txt  解释的很清楚
             #    我在这再添个逼脸给自己再解释一下
             #    因为我是在 glance2的使用.py 这个文件调用包，执行时的sys.path是 D:\\pythonPrac\\常用包py语言点\\package
             #    在 glance2的使用.py 第二个标题下写的是 import aaa.glance2 这句话
             #    拼上sys.path的路径 D:\\pythonPrac\\常用包py语言点\\package\\aaa\\glance2，能找到，能运行到这
             #    没毛病，继续说
             #    看上去风平浪静，然后呢？
             #    你要知道，在 glance2的使用.py 第二个标题下写的 import aaa.glance2 会在 glance2的使用.py以D:\\pythonPrac\\常用包py语言点\\package这个sys.path下执行aaa\\__init__.py 和 aaa\\glance2\\__init__.py
             #    走到这，问题就出现了：以aaa\\glance2\\__init__.py这个文件为例 (其实绕了一圈转回来了)
             #    aaa\\glance2\\__init__.py 中的 import api 这句话 与 执行文件 glance2的使用.py 以D:\\pythonPrac\\常用包py语言点\\package这个sys.path  拼接不起来(D:\\pythonPrac\\常用包py语言点\\package\\api 目录错误 ModuleNotFoundError: No module named 'api')



# from glance2 import api # 写入这句话以后，
                        # 在当前文件执行时出错，原因是当前的sys.path是D:\\pythonPrac\\常用包py语言点\\package\\aaa\\glance2
                        #                             再拼上D:\\pythonPrac\\常用包py语言点\\package\\aaa\\glance2\\glance2\\api  目录错误

                        # 在glance2的使用.py 第二个标题 运行会报错  为什么？ 见 包.txt  解释的很清楚
                        #    我在这再添个逼脸给自己再解释一下
                                     #    因为我是在 glance2的使用.py 这个文件调用包，执行时的sys.path是 D:\\pythonPrac\\常用包py语言点\\package
                                     #    在 glance2的使用.py 第二个标题下写的是 import aaa.glance2 这句话
                                     #    拼上sys.path的路径 D:\\pythonPrac\\常用包py语言点\\package\\aaa\\glance2，能找到，能运行到这
                                     #    没毛病，继续说
                                     #    看上去风平浪静，然后呢？
                                     #    你要知道，在 glance2的使用.py 第二个标题下写的 import aaa.glance2 会在 glance2的使用.py以D:\\pythonPrac\\常用包py语言点\\package这个sys.path下执行aaa\\__init__.py 和 aaa\\glance2\\__init__.py
                                     #    走到这，问题就出现了：以aaa\\glance2\\__init__.py这个文件为例 (其实绕了一圈转回来了)
                                     #    aaa\\glance2\\__init__.py 中的 from glance2 import api 这句话 与 执行文件 glance2的使用.py 以D:\\pythonPrac\\常用包py语言点\\package这个sys.path  拼接不起来(D:\\pythonPrac\\常用包py语言点\\package\\glance2\\api 目录错误 ModuleNotFoundError: No module named 'glance2')



from aaa.glance2 import api # 写入这句话以后，
                              # 在当前文件执行时出错，原因是当前的sys.path是D:\\pythonPrac\\常用包py语言点\\package\\aaa\\glance2
                              #                             再拼上D:\\pythonPrac\\常用包py语言点\\package\\aaa\\glance2\\aaa\\glance2\\api  目录错误

                              # 在glance2的使用.py 第二个标题 运行不会报错
                              # 可以实现在 在glance2的使用.py 第二个标题import aaa.glance2的时候把glance2下的api包导入成功
