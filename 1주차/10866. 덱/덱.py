import sys
from collections import deque

q = deque([])

n = int(sys.stdin.readline())

for i in range(n):
    str = sys.stdin.readline().split()
    com = str[0]
    if com == 'push_front':
        q.appendleft(str[1])
    elif com == 'push_back':
        q.append(str[1])
    elif com == 'pop_front':
        if (len(q)):
            print(q.popleft())
        else:
            print(-1)
    elif com == 'pop_back':
        if (len(q)):
            print(q.pop())
        else:
            print(-1)
    elif com == 'size':
        print(len(q))
    elif com == 'empty':
        if (len(q)):
            print(0)
        else:
            print(1)
    elif com == 'front':
        if (len(q)):
            print(q[0])
        else:
            print(-1)
    elif com == 'back':
        if (len(q)):
            print(q[-1])
        else:
            print (-1)
