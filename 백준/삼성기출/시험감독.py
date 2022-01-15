#https://www.acmicpc.net/problem/13458

import sys
input = sys.stdin.readline

n = int(input()) #시험장 수
student = list(map(int, input().split()))
a, b = map(int, input().split())

total = 0
for i in student:
    rest = i - a
    total += 1
    
    if rest > 0:
        total += rest // b

        if rest % b > 0:
            total += 1

print(total)