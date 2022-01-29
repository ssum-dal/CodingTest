'''
https://www.acmicpc.net/problem/1916
최단 경로 다익스트라
'''

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
v = int(input())

graph =[[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(v):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = i[1] + dist

        if cost < distance[i[0]]:
            heapq.heappush(q, (cost, i[0]))
            distance[i[0]] = cost

print(distance[end])