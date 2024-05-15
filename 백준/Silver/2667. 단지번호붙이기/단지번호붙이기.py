import sys
from collections import deque

N = int(sys.stdin.readline())

graph = [[0] * N for _ in range(N)]

for i in range(N):
    line = sys.stdin.readline()
    for j in range(N):
        graph[i][j] = int(line[j])

def bfs(start):
    q = deque([start])
    visited[start[0]][start[1]] = 1
    cnt = 0
    while q:
        this = q.popleft()
        x1, y1 = this[0], this[1]
        cnt += 1
        for node in ((x1-1, y1), (x1, y1-1), (x1+1, y1), (x1, y1+1)):
            x2, y2 = node[0], node[1]
            if (0 <= x2 <= N-1) and (0 <= y2 <= N-1):
                if (graph[x2][y2] == 1) and (visited[x2][y2] == 0):
                    q.append((x2, y2))
                    visited[x2][y2] = 1
    return cnt
        
visited = [[0] * N for _ in range(N)]
counts = []
for i in range(N):
    for j in range(N):
        if (graph[i][j] == 1) and (visited[i][j] == 0):
            cnt = bfs((i, j))
            counts.append(cnt)
counts.sort()
            
print(len(counts))
for elem in counts:
    print(elem)
    