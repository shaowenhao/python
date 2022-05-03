# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 4/30/2022 2:09 PM
# 文件名称: test1.PY

import datetime
myear = input("please input your birthday:")
nowyear = datetime.datetime.now().year
imyear = int(myear)
age = nowyear - imyear

if age < 18:
    print("yong")
if age > 18:
    print("old")
