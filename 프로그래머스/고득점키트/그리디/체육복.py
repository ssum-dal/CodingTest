def solution(n, lost, reserve):
    new_reserve = list(set(reserve) - set(lost))
    new_lost = list(set(lost) - set(reserve))
    answer = n - len(new_lost)
    
    for i in range(len(new_reserve)):
        if new_reserve[i]-1 in new_lost:
            answer += 1
            new_lost.remove(new_reserve[i]-1)
        elif new_reserve[i]+1 in new_lost:
            answer += 1
            new_lost.remove(new_reserve[i]+1)
    
    return answer