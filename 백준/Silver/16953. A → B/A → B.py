import sys
A, B = map(int, sys.stdin.readline().split())

cnt, n = 1, B

while n > A:
    if n%2 == 0:
        n = n//2
        cnt += 1
    elif str(n)[-1] == '1':
        n = int(str(n)[:-1])
        cnt += 1
    else:
        break

if n == A:
    print(cnt)
else: 
    print(-1)