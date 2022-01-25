'''
https://www.acmicpc.net/problem/2206
bfs
visited[x][y][0] (x, y)까지 벽을 뚫지 않고 왔을 때 거리 기록
visited[x][y][1] (x, y)까지 벽을 한 번이라도 뚫고 온 거리 기록
'''

import sys
from collections import deque

input = sys.stdin.readline
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(a, b):
    q = deque()
    q.append((a, b, 0))
    visited[0][0][0] = 1

    while q:
        x, y, w = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or ny  < 0 or nx > n-1 or ny > m-1:
                continue

            if arr[nx][ny] == 0 and visited[nx][ny][w] == 0:
                q.append((nx, ny, w))
                visited[nx][ny][w] = visited[x][y][w]+1
            
            elif arr[nx][ny] == 1 and w == 0:
                q.append((nx, ny, 1))
                visited[nx][ny][1] = visited[x][y][w]+1

    return -1


n, m = map(int, input().split())
arr = []
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().strip())))

print(bfs(0, 0))

