import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
tomato = []
rippen = []
for i in range(N):
    elem = list(map(int, input().split()))
    for j in range(M):
        if elem[j] == 1:
            rippen.append((i, j))
    tomato.append(elem)

def bfs():
    q = deque()
    res = 0
    for elem in rippen:
        q.append(elem)
    while q:
        t = q.popleft()
        x1, y1 = t[0], t[1]
        for elem in ((x1+1, y1), (x1, y1+1), (x1-1, y1), (x1, y1-1)):
            if 0<=elem[0]<N and 0<=elem[1]<M:
                x2, y2 = elem[0], elem[1]
                if (not tomato[x2][y2]):
                    q.append((x2, y2))
                    tomato[x2][y2] = tomato[x1][y1] + 1
        res = tomato[x1][y1]
    return res

res = bfs()-1
for i in range(N):
    for j in range(M):
        if not tomato[i][j]:
            res = -1
            break
print(res)