import sys
from itertools import combinations

N = int(sys.stdin.readline())
ingredients = [0 for _ in range(N)]

for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    ingredients[i] = arr

combis = []
for i in range(N):
    arr = combinations(ingredients, i+1)
    combis.extend(arr)

diff = 200000000000
for elem in combis:
    s, b = 1, 0
    for elem in elem:
        s *= elem[0]
        b += elem[1]
    if (abs(s - b) < diff):
        diff = abs(s - b)
        
print(diff)