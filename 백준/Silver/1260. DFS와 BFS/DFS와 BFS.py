import sys

N, M, V = map(int, sys.stdin.readline().split())

graph = dict()
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
       
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]
    
for k in graph.keys():
    graph[k].sort()

def dfs(start, visited):
    visited.append(start)
    if start in graph.keys():
        for node in graph[start]:
            if node not in visited:
                dfs(node, visited)
    return visited

def bfs(start, visited, q):
    q.append(start)
    while q:
        if q[0] in graph.keys():
            for node in graph[q[0]]:
                if (node not in q) and (node not in visited):
                    q.append(node)
        visited.append(q.pop(0))
    return visited

res = ""
for elem in dfs(V, []):
    res += str(elem)
    res += ' '
print(res)

res = ""
for elem in bfs(V, [], []):
    res += str(elem)
    res += ' '
print(res)