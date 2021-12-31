import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    global count
    visited[v] = True

    for i in arr[v]:
        if not visited[i]:
            count += 1
            dfs(i)
    
n = int(input())
c = int(input())
arr = [[] for _ in range(n+1)]
visited = [False]*(n+1)
count = 0

for i in range(c):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)


dfs(1)
print(count)