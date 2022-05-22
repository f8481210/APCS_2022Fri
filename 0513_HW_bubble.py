#bubble sort
"""
最少需要用到多少次交換的動作

來將輸入的序列由小到大排序
"""
try:
    while True:
        n = int(input()) #list裡有多少數字
        num = list(map(int, input().split()))
        ans = 0 #交換次數
        for i in range(len(num)):
            for j in range(len(num)-i-1):
                if num[j] > num[j+1]:
                    num[j],num[j+1] = num[j+1],num[j]
                    ans += 1
        
        print('Minimum exchange operations : '+str(ans))
except EOFError:
	pass