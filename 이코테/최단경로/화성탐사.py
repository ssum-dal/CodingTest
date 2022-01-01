'''
기출 39
다익스트라
'''

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

t = int(input())

for _ in range(t):
    graph = []
    q = []
    
    n = int(input())

    for i in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF]*n for _ in range(n)]

    heapq.heappush(q, (0, 0, graph[0][0]))
    distance[0][0] = graph[0][0]

    while q:
        x, y, dist = heapq.heappop(q)
    
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue

            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (nx, ny, cost))
    
    print(distance[n-1][n-1])