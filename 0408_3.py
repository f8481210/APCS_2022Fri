def compute(score):
	return int((score+33)*1.1-20)
# 輸入三科成績
x, y, z = map(int, input().split())
# 輸出新成績
print(compute(x), compute(y), compute(z))