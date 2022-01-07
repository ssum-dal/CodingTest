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
parent = [0]*(n)
edges = []
total = 0

for i in range(n):
    parent[i] = i

for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))
    total += z

edges.sort()
result = 0

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost
        print(cost, a, b)

print(total-result)


