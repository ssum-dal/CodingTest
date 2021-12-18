def solution(N, stages):
    answer = {}
    people = len(stages)
    
    for i in range(1, N+1):
        if people == 0:
            answer[i] = 0
        else:
            n = stages.count(i)
            answer[i] = n / people
            people -= n

    answer = sorted(answer, key=lambda x: answer[x], reverse=True)
    
    return answer