'''
화폐 단위에서 큰 단위가 작은 단위의 배수가 아니기 때문에 그리디를 사용할 수 없다.
'''

n, m = map(int, input().split())
coin = [int(input()) for _ in range(n)]

d = [10001]*(m+1)
d[0] = 0

for i in range(coin[0], m+1):
    for j in range(n):
        d[i] = min(d[i], d[i-coin[j]]+1)

if d[m] == 10001:
    print(-1)

else:
    print(d[m])