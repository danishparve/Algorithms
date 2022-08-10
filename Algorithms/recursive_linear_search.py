import time

start = time.time()

def recursive_linear_search(A, n, i, x):
		
	if i >= n:
		return 'NOT-FOUND'
	
	elif  i <= n and A[i] == x:
		return i
		
	elif i <= n and A[i] != x:
		return  recursive_linear_search(A, n, i+1, x)
		
A = [8,5,9,0,3,5,3,5,7,1]
n = len(A)
x = 7
i = 0

print(recursive_linear_search(A, n, i, x))

end = time.time()
print(end-start)