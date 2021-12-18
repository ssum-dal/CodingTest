'''
https://www.acmicpc.net/problem/16234
'''
from collections import deque

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(initX, initY):
    q = deque()
    q.append([initX, initY])
    visited[initX][initY] = True
    count = 1
    people_num = arr[initX][initY]
    union = [[initX , initY]]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue

            if not visited[nx][ny] and ( l <= abs(arr[x][y] - arr[nx][ny]) <= r):
                q.append([nx, ny])
                visited[nx][ny] = True
                count += 1
                people_num += arr[nx][ny]
                union.append([nx, ny])

    if count > 1:
        average = people_num // count

        for i in union:
            x, y = i[0], i[1]
            arr[x][y] = average
        
        return True
    else:
        return False



arr = []
answer = 0
n, l, r = map(int, input().split())

for i in range(n):
    arr.append(list(map(int, input().split())))

while True:
    visited = [[False]*n for _ in range(n)]
    moved = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j):
                    moved = True
    
    if not moved:
        break
    else:
        answer += 1

print(answer)





