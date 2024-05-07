import sys, itertools

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0

for x in range(n):
    combi_li = itertools.combinations(arr, x+1)
    for elem in combi_li:
        if (sum(elem) == s):
            cnt += 1

print(cnt)