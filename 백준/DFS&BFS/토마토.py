from collections import deque
import sys

input = sys.stdin.readline

move = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
q = deque()

def bfs():
    global answer

    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nz = z + move[i][0]
            nx = x + move[i][1]
            ny = y + move[i][2]

            if nz < 0 or nx < 0 or ny < 0 or nz > h-1 or nx > n-1 or ny > m-1:
                continue

            if arr[nz][nx][ny] == 0:
                q.append([nz, nx, ny])
                arr[nz][nx][ny] = arr[z][x][y] + 1
                answer = max(arr[z][x][y] + 1, answer)

    
answer = -1
check = True
m, n, h = map(int, input().split())
arr = [[] for _ in range(h)]

for i in range(h):
    for j in range(n):
        arr[i].append(list(map(int, input().split())))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append([i, j, k])

            if arr[i][j][k] == 0:
                check = False

bfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                print(-1)
                sys.exit(0)

if check:
    print(0)
else:
    print(answer-1)