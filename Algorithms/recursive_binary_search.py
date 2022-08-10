def recursive_binary_search(A, p, r, x):
	
	if p > r:
		return 'NOT-FOUND'
	elif p <= r:
		q = (p+r)//2
		
		if A[q] == x:
			return q
		elif A[q] > x:
			return recursive_binary_search(A, p, q-1, x)
		elif A[q] < x:
			return recursive_binary_search(A, q+1, r, x)
A = [1,2,3,4,5,6,7,8,9,10]
p = 0
r = len(A)-1
x = 11
print(recursive_binary_search(A, p, r, x))