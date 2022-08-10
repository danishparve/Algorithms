A = [1,0,3,6,8,4,9,5,2,7]
p = 0
r = len(A)-1

def quicksort(A,p,r):
	
	if p >= r:
		return A
	q = partition(A,p,r)
	quicksort(A,p,q-1)
	quicksort(A,q+1,r)
	return A
		
def partition(A,p,r):
	
	q = p
	for u in range(p, r):
		if A[u] <= A[r]:
			A[q], A[u] = A[u], A[q]
			q += 1
	A[q], A[r] = A[r], A[q]
	return q
	
print(quicksort(A,p,r))