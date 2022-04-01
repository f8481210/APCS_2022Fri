# 輸入三科成績+轉成整數
x, y, z = map(int, input().split())
# 兩兩比較大小，若順序不對就交換
if x < y:
	x, y = y, x
if y < z:
	y, z = z, y
if x < y:
	x, y = y, x
# 輸出排好的成績
print(x, y, z)