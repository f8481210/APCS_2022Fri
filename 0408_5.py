class Student:
	def __init__(self, name, chinese, english, math):
		self.name = name
		self.chinese = int(chinese)
		self.english = int(english)
		self.math = int(math)
students = []
for i in range(3):
	data = list(input().split())
	students.append(Student(data[0], data[1], data[2], data[3]))
query, subject = input().split()
while query != '0':
	for i in students:
		if i.name == query:
			if subject == 'Chinese':
				print(int((i.chinese+33)*1.1-20))
			elif subject == 'English':
				print(int((i.english+33)*1.1-20))
			else:
				print(int((i.math+33)*1.1-20))
	query, subject = input().split()