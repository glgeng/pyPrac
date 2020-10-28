# 导入包 相当于执行了这个包下面的__init__.py
'''
1.只导glance2这个包
    在aaa下的__init__.py 和 aaa\\glance2下的__init__.py文件中都不导包
'''

import aaa.glance2

'''
运行结果
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\__init__.py
我是aaa下的__init__.py文件
执行aaa下的__init__.py文件
我的文件路径是==> D:\pythonPrac\常用包py语言点\package\aaa\glance2\__init__.py
我是glance2下的__init__.py文件
执行glance2下的__init__.py文件
'''


'''
2.import aaa.glance2 我想只写这句话 与此同时 导入glance2/api这个包 咋办？
        (这么办：在glance2\\__init__.py中加入 from aaa.glance2 import api)
  设计一下aaa/glance2/__init__.py文件来完成一些模块的导入
  但是如果在aaa/glance2/__init__.py中写import api这句话会报错
  这是为什么呢？
  见 glance2\\__init__.py，解释的很明白了
'''
# # 设计一下__init__.py文件来完成一些模块的导入


'''
绝对导入
3.我想在这个 glance2的使用.py 文件中 只写import aaa.glance2 这句话
    但是我可以直接使用 aaa\\glance2\\api\\policy.py 这个模块中的方法  咋办？ 
    
    这么办：
        在 glance2\\__init__.py 文件中写入  from aaa.glance2 import api
        在 glance2\\api\\__init__.py 文件中写入 from aaa.glance2.api import policy
'''
aaa.glance2.api.policy.get()  # 成功

'''
使用绝对导入，结论：
    如果我想 在和一个包的同级目录下的一个脚本.py文件中，调用这个包中某一个模块下的方法
    最原始的办法是我可以，从这个脚本.py文件所在目录开始，from 包.包. ... import 模块名
    然后通过 模块名.模块中的方法名来调用
    
    然而这种办法非常的麻烦、看上去也非常的low，尤其是你想把这个包提供给别人用的时候
    就会显得非常的不友好，因为使用这个包的其他人不希望挨个记住这个包下的每个子包中的每个模块分别有什么方法，挨个去from 包.包. ... import 模块名
    
    那么有没有什么解决办法呢？就是可以达到，我在这个脚本.py文件文件中 import 包名之后
    就直接可以使用 包名.模块名.模块中的方法名 来使用这个方法呢？
    就不用在每次使用某个模块下的方法时舔着个逼脸来 from 包.包. ... import 模块名了呢？
    
    这就需要我们在包下的__init__.py文件中写一些内容
    记住秘诀！以绝对导入为例：
        这个glance2的使用.py 就是我说的一个脚本.py文件，这个脚本文件的当前目录是 \\package
        我要导入glance2这个包，同时实现导完这个包之后，直接可以调用这个包中模块下的方法(以我要使用aaa\\glance2\\api\\policy.py 中的get为例)
        第一步：我要在这个脚本文件中写 import aaa.glance2 (要和脚本.py文件的当前目录能拼起来)
        第二步：我要在glance2\\__init__.py 文件中写这么一句话：
            from aaa.glance2 import api (以这个脚本.py文件所在的当前目录开始拼,因为执行的是这个脚本.py文件,看的是这个脚本.py文件的sys.path)
        第三步：在glance2\\api\\__init__.py 文件中写这么一句话：
            from aaa.glance2.api import policy(以这个脚本.py文件所在的当前目录开始拼,因为执行的是这个脚本.py文件,看的是这个脚本.py文件的sys.path)
        第四步：我就可以在这个脚本文件中直接使用 aaa.glance2.api.policy.get()了，就不用舔着个逼脸from 包.包. ... import 模块名了
    
    这个难点或者说是别扭的地方就是在于，比如说我在glance2\\api\\__init__.py 中 写 from aaa.glance2.api import policy
    乍眼一看怎么和这个__init__.py的当前目录拼不上
    你要明确，一个包是用来被其他脚本.py文件调用的，包不是用来直接执行的，而是用来被别人调用的，
            我是在这个脚本.py文件中执行，放在这来讲,脚本文件就是glance2的使用.py，运行的是这个文件，运行这个文件时,有关的sys.path是它的当前目录，也就是到\\package
            所以我需要写from aaa.glance2.api import policy，这样路径才能拼起来
    你可能还会有疑问，我在这个脚本文件中写了 import aaa.glance2 不是要执行aaa\\__init__.py 和 aaa\\glance2\\__init__.py 这两个文件吗？我为什么不看这两个.py文件的
    sys.path呢？在这里我的理解是，你run的还是这个脚本文件，这个脚本.py文件是一切行为的发起者，虽然说，我在这个脚本.py文件中 import aaa.glance2时，
    会触发aaa\\__init__.py 和 aaa\\glance2\\__init__.py 这两个文件的运行，但是此时有关的sys.path还是以这个脚本文件.py所在的当前目录为准/为参照
    
    
    
使用相对导入就不用这么别扭的想了
    第一步：我要在这个脚本文件中写 import aaa.glance2 (要和脚本.py文件的当前目录能拼起来)
    第二步：在\\aaa\\glance2\\__init__.py 中 写这么一句话：
        from . import api
    第三步：在\\aaa\\glance2\\api\\__init__.py 中 写这么一句话
        from . import policy
    第四步：我就可以在这个脚本文件中直接使用 aaa.glance2.api.policy.get()了，就不用舔着个逼脸from 包.包. ... import 模块名了
'''