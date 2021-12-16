'''
https://www.acmicpc.net/problem/1012
'''

import sys
sys.setrecursionlimit(10**6)

move=[(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]

        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            continue

        if not visited[nx][ny] and arr[nx][ny] == 1:
            dfs(nx, ny)
    
t = int(input())

for a in range(t):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    answer = 0 
    
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                dfs(i, j)
                answer += 1
    
    print(answer)