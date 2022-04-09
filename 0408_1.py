A = list(map(int, input().split()))
X = int(input())
ans = 0
for i in range(len(A)):
	for j in range(i+1,len(A)): 
		if A[j] == X-A[i]:
			ans += 1
print(ans)