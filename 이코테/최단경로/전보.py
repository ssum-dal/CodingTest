import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
arr = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    i, j, k  = map(int, input().split())
    arr[i].append((j, k))

q = []
distance[c] = 0
heapq.heappush(q, (0, c))

while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue

    for i in arr[now]:
        cost = dist + i[1]

        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

city = 0
maxDist = 0

for i in range(1, n+1):
    if distance[i] != INF and distance[i] != 0:
        city += 1
        maxDist = max(maxDist, distance[i])

print(city, maxDist)