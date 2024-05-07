import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

visited = [0]*100001
MIN, MAX = 0, 100000

def bfs(start, q=deque()):
    visited[start] = 1
    q.append(start)
    while q:
        x = q.popleft()
        if x == K:
            print(visited[x]-1)
            break
        for y in (x-1, x+1, x*2):
            if y >= MIN and y <= MAX and (not visited[y]):
                q.append(y)
                visited[y] = visited[x] + 1

bfs(N)