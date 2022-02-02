'''
https://www.acmicpc.net/problem/1303
dfs
'''
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(x, y, color):
    global num

    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]

        if nx < 0 or ny < 0 or nx > h-1 or ny > w-1:
            continue

        if color == arr[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            num += 1
            dfs(nx, ny, color)


w, h = map(int, input().split())
arr = []
visited = [[False]*w for _ in range(h)]
answer1 = 0
answer2 = 0

for _ in range(h):
    arr.append(list(map(str, input())))

for i in range(h):
    for j in range(w):
        if not visited[i][j]:
            num = 1
            visited[i][j] = True
            
            dfs(i, j, arr[i][j])
            
            if arr[i][j] == 'W':
                answer1 += num**2
            else:
                answer2 += num**2

print(answer1, answer2)
            