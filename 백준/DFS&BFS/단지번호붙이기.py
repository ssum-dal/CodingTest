'''
https://www.acmicpc.net/problem/2667
'''

import sys
sys.setrecursionlimit(10**6)

move = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1
    
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]

        if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
            continue

        if not visited[nx][ny] and arr[nx][ny] == 1:
            dfs(nx, ny)

n = int(input())
arr = []
answer = []
visited = [[False]*n for _ in range(n)]

for i in range(n):
    arr.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            count = 0
            dfs(i,j)
            answer.append(count)

answer.sort()

print(len(answer))
for i in answer:
    print(i)