'''
https://www.acmicpc.net/problem/2589
pypy 제출
'''

import sys
from collections import deque

input = sys.stdin.readline
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(arr, visited, i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or ny < 0 or nx > h-1 or ny > w-1:
                continue

            if visited[nx][ny] == -1 and arr[nx][ny] == 'L':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y]+1
    
    return visited[x][y]

h, w = map(int, input().split())
arr = []
lands = []

for _ in range(h):
    arr.append(list(input().strip()))

for i in range(h):
    for j in range(w):
        if arr[i][j] == 'L':
            lands.append((i, j))

answer = 0
for land in lands:
    x, y = land
    visited = [[-1]*w for _ in range(h)]
    visited[x][y] = 0
    answer = max(bfs(arr, visited, x, y), answer)

print(answer)