import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append((b, 1))
    arr[b].append((a, 1))

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in arr[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

result = []
maxDist = max(distance[1:])

for i in range(1, n+1):
    if distance[i] == maxDist:
        result.append(i)

print(result[0], maxDist, len(result))

