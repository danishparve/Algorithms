def sentinel_linear_search(A, n, x):
	
	last = A[-1]
	A[-1] = x
	i = 0
	answer = 'NOT-FOUND'
	
	while A[i] != x:
		i += 1
	A[-1] = last
	
	if (i < n - 1) or A[-1] == x:
		return i
	else:
		return answer

A = [65,81,39,75,10,22,99,43,82,82,81,66,67,100,5,7,9,99,69,69,65,0,56,65]

n = len(A)

x = int(input())

print(sentinel_linear_search(A, n, x))