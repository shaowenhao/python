# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 5/6/2022 5:10 PM
# 文件名称: test6_chapter8_if.PY

# if 选择语句

# number = int(input("请输入号码"))
# if number == 123:
#     print("is 123")
#     print("correct!!")
#
# if number != 123:
#     print("is not 123")

# if else语句

# num = int(input("input num"))
# if num ==456:
#     print("its")
# else:
#     print("its not")


#简写
a = -9
b=a if a > 0 else -a
print(b)

# if elif else 语句

# num = int(input("input num"))
# if num >= 100:
#     print("A")
# elif num > 50 and num < 100:
#     print("B")
# else:
#     print("C")

#if 语句嵌套

# num = int(input('input num'))
# if num >= 1000:
#     print("A")
# else:
#     if num >= 500:
#         print("B")
#     else:
#         if num >= 300:
#             print("C")
#         else:
#             print("D")

# 使用and连接条件的选择语句
# age = int(input("请输入年龄:"))
# if age>=18 and age<=70 :
#     print("可以申请")

#使用or连接条件的选择语句
sales = 7
if sales<10 or sales>100:
    print("注意该销售额")


#使用not关键字的选择语句
# Python中 False None 空字符串 空列表 空元祖 空字典 都相当于 False

data = None
if not data:
    print("you win")
else:
    print("you lose")


#判定值是否再列表中 可以治愈关键字in
num1 = 1
list1 = [1,2,3,4,5]
if num1 in list1:
    print("correct")
