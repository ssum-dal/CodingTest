def solution(numbers):
    answer = ''
    
    #for i in range(len(numbers)):
    #    numbers[i] = str(numbers[i])*3
    #numbers.sort(reverse = True)

    #이렇게 바꾸기
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    #for i in numbers:
    #    answer = answer + i[0:len(i)//4]

    answer = str(int(''.join(numbers)))
    
    return answer

solution([0, 0, 0, 0])