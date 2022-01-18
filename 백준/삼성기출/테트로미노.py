'''
https://www.acmicpc.net/problem/14500
pypy 제출
'''

import sys
input = sys.stdin.readline

result = 0
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
fmove = [(-1, 1 ,1), (-1, 1, -1), (1, -1, 1), (1, -1, -1)]

def dfs(x, y, count, sum):
    global result
    if count == 4:
        result = max(result, sum)
        return
    
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]

        if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
            continue

        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, count+1, sum+arr[nx][ny])
            visited[nx][ny] = False

# ㅗ, ㅜ, ㅓ, ㅏ
def fy(x, y):
    global result
    
    for i in range(4):
        if i < 2:
            a = y + fmove[i][0]
            b = y + fmove[i][1]
            c = x + fmove[i][2]

            if a < 0 or b < 0 or c < 0:
                continue

            if a > m-1 or b > m-1 or c > n-1:
                continue

            tmp = arr[x][y] + arr[x][a] + arr[x][b] + arr[c][y]

        else:
            a = x + fmove[i][0]
            b = x + fmove[i][1]
            c = y + fmove[i][2]

            if a < 0 or b < 0 or c < 0:
                continue

            if a > n-1 or b > n-1 or c > m-1:
                continue

            tmp = arr[x][y] + arr[a][y] + arr[b][y] + arr[x][c]

        result = max(result, tmp)

arr = []
n , m = map(int, input().split())
visited = [[False]*m for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j, 1, arr[i][j])
            visited[i][j] = False

        fy(i, j)

print(result)