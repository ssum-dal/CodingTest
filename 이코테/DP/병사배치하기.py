'''
https://www.acmicpc.net/problem/18353
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = [1]*n

for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            d[i] = max(d[i], d[j]+1)

print(n-max(d))