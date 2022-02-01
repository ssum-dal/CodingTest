'''
https://www.acmicpc.net/problem/2210
dfs
'''
import sys
input = sys.stdin.readline
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y, n, num):
    if n == 6:
        s.add(num)
        return
    
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]

        if nx < 0 or ny < 0 or nx > 4 or ny > 4:
            continue
        
        dfs(nx, ny, n+1, num+arr[nx][ny])

arr = []
s = set()
for _ in range(5):
    arr.append(list(map(str, input().split())))

for i in range(5):
    for j in range(5):
        dfs(i, j, 1, arr[i][j])

print(len(s))