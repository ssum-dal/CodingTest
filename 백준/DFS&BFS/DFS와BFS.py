from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    visited[v] = True
    q = deque([v])

    while q:
        value = q.popleft()
        print(value, end=' ')
        for i in graph[value]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

dfs(graph, v, [False]*(n+1))
print()
bfs(graph, v, [False]*(n+1))