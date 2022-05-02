def DFS(r, d):
	global child
	if not child[r]:
		return d
	ans = d
	for c in child[r]:
		ans = max(ans, DFS(c, d+1))
	return ans

n = int(input())	# 有幾個點
m = int(input())	# 有幾個敘述
parent = [0 for _ in range(n+1)]
child = [[] for _ in range(n+1)] #二維的list

#parent 存parent number
#child 存child number

for _ in range(m):
	data = [int(x) for x in input().split()]
	for i in range(1, len(data)):
		parent[data[i]] = data[0]
	child[data[0]] += data[1:]
root = None
for i in range(1, len(parent)):
	if parent[i] == 0:
		root = i
		break
print('root: ', root)
print('depth: ', DFS(root, 1))