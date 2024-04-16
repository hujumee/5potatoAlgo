import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(trees)
res = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for elem in trees:
        if elem > mid:
            cnt += elem - mid
    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1
    res = end

print(res)    
    