'''
https://www.acmicpc.net/problem/18352
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    distance[start] = 0

    while q:
        value = q.popleft()

        for i in arr[value]:
            if distance[i] == -1:
                distance[i] = distance[value] + 1
                q.append(i)


n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
distance = [-1]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

bfs(x)

if not k in distance:
    print(-1)
else:
    for i in range(1, n+1):
        if k == distance[i]:
            print(i)


