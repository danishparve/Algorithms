def insertion_sort(A, n):
	
	for i in range(1, n):
		key = A[i]
		j = i-1
		
		while j >= 0 and A[j] > key:
			A[j+1] = A[j]
			j = j-1
			
		A[j+1] = key
		
	return A

A = [9,2,6,7,0,10,3,5,4,1,8]
n = len(A)	
print(insertion_sort(A, n))