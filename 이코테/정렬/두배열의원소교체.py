'''
두 개의 배열 A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있으며,
배열의 원소는 모두 자연수이다. 최대 K번의 바꿔치기 연산을 수행할 수 있는데
바꿔치기 연산이란 A에 잇는 원소 하나와 배열 B에 있는 원소 하나를 골라서
두 원소를 서로 바꾸는 것을 말한다. 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.
'''

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))