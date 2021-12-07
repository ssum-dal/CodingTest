'''
3-1 거스름돈
당신은 음식점의 계산을 도와주는 점원이다.
카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원 동전이 무한히 존재한다.
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라.
단 거슬러 줘야 할 돈N은 항상 10의 배수이다.
'''

import sys

input = int(sys.stdin.readline())
result = 0

coinArray = [500, 100, 50, 10]

for c in coinArray:
    result += input // c
    input %= c

print(result)