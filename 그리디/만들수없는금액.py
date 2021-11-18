'''
동네 편의점의 주인인 동빈이는 N개의 동전을 가지고 있다.
이때 N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하시오
ex) N=5 동전이 3원, 2원, 1원, 1원, 9원이라 가정,
동빈이가 만들 수 없는 금액 중 최솟값은 8원
'''

n = int(input())
coin = list(map(int, input().split()))
coin.sort()

result = 1

for i in coin:
    print(result, i)
    if result < i:
        break
    result += i

print(result)