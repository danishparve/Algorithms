#LINEAR SEARCH
A = list(map(int, input().split()))
x = int(input())

def linear_search(Array, Value):
	
	n = len(A)
	answer = 'NOT FOUND'
	for i in range(n):
		if A[i] == x:
			answer = i
	return answer

print(linear_search(A, x))	