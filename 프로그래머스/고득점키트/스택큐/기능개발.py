import math

def solution(progresses, speeds):
    answer = []
    rest = []
    
    for i in range(len(progresses)):
        rest.append(math.ceil((100-progresses[i])/speeds[i]))

    tmp = rest[0]
    count = 1
    for i in range(1, len(rest)):
        if rest[i] > tmp :
            answer.append(count)
            tmp = rest[i]
            count = 0
        count += 1
    answer.append(count)
            
    return answer