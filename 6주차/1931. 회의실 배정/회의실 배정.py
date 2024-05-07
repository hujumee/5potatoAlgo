import sys

N = int(sys.stdin.readline())
times = []
for _ in range(N):
    times.append(tuple(map(int, sys.stdin.readline().split())))
    
times.sort(key=lambda x: (x[1], x[0]))
cnt, end = 0, 0

for i in range(N):
    if times[i][0] >= end:
        end = times[i][1]
        cnt += 1

print(cnt)