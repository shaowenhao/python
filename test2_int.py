# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 4/30/2022 3:54 PM
# 文件名称: test2_int.PY

height = 1.70
print("your height:" + str(height))
weight = 48.5
print("your weight:" + str(weight))

bmi = weight / (height*height)

if bmi < 18.5:
    print("aaa")
if bmi >= 18.5 and bmi < 24.9:
    print('bbb')
