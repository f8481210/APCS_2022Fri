# -*- coding: utf-8 -*-
"""
三角形辨別
"""

# 輸入三線段長
a, b, c = map(int,input().split())

# 排序
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
    
# 判斷三角形
if a+b <= c:
    print('No')
elif a*a+b*b == c*c:
    print('Right')
elif a*a+b*b < c*c:
    print('Obtuse')
else:
    print('Acute')


