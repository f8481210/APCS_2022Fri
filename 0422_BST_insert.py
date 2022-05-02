class Node:
	def __init__(self, val=None):
		self.data = val
		self.left = None
		self.right = None
	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data
	def search(self, data):
		if data == self.data:
			return True
		elif data < self.data:
			if self.left is None:
				return False
			self.left.search(data)
		elif data > self.data:
			if self.right is None:
				return False
			self.right.search(data)

'''
arr = [int(x) for x in input().split()]
root = Node()
for i in arr:
	root.insert(i)

data = int(input('請輸入搜尋值: '))
if root.search(data) == True:
	print('找到了')
else:
	print('找不到')
'''