import sys

N = int(sys.stdin.readline())
lengths = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

res, min = 0, 1000000000

for i in range(N-1):
    if prices[i] < min:
        min = prices[i]
    res += min*lengths[i]

print(res)