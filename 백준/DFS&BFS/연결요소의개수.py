'''
https://www.acmicpc.net/problem/11724
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):
    visited[start] = True

    for i in arr[start]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [False]*(n+1)
answer = 0

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, len(arr)):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)