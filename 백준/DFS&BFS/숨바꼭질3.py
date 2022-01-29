'''
https://www.acmicpc.net/problem/13549
bfs
시간 가중치가 다른 점 주의
'''

import sys
from collections import deque

input = sys.stdin.readline

def bfs(a):
    global answer
    q = deque()
    q.append((a, 0))
    visited[a] = True

    while q:
        x, time = q.popleft()
        
        if x == k:
            return time

        for i, nx in enumerate([2*x, x-1, x+1]):

            if nx < 0 or nx > 100000:
                continue

            if not visited[nx]:
                if i == 0:
                    q.append((nx, time))
                else:
                    q.append((nx, time+1))
                visited[nx] = True             

n, k = map(int, input().split())
visited = [False]*100001

print(bfs(n))