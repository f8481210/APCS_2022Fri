#merge sort
def merge(arr1, arr2):
    global ans
    arr3 = []
    p1 = p2 = 0 #arr1 和 arr2的index
    for _ in range(len(arr1)+len(arr2)):
        if p1 == len(arr1):
            arr3.append(arr2[p2])
            p2 += 1
        elif p2 == len(arr2):
            arr3.append(arr1[p1])
            p1 += 1
        elif arr1[p1] <= arr2[p2]:
            arr3.append(arr1[p1])
            p1 += 1
        else:
            arr3.append(arr2[p2])
            p2 += 1
            ans += len(arr1)-p1
        return arr3

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    m = (len(arr))//2
    return merge(merge_sort(arr[:m]), merge_sort(arr[m:]))

n = int(input())
ans = 0
while n != 0:
    num = []
    ans = 0
    num = [int(input()) for _ in range(n)]
    merge_sort(num)
    print(ans)
    n = int(input())