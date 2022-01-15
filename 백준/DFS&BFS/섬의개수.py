#https://www.acmicpc.net/problem/4963

import sys
from collections import deque

input = sys.stdin.readline
move = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def bfs(arr, a, b):
    q = deque()
    q.append((a, b))
    arr[a][b] = 2
    
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or ny < 0 or nx > h-1 or ny > w-1:
                continue

            if arr[nx][ny] == 1:
                arr[nx][ny] = 2
                q.append((nx, ny))

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))

    answer = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(arr, i, j)
                answer += 1
    print(answer)

    