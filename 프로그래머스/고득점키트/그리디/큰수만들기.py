def solution(number, k):
    answer = ''
    tmp = ''.join(sorted(number,reverse=True))
    
    i = 0
    while True:
        if k == 0 or k == len(number):
            if k == 0:
                answer = answer + number
            break
        
        index = number.find(tmp[i])
        if index <= k:
            k  -= index
            answer += tmp[i]
            number = number[index+1:]
            tmp = tmp[0:i]+tmp[i+1:]
            i = 0
        else:
            i += 1
            
    return answer