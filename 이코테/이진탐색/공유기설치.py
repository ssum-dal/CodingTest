'''
https://www.acmicpc.net/problem/2110
'''
import sys
input = sys.stdin.readline

def binary_search(arr, c, start, end):
    global answer
    while start <= end:
        mid = (start+end)//2
        prev = arr[0]
        count = 1

        for i in range(1, n):
            if arr[i] - prev >= mid:
                count += 1
                prev = arr[i]

                if count == c:
                    break  
        if count == c:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

answer = 0
n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

binary_search(arr, c, 1, arr[-1]-arr[0])
print(answer)