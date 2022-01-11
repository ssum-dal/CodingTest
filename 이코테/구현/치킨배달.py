from itertools import combinations
import sys

input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split())
h, c = [], []

for i in range(n):
    tmp = list(map(int, input().split()))

    for j in range(n):
        if tmp[j] == 0:
            continue

        if tmp[j] == 1:
            h.append((i, j))
        else:
            c.append((i, j))

chicken = list(combinations(c, m))

answer = INF
for i in chicken:
    cost = 0

    for j in h:
        hx, hy = j
        tmp = INF
        for k in i:
            cx, cy = k
            tmp = min(tmp, abs(hx-cx)+abs(hy-cy))

        cost += tmp
    
    answer = min(cost, answer)

print(answer)
