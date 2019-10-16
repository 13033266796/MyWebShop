# -*-coding：utf-8-*-
'''
输入一个年龄
0-12	幼年
13-20	少年
21-30	青年
31-40	壮年
41-50	中年
51-150	老年
150-	妖怪	
'''

age = int(input("请输入你的年龄:"))

print(type(age))

if age <= 12 :
	print('幼年')

if age>12 and age <= 20 :
	print('少年')