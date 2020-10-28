import logging

# logging模块高级使用：

# logger：产生日志的对象
# Filter：过滤日志的对象
# Handler：接收日志然后控制打印到不同的地方，FileHandler用来打印到文件中，StreamHandler用来打印到终端
# Formatter对象：可以定制不同的日志格式对象，然后绑定给不同的Handler对象使用，以此来控制不同的Handler的日志格式

# 1. 初始化 logger = logging.getLogger("endlesscode")，getLogger()方法后面最好加上所要日志记录的模块名字，后面的日志格式中的%(name)s 对应的是这里的模块名字
# 2. 设置级别 logger.setLevel(logging.DEBUG),Logging中有NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL这几种级别，日志会记录设置级别以上的日志
# 3. Handler，常用的是StreamHandler和FileHandler，windows下你可以简单理解为一个是console和文件日志，一个打印在CMD窗口上，一个记录在一个文件上
# 4. formatter，定义了最终log信息的顺序,结构和内容，我喜欢用这样的格式 '[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S'，

logger1 = logging.getLogger('root.user1')

logger1.setLevel(logging.ERROR)

#3、Handler对象：接收logger传来的日志，然后控制输出
h1 = logging.FileHandler('../py2/t1log.txt')
h1.setLevel(logging.DEBUG)
h2 = logging.StreamHandler()

#4、Formatter对象：日志格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 5、为Handler对象绑定格式
h1.setFormatter(formatter)
h2.setFormatter(formatter)

#6、将Handler添加给logger
logger1.addHandler(h1)
logger1.addHandler(h2)

logger1.debug('调试debug')
logger1.info('消息info')
logger1.warning('警告warn')
logger1.error('错误error')
logger1.critical('严重critical')