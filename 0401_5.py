a, b, c = map(int, input().split())
if b == 0 and a == c:
	print(c)
elif b == 0:
	print('failed')
elif (c-a)%b != 0:
	print('failed')
elif (c-a)*b < 0: 
	print('failed')
else:
	for i in range(a,c,b):
		print(i, end = " ")
	print(c)