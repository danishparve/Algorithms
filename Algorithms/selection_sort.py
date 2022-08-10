A = [6,9,3,0,2,4,7,1,8,10,5]
n = len(A)

def selection_sort(A, n):

	for i in range(n):
		smallest = i
		
		for j in range(i+1, n):
			if A[j] < A[smallest]:
				smallest = j
		(A[i], A[smallest]) = (A[smallest], A[i])
	
	return A

print(selection_sort(A, n))