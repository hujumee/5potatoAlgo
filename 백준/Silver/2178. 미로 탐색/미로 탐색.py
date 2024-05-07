import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [[] for _ in range(N)]
for i in range(N):
    line = input()
    for j in range(M):
        maze[i].append(int(line[j]))

start = (0,0)
visited = [[0]*M for _ in range(N)]
def bfs(q=[]):
    q.append(start)
    visited[0][0] = 1
    while q:
        elem = q.pop(0)
        x1, y1 = elem[0], elem[1]
        if x1 == N-1 and y1 == M-1:
            break
        for k in ((x1, y1+1), (x1+1, y1), (x1-1, y1), (x1, y1-1)):
            if k[0]>=0 and k[0]<N and k[1]>=0 and k[1]<M:
                x2, y2 = k[0], k[1]
                if (maze[x2][y2] == 1) and (not visited[x2][y2]):
                    q.append((x2, y2))
                    visited[x2][y2] = visited[x1][y1] + 1
    return visited

print(bfs()[N-1][M-1])