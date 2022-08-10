import time
start = time.time()
A = [3, 9, 8, 4, 7, 6, 1]
n = len(A)
x = 1
def sentinel_linear_search(A, n, x):
	last = A[-1]
	A[-1] = x
	i = 0
	answer = 'NOT-FOUND'
	while A[i] != x:
		i = i+1
	A[n-1] = last
	if i < n-1 or A[-1] == x:
		return i
	else:
		return answer

print(sentinel_linear_search(A, n, x))
end = time.time()
print(end-start)