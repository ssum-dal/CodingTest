def dfs(numbers, target, num, index, l):
    global answer

    if index == l:
        if num == target:
            answer += 1
        return 
    
    dfs(numbers, target, num+numbers[index+1], index+1, l)
    dfs(numbers, target, num-numbers[index+1], index+1, l)
        

def solution(numbers, target):
    l = len(numbers)
    
    dfs(numbers, target, numbers[0], 0 , l-1)
    dfs(numbers, target, numbers[0]*-1, 0, l-1)
    
    return answer

answer = 0
