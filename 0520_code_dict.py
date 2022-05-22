code = {'0101':'A',
        '0111':'B',
        '0010':'C',
        '1101':'D',
        '1000':'E',
        '1100':'F'}

n = int(input())
ans=[]
for _ in range(n):
    ans += code[input()]
    #temp = input()
    #print(code[temp],end='')
for i in ans:
    print(i,end='')
print()