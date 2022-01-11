'''
https://www.acmicpc.net/problem/3190
'''
from collections import deque
import sys

input = sys.stdin.readline

move = [(0, 1), (1, 0), (0, -1), (-1, 0)] #오 아래 왼 위

n = int(input())
k = int(input()) #사과
arr = [[0]* n for _ in range(n)]
dir = []
q = deque()

for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

l = int(input())

for _ in range(l):
    time, rot = input().split()
    dir.append((int(time), rot))



x, y = 0, 0
q.append([x, y])
time = 0
rot = 0
i = 0

while True:
    nx = x + move[rot][0]
    ny = y + move[rot][1]

    if nx < 0 or ny < 0 or nx > n-1 or ny > n-1 or arr[nx][ny] == 2:
        time += 1
        break

    else:
        if arr[nx][ny] == 1:
            arr[nx][ny] = 2
            q.append((nx, ny))
        
        elif arr[nx][ny] == 0:
            arr[nx][ny] = 2
            q.append((nx, ny))
            tailx, taily = q.popleft()
            arr[tailx][taily] = 0

    time += 1
    x, y = nx, ny

    if i < l and time == dir[i][0]:
        if dir[i][1] == 'D':
            if rot == 0:
                rot = 1
            elif rot == 1:
                rot = 2
            elif rot == 2:
                rot = 3
            else:
                rot = 0
        else:
            if rot == 0:
                rot = 3
            elif rot == 1:
                rot = 0
            elif rot == 2:
                rot = 1
            else:
                rot = 2
        i += 1

print(time)



