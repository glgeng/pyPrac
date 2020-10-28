# _*_ coding:utf-8 _*_
# Creating time : 2020/10/24  18:28
import os
config_path = r'%s\%s' % (os.path.dirname(os.path.abspath(__file__)),'config.ini')
user_db_path = r'%s\%s' % (os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'db')
user_timeout = 10