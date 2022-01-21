'''
https://www.acmicpc.net/problem/2573
pypy 제출
bfs
'''
import sys
from collections import deque

input = sys.stdin.readline
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(a, b):
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue

            if not visited[nx][ny] and arr[nx][ny] != 0:
                q.append((nx, ny))
                visited[nx][ny] = True


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = 0
while True:
    visited = [[False]*m for _ in range(n)]
    glacier = 0
    check = True
    
    for i in range(1, n-1):
        for j in range(1, m-1):
            if arr[i][j] != 0 and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)
                glacier += 1

            if arr[i][j] != 0:
                check = False

    if glacier > 1:
        break

    if check:
        answer = 0
        break
    
    tmp = [[0]*m for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if arr[i][j] == 0:
                continue
            sea = 0
            if arr[i-1][j] == 0:
                tmp[i][j] += 1
            if arr[i+1][j] == 0:
                tmp[i][j] += 1
            if arr[i][j-1] == 0:
                tmp[i][j] += 1
            if arr[i][j+1] == 0:
                tmp[i][j] += 1

    for i in range(1, n-1):
        for j in range(1, m-1):
            if tmp[i][j] > arr[i][j]:
                arr[i][j] = 0
            else:
                arr[i][j] -= tmp[i][j]
    
    answer += 1

print(answer)