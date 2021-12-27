'''
못생긴 수란 오직 2, 3, 5 만을 소인수로 가지는 수를 의미한다. 다시 말해 오직 2, 3, 5를
약수로 가지는 합성수를 의미한다. 1은 못생긴 수라고 가정한다. 따라서 못생긴 수들은
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15 ... 순으로 이어지게 된다.
이때 n번째 못생긴 수를 찾는 프로그램을 작성하라

다시 풀어보기
'''
n = int(input())

d = [0]*n
d[0] = 1

two, three, five = 0, 0, 0
ntwo, nthree, nfive = 2, 3, 5

for i in range(1, n):
    d[i] = min(ntwo, nthree, nfive)

    if d[i] == ntwo:
        two += 1
        ntwo = d[two]*2
    
    if d[i] == nthree:
        three += 1
        nthree = d[three]*3

    if d[i] == nfive:
        five += 1
        nfive = d[five]*5

print(d[n-1])
