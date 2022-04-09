# -*- coding: utf-8 -*-
"""
一個10進位的數字換成二進位數字
"""
try:
    while(1):
        n = int(input())
        ans = ''
        while n != 0:
            ans = str(n%2) + ans
            n //= 2
        print(ans)
    
except EOFError:
    pass

