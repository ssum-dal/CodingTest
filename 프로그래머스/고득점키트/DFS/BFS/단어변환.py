from collections import deque

def compare(a, b):
    check = 0
    for i in range(len(b)):
        if a[i] != b[i]:
            check += 1

    if check == 1:
        return True
    else:
        return False
    
def solution(begin, target, words):
    answer = []
    q = deque()
    q.append([begin, 0])
    visited = [False]*len(words)
    
    if not target in words:
        return 0

    while q:
        word, distance = q.popleft()

        if word == target:
            answer.append(distance)

        for i in range(len(words)):
            if compare(word, words[i]) and not visited[i]:
                visited[i] = True
                q.append([words[i], distance+1])
      
    return min(answer)