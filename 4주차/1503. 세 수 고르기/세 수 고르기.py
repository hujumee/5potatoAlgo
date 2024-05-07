import sys

N, M = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))

ans = sys.maxsize
for x in range(1, 1002):
    if x in S: 
        continue
    for y in range(1, 1002):
        if y in S:
            continue
        for z in range(1, 1002):
            if z in S:
                continue
            xyz = x * y * z
            if (abs(N - xyz) < ans):
                ans = abs(N - xyz)
            if N < xyz:
                break
print(ans)