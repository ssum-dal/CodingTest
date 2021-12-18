def solution(numbers):
    answer = ''
    
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])*4
    
    numbers.sort(reverse = True)
    
    for i in numbers:
        answer = answer + i[0:len(i)//4]
    
    return answer

solution([0, 0, 0, 0])