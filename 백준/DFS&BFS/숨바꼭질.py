'''
https://www.acmicpc.net/problem/1697
'''

from collections import deque

def bfs(start):
    q = deque()
    q.append([start, 0])
    visited[start] = True
    
    while q:
        x, count = q.popleft()
        
        if x == k:
            return count

        for i in range(3):
            if i == 0:
                nx = x + 1
            elif i == 1:
                nx = x - 1
            else:
                nx = x * 2
            
            if nx < 0 or nx > 100000:
                continue

            if not visited[nx]:
                q.append([nx, count+1])
                visited[nx] = True

n, k = map(int, input().split())
visited = [False]*100001

answer = bfs(n)

print(answer)