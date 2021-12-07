'''
2,4,5,4,6으로 이루어진 배열이 있을 때 M이 8이고 K가 3이라면,
특정한 인덱스의 수가 연속해서 3번 더해질 수 있다
6+6+6+5+6+6+6+5 = 48

3,4,3,4,3으로 이루어진 배열이 있을 때 M이 7이고 K가 2라면,
4+4+4+4+4+4+4 = 28
'''

N, M, K = map(int, input().split())
arr = list(map(int,input().split()))

arr.sort()

result = 0
firstNum = arr[-1]
secondNum = arr[-2]


a = 1
for i in range(M):
    if a != K+1:
        result += firstNum
    else:
        result += secondNum
        a = 0
    a += 1

print(result)

