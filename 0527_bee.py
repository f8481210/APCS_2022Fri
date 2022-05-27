import time 
male = [0] #存 male 生產數量
female = [1] # 存 female 生產數量

#female(n) : male(n-1)
#male(n) : male(n-1) + female(n-1)

while True:
    n = int(input())
    if n == -1:
        break
    
    if len(male) > n:
        print(male[n], male[n] + female[n])
    else:
        for _ in range(len(male),n+1):
            male.append(male[-1] + female[-1])
            female.append(male[-2]+1)
        
        time.sleep(3)
        print(male[n],male[n] + female[n])