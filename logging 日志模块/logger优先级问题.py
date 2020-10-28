import logging
# logger的优先级如果高于hander，则从logger优先级开始
# logger的优先级如果低于hander，则从hander优先级开始
# logger是第一级过滤，然后才能到handler，我们可以给logger和handler同时设置level，但是需要注意的是
    # Logger也是第一个根据级别筛选消息的用户-如果将Logger设置为INFO，并且将所有处理程序都设置为DEBUG，
    # 则仍然无法在处理程序上接收调试消息-它们将被Logger本身拒绝。

    # 如果将logger设置为DEBUG，但将所有处理程序设置为INFO，则也不会收到任何调试消息
    # 因为当logger说“好，处理这个”时，处理程序会拒绝它（DEBUG<INFO）

form=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',)

ch=logging.StreamHandler()

ch.setFormatter(form)
# ch.setLevel(10)
ch.setLevel(20)

l1=logging.getLogger('root')
# l1.setLevel(20)
l1.setLevel(10)
l1.addHandler(ch)

l1.debug('l1 debug')
l1.debug('debug')
l1.info('info')
l1.warning('warning')
l1.error('error')
l1.critical('critical')

'''
critical=50
error =40
warning =30
info = 20
debug =10
'''