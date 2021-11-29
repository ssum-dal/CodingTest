def solution(brown, yellow):
    answer = []
    w = 0
    
    if yellow == 1:
        answer = [3, 3]

    for i in range(1, yellow//2+1):
        if yellow % i == 0:
            w = yellow // i
            if 2*(w+2) + i*2 == brown:
                answer = [w+2, i+2]
                break
    return answer