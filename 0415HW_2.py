# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 19:01:45 2022

@author: N
"""

parentheses = list(input())

stack = [] #存左括號 (

ans = 'yes'

for i in parentheses:
    if i == '(':
       stack.append('(') 
    elif i == ')':
        if stack: # stack == true 裡面有東西
            stack.pop()
        else:
            print('no')

if stack:
	ans = 'no'
print(ans)
