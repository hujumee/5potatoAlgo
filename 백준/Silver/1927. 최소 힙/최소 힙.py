import sys
import heapq

q = []

n = int(sys.stdin.readline())
for i in range(n):
    x = int(sys.stdin.readline())
    if (x):
        heapq.heappush(q, x)
    else:
        if (len(q)):   
            pop = heapq.heappop(q)
            print(pop)
        else:
            print(0)