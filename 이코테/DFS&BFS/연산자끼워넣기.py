'''
https://www.acmicpc.net/problem/14888

'''
def dfs(index):
    global result
    if index == n:
        answer.append(result)
        return
    
    for i in range(4):
        tmp = result
        if operator[i] != 0:
            if i == 0:
                result += num[index]
            elif i == 1:
                result -= num[index]
            elif i == 2:
                result *= num[index]
            else:
                if result >= 0:
                    result //= num[index]
                else:
                    result = (result*-1 // num[index]) * -1
        
            operator[i] -= 1
            dfs(index+1)
            result = tmp
            operator[i] += 1

n = int(input())
num = list(map(int, input().split()))
operator=list(map(int, input().split()))
result = num[0]
answer = []

dfs(1)

print(max(answer))
print(min(answer))