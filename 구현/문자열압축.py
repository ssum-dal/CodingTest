'''
프로그래머스 : https://programmers.co.kr/lear/courses/30/lessons/60057 , 2020 카카오 신입 공채 
'''

def solution(s):
    resultArr = []
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)//2+1):
        num = 1
        answer = ''
        tmp = s[:i]
        
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:
                num += 1
            else:
                if num == 1:
                    answer += tmp
                else:
                    answer += str(num)+tmp
                num = 1
            tmp = s[j:j+i]
        
        if num == 1:
            answer += tmp
        else:
            answer += str(num)+tmp
        
        resultArr.append(len(answer))

    return min(resultArr)