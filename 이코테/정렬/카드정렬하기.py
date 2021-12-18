import sys
import heapq
input = sys.stdin.readline

n = int(input())
answer = 0
heap = [int(input()) for _ in range(n)]

heapq.heapify(heap)

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    answer += a+b

    heapq.heappush(heap,a+b)

print(answer)
