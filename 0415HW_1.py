# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:40:11 2022

@author: N
"""

train = list(input().split())
#print(train)
n = int(input()) #幾次動作

while n > 0:
    n -= 1 #因為做了一次操作
    todo , car = input().split()
    # 1 append 2 del
    if todo == '1':
        train.append(car)
    elif todo == '2':
        train.remove(car)
    else:
        print('ERROR')
"""        
for i in train: #i = 每一個值都跑過一遍
    print(i,end=' ')
 """       
for i in range(len(train)): #i = index
    print(train[i],end=' ')