'''
https://www.acmicpc.net/problem/17070
pypy 제출
파이썬은 bfs 시간초과
dfs는 반복문을 사용해서 이동하면 시간초과
dp로 풀거나 dfs는 반복문을 이동하여 이동하면 안됨
'''
import sys

input = sys.stdin.readline

def dfs(x, y, dir):
    global answer
   
    if x == n-1 and y == n-1:
        answer += 1
        return

    if dir == 0 or dir == 1:
        ny = y+1
        if ny < n:
            if arr[x][ny] == 0:
                dfs(x, ny, 0)
        
    if dir == 1 or dir == 2:
        nx = x+1
        if nx < n:
            if arr[nx][y] == 0:
                dfs(nx, y, 2)
    
    if dir == 0  or dir == 1 or dir == 2:
        nx = x+1
        ny = y+1
        if nx < n and ny < n:
            if arr[nx][ny] == 0 and arr[nx-1][ny] == 0 and arr[nx][ny-1] == 0:
                dfs(nx, ny, 1)

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = 0

if arr[n-1][n-1] == 1:
    print(0)
else:
    dfs(0, 1, 0)
    print(answer)