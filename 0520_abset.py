try:
	while True:
		A = set(input().split())
		B = set(input().split())
		if A == B:
			print('A equals B')
		elif A <= B:
			print('A is a proper subset of B')
		elif B <= A:
			print('B is a proper subset of A')
		elif not A.intersection(B):
			print('A and B are disjoint')
		else:
			print('I\'m confused!')
except EOFError:
	pass