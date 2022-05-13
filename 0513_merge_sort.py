def merge(arr1, arr2):
	arr3 = []
	p1 = p2 = 0
	for _ in range(len(arr1)+len(arr2)):
		if p1 == len(arr1):
			arr3.append(arr2[p2])
			p2 += 1
		elif p2 == len(arr2):
			arr3.append(arr1[p1])
			p1 += 1
		elif arr1[p1] < arr2[p2]:
			arr3.append(arr1[p1])
			p1 += 1
		else:
			arr3.append(arr2[p2])
			p2 += 1
	return arr3

def merge_sort(arr):
	if len(arr) == 1:
		return arr
	m = (len(arr))//2
	return merge(merge_sort(arr[:m]), merge_sort(arr[m:]))

n = int(input())
num = list(map(int, input().split()))
print(merge_sort(num))