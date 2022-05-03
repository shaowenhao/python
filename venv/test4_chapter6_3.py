# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 5/3/2022 2:25 PM
# 文件名称: test4_chapter6_3.PY

#6.3 元组 tuple
# 元组是不可变序列 列表是可变序列

#6.3.1 元组的创建和删除

# tuplename = (element1,element2,....)
#使用赋值运算符创建元组
language = ("java","python","c#")

print(language)

#type函数测试变量的类型
team = ("aa",)
print(team)
print(type(team))
team2 = ("bb")
print(team2)
print(type(team2))


#创建数值元组
nums = tuple(range(10,20,2))
print(nums)

#删除元组
del nums

#6.3.2 访问元组元素 切片
nums2 = (1,2,3,4,5)
print(nums2[:3])

for i in nums2:
    print(i)

#对元组重新赋值 不能修改
player = ("a","b")
player = ("aa","bb")
print("新元组:",player)

city = ("bj","sh")
info =  player + city
print("new truple",info)

# 元组推导式 生成器对象
import random
randomnumber = (random.randint(10,100) for i in range(10))
randomnumber = tuple(randomnumber)
print(randomnumber)

#遍历后 如果再想使用生成器对象 必须重新创建一个 因为原来的对象已经不存在
number = (i for i in range(3))
print(number.__next__())
print(number.__next__())
print(number.__next__())
number = tuple(number)
print(number)


number2 = (i for i in range(4))
for i in number2:
    print(i)
print(tuple(number2))



# 元组比列表的访问和处理速度快 所以如果只需对其进行访问，不进行