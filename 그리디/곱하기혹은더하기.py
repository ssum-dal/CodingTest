'''
각 자리가 숫자로 이루어진 문자열 S가 주어졌을 때,
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 x 혹은 +연산자를 넣어
결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성
단 +보다 x를 먼저 계산하는 일반적인 방식과는 달리 왼쪽에서부터 순서대로 이루어진다.
ex) 02984라는 무자열이 주어지면 만들어질 수 있는 가장 큰 수는 0+2x9x8x4
'''
input = list(map(int, input()))
result = input[0]

for i in range(len(input)-1):
    if(result <= 1 or input[i+1] <= 1):
        result += input[i+1]
    else:
        result *= input[i+1]

print(result)