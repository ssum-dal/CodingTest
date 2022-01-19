'''
https://www.acmicpc.net/problem/14501
dp
'''

n = int(input())
day = []
cost = []
d = []

for i in range(n):
    a, b = map(int, input().split())
    day.append(a)
    cost.append(b)
    d.append(b)

d.append(0)

for i in range(n-1, -1, -1):
    if n < day[i] + i:
        d[i] = d[i+1]
    else:
        d[i] = max(d[i+1], cost[i]+d[i+day[i]])

print(d[0])