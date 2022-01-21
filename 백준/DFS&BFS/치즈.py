'''
https://www.acmicpc.net/problem/2636
bfs
'''
import sys
from collections import deque

input = sys.stdin.readline
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs():
    visited = [[False]*m for _ in range(n)]
    q  = deque()
    q.append((0, 0))
    visited[0][0] = True
    deleted = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue

            if visited[nx][ny]:
                continue

            if arr[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True

            else:
                arr[nx][ny] = 0
                visited[nx][ny] = True
                deleted += 1
    
    deletedArr.append(deleted)
    return deleted


n, m = map(int, input().split())
arr = []
deletedArr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = 0   
while True:
    deleted = bfs()
    if deleted == 0:
        break
    
    answer += 1

print(answer)
print(deletedArr[-2])