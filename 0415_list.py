list1 = ['a','b','c','d']

#新增append 新增在最後一個
list1.append('e')
#print(list1)

#插入insert 插入在第n項後面
list1.insert(0,'123')
print(list1)

#刪除 1.del 2.remove 3.pop
#del 刪除第幾個 index
#del list1[0]
#print(list1)

#remove 要刪掉的 值
#list1.remove('b')
#print(list1)

#pop 刪除第幾個 index
#括號內未填index 預設從最後一個刪除
list1.pop()
print(list1)

#搜尋 1.in 2.index
#in T/F
#temp = '123' in list1
#print(temp)

#index 要找誰 回傳index給我
print(list1.index('b'))