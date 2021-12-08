'''
동빈이는 n * m 크기의 직사각형 형태의 미로에 갇혀 있다.
미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 동빈이의 위치는 (1, 1)이고 미로의 출구는 (n, m)의 위치에 존재하며
한 번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다
미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.
'''
from collections import deque

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y):
    q = deque()
    q.append([x, y, 1])

    while q:
        currentx, currenty, distance = q.popleft()

        for i in move: 
            nx = currentx + i[0]
            ny = currenty + i[1]

            if nx < 0 or ny < 0  or nx > n-1 or ny > m-1:
                continue

            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                if nx == n-1 and ny == m-1:
                    answer.append(distance+1)
                q.append([nx, ny, distance+1])

n, m = map(int, input().split())
arr = []
answer = []

for i in range(n):
    arr.append(list(map(int, input())))

bfs(0, 0)
print(min(answer))
