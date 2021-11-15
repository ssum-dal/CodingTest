'''
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택 수행
단 두 번째 연산은 N이 K로 나누어떨어질 때만 가능
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
N과 K가 주어질 때 N이 1이 될 때까지의 최소 횟수
'''

n, k = map(int, input().split())
result = 0

while True:
    if n == 1:
        break

    if n % k == 0:
        n = n / k
    else:
        n -= 1
    
    result += 1

print(result)
