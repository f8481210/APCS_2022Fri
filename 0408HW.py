try:
	n = int(input())
	case = 1
	input()	# 第一行空白
	while case <= n:
		print('Case #'+str(case)+':')
		msg = input().split()	# msg 為一個 str 組成的 list
		while len(msg):
			index = 0
			for i in msg:
				if index < len(i):	# 要找的字母index必須小於該單字的長度
					print(i[index], end='')
					index += 1
			print()
			msg = input().split()
		print()
		case += 1
except EOFError:
    pass