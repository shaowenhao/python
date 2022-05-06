# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 5/4/2022 1:56 PM
# 文件名称: test5_chapter7_regular.PY

# 正则表达式基础

# 行定位 ^ $

#Python中re模块实现正则表达式操作
import re

#匹配字符串
# match()方法
# re.match(pattern,string,[flags]) flags可选，用于控制匹配方式 如：是否区分大小写
# match()方法从字符串的开始位置开始匹配，当第一个字母不符合条件，则不进行匹配，直接返回None
# \w 字母 数字 下划线
pattern = r'mr_\w+'
str1 =  'MR_SHOP mr_shop2'
match1 = re.match(pattern,str1,re.I)
print('match() match1',match1)
str2 = 'test mr_shop'
match2 =  re.match(pattern,str2,re.I)
print('match() match2',match2)
print('匹配值的起始位置',match1.start())
print('匹配位置的元组',match1.span())
print('匹配数据',match1.group())

#使用search()方法进行匹配 search()不仅在起始位置搜索，其他位置也搜索。匹配成功返回Match对象，否则None

str3 = '项目名称MR_SHOP mr_shop'
match3 = re.search(pattern,str3,re.I)
print(' search() mqtch3',match3)

#findall()方法进行匹配,匹配成功返回包含匹配结构的列表 否则空列表
mathch4 = re.findall(pattern,str2,re.I)
print('findall() match4:',mathch4)

#分组
pattern_group = r'[1-9]{1,3}(\.[0-9]{1,3}){3}'
str5 = '127.0.0.1 192.168.1.66'
mathch5 = re.findall(pattern_group,str5)
print(mathch5)

pattern_group2 = r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
mathch6 = re.findall(pattern_group2,str5)
for item in mathch6:
    print(item[0])


#7.3.2 替换字符串
