'''
문제 A -> B
https://www.acmicpc.net/problem/16953
'''

from collections import deque

def bfs(start):
    q = deque()
    q.append([start, 0])

    while q:
        x, count = q.popleft()

        for i in range(2):
            if i == 0:
                nx = x * 2
            else:
                nx = int(str(x)+'1')

            if nx > 10**9:
                continue

            if nx == b:
                return count+2

            q.append([nx, count+1])

    return -1
            
answer = 0
a, b = map(int, input().split())
answer = bfs(a)

print(answer)