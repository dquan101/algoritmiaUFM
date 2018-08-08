def isHeap(arr, n):
	for i in arr:
		if (arr[2*i + 1] > arr[i]):
			return False
		if (arr[2*1 + 2 > arr[i]]):
			return False
	return True;

if __name__ == '__main__':

	arr = [16,14,10,8,7,9,3,2,4,1]
	n = len(arr)
	if isHeap == True:
		print("Si es")
	else:
		print("No es")