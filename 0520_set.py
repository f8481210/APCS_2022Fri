"""
temp = 'abc'
n = 'defg'

print(temp+n)


temp = ['Flase']
print(temp*2)
"""
"""
#建立集合 - 1 
s1 = set() #空集合
print(s1)

# - 2
s2 = {"one","two","three"}
#print(s2)

# - 3
s3 = set(("four","five","six"))
#print(s3)

#新增元素
s1.add(5)
s1.add(6)
s1.add(7)
print(s1)

#刪除元素 - 1
s1.remove(5)
print(s1)

# - 2
s1.pop()
print(s1)

#複製集合
s4 = s1.copy()
print('s4:',s4)

#清空集合
s4.clear()
print(s4)

#集合沒有順序性
s1 = {'apple','banana','coconut'}
s2 = {'banana','coconut','apple'}

print(s1 == s2)
s1 = {'apple','banana'}

print(s1 != s2)

print(s1 <= s2)

print(s1 >= s2)
"""

s1 = {1,2,3,4,5}
s2 = {5,6,7,8,9}

#交集
print(s1.intersection(s2))
#聯集
print(s1.union(s2))
#差集
print(s1.difference(s2))




