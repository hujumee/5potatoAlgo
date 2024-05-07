import sys

N = int(sys.stdin.readline())
cranes = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))

cranes.sort(reverse=True)  #O(N)
weights.sort(reverse=True) # O(M)

cnt = 0

if weights[0] > cranes[0]:
    print(-1)
    sys.exit()

while weights: # O(N*M)
    for crane in cranes:
        if weights and crane < weights[-1]:
            continue
        for weight in weights:
            if crane >= weight:
                weights.remove(weight)
                break
    cnt += 1

print(cnt)