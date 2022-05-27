target = 53

money = [50,25,24,10,5,1] #幣值
dp = [0] + [float("inf")]*target #紀錄有幾枚硬幣

for i in range(1,target+1):
    for m in money:
        if i - m >= 0:
            dp[i] = min(dp[i],dp[i-m]+1)
print(dp)