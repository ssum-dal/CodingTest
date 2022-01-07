'''
https://www.acmicpc.net/problem/1647
전체 그래프에서 2개의 최소 신장 트리를 만들어야 한다.
가장 간단한 방법은 크루스칼 알고리즘으로 최소 신장 트리를 찾은 뒤
최소 신장 트리를 구성하는 간선 중에서 가장 비용이 큰 간선을 제거하는 것
'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0]*(n+1)

edges=[]

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
result = 0
hcost = 0

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost
        hcost = cost

print(result-hcost)

