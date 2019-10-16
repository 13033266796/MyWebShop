# -*-coding:utf-8-*-

# 1、将list[1,2,3,4,5,1,2,3]去重，即输出[1,2,3,4,5]
# list_1 = [1, 2, 3, 4, 5, 1, 2, 3]
# list_1 = list(set(list_1))
# print(list_1)

# 2、将dict{'1':'a','2':'b','3':'c','4':'d'}的键和值互换
# dict_1 = {'1':'a','2':'b','3':'c','4':'d'}
# dict_2 = {}
# for key in dict_1.keys():
#     dict_2[dict_1[key]] = key
# print(dict_2)

#3、打印乘法口诀表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d = %d"%(i,j,i*j),end='  ')
#     print()

#4、用*画长方形
# for i in range(10):
#     for j in range(20):
#         print("*",end='')
#     print()

#5、三角形
# high = int(input("打印的行数："))
# space = (high-1)
# for i in range(high):#四行
#     print(" "*(space),"*"*(2*i+1))
#     space -= 1

#6、菱形
# high = int(input("打印几行(奇数)："))
# def liingxing(high):
#     space = (high-1)//2
#     for i in range(high):#四行
#         if i < high//2+1:
#             print(" "*(space),"*"*(2*i+1))
#             if i < high//2:
#                 space -= 1
#         else:
#             space += 1
#             print(" "*space,"*"*( (2*(high//2)+1)-(space*2) ))
# liingxing(high)

#7、判断奇、偶数
# number = int(input("请输入一个整数："))
# if number%2 == 0:
#     print("我是偶数")
# else:
#     print("我是奇数")

#8、判断是否为水仙花数
# number_2 = int(input("请输入一个三位整数："))
# bai = number_2//100
# shi = number_2%100//10
# ge = number_2%10
# if bai**3+shi**3+ge**3 ==number_2:
#     print("我是水仙花数")
# else:
#     print("我不是水仙花数")

#9、判断是否是闰年
# year = int(input("请输入一个年份："))
#
# if (year%4==0 and year%100 != 0) | (year%400==0):
#     print("我是闰年")
# else:
#     print("我不是闰年")

#10、输入一个字符串，计算字符串中数字之和
#       aaa1aaa23aaaa4sss5--->15
# str_1 = 'aaa1aaa23aaaa4sss5'
# sum = 0
# for i in range(len(str_1)):
#     if str_1[i] in '0123456789':
#         sum += int(str_1[i])
#
# print(sum)

#11、输入一个字符串，计算字符串中数字之和
#       aaa1aaa23aaaa4sss5--->33
# str_2 = '1aaa1aaa235aaaa4sss5fd5s'
# sum = 0
# flag = 0
# temp = 0 #暂存数字
# for i in range(len(str_2)):
#     if str_2[i] in '0123456789':
#         flag += 1
#         if flag == 1:
#             temp = int(str_2[i])
#         else:
#             temp = temp*10+int(str_2[i])
#     else:
#         if flag>0:
#             sum += temp
#         flag = 0
#         temp = 0
# sum += temp
# print(sum)

# import re
# sum_2 = 0
# str_3 = '1aaa1aaa235aaaa4sss5fd5s'
# for i in re.findall(r'\d+',str_3):
#     sum_2 += int(i)
# print(sum_2)
