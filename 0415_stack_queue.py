#stack 堆疊
stack = []
for i in range(5):
    stack.append(i)
print(stack)
for i in range(len(stack),0,-1):
    stack.pop()
    print(stack)
    
# queue 佇列
queue = []
for i in range(5):
    queue.append(i)
print(queue)

while len(queue) > 0:
    pop = queue.pop(0)
    print(queue)