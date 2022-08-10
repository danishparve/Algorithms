A = [1,2,3,4,5]
n = 5
x = 3

def linear_search(A, n, x):
	answer = 'NOT-FOUND'
	for i in range(n):
		if A[i] == x:
			return i
	return answer

print(linear_search(A, n, x))