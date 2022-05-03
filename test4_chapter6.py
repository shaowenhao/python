# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 5/2/2022 2:37 PM
# 文件名称: test4_chapter6.PY

#6.1.1 序列 索引

verse =  ["abc","def","test"]
print(verse[1])
print(verse[-1])

# 6.1.2 切片
student = ["s1","s2","s3","s4","s5","s6"]
print(student[1:5])
print(student[0:5:2])
print(student[:])

#6.1.3 序列相加
city = ["bj","sh","gz"]
print(student+city)


#6.1.4  乘法
phone = ["huawei","xiaomi"]
print(phone * 2)

#6.1.5 检查元素是否是序列的成员
print("s1" in student)


#6.1.6 计算序列的长度 最大最小值
nums = [1,3,5,9,7,6]
print("序列长度:",len(nums))
print(max(nums))
print(min(nums))

