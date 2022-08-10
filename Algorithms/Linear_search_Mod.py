import time

#Linear Search

A = list(map(int, input().split()))
x = int(input())

def linear_search(Array, Value):
	
	answer = 'NOT-FOUND'
	for i in range(len(A)):
		if A[i] == x:
			answer = i
			return answer
	return answer

start = time.time()
print(linear_search(A, x))
end = time.time()
print('Time taken: {} seconds'.format(end-start))