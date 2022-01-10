'''
https://www.acmicpc.net/problem/2887
'''
import sys
input = sys.stdin.readline

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

n = int(input())
planet = []
edges = []
parent = [0]*n
result = 0

for i in range(n):
    parent[i] = i

for i in range(n):
    x, y, z = map(int, input().split())
    planet.append((x, y, z, i))

for i in range(3):
    planet.sort(key=lambda x:x[i])
    for j in range(1, n):
        edges.append((abs(planet[j - 1][i] - planet[j][i]), planet[j - 1][3], planet[j][3]))

print(edges)
        

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost

print(result)

