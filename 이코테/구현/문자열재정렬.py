'''
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
K1KA5CB7 -> ABCKK13
'''

input = list(input())
input.sort()
num = 0
answer=''

for i in input:
    if ord(i)-ord('A') < 0:
        num += int(i)
    else:
        answer += i

if num == 0:
    print(answer)
else:
    print(answer+str(num))


#답안
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))


    