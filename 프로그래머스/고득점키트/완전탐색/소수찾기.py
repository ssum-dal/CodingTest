from itertools import permutations

def solution(numbers):
    answer = 0
    permute = []
    intPermute = []
    
    for i in range(1, len(numbers)+1):
        permute += list(permutations(numbers,i))
        
    intPermute = set([int(("").join(i)) for i in permute])
    answer = len(intPermute)
    
    for i in intPermute:
        if i < 2:
            answer -= 1
            continue
        
        for j in range(2, i):
            if i % j == 0:
                answer -= 1
                break
        
    return answer