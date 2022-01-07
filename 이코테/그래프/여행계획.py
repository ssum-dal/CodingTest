import sys

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
parent =[0]*(n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    tmp = list(map(int, input().split()))

    for j in range(n):
        if tmp[j] == 1:
            union(parent, i+1, j+1)

plan = list(map(int, input().split()))

for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        print('NO')
        sys.exit()

print('YES')