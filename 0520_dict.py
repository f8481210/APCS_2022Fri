#利用key去快速找到對應的value
#key:value
"""
#建立字典
d1 = dict() #空字典
print(d1)

d2 = {'one':1,'two':2,'three':3}
print(d2)

d3 = dict({'one':1,'two':2,'three':3})
print(d3)

d4 = dict(one=1,two=2,three=3)
print(d4)

d5 = dict([('one',1),('two',2),('three',3)])
print(d5)

#列出所有key
print(d2.keys())

#列出所有value
print(d2.values())

#列出所有項目
print(d2.items())

#複製字典
a = d2.copy()
print(a)

#清空字典
a.clear()
print(a)
"""
"""
#新增元素 字典名[key] = value
d = {'Amy':3,'Becky':5,0:'egg'}
print(d)
d[2022] = 'covid'
print(d)

#修改 字典名[key] = value
d['Becky'] ='cute'
print(d)

#刪除 - 1 del 字典名[key]
del d[0]
print(d)

# - 2 pop 需要接收pop出來的結果
temp = d.pop(2022)
print(d)
print(temp)
"""
#計算字典中的元素個數
d = {'Amy':3,'Becky':5,0:'egg'}
#print(len(d))

#檢查指定的 key 是否存在於字典中 in
#print('Amy' in d)
"""
#把所有key都走過一遍
for key in d.keys():
    print(d[key])
    
#把所有value都走過一遍
for value in d.values():
    print(value)
"""
#同時走過所有的key和value
for key,value in d.items():
    print(key,value)