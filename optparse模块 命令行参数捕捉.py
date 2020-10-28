'''
python optparse命令行参数捕捉解析
需求：

有时候我们需要在命令行启动脚本时需要指定这个脚本的一些参数，简单举例，例如 python start.py -n kitty -s fly  abc bde

脚本文件后面的-n kitty -s fly  abc bde参数如何在脚本当中取到呢，这时候就需要使用optparse模块了



首先，我们需要创建一个OptionParser的对象

from optparse import OptionParser
op=OptionParser()
然后，我们需要用到add_option方法绑定参数，参数绑定后，用op.parse_args方法解析，得到两个变量，options为已经绑定的参数，args是除了绑定的参数之外的参数，统一存放在args中

op.add_option('-n','--name',dest='name')
op.add_option('-s','--skill',dest='skill')
options,args=op.parse_args()
print(options,args)
绑定完了之后，我们在命令行模式下输入命令

命令行下输入：python test.py -n kitty -s fly abc  bde
输出：{'name': 'kitty', 'skill': 'fly'} ['abc', 'bde'] #参数看似已经捕捉到了，并存放在一个字典和列表中，但其options并不是字典！！！
之所以说options并不是字典，因为我们可以通过type（options）得知其是<class 'optparse.Values'>的一个类，所以我们要拿到某个参数的值，我们并不能通过 dict['key'] 或者dict.get('key) 的方式去拿数据，而是要通过 obj.attr （对象.属性）的方式取值

print(options.name,options.skill)   #name，skill属性已经在add__option方法执行后封装成了一个属性
命令行中再次运行：python test.py -n kitty -s fly abc  bde
输出：kitty fly'''