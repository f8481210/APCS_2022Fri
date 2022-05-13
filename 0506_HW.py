# -*- coding: utf-8 -*-
from collections import deque

n = int(input()) #頂點

while n != 0:
    m = int(input()) #邊
    graph = [] #圖
    visited = [] #檢查走過沒有
    queue = deque([0])
    for _ in range(n):
        graph.append([])
        visited.append(-1) #沒走過-1
    while m > 0:
        x, y = map(int, input().split())
        m -= 1
        graph[x].append(y)
        graph[y].append(x)
        
    visited[0] = 0 #走過 0
    
    #顏色1 顏色2
    while queue:
        for i in graph[queue[0]]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = (visited[queue[0]]+1)%2
                
            #跟我連接的點 顏色不能相同
            elif visited[i] == visited[queue[0]]:
                print('NOT BICOLORABLE.')
                break
            
            else:
                queue.popleft()
                continue
            break
    
    print('BICOLORABLE.')
    n = int(input())
            
            
            
            
                
        
    
