# 2번 과정
def devideUv(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        
        if count == 0:
            u, v = p[:i+1], p[i+1:]
            return u, v

#3번 과정
def isCorrectString(u):
    counter = 0
    
    for i in range(len(u)):
        if u[i] == '(':
            counter += 1
        else:
            if counter == 0:
                return False
            counter -= 1
            
    return True
            
def solution(p):
    answer = ''

    if not p :
        return ''
    
    u, v = devideUv(p)
    
    if isCorrectString(u):
        return u + solution(v)
    #4 과정
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        
        u = list(u[1:-1]) #'str' object does not support item assignment
   
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
                
        answer += ''.join(u)

    return answer

