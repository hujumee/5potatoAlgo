import sys

N = int(sys.stdin.readline())
network = dict()

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    
    if a in network:
        network[a].append(b)
    else:
        network[a] = [b]
    
    if b in network:
        network[b].append(a)
    else:
        network[b] = [a]
for k in network.keys():
    network[k].sort()
        
def dfs(start, visited = []):
    visited.append(start)
    if start in network.keys():
        for node in network[start]:
            if node not in visited:
                dfs(node, visited)
    return visited

res = len(dfs(1)) - 1
print(res)