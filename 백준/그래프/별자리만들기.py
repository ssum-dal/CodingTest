import math
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
parent = [i for i in range(n+1)]

star = []
edges = []
result = 0

for _ in range(n):
    x, y = map(float, input().split())
    star.append((x, y))

for i in range(n-1):
    for j in range(i+1, n):
        edges.append((math.sqrt((star[i][0]-star[j][0])**2 + (star[i][1] - star[j][1])**2), i, j))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost

print("{:.2f}".format(result))