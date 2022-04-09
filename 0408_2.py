s = input()
s_len = len(s)
i = 0
while i < s_len:
	if s[i:i+2] == 'ab':
		print(i, end=' ')
		s = s[:i] + ' ' + s[i:]
		s_len += 1
		i += 2
	else:
		i += 1
print()
print(s)

# 以下為錯誤示範，因len(s)會變動，所以沒辦法用for loop
'''
s = input()
for i in range(len(s)):
	if s[i:i+2] == 'ab':
		print(i, end=' ')
		s = s[:i] + ' ' + s[i:]
print()
print(s)
'''