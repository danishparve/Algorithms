import time

A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
n = len(A)
x = 1

def binary_search(A, n, x):
	
	p = 0
	r = n-1
	
	while p <= r:
		q = ((p+r)//2)
		
		if A[q] == x:
			return q
		elif A[q] != x and A[q] > x:
			p = q+1
		elif A[q] < x:
			r = q-1
		
	return 'NOT-FOUND'
	
start = time.time()
print(binary_search(A, n, x))
end = time.time()
print(end-start)	