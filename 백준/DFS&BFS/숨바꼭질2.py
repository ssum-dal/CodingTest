'''
https://www.acmicpc.net/problem/12851
bfs
'''

import sys
from collections import deque

input = sys.stdin.readline

def bfs(a):
    global answer
    q = deque()
    q.append((a, 0))
    minTime = int(1e9)
    
    while q:
        x, time = q.popleft()
        visited[x] = True
        
        if x == k and time <= minTime:
            answer += 1
            minTime = min(minTime, time)

        for nx in (x-1, x+1, 2*x):

            if nx < 0 or nx > 100000:
                continue

            if not visited[nx]:
                q.append((nx, time+1))
    
    return minTime            

n, k = map(int, input().split())
visited = [False]*100001
answer = 0

time = bfs(n)
print(time)
print(answer)