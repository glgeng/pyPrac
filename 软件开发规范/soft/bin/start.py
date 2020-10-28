# _*_ coding:utf-8 _*_
# Creating time : 2020/10/24  18:23
# 存放执行脚本
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main
from conf import my_log_settings

if __name__ == '__main__':
    my_log_settings.load_my_logging_cfg()
    main.run()