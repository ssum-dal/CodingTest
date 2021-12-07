'''
게임의 아웃복서 캐릭터는 필살기인 럭키 스트레이트 기술이 있다.
이 기술은 매우 강력한 대신에 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있다.
특정 조건이란 현재 캐릭터의 점수를 n이라고 할 때 자릿수를 기준으로 점수 n을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과
오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미한다.
현재 점수 n이 주어지면 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하세요.
'''

input = input()
length = len(input)

sum1 = 0
sum2 = 0

for i in range(length//2):
    sum1 += int(input[i])
    sum2 += int(input[-i-1])

if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')