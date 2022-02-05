'''
https://www.acmicpc.net/problem/5430
구현
R 마다 reverse 사용하면 시간초과
출력이 너무 더럽다..
'''
from collections import deque
import sys

def RD(arr, f, n):
    r = 0
    for i in f:
        if i == 'R':
            r += 1
        else:
            if n == 0:
                return 'error', r
            else:
                if r % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
                n -= 1
    return arr, r

t = int(input())

for i in range(t):
    f = input()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    arr = deque(arr)

    result, r = RD(arr, f, n)

    if result == 'error':
        print(result)
    else:
        if r % 2 != 0:
            result.reverse()
        print("[" + ",".join(result) + "]")