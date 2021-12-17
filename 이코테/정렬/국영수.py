'''
https://www.acmicpc.net/problem/10825
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    name, korean, eng, math = input().split()
    arr.append([name, int(korean), int(eng), int(math)])

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(arr[i][0])