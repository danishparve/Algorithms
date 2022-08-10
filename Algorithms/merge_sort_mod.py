import sys

INF_INTEGER = sys.maxsize
array = [12,9,3,7,14,11,6,2,10,5]
p = 0
r = len(array)
def merge_sort(array, p=0, r=None):

    if r is None:
        array = array.copy()
        r = len(array)
    if r - p <= 1:
        return
    q = (p + r + 1) // 2
    merge_sort(array, p, q)
    merge_sort(array, q, r)
    merge(array, p, q, r)
    return array


def merge(A, p, q, r):

    B = A[p:q].copy() + [INF_INTEGER]
    C = A[q:r].copy() + [INF_INTEGER]
    i = 0
    j = 0
    for k in range(p, r):
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
print(merge_sort(array, p, r))