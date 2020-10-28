# _*_ coding:utf-8 _*_
# Creating time : 2020/10/24  18:50
# lib目录：存放自定义的模块与包
import configparser
def read(config_file):
    config=configparser.ConfigParser()
    config.read(config_file)
    return config