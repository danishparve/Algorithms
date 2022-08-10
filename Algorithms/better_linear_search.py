def better_linear_search(A, n, x):
	
	answer = 'NOT-FOUND'
	for i in range(n):
		if A[i] == x:
			return i
	return answer

A = [5, 8, 10, 3, 6, 3, 9, 7, 1, 0]
n = len(A)
x = 11
			
print(better_linear_search(A, n, x))