# _*_ coding:utf-8 _*_
# Creating time : 2020/10/26  21:54

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='test.txt',
    filemode='w'
)


class Manager:
    def __init__(self, name):
        self.name = name

    def create_student(self):
        stu_name = input('student_name:')
        # 输入了一系列的事情，创造了一个学生
        logging.info('%s create a student %s' % (self.name, stu_name))


alex = Manager('alex')
alex.create_student()
