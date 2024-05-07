import sys
import heapq as hq

n = int(sys.stdin.readline())

li = []

for i in range(n):
    new = list(map(int, sys.stdin.readline().split()))
    for m in new:
        if (i == 0):
            hq.heappush(li, m)
        else:
            if (li[0] < m):
                hq.heappop(li)
                hq.heappush(li, m)

print(hq.heappop(li))