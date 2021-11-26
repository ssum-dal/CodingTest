def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    safe = 0
    left = 0
    right = -1
    
    while True:
        if len(people)-safe <= 1:
            if len(people)-safe == 1:
                answer += 1
            break
        
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            safe += 2
        else:
            left += 1
            safe += 1
    
        answer += 1
    return answer