'''
https://www.acmicpc.net/problem/18405
'''
from collections import deque

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs():
    while q:
        value, x, y, sec = q.popleft()

        if sec == s:
            break
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue

            if arr[nx][ny] == 0:
                arr[nx][ny] = value
                q.append([arr[nx][ny], nx, ny, sec+1])
            
arr = []
q = []
n, k = map(int, input().split())

for i in range(n):
    arr.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            q.append([arr[i][j], i, j, 0])

q.sort()
q = deque(q)

bfs()

print(arr[x-1][y-1])
