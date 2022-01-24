'''
https://www.acmicpc.net/problem/13913
bfs
'''

import sys
from collections import deque

input = sys.stdin.readline

def find_path(x):
    arr = []
    tmp = x
    for _ in range(visited[x]+1):
        arr.append(tmp)
        tmp = parent[tmp]
    arr.reverse()
    for i in arr:
        print(i, end=' ')

def bfs(a):
    q = deque()
    q.append(a)
    
    while q:
        x = q.popleft()

        if x == k:
            print(visited[x])
            find_path(x)
            return

        for nx in (x-1, x+1, 2*x):

            if nx < 0 or nx > 100000:
                continue

            if visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[x] + 1
                parent[nx] = x

n, k = map(int, input().split())
visited = [0]*100001
parent = [0]*100001

bfs(n)