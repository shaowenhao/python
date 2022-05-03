# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 5/2/2022 4:06 PM
# 文件名称: test4_chapter6_2.PY

#6.2 列表 列表中的元素类型可以不同，它们之间没有任何关系


#6.2.1 创建和删除
emptylist = []

#list()函数创建数值列表
print(list(range(10,20,2)))

#不再使用删除列表
del emptylist

#6.2.2 访问列表元素
untitle = ['Python',28,"人生苦短,我用Python",["web","UI"]]
print(untitle)
print(untitle[2])

#6.2.3遍历列表
team = ['北京','上海','广州']
for item in team:
    print(item)


for index,item in enumerate(team):
    print(index+1,item)

#6.2.4 添加 修改 和删除
team.append("深圳")
print(len(team))
print(team)

#将team2的内容添加到team
team2 = ["江西","杭州"]
team.extend(team2)
print(team)

del team[-1]
del team[-1]
print(team)

#删除不确定位置的元素
team.remove('深圳')
print(len(team))
print(team)

#count() 判断指定元素出现的次数 返回0 表示不存在
value = "北京"
if team.count(value) > 0:
    team.remove(value)
print(team)

#6.2.5 列表统计计算
#count 出现的次数 index首次出现下标
name = ['a1','a2','a3','a2','a4']
print(name.count('a2'))
print(name.index('a2'))

result = [1,2,3,4,5]
total = sum(result)
print(total)

#统计结果加上所指定的数
partTotal = sum(result,2)
print(partTotal)

#6.2.6 排序
#sort()排序原列表的元素顺序改变
grade = [98,99,97,100]
print("原列表:",grade)
grade.sort()
print("升序:",grade)
grade.sort(reverse=True)
print("降序:",grade)


char = ['cat','Tom','Angela','pet']
char.sort()
print(char)

char.sort(key=str.lower)
print(char)

#sorted()排序 原列表的元素顺序不变
grade2 = [98,99,97,100]
grade2_as = sorted(grade2)
print(grade2_as)
grade2_des = sorted(grade2,reverse=True)
print(grade2_des)


#6.2.7 列表推到
#list = [Expression for var in range] 生成指定范围的数值列表
import random
randomnumber = [random.randint(10,100) for i in range(10)]
print("生成的随机数:",randomnumber)


#根据列表生成指定需求的列表 newlist = [Expression for var in list]
price = [1200,1988,8888]
sale = [int(x*0.5) for x in price]
print(price)
print(sale)

#列表中选择符合条件的元素组成新的列表
# newlist =  [Expression for vat in list if condition]
price2 = [1200,1988,8888]
sale2 = [x for x in price2 if x>8000]
print(sale2)