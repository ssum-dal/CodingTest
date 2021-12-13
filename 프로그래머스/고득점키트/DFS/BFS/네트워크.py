def dfs(n, computers, v, visited):
    visited[v] = True
    for i in range(n):
        if not visited[i] and computers[v][i] == 1:
            visited[i] = True
            dfs(n, computers, i, visited)
        

def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i, visited)
            answer += 1
    return answer