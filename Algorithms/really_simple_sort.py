def really_simple_sort(A, n):
	k = 0
	for i in range (0, n):
		if A[i] == 1:
			k += 1
	
	for i in range (0, k):
		A[i] = 1
	
	for i in range (k+1, n):
		A[i] = 2
	return A

A = [1, 2, 2, 1, 2, 1, 1, 2, 2, 1]
n = len (A)

print(really_simple_sort(A, n))