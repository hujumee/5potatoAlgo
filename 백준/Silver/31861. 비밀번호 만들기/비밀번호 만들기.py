import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

dp = [[0]*27 for _ in range(M+1)]
for j in range(27):
    dp[1][j] = 1
    
for i in range(2, M+1):
    for j in range(1, 27):
        for k in range(1, 27):
            if abs(j-k) >= N:
                dp[i][j] = (dp[i][j] + dp[i-1][k]) % (10**9 + 7)
    
res = 0    
for j in range(1, 27):
    res = (res + dp[M][j]) % (10**9 + 7)
print(res)