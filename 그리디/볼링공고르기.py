'''
A, B 두 사람이 볼링을 치고 있다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 한다.
볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여된다.
같은 무게의 공이 여러 개 있을 수 있지만, 서로 다른 공으로 간주한다.
볼링공의 무게는 1부터 M까지의 자연수 형태로 존재
N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하시오
'''

n, m = map(int, input().split())
bw = list(map(int, input().split()))
result = 0

bw.sort()

for i in range(n-1):
    for j in range(i+1, n):
        if bw[i] == bw[j]:
            continue

        result += 1

print(result)