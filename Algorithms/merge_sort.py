A = [12, 9, 3, 7, 14, 11, 6, 2, 10, 5]
p = 0
r = len(A) -1

def merge_sort(A, p, r):
	if p >= r:
		return A
	else:
		q = (p+r)//2
		merge_sort(A, p, q)
		merge_sort(A, q+1, r)
		merge(A, p, q, r)
		
def merge(A, p, q, r):
	
	n1 = q-p+1
	n2 = r-q
	B = [0]*(n1)
	C = [0]*(n2)
	i = 0
	j = 0
	
	for a in range(0, n1):
		B[a] = A[p+a]
	for b in range(0, n2):
		C[b] = A[q+1+b]
	B[-1] = -1
	C[-1] = -1
	
	for k in range(p, r):
		if B[i] <= C[j]:
			A[k] = B[i]
			i = i+1
		elif B[i] > C[j]:
			A[k] = C[j]
			j = j+1
	 		
print(merge_sort(A, p, r)) 