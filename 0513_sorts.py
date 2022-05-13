def insertionSort(n):
    for i in range(len(n)):
        # i 現在要處理的data 的index
        temp = n[i]
        
        j = i-1 #j 要比較前幾筆資料
        while j >= 0 and temp < n[j]:
            n[j+1] = n[j]
            j-=1
        #insert
        n[j+1] = temp 

def selectionSort(n):
    for i in range(len(n)): #我要做n次
        minindex = i
        for j in range(i+1,len(n)): #每一輪找min number
            if n[j] < n[minindex]:
                minindex = j
        """
        temp = n[j]
        n[j] = n[minindex]
        n[minindex] = temp
        """
        
        n[i],n[minindex] = n[minindex],n[i]
        
def bubbleSort(n):
    for _ in range(len(n)): #我要做幾次
        for j in range(len(n)-1): #進行左右交換 -1代表n-1組
            if n[j] < n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]

n = [5,2,8,6,1]
insertionSort(n)
print('insertionSort',n)

n = [5,2,8,6,1]
selectionSort(n)
print('selectionSort',n)

n = [5,2,8,6,1]
bubbleSort(n)
print('bubbleSort',n)
