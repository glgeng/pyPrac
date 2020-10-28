import sys, time

bar_length = 100
# 进度条为 100 个 '='
x = 0
y = 1000
mode = '下载中'

while x != y:
    x += 10
    percent = float(x) / float(y)  # 计算是否是断点续传，当为 x 为0 表示第一次传输，当 x 为非零数 表示续传；
    hashes = '=' * int(percent * bar_length)  # 计算进度条百分比， 1% 代表 1个'=' 10% 代表 10个 '='
    spaces = ' ' * (bar_length - len(hashes))  # 计算进度条剩余长度，用空格表示
    # \r 要写在行首，mode：模式， x：增长长度，y：总大小， percent*100 增长的百分比， hashes: 进度条长度 spaces: 空格长度  hashes+spaces = 100%
    sys.stdout.write('\r%s:%.2f/%.2f %d%% [%s]' % (mode, x, y, percent * 100, hashes + spaces))
    sys.stdout.flush()
    time.sleep(0.2)


# 常用sys模块的方法
'''
# print(sys.path)
# print(os.getcwd())
# os.chdir("E:\\linuxvideo")
# print(os.getcwd())
# makedirs(name, mode=0o777, exist_ok=False):
# os.makedirs(r"aa\bb\cc")
# os.removedirs(r"aa\bb")
# print(os.listdir(os.getcwd()))
# print(os.stat("file.py").st_size)

# os.rename("aa","bb")
#
# print(__file__) #获取当前文件路劲的文件名
# print(os.path.abspath(__file__))
# print(os.path.split(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  #返回当前文件的上一级目录
# # os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# print(os.path.join("d:\\"))
# print(os.path.join("d:\\","www","baidu","a.py"))
print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(os.path.dirname(os.path.abspath(__file__)),"bb","123.txt"))

'''
