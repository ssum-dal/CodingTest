'''
n * m 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오
'''
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y):
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    
    if arr[x][y] == 0:
        arr[x][y] = 1
        for i in move:
            dfs(x+i[0], y+i[1])
        return True

n, m = map(int, input().split())
arr = []
answer = 0

for i in range(n):
    arr.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            if(dfs(i, j)):
                answer += 1

print(answer)