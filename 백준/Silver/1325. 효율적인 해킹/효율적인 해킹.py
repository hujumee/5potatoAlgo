import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = dict()
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

count = dict()
def bfs(start):
    visited = [0] * (N+1)
    cnt = -1
    q = deque([start])
    visited[start] = 1
    while q:
        node = q.popleft()
        if node in graph.keys():
            for elem in graph[node]:
                if visited[elem] == 0:
                    q.append(elem)
                    visited[elem] = 1
                    cnt += 1
    return cnt

for key in graph.keys():
    cnt = bfs(key)
    if cnt in count:
        count[cnt].append(key)
    else:
        count[cnt] = [key]

max_cnt = max(count.keys())
count[max_cnt].sort()
res = ""
for elem in count[max_cnt]:
    res += str(elem) + " "
print(res)