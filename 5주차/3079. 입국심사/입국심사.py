import sys

N, M = map(int, sys.stdin.readline().split())
times = []

for _ in range(N):
    times.append(int(sys.stdin.readline()))

start, end = min(times), min(times)*M
ans = 0
while start <= end:
    mid = (start+end) // 2
    sum_ppl = 0
    for time in times:
        sum_ppl += mid // time
    if sum_ppl < M:
        start = mid + 1
    else:
        end = mid - 1
    ans = start

print(ans)
    

                
