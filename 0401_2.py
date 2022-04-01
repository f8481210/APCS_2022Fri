# 輸入三科成績
x, y, z = input().split()
# 計算新成績
x = int((int(x)+33)*1.1-20)
y = int((int(y)+33)*1.1-20)
z = int((int(z)+33)*1.1-20)
# 輸出新成績
print(x, y, z)