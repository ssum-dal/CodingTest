'''
다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다.
다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다.
다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것
문자열 S가 주어졌을 때, 다솜이가 해야 하는 행동의 최소 횟수를 출력
'''

s = input()
result = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        result += 1
        
print((result + 1) // 2)

