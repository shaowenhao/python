# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 5/3/2022 5:20 PM
# 文件名称: test5_chapter7.PY

# 字符串与正则表达式

#7.1.1 拼接字符串

name =  "shaowenhao"
city = "beijing"
message =  name + city
print(message)

#字符串不允许与其他类型数据拼接

age = 33
message_info = name + str(age)
print(message_info)


# 计算字符串的长度
str1 = "我们we are family"
length = len(str1)
print(length)

#encode()进行编码后再进行获取 UTF-8编码 汉字 3个字节, GBK 汉字 2个字节
str2 = "我们"
length2 = len(str2.encode())
print(length2)

str3 = "我们"
length3 = len(str3.encode('gbk'))
print(length3)


#7.1.3 截取字符串
# string[start:end:step]

str4 = '人生苦短,我用Python!'
substr1 = str4[1]
substr12 = str4[5:]
substr13 = str4[:5]
substr14 = str4[2:5]
print("原字符串:",str4)
print(substr1+'\n'+substr12+'\n'+substr13+'\n'+substr14)


# try..except
str1 = "人生苦短，我用Python!"
try:
    substr11 = str1[15]
except IndexError:
    print("指定的索引不存在")


#7.1.4 分割字符串
#str.split(sep,maxsplit) sep指定分隔符 maxsplit指定分割的次数

str5 = '明 日 学 院 官 网 >>> www.mingrisoft.com'
print('原字符串:',str5)
list1 = str5.split()
print(list1)
list2 = str5.split('>>>')
print(list2)
list3 = str5.split('.')
print(list3)
list4 = str5.split(' ',4)
print(list4)
# ['明 日 学 院 官 网 ', '', '', ' www.mingrisoft.com']
list5  = str5.split('>')
print(list5)

#7.1.5 检索字符串
#str.count(sub[,start[,end]])
# 检索指定字符串再另一个字符串中出现的次数 如果不存在返回0 存在返回出现的次数
str6 = '@明日科技 @扎克伯格 @雷军'
print('字符串"',str6,'"中包括',str6.count('@'),'个@符号')


# find() 方法
# 该方法用于检索是否包含指定的字符串，如果检索的字符串不存在 返回 -1， 如果存在返回首次出现的索引
print('字符串"',str6,'"首次出现@的索引在',str6.find('@'))
print('字符串"',str6,'"首次出现@的索引在',str6.find('*'))

#index()方法 与find()类似 但不存在指定的字符串会抛出异常
#ValueError: substring not found

# print('字符串"',str6,'"首次出现@的索引在',str6.index('#'))

# startwith()方法
print('字符串"',str6,'"是否以@符号开头，结果为:',str6.startswith('@'))

# endswith()
str7 = 'http://siemens.com'
print(str7,'"是否以.com结尾"',str7.endswith('.com'))

# 7.1.6 字母的大小写转换
# str.lower() str.upper()

str8 = "www.BaiDu.com"
print(str8.lower())
print(str8.upper())

# 7.1.7 去除字符串的空格和特殊字符
str9 = '  http://www.mingrisoft.com  \t\n\r'
print(str9.strip())

#左右两边去除@或.
str10 = '@明日科技.@.'
print(str10.strip('@.'))

#lstrip() 去掉字符串左侧的空格和特殊字符
print(str10.lstrip('@.'))

#rstrip()

#7.1.8 格式化字符串
