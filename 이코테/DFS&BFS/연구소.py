'''
https://www.acmicpc.net/problem/14502
'''
from collections import deque
import copy
import sys
input = sys.stdin.readline

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs():
    q = deque(virus)
    tmp = copy.deepcopy(lab)

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue
            
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append([nx, ny])

    safe = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                safe += 1
    answer.append(safe)

def makeWall(x):
    if x == 3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if lab[i][j] == 0:
                    lab[i][j] = 1
                    makeWall(x+1)
                    lab[i][j] = 0

n, m = map(int, input().split())
lab = []
virus = []
answer = []

for i in range(n):
    lab.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            virus.append([i, j])

makeWall(0)
print(max(answer))