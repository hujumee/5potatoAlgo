import sys

n = int(sys.stdin.readline())
n_li = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_li = list(map(int, sys.stdin.readline().split()))
A = sorted(n_li)

def bin_search(start, end, x):
    if start > end:
        return 0
    mid = (start + end) // 2
    if A[mid] == x:
        return 1
    elif x < A[mid]:
        return bin_search(start, mid-1, x)
    elif x > A[mid]:
        return bin_search(mid+1, end, x)

for elem in m_li:
    if elem > A[-1] | elem < A[0]:
        print(0)
    else:
        result = bin_search(0, n-1, elem)
        print(result)
    