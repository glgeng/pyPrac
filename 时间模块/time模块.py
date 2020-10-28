import time

##时间戳：
# print(time.time()) #1583231004.3890357

## 显示一个结构化时间
# print(time.localtime()) #time.struct_time(tm_year=2020, tm_mon=3, tm_mday=3, tm_hour=18, tm_min=24, tm_sec=4, tm_wday=1, tm_yday=63, tm_isdst=0)
# 相当于：print(time.localtime(time.time()))  将时间戳转换为结构化时间
# t = time.localtime()
# print(t.tm_wday)  # 显示周几


##================
# 将结构化时间转换为字符串时间：
print(time.strftime("%Y--%m--%d %X", time.localtime()))  # 2020--03--03 18:25:01
print(time.strftime("%Y--%m--%d %X"))  # 2020--03--03 18:25:01

# #================
# 将结构化时间转换为时间戳：
# print(time.mktime(time.localtime()))


# #================
# 将字符串时间转换为结构化时间：
# print(time.strptime('2020:01:05:11:00:40', '%Y:%m:%d:%X'))  #time.struct_time(tm_year=2020, tm_mon=1, tm_mday=5, tm_hour=11, tm_min=0, tm_sec=40, tm_wday=6, tm_yday=5, tm_isdst=-1)

# #================
# print(time.asctime())  #简便将结构化时间转换成一种固定的字符串时间 #Tue Mar  3 18:26:04 2020
# print(time.ctime())    #简便将时间戳转换成一种固定的字符串时间 #Tue Mar  3 18:26:14 2020
