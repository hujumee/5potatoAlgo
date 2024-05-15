import sys
from collections import deque

link = dict()

N = int(sys.stdin.readline())
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    if a in link:
        link[a].append(b)
    else:
        link[a] = [b]
    if b in link:
        link[b].append(a)
    else:
        link[b] = [a]
        
parents = [0] * (N-1)

def bfs(start):
    q = deque()
    q.append(start)
    visited = [0] * (N+1)
    while q:
        node = q.popleft()
        visited[node] = 1
        for elem in link[node]:
            if visited[elem] == 0:
                parents[elem-2] = node
                q.append(elem)

bfs(1)
for elem in parents:
    print(elem)